# ระบบจองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้
## Software Requirements Specification (SRS) — Draft v1

> **Document ID:** CASE01-SRS-W07-v1 | **Version:** 0.1-draft | **Status:** Baseline Candidate  
> **Team:** Group 5 (วรสิทธิ์ บุญยปรีดี, ปริษฎา สุทธดุก)  
> **Source:** `docs/05-requirement-backlog.md` (v1.2) · `docs/06-requirement-models.md`

---

## 1. บทนำ (Introduction)

### 1.1 จุดประสงค์
เอกสาร SRS ฉบับนี้กำหนดข้อกำหนดความต้องการของ **เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้** เพื่อให้ทีมพัฒนา ผู้ตรวจสอบ และผู้มีส่วนได้ส่วนเสียเข้าใจตรงกัน และใช้เป็นฐานในการออกแบบระบบ Week 08 ต่อไป

### 1.2 ปัญหาและเป้าหมาย

ปัญหาที่พบจาก Case Card และการรวบรวมหลักฐาน (docs/04):

| ปัญหา | หลักฐาน | เป้าหมาย |
|---|---|---|
| จองห้องซ้ำซ้อน (Double Booking) เพราะไม่มีสถานะ Real-time | E-01 (Case Card) | แสดงสถานะว่างแบบ Real-time และป้องกัน Double Booking |
| ต้องเดินถามหรือแชตส่วนตัว ทำให้เสียเวลา | E-01, E-02 | จองผ่านเว็บได้ตลอด 24 ชม. |
| ไม่มีระบบติดตามการยืม-คืนอุปกรณ์ | E-08 | บันทึก Asset ID และสภาพอุปกรณ์ทุกรายการ |
| มีการจองทิ้งไว้โดยไม่มาใช้ (No-show) | E-06, C-02 | ตัดสิทธิ์อัตโนมัติหากไม่ Check-in ภายใน 15 นาที |

### 1.3 ขอบเขตระบบ (Product Scope)

**อยู่ใน Scope:**
- ค้นหาและตรวจสอบสถานะว่างของห้องและอุปกรณ์แบบ Real-time
- จองห้องกลุ่มพร้อมระบุอุปกรณ์เสริมในขั้นตอนเดียว
- เจ้าหน้าที่อนุมัติ/ปฏิเสธคำขอจองห้อง
- Check-in ด้วย QR Code และตัดสิทธิ์ No-show อัตโนมัติ
- บันทึกการรับ-คืนอุปกรณ์พร้อมสภาพ

**อยู่นอก Scope** *(ตาม CASE_CARD.md)*:
- ระบบชำระเงินออนไลน์ (ใช้ Penalty Points แทน)
- เชื่อมต่อกลอนประตู IoT (ใช้ QR Code + เจ้าหน้าที่ให้กุญแจแทน)
- ระบบแนะนำห้องด้วย AI (เลื่อนไป Future Scope — มติ W06)

---

## 2. ภาพรวมระบบ (Overall Description)

### 2.1 บริบทผลิตภัณฑ์
ระบบเป็น **Responsive Web Application** รองรับ Desktop และ Mobile Browser (375px ขึ้นไป) ทำหน้าที่เป็น System of Record การจัดการตารางห้อง สถานะอุปกรณ์ และประวัติการทำรายการ ประสานงานกับผู้ใช้ผ่าน Web Notification และ Email สถาบัน

### 2.2 ผู้ใช้งานและสิทธิ์

| Actor | เป้าหมาย | สิ่งที่ทำได้ | ข้อจำกัด |
|---|---|---|---|
| **นักศึกษา / บุคลากร** | ค้นหาและจองห้อง/อุปกรณ์ | ค้นหา, สร้างคำขอจอง, ยกเลิกล่วงหน้า, Check-in | จองได้ ≤ 3 ชม./วัน, ล่วงหน้า ≤ 7 วัน |
| **เจ้าหน้าที่ (Staff)** | บริหารคำขอและอุปกรณ์ | อนุมัติ/ปฏิเสธคำขอ, บันทึกรับ-คืนอุปกรณ์ | ไม่แก้ไข Audit Log |
| **ผู้ดูแลระบบ (Admin)** | ควบคุมความปลอดภัยและกฎระบบ | จัดการ RBAC, ตั้งค่าพารามิเตอร์, ดู Audit Log | ไม่ลบ Audit Log |
| **อาจารย์ / ผู้บริหาร** | ติดตามสถิติ | ดู Dashboard, Export รายงาน | ดูอย่างเดียว ไม่แก้ไขข้อมูล |

