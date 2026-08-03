# Week 04 — Evidence-linked Requirement Candidates

> **Team:** Group 5 — Group Space And Learning Equipment Booking System  
> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้  
> **Version:** v1.0 — Evidence-linked Requirement Candidates

---

## 1. Candidate writing rule

Candidate ที่ดีใน Week 04 ต้องมี actor/system behavior หรือ quality concern ที่ชัดพอให้วิเคราะห์ต่อ อ้าง E-ID ระบุสถานะ/confidence และบอกช่องว่างที่ต้อง verify โดยยังไม่รีบสร้างรายละเอียด UI/technology/penalty ที่ไม่มี evidence

---

## 2. Requirement candidates

| RC ID | Candidate statement | Type | Evidence / Decision | Status | Confidence | Follow-up / acceptance hint |
|---|---|---|---|---|---|---|
| **RC-01** | ระบบต้องให้ผู้ใช้สามารถค้นหา ตรวจสอบตารางเวลาว่างแบบ Real-time และส่งคำขอจองพื้นที่ทำงานกลุ่มหรืออุปกรณ์การเรียนรู้ผ่านหน้าเว็บไซต์ได้ | Functional | E-01, E-02 | Candidate | High | ยืนยันข้อมูลขั้นต่ำที่ต้องใช้ในฟอร์มการจอง และทดสอบความถูกต้องของตารางแสดงเวลาว่าง |
| **RC-02** | ระบบต้องมีหน้าจอให้เจ้าหน้าที่ตรวจสอบและกดยอมรับหรือปฏิเสธ (Approve/Reject) คำขอจองพื้นที่ทำงานกลุ่ม พร้อมระบุเหตุผลกรณีปฏิเสธได้ | Functional / Workflow | E-03, C-01 | Candidate | High | ยืนยันสถานะการจอง (Pending/Approved/Rejected) และทดสอบการเปลี่ยนสถานะบนหน้าเว็บ |
| **RC-03** | ระบบต้องอนุมัติการจองอุปกรณ์การเรียนรู้ประเภททั่วไปแบบอัตโนมัติ (Auto-approve) ตามลำดับคิวและจำนวนสต็อกคงเหลือในระบบ | Functional / Business Rule | E-04, C-01 | Candidate | Medium | ยืนยันรายการประเภทอุปกรณ์ที่ใช้อนุมัติอัตโนมัติ และทดสอบกรณีสต็อกอุปกรณ์หมด |
| **RC-04** | ระบบต้องตรวจสอบเงื่อนไขนโยบายการจอง โดยจำกัดระยะเวลาจองห้องไม่เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน | Functional / Business Rule | E-05 | Candidate | High | ทดสอบระบบ Validation Rule เมื่อผู้ใช้เลือกเวลาจองเกินโควตาที่กำหนด |
| **RC-05** | ระบบต้องยกเลิกคำขอจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาเช็กอินเข้าใช้พื้นที่ภายใน 15 นาทีหลังจากถึงเวลาจอง | Functional / Business Rule | E-06, C-02 | Provisional | Medium | ยืนยันกลไกการนับเวลา (Timer) และการเปลี่ยนสถานะเป็น No-show / Available |
| **RC-06** | ระบบต้องแจ้งเตือนสถานะคำขอจอง (อนุมัติ/ปฏิเสธ/ยกเลิก) ให้ผู้ใช้งานทราบผ่าน Web Notification และ Email สถาบัน | Functional / Usability | E-07, C-04 | Candidate | Medium | ยืนยันรูปแบบข้อความแจ้งเตือนและช่องทางการส่ง Email สถาบัน |
| **RC-07** | ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนที่เจ้าหน้าที่ส่งมอบและรับคืนอุปกรณ์หน้าเคาน์เตอร์ | Functional / Inventory | E-08 | Candidate | High | ยืนยันฟิลด์ข้อมูลที่ต้องบันทึกตอนรับ-คืน และการอัปเดตสต็อกอุปกรณ์ |
| **RC-08** | ระบบต้องบันทึกประวัติการดำเนินงาน (Audit Log) ทุกขั้นตอน ทั้งการสร้างคำขอ การอนุมัติ การยกเลิก และการส่งมอบอุปกรณ์ โดยไม่อนุญาตให้แก้ไข Log ย้อนหลัง | Functional / Security | E-09 | Candidate | High | ยืนยันโครงสร้างตาราง Audit Log ระยะเวลาการเก็บรักษา และสิทธิ์การเข้าถึงข้อมูล |
| **RC-09** | ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการเข้าใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติผู้ไม่มาตามนัด (No-show) สำหรับผู้บริหารและผู้จัดการพื้นที่ | Functional / Reporting | E-10 | Candidate | Medium | ยืนยันตัวกรองข้อมูล รูปแบบกราฟ/ตาราง และตัวชี้วัดที่ผู้บริหารต้องการ |

