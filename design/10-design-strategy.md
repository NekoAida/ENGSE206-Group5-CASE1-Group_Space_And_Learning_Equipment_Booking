# Design Strategy v0.1 — Group Space & Learning Equipment Booking System

> **สถานะ:** Design Draft | **Assignment:** W10-v1.0 | **Case:** ENGSE206-Group5-CASE1 (Group Space and Learning Equipment Booking System)
> **ฐาน SRS ที่ใช้:** `docs/07-srs-v1.md` สถานะ Baseline Candidate — *ไม่อ้างว่า Approved*
> **Change request ที่รู้และยัง Pending:** CR-01 (การปรับเกณฑ์เวลา Soft Lock สำหรับผู้พิการทางสายตาเป็น 10 นาที)

---

## 1. ระบบนี้ทำอะไร (ไม่เกิน 4 บรรทัด สำหรับ Dev)

นักศึกษาสามารถค้นหา ตรวจสอบสถานะ Real-time และทำการจองห้องกลุ่มพร้อมยืมอุปกรณ์การเรียนได้ในขั้นตอนเดียว ระบบดำเนินการล็อกรายการชั่วคราว (Soft Lock) และออก QR Code สำหรับ Check-in ภายใน 15 นาที โดยมีเจ้าหน้าที่ทำหน้าที่ตรวจรับ-ส่งมอบอุปกรณ์ และ Admin กำหนดกฎเกณฑ์ พร้อมติดตาม Audit Log จบงานเมื่อการใช้งานเสร็จสิ้นและคืนทรัพยากรเข้าสู่ระบบ

---

## 2. ขอบเขตรุ่นแรก: Build now / Overview / Later / ไม่ทำในวิชานี้

> กติกา: จัดลำดับพัฒนา **ไม่ลบอะไรออกจาก SRS**; ทุกแถวต้องมี requirement ID

| ระดับ | Use case / ความสามารถ | Requirement IDs | เหตุผลสั้น |
|---|---|---|---|
| **Build now** | ค้นหาและจองพื้นที่กลุ่มพร้อมยืมอุปกรณ์ (Soft Lock 5 นาที & ออก QR Code) | FR-01, FR-02, BR-01 | ฟังก์ชันหลักที่เป็น Core Transaction ของระบบ ป้องกันการจองซ้ำซ้อน |
| **Build now** | เช็คอินเข้าใช้งานด้วย QR Code และระบบปลดล็อก No-Show อัตโนมัติ (15 นาที) | FR-04, BR-02 | แก้ปัญหาการจองกั๊กพื้นที่และหมุนเวียนทรัพยากรให้ผู้อื่น |
| **Build now** | ตรวจรับ-คืนอุปกรณ์ บันทึกสภาพอุปกรณ์ และจัดการอนุมัติคำขอพื้นที่พิเศษ | FR-05, FR-06, FR-07, BR-03 | กระบวนการทำงานหลักของเจ้าหน้าที่หน้าเคาน์เตอร์ |
| **Build now** | กำหนดกฎเกณฑ์การจอง และจัดการบทบาทสิทธิ์ผู้ใช้งาน (RBAC) | FR-08, FR-12, BR-04, BR-06 | ควบคุมเงื่อนไขระบบและความปลอดภัยในการเข้าถึงฟังก์ชัน |
| **Overview** | ตรวจสอบรายงานสรุปสถิติการใช้งาน และเรียกดู Audit Log | FR-09, FR-10, BR-05 | แสดงผลภาพรวมข้อมูลสถิติและประวัติย้อนหลังในรูปแบบ Read-Only Dashboard |
| **Later** | การขยายเวลา Soft Lock เป็น 10 นาที และอ่านหน้าจอสำหรับผู้พิการทางสายตา (Accessibility) | FR-03, NFR-02 | เลื่อนไปเก็บรายละเอียด UI/UX Accessible Components ใน Iteration ถัดไป |
| **ไม่ทำในวิชานี้ / รอคำตอบ** | ระบบปลดล็อกประตูห้องจองอัตโนมัติด้วย Smart Door Lock (IoT Integration) | NFR-01 (Constraint) | ปรับใช้การ Check-in ผ่าน Web App และให้เจ้าหน้าที่ส่งมอบกุญแจแทน เพื่อลดความซับซ้อน Hardware |
| **ไม่ทำในวิชานี้ / รอคำตอบ** | ระบบปรับเงินอัตโนมัติกรณีคืนอุปกรณ์สายหรือชำรุด (Fine Payment Gateway) | NFR-03 (Constraint) | เปลี่ยนเป็นระบบบันทึก Penalty Points และระงับสิทธิ์การจองชั่วคราว |

---

## 3. สามเรื่องที่ถ้าออกแบบพลาด ระบบนี้พัง (Design Drivers)

| ID | เรื่องห้ามพลาด (ภาษาง่าย 1 บรรทัด) | มาจาก (BR/NFR/FR/AC) | ผลต่อการออกแบบใน W11 / W12 / W13 |
|---|---|---|---|
| **D1** | ห้ามเกิดการจองซ้ำซ้อนในเวลาเดียวกัน (Race Condition / Double Booking) | FR-02, BR-01, AC-02, NFR-02 | W11: ต้องออกแบบ State & Concurrency Control (Pessimistic Locking หรือ Atomic Transaction) ตอนกด Soft Lock<br>W12: ออกแบบ Database Transaction Isolation Level ให้รองรับ Concurrent Write<br>W13: เขียน Test Case จำลองการกดจองพร้อมกัน |
| **D2** | การยกเลิกการจองอัตโนมัติเมื่อเลยเวลา Check-in (No-Show Release) ต้องแม่นยำและไม่ค้าง State | FR-04, BR-02, AC-04 | W11: ออกแบบ Background Scheduler / Cron Job ที่ทำงานสม่ำเสมอทุก 1 นาที<br>W12: ออกแบบ State Machine เปลี่ยนสถานะจาก `Reserved` $\rightarrow$ `No-Show` $\rightarrow$ `Available` พร้อมคืนสต็อกอุปกรณ์แบบ Atomic<br>W13: ทดสอบการทำงานของ Background Worker |
| **D3** | การตัดสต็อกอุปกรณ์ชั่วคราวและการคืนสต็อกเข้าคลังเมื่อส่งคืนหรือยกเลิกต้องถูกต้อง 100% | FR-05, FR-06, BR-03, AC-05 | W11: ออกแบบ Domain Logic สำหรับการบริหารจัดการคลังอุปกรณ์ (Inventory Deduction & Restoration)<br>W12: บันทึก Transaction Log ทุกครั้งที่มีการเปลี่ยนแปลงสต็อกเพื่อทำ Audit Trail<br>W13: ทดสอบการทำ Concurrent Borrow/Return |

---

## 4. Design Spine

> ดูรายละเอียดฉบับเต็มที่ `design/00-design-spine.md`

| Step | Actor | Use Case ID | W10 Design Intent & Focus |
|---|---|---|---|
| 1 | นักศึกษา / ผู้ใช้ | UC-01 | ออกแบบ Search Filter และระบบ Soft Lock Timer (3–5 นาที) ป้องกัน Race Condition |
| 2 | นักศึกษา / ผู้ใช้ | UC-01 | ออกแบบการสร้าง Booking Ticket / QR Code เอกเทศ (Unique Reference) หลังกดยืนยันการจอง |
| 3 | นักศึกษา / ผู้ใช้ | UC-02 | ออกแบบ QR Code Scanner Integration และระบบตรวจสอบเงื่อนไขเวลาเข้าใช้งาน (Check-in Window) |
| 4 | เจ้าหน้าที่ (Staff) | UC-03 | ออกแบบ Staff Counter Dashboard สำหรับสแกนรับ-ส่งมอบอุปกรณ์ และแบบฟอร์มเช็กสภาพอุปกรณ์ (ปกติ/ชำรุด) |
| 5 | เจ้าหน้าที่ (Staff) | UC-03 | ออกแบบ Workflow การพิจารณาอนุมัติ/ปฏิเสธ คำขอใช้พื้นที่พิเศษพร้อมระบุเหตุผล |
| 6 | ผู้ดูแลระบบ (Admin) | UC-04 | ออกแบบหน้าตั้งค่า Dynamic System Parameters (เวลาจองสูงสุด, เวลาสาย No-Show, Penalty Rules) |
| 7 | ผู้ดูแลระบบ (Admin) | UC-05 | ออกแบบ Read-Only Audit Log Viewer และ Dashboard แสดงผลรายงานสถิติการใช้งาน |
| 8 | ผู้ดูแลระบบ (Admin) | UC-06 | ออกแบบระบบ Role-Based Access Control (RBAC) เพื่อควบคุม Guard Permissions |

---

## 5. ข้อตกลงที่ W11 ต้องรักษา (ยังไม่เลือก architecture/เทคโนโลยี)

1. **Single Source of Truth for Validation Rules:** กติกาและเงื่อนไขการตรวจสอบทั้งหมด (เช่น เวลาจองสูงสุด 7 วัน, เวลาสาย No-show 15 นาที, ขีดจำกัดการยืมอุปกรณ์) ต้องถูกประมวลผลที่ Domain Logic Layer เพียงจุดเดียว ห้ามแยกเขียนกระจายไว้ตาม UI Components
2. **State Explicit Persistence:** สถานะการจองและการยืมทรัพยากร (`Pending_Hold`, `Reserved`, `In-Use`, `Completed`, `No-Show`, `Cancelled`) ต้องจัดเก็บเป็นข้อมูล Enum/State ที่ลงดิสก์ได้จริง ห้ามอ้างอิงจากสถานะชั่วคราวของ UI หรือสีของปุ่มกด
3. **External Authentication & Central Student Data:** ข้อมูลระบุตัวตนและสถานะนักศึกษา/เจ้าหน้าที่ ต้องดึงมาจากระบบยืนยันตัวตนกลางของสถาบัน (OAuth2/SSO) ระบบนี้จะทำหน้าที่รับค่า User ID และ Role มาใช้งานต่อเท่านั้น
4. **Immutability of Audit Logs:** บันทึกประวัติการทำธุรกรรม (Audit Log) ต้องถูกออกแบบให้เป็นแบบ Append-Only (Read-Only) ห้ามมีฟังก์ชันการแก้ไขหรือลบประวัติย้อนหลังโดยเด็ดขาด

---

## 6. Open Decisions ของรุ่นแรก (ไม่เกิน 5)

| ID | คำถามที่ยังไม่มีคำตอบ | เชื่อม OI/ID ใน SRS | เจ้าของคำตอบ | ผลถ้ายังไม่ตอบ | รุ่นแรกทำอย่างไรระหว่างรอ |
|---|---|---|---|---|---|
| **DD-01** | ระยะเวลา Soft Lock ในช่วง Checkout ควรใช้ 3 นาที หรือ 5 นาทีเป็นมาตรฐาน? | OI-01 (Soft Lock Duration) | Product Owner / ทีมวิเคราะห์ | ผู้ใช้อาจกรอกข้อมูลไม่ทัน หรือทำให้ทรัพยากรติด Hold นานเกินไป | ใช้ค่าตั้งต้นที่ **5 นาที** และทำโครงสร้างระบบให้รองรับการปรับเปลี่ยนพารามิเตอร์ผ่าน Admin Config |
| **DD-02** | เกณฑ์การตัดสิทธิ์การจอง (Penalty Block) เมื่อเกิด No-Show สะสม ต้องใช้กี่ครั้ง และตัดสิทธิ์กี่วัน? | OI-02 (Penalty Policy) | เจ้าหน้าที่ห้อง / Admin | ไม่สามารถลงโทษผู้กั๊กสิทธิ์ได้อย่างเป็นรูปธรรม | กำหนดเกณฑ์ชั่วคราวที่ **No-Show ครบ 3 ครั้ง/เดือน ระงับสิทธิ์ 14 วัน** โดยเตรียม Field บันทึกคะแนนไว้ใน Database |
| **DD-03** | การสแกน QR Code เพื่อ Check-in จะสแกนผ่านเครื่องสแกนประจำห้อง หรือสแกนผ่านกล้องมือถือของเจ้าหน้าที่? | OI-03 (Check-in Hardware Method) | เจ้าหน้าที่อาคาร / IT Facility | ออกแบบ UI/UX และระบบรับข้อมูลสแกนไม่ถูกจุด | ออกแบบ Web-based QR Reader ให้รองรับการทำงานผ่านกล้อง Web Browser ทั้งมือถือและโน้ตบุ๊ก |

---

## 7. Done checklist (ติ๊กก่อนส่ง)

- [x] scope table แบ่ง 4 ระดับ โดยไม่ลบ FR ใดออกจาก SRS
- [x] ทุกแถวใน scope table มี requirement ID
- [x] drivers 3 ข้อ อ้าง ID และบอกผลต่อการออกแบบ
- [x] Spine 5–8 แถว มี actor + UC ทุกแถว เรียงตามผู้ใช้ทำจริง
- [x] open decisions $\le$ 5 มีเจ้าของ + ผลกระทบ + ระหว่างรอทำอย่างไร ไม่มีค่าที่แต่งขึ้น
- [x] ระบุสถานะ SRS ตามจริง ไม่อ้าง Approved

---

## 8. AI use และการตรวจโดยมนุษย์

* **การใช้ AI:** ใช้ AI ช่วยเรียบเรียงโครงสร้างเอกสาร Design Strategy v0.1 จัดระเบียบตาราง Scope, Design Drivers, Design Spine และสรุป Open Decisions ให้สอดคล้องกับเอกสาร Requirement 6 Use Cases
* **การตรวจสอบโดยมนุษย์:** ตรวจสอบและกำกับโดย **วรสิทธิ์ บุญยปรีดี (นักศึกษา)** ร่วมกับสมาชิกกลุ่ม ENGSE206 Group 5 เพื่อยืนยันความถูกต้องของ Requirement IDs, Business Rules, Traceability Matrix และข้อตกลงทางสถาปัตยกรรมสำหรับ W11