*(ที่มา: CASE_CARD.md, docs/00-project-profile.md, E-02, E-03)*

### 2.3 ข้อจำกัดและข้อสมมติ

| ID | ประเภท | ข้อความ | ที่มา |
|---|---|---|---|
| CT-01 | Technical | ต้องพัฒนาเป็น Responsive Web (Mobile-Friendly) | CASE_CARD.md |
| CT-02 | Scope | Phase 1 ไม่รวมระบบชำระเงินและ IoT | CASE_CARD.md |
| CT-03 | Security | Audit Log ต้องเป็น Append-Only ห้ามแก้ไขหรือลบ | E-09 |
| AS-01 | Assumption | ผู้ใช้ทุกคนมีบัญชีสถาบันและ Login ผ่านระบบกลาง | W04 |
| AS-02 | Assumption | No-show เกิน 15 นาทีระบบตัดสิทธิ์อัตโนมัติ (รอยืนยัน Policy ลายลักษณ์อักษร) | C-02, E-06 |

---

## 3. ข้อกำหนดเชิงฟังก์ชัน (Functional Requirements)

*ID คง Baseline จาก docs/05-requirement-backlog.md v1.2*

| ID | ข้อกำหนด | ที่มา | Priority | สถานะ |
|---|---|---|---|---|
| **FR-01** | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่เลือกภายใน 3 วินาที และส่งคำขอจองได้สำเร็จพร้อมแสดงรหัสคำขอจอง | E-01, E-02 → RC-01 | Must | Ready |
| **FR-02** | ระบบต้องมีหน้าจอให้เจ้าหน้าที่กดอนุมัติหรือปฏิเสธคำขอจองห้อง พร้อมบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที | E-03, C-01 → RC-02 | Must | Ready |
| **FR-03** | ระบบต้องยกเลิกคำขอจองอัตโนมัติหากผู้ใช้ไม่มาเช็กอินภายใน 15 นาทีหลังถึงเวลาจอง | E-06, C-02 → RC-05 | Could | รอ Policy ลายลักษณ์อักษร (OI-01) |
| **FR-04** | ระบบต้องส่งแจ้งเตือนสถานะคำขอ (อนุมัติ/ปฏิเสธ/ยกเลิก) ผ่าน Web Notification และ Email สถาบันภายใน 5 วินาที | E-07, C-04 → RC-06 | Should | รอสเปก Email API (OI-02) |
| **FR-05** | ระบบต้องรองรับการบันทึก Asset ID และสภาพอุปกรณ์ในขั้นตอนส่งมอบและรับคืนหน้าเคาน์เตอร์ | E-08 → RC-07 | Must | Ready |
| **FR-06** | ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติ No-show สำหรับผู้บริหาร | E-10 → RC-09 | Could | รอยืนยัน KPI จากผู้บริหาร (OI-03) |

---

### Deep Specification — FR-01 (ค้นหาและจองพื้นที่/อุปกรณ์)

> *(เลือก FR-01 เพราะเป็น Core Flow หลักที่สุดของระบบ)*

| ฟิลด์ | รายละเอียด |
|---|---|
| **Requirement ID** | FR-01 |
| **Statement** | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่ผู้ใช้ระบุแบบ Real-time และรองรับการส่งคำขอจองพร้อมระบุอุปกรณ์เสริมในขั้นตอนเดียว โดยออก Booking ID ทันทีเมื่อสำเร็จ |
| **Rationale** | แก้ปัญหา Double Booking (E-01) และความยุ่งยากในการประสานงานหลายช่องทาง (E-02) |
| **Trigger** | ผู้ใช้ระบุวัน เวลา จำนวนคน แล้วกดค้นหา หรือกดยืนยันในหน้าสรุปการจอง |
| **เงื่อนไขก่อนทำรายการ** | 1. Login เข้าระบบแล้ว  2. ช่วงเวลาที่เลือก ≤ 3 ชม./วัน และ ≤ 7 วันล่วงหน้า (BR-02)  3. ไม่มีการจองที่ Confirmed ในห้องและเวลาเดียวกัน |
| **ผลลัพธ์ที่คาดหวัง** | 1. ระบบแสดงห้องและอุปกรณ์ที่ว่างตามเงื่อนไข  2. เมื่อยืนยัน: สร้าง Record สถานะ `Pending_Approval` (ห้อง) หรือ `Confirmed` (อุปกรณ์ Auto-approve)  3. แสดงหน้ายืนยันพร้อม Booking ID และ QR Code |
| **Business Rules** | BR-01 (Real-time, จองล่วงหน้า ≤ 7 วัน), BR-02 (โควตา ≤ 3 ชม./วัน) |
| **NFR ที่เกี่ยวข้อง** | NFR-03 (Concurrency Guard), NFR-04 (Response ≤ 3 วินาที) |
| **วิธีตรวจสอบ** | Scenario Test: Login → ค้นหาห้องอีก 2 วันข้างหน้า → เลือก Study Room 1 + ไมโครโฟน 1 ตัว → กดยืนยัน → ระบบต้องออก Booking ID และเปลี่ยนสถานะห้องในปฏิทินทันที |

---

### Deep Specification — FR-02 (อนุมัติ/ปฏิเสธคำขอจองห้อง)

> *(เลือก FR-02 เพราะเป็น Core Workflow ของเจ้าหน้าที่ที่สำคัญที่สุด)*

| ฟิลด์ | รายละเอียด |
|---|---|
| **Requirement ID** | FR-02 |
| **Statement** | ระบบต้องมีหน้าจอสำหรับเจ้าหน้าที่ตรวจสอบคำขอจองที่รอดำเนินการ และกดอนุมัติหรือปฏิเสธได้ โดยต้องบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที |
| **Rationale** | เจ้าหน้าที่ต้องคัดกรองก่อนเปิดใช้ห้อง เพราะผู้ใช้อาจไม่มาจริงหรือมีอาจารย์ขอแทรก (E-03, C-01) |
| **Trigger** | เจ้าหน้าที่เปิดหน้า Pending Queue และกด "อนุมัติ" หรือ "ปฏิเสธ" ในรายการคำขอ |
| **เงื่อนไขก่อนทำรายการ** | 1. Login ด้วยบทบาท `Staff` หรือ `Admin`  2. คำขออยู่ในสถานะ `Pending_Approval`  3. กรณีปฏิเสธ: ต้องระบุเหตุผล (Dropdown หรือข้อความ) |
| **ผลลัพธ์ที่คาดหวัง** | 1. สถานะเปลี่ยนเป็น `Confirmed` (อนุมัติ) หรือ `Rejected` (ปฏิเสธ)  2. บันทึกเวลาและ ID เจ้าหน้าที่ผู้ทำรายการ  3. ปฏิทินห้องอัปเดต และส่งสัญญาณแจ้งเตือนผู้จอง |
| **Business Rules** | BR-01 (ตรวจห้องว่างซ้ำ ณ เวลาอนุมัติ) |
| **NFR ที่เกี่ยวข้อง** | NFR-01 (Audit Log บันทึกทุกการเปลี่ยนสถานะ), NFR-02 (RBAC) |
| **วิธีตรวจสอบ** | Negative Test: กดปฏิเสธโดยไม่กรอกเหตุผล → ระบบต้องไม่บันทึกและแสดง error  Demonstration: กดอนุมัติ → สถานะเปลี่ยนเป็น Confirmed ใน ≤ 3 วินาที |

---

## 4. กฎเกณฑ์ทางธุรกิจ (Business Rules)

| ID | กฎ | ที่มา | Status |
|---|---|---|---|
| **BR-01** | ผู้ใช้จองล่วงหน้าได้ไม่เกิน 7 วัน และข้อมูลสถานะห้องต้องเป็น Real-time | E-05, Policy Doc | Confirmed |
| **BR-02** | จองห้องได้รวมไม่เกิน 3 ชม./วัน และหากไม่ Check-in ภายใน 15 นาที ระบบยกเลิกอัตโนมัติ | E-05, E-06, C-02 | Confirmed (Policy detail รอ OI-01) |
| **BR-03** | ผู้ยืมต้องรับและคืนอุปกรณ์ด้วยตนเองหน้าเคาน์เตอร์ หากอุปกรณ์ชำรุด/สูญหาย ระงับสิทธิ์ชั่วคราวจนกว่าจะตรวจสอบ | E-08, C-03 | Confirmed |
| **BR-04** | การปรับพารามิเตอร์การจองโดย Admin มีผลเฉพาะรายการ**ใหม่**หลังจากบันทึกเท่านั้น | Policy | Confirmed |

---

## 5. ข้อกำหนดคุณภาพ (Non-Functional Requirements)

| ID | ด้านคุณภาพ | เงื่อนไข / วิธีวัด | ที่มา |
|---|---|---|---|
| **NFR-01** | Auditability | Audit Log ทุก Action ต้อง Append-Only 100% ทดสอบด้วย DB Trigger Review | E-09 |
| **NFR-02** | RBAC Security | ฟังก์ชันข้ามบทบาทต้อง 403 Forbidden ทดสอบด้วย Negative Test | W06 Security Model |
| **NFR-03** | Concurrency Guard | Double Booking ต้องไม่เกิด แม้กดพร้อมกัน ทดสอบด้วย Concurrent Load Simulation | G-01 |
| **NFR-04** | Response Time | แสดงผลหน้าค้นหา ≤ 3 วินาที ที่ 95th Percentile | FR-01 |
| **NFR-05** | Responsive UI | ใช้งานได้บน Desktop (≥1366px) และ Mobile (≥375px) ทดสอบ Cross-device | CASE_CARD.md |

---

## 6. โครงสร้างข้อมูลหลัก (Data Requirements — Conceptual)

> ยังไม่ใช่ Physical Schema เป็นเพียงนิยาม Entity หลัก

| Entity | ข้อมูลหลักที่ต้องเก็บ | เชื่อมกับ | ที่มา |
|---|---|---|---|
| **BookingRequest** | bookingId, requesterId, spaceId, startDateTime, endDateTime, purpose, **status** (Pending_Approval / Confirmed / Rejected / Cancelled / In_Use / Completed / No_Show) | GroupSpace, EquipmentBorrowRecord | FR-01, FR-02, FR-03 |
| **GroupSpace** | spaceId, name, capacity, location, facilitiesList, operationalStatus | BookingRequest | FR-01 |
| **LearningEquipment** | equipmentId, name, category, availableQuantity, **isAutoApprove** | EquipmentItem | FR-01, FR-05 |
| **EquipmentBorrowRecord** | borrowRecordId, bookingId, assetId, dispatchTime, returnTime, **conditionOnReturn** (Normal / Damaged / Lost) | BookingRequest | FR-05 |
| **AuditLog** | logId, timestamp, actorId, actorRole, actionType, targetEntity, previousState, newState | ทุก Entity | NFR-01 |

---

## 7. วงจรสถานะ (Lifecycle Rules)

### ก. สถานะคำขอจองห้อง

```
[Initial] ──ผู้ใช้ยืนยัน──▶ Pending_Approval
Pending_Approval ──Staff อนุมัติ──▶ Confirmed
Pending_Approval ──Staff ปฏิเสธ──▶ Rejected
Pending_Approval / Confirmed ──ผู้ใช้ยกเลิก (≥30 นาทีล่วงหน้า)──▶ Cancelled
Confirmed ──สแกน QR Check-in ใน ≤15 นาที──▶ In_Use
Confirmed ──ไม่ Check-in เกิน 15 นาที──▶ No_Show (Auto)
In_Use ──สิ้นสุดเวลา / Check-out──▶ Completed
```

### ข. สถานะอุปกรณ์รายชิ้น

```
Available ──เจ้าหน้าที่ส่งมอบ──▶ In_Use
In_Use ──คืนสภาพปกติ──▶ Available
In_Use ──คืนสภาพชำรุด──▶ Under_Maintenance
```

*(ที่มา: FR-01, FR-02, FR-03, FR-05, BR-02, US-03, US-04)*

---

## 8. ประเด็นค้างคา (Open Issues)

| ID | คำถาม / TBD | กระทบ ID | Owner | ต้องการภายใน |
|---|---|---|---|---|
| **OI-01** | บทลงโทษ No-show สะสม (ขาดกี่ครั้งระงับสิทธิ์กี่วัน?) ยังไม่มีลายลักษณ์อักษร | FR-03, BR-02 | วรสิทธิ์ บุญยปรีดี | Week 08 |
| **OI-02** | สเปก API และ Credential ระบบ Email สถาบัน รวมถึง Rate Limit | FR-04 | ปริษฎา สุทธดุก | Week 08 |
| **OI-03** | KPI ที่ผู้บริหารต้องการดูบน Dashboard (กราฟอะไร สูตรคำนวณอะไร?) | FR-06 | ปริษฎา สุทธดุก | Week 10 |

---

## 9. แผนการตรวจสอบ (Verification Plan)

| ID | วิธี | FR/BR เป้าหมาย | สิ่งที่ต้องดู |
|---|---|---|---|
| VF-01 | Scenario Test + Negative Test | FR-01, BR-01, BR-02 | จองปกติ / จองเกิน 3 ชม. / จองเกิน 7 วัน / จองซ้อนเวลา |
| VF-02 | Demonstration | FR-02 | Staff อนุมัติ/ปฏิเสธ, บังคับใส่เหตุผลกรณีปฏิเสธ |
| VF-03 | Automated Scheduled Test | FR-03, BR-02 | Background Worker ตัด No_Show หลัง 15 นาที |
| VF-04 | Inspection | FR-04 | Event trigger แจ้งเตือน, Log การส่ง Mail |
| VF-05 | DB Trigger Review | FR-05, NFR-01 | Audit Log Append-Only, บันทึกสภาพอุปกรณ์ครบ |

---

## Appendix A — Requirement Disposition (จาก W05 Backlog)

| Backlog ID | Priority | Admission | Disposition | SRS Section |
|---|---|---|---|---|
| FR-01 | Must | Core | Included — Deep Spec | หัวข้อ 3 |
| FR-02 | Must | Core | Included — Deep Spec | หัวข้อ 3 |
| FR-03 | Could | Supporting | Included (รอ OI-01) | หัวข้อ 3 |
| FR-04 | Should | Supporting | Included (รอ OI-02) | หัวข้อ 3 |
| FR-05 | Must | Core | Included | หัวข้อ 3 |
| FR-06 | Could | Extension | Included บางส่วน (รอ OI-03) | หัวข้อ 3 |
| BR-01 | Should | Supporting | Included | หัวข้อ 4 |
| BR-02 | Must | Core | Included | หัวข้อ 4 |
| NFR-01 | Must | Core | Included | หัวข้อ 5 |

> **หมายเหตุ:** FR-07 (Special Space), FR-08 (Admin Config), FR-10 (Audit Log View), FR-12 (RBAC) และ BR-06 (Admin ≥ 1 คน) จาก W06 Models — รับเข้า SRS ฉบับนี้ผ่าน US-07 (BR-04), NFR-02 (RBAC) และ NFR-01 (Audit) ตามลำดับ โดยยังไม่กำหนด FR ID ใหม่จนกว่าจะมี Change Request อย่างเป็นทางการ

---

## Appendix B — AI Use Disclosure

| กิจกรรม | ความช่วยเหลือจาก AI | การตรวจสอบโดยทีม |
|---|---|---|
| โครงร่างและจัดตาราง SRS | ใช้ Antigravity (Gemini) ช่วยจัดโครงสร้างและผสานเนื้อหาจาก W01–W06 | ตรวจสอบ ID ทุกตัว (FR, BR, NFR) เทียบกับ Backlog และตัดเนื้อหาที่อยู่นอก Scope ออก |
| Deep Specification (FR-01, FR-02) | AI ช่วยร่างตาราง Field-Value | แก้ไขเงื่อนไขเวลาให้ตรงตามมติเคส (15 นาที, 3 ชม., 7 วัน) |