---

## 3. Coverage and traceability matrix

| Week 02 source | Week 03 objective/questions | Week 04 evidence/negotiation | Candidate |
|---|---|---|---|
| F-01, OQ-01 | EO-01; Q-01–Q-03 | E-01, E-02 | **RC-01** |
| F-02, OQ-01 | EO-01; Q-01–Q-03 | E-03, C-01 | **RC-02** |
| OQ-01 | EO-01; Q-01 | E-04, C-01 | **RC-03** |
| F-03, OQ-02 | EO-02; Q-04–Q-06 | E-05 | **RC-04** |
| OQ-03 | EO-03; Q-07–Q-08 | E-06, C-02, C-03 | **RC-05** |
| F-04, OQ-03 | EO-03; Q-08 | E-07, C-04 | **RC-06** |
| F-05, OQ-04 | EO-04; Q-09–Q-10 | E-08 | **RC-07** |
| AS-01 | EO-04; Q-11 | E-09 | **RC-08** |
| F-06 | EO-04; Q-12 | E-10 | **RC-09** |

---

## 4. Quality review

| Check | Result | Note |
|---|---|---|
| **Traceable** | Pass | Candidate (RC) ทุกข้อเชื่อมโยงกับ Evidence (E-ID) และ Decision ใน Week 04 ชัดเจน |
| **No unsupported approval** | Pass | คงสถานะ Candidate และ Provisional ตามหลักฐานที่มี ไม่แอบอ้างการอนุมัติจริง |
| **Solution-neutral** | Pass | ยังไม่ระบุเฟรมเวิร์ก เทคโนโลยีฐานข้อมูล หรือดีไซน์หน้าจอ UI ที่เกินกว่า Evidence |
| **Atomic enough for Week 05** | Pass | แต่ละ RC มีขอบเขตชัดเจน สามารถนำไปจัดทำ User Story / Functional Specification ต่อใน Week 05 ได้ |
| **Privacy / Security** | Pass | RC-08 ครอบคลุม Audit Log และการควบคุมสิทธิ์การเข้าถึงข้อมูลตามนโยบายความเป็นส่วนตัว |
| **Testability direction** | Pass | ทุก RC มี Acceptance Hint ชัดเจน สำหรับใช้เขียน Acceptance Criteria ใน Week 06 |

---

## 5. Week 05 handoff backlog

### Analysis tasks

1. จัดประเภท Functional / Business Rule / NFR / Data / Interface สำหรับระบบเว็บไซต์
2. แยก RC ที่มีหลาย concern ออกเป็น Sub-requirements (เช่น แยกการจองพื้นที่ออกจากอุปกรณ์)
3. กำหนด Dependency: RC-02/RC-03 ต้องทำหลัง RC-01; RC-05 ขึ้นอยู่กับระบบ Timer/Cron Job
4. จัด Priority ด้วย Value / Risk / Dependency โดยไม่อิงตามความชอบส่วนบุคคล
5. คงสถานะ Issues ของ C-02/C-03 เป็น Unresolved หรือ Provisional เพื่อรอการ Verify เพิ่มเติม

### Do not do yet

- อย่าเพิ่งกำหนดอัลกอริทึมการลงโทษ No-show หรือระยะเวลาแบนที่ยังไม่มีเอกสารอนุมัติจริง
- อย่าฟันธงเลือกใช้ Framework, Database หรือ Third-party Mail API เฉพาะเจาะจง
- อย่าเลื่อนสถานะจาก Provisional เป็น Approved หากยังไม่ได้ผ่านการตรวจสอบสิทธิ์กับ Stakeholder ตัวจริง