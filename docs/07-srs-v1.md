# ระบบจองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้ — Software Requirements Specification Draft v1

## 0. Document Control

| Field | Value |
|---|---|
| Case ID | `CASE-01` |
| Document ID | `CASE01-SRS-W07-v1` |
| Version | `0.1-draft` |
| Status | Baseline Candidate |
| Team/Owner | Group 5 (วรสิทธิ์ บุญยปรีดี, ปริษฎา สุทธดุก) |
| W05 source snapshot | `docs/05-requirement-backlog.md` (v1.2 Baseline Locked, 2026-08-18) |
| W06 source snapshot | `docs/06-requirement-models.md` (W06 Baseline Candidate, 2026-08-25) |

---

## 1. Introduction

### 1.1 Purpose
เอกสารฉบับนี้จัดทำขึ้นเพื่อกำหนดข้อกำหนดความต้องการเชิงซอฟต์แวร์ (Software Requirements Specification: SRS) สำหรับ **ระบบเว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้ (Group Space and Learning Equipment Booking Website)** ในระดับ Baseline Candidate สำหรับการตรวจประเมิน Week 07 ของรายวิชา ENGSE206 เพื่อให้ผู้พัฒนา ผู้ตรวจสอบคุณภาพ (QA) และผู้มีส่วนได้ส่วนเสีย (Stakeholders) มีความเข้าใจร่วมกันในขอบเขต พฤติกรรมการทำงาน กฎเกณฑ์ทางธุรกิจ และเป็นเกณฑ์อ้างอิงในการออกแบบสถาปัตยกรรมระบบใน Week 08 ต่อไป

### 1.2 Problem and Goals

| Goal | Desired outcome | Source | Status |
|---|---|---|---|
| `G-01` ขจัดปัญหาการจองพื้นที่ซ้ำซ้อน (Zero Double Booking) | ระบบแสดงสถานะห้องว่างแบบเรียลไทม์ และมีระบบป้องกันการอนุมัติช่วงเวลาทับซ้อน (Concurrency Guard) | E-01, E-02 | Fact / Decision |
| `G-02` รวมศูนย์การจองพื้นที่และยืมอุปกรณ์ (Unified Self-Service) | ผู้ใช้งานสามารถค้นหาและจองห้องทำงานกลุ่มพร้อมระบุอุปกรณ์เสริมได้ในขั้นตอนเดียวผ่านเว็บ | E-02, C-01 | Fact / Decision |
| `G-03` ติดตามทรัพยากรและตรวจสภาพอุปกรณ์อย่างโปร่งใส | เจ้าหน้าที่มีระบบบันทึกรหัสครุภัณฑ์ (Asset ID) และบันทึกสภาพอุปกรณ์ทั้งตอนส่งมอบและรับคืน | E-08, E-09 | Fact / Decision |
| `G-04` จัดสรรทรัพยากรอย่างเป็นธรรมและลดปัญหา No-show | มีระบบตรวจจับและยกเลิกคำขออัตโนมัติหากไม่มาเช็กอินภายในเวลาที่กำหนด พร้อมเก็บบันทึกประวัติ | E-06, C-02 | Decision / Assumption |

### 1.3 Product Scope

| In Scope | Out of Scope / Extension | Reason/source |
|---|---|---|
| การค้นหาและตรวจสอบสถานะว่างของห้องและอุปกรณ์แบบเรียลไทม์ | การเชื่อมต่อกลอนประตูดิจิทัลอัจฉริยะ (IoT Smart Lock) | CASE_CARD.md กำหนดให้ใช้การสแกน QR Code หรือติดต่อเจ้าหน้าที่หน้าเคาน์เตอร์เพื่อรับกุญแจแทน |
| การจองห้องกลุ่มพร้อมอุปกรณ์เสริมในขั้นตอนเดียว | ระบบชำระเงินและคิดค่าปรับออนไลน์ (Payment Gateway) | CASE_CARD.md และการเจรจา Week 04 สรุปให้ใช้ระบบตัดแต้มความประพฤติ (Penalty Points) และระงับสิทธิ์แทน |
| ระบบพิจารณาอนุมัติ/ปฏิเสธคำขอจองห้องโดยเจ้าหน้าที่ | ระบบแนะนำห้องจองอัตโนมัติด้วยปัญญาประดิษฐ์ (AI Recommendation) | มติ Week 06 เลื่อนเป็น Future Scope เพื่อมุ่งเน้นระบบคัดกรองตามเงื่อนไข (Filtering) ให้เสถียร |
| การบันทึกรับ-คืนอุปกรณ์พร้อมบันทึกสภาพ (ปกติ/ชำรุด) | การจัดการสต็อกครุภัณฑ์ข้ามวิทยาเขต | จำกัดขอบเขตเฉพาะพื้นที่และอุปกรณ์ภายในศูนย์การเรียนรู้ที่กำหนด |
| การเช็กอินเข้าใช้งาน (Check-in) และการตัดสิทธิ์ No-show | การติดตามพิกัด GPS ผู้ใช้งานแบบเรียลไทม์ | อยู่นอกเหนือข้อตกลงและป้องกันปัญหาความเป็นส่วนตัวของข้อมูล |

### 1.4 Definitions

| Term | Meaning | Source/Decision |
|---|---|---|
| Group Space | พื้นที่หรือห้องติวสำหรับการทำงานร่วมกันเป็นกลุ่มของนักศึกษาและบุคลากร | Case Card |
| Learning Equipment | อุปกรณ์สนับสนุนการเรียนรู้ที่เปิดให้ยืม (เช่น หัวแปลงสัญญาณ, เว็บแคม, ไมโครโฟน, สายสัญญาณ) | Case Card |
| Double Booking | สภาวะที่มีคำขอจองได้รับการยืนยันมากกว่าหนึ่งรายการในพื้นที่และช่วงเวลาเดียวกัน | Problem Brief |
| Auto-cancellation (No-show) | การที่ระบบตัดสิทธิ์และยกเลิกรายการจองโดยอัตโนมัติเมื่อผู้จองไม่มาแสดงตนภายในเวลาที่กำหนด | TD-Policy / E-06 |
| Check-in | การยืนยันการเข้าใช้งานพื้นที่จริงผ่านการสแกน QR Code หน้าห้องหรือจุดบริการ | US-04 / AC-04 |
| Audit Log | บันทึกประวัติเหตุการณ์สำคัญในระบบที่ไม่สามารถลบหรือแก้ไขได้ ใช้สำหรับการตรวจสอบย้อนหลัง | NFR-01 / AC-09 |

---

## 2. Overall Description

### 2.1 Product Context
ระบบเป็น Web Application ที่ทำงานบนสถาปัตยกรรมแบบ Responsive Web รองรับการใช้งานผ่าน Desktop และ Mobile Browser โดยทำหน้าที่เป็น System of Record ในการจัดสรรตารางเวลาการใช้พื้นที่ (Calendar Schedule) การจัดการสถานะคำขอจอง และการควบคุมสต็อกอุปกรณ์การเรียนรู้ ระบบมีการประสานงานกับผู้ใช้งานผ่าน Web Notification และ Email Service โดยในเฟสนี้ยังไม่มีการพึ่งพา Hardware ภายนอกหรือระบบการเงิน

### 2.2 User Classes and Authority

| Actor | Goal | Authorized actions | Restrictions | Source |
|---|---|---|---|---|
| `ACT-01` นักศึกษา / บุคลากร (Requester) | ค้นหา จอง ยกเลิกการจอง และเช็กอินเข้าใช้งานพื้นที่/อุปกรณ์ | ค้นหาทรัพยากร, สร้างคำขอจอง, ขอยกเลิกล่วงหน้า, สแกน Check-in, ดูประวัติตนเอง | ไม่สามารถอนุมัติคำขอตนเอง, จองได้ไม่เกิน 3 ชม./วัน และล่วงหน้าไม่เกิน 7 วัน | Case Card / E-01 |
| `ACT-02` เจ้าหน้าที่ดูแล (Staff) | บริหารจัดการการใช้งาน จัดสรรห้อง และควบคุมการยืม-คืนอุปกรณ์ | ตรวจสอบคำขอ, กดอนุมัติ/ปฏิเสธคำขอจอง, บันทึกการส่งมอบและรับคืนอุปกรณ์, ตรวจสภาพอุปกรณ์ | ไม่สามารถแก้ไขกฎเกณฑ์ของระบบ (Policy) หรือแก้ไขบันทึก Audit Log | Case Card / E-03 |
| `ACT-03` ผู้ดูแลระบบ (System Admin) | ควบคุมความปลอดภัย สิทธิ์ผู้ใช้งาน และกฎเกณฑ์ของระบบ | กำหนดพารามิเตอร์การจอง, จัดการบทบาทสิทธิ์ (RBAC), ตรวจสอบ Audit Log, จัดการข้อมูลห้อง/อุปกรณ์ | ไม่สามารถลบประวัติการทำรายการใน Audit Log ได้ตามกฎ NFR-01 | Case Card / US-07 |
| `ACT-04` อาจารย์ / ผู้บริหาร (Executive/Observer) | ติดตามสถิติเพื่อการวางแผนและปรับปรุงทรัพยากร | เรียกดู Dashboard สรุปสถิติอัตราการใช้พื้นที่และอุปกรณ์, Export รายงานสถิติ | ดูข้อมูลเชิงสถิติและภาพรวมเท่านั้น ไม่สามารถอนุมัติหรือดัดแปลงข้อมูลการจอง | Case Card / US-08 |

### 2.3 Capabilities

| CAP | Capability | FR/BR/NFR/DR | US/UC/AC | Coverage |
|---|---|---|---|---|
| `CAP-01` Space & Equipment Availability Checking | ตรวจสอบตารางและสถานะความพร้อมของทรัพยากรแบบเรียลไทม์ | FR-01, BR-01, DR-02, DR-03 | US-01, UC-01, AC-01 | Detailed |
| `CAP-02` Booking Request Management | การสร้างและส่งคำขอจองพื้นที่พร้อมอุปกรณ์เสริม | FR-01, BR-02, DR-01 | US-02, UC-01, AC-02 | Detailed |
| `CAP-03` Request Review & Approval Workflow | กระบวนการตรวจสอบและพิจารณาอนุมัติ/ปฏิเสธคำขอจอง | FR-02, BR-01, DR-01 | US-06, UC-03, AC-06 | Detailed |
| `CAP-04` Check-in & No-Show Lifecycle Handling | การยืนยันเข้าใช้งานและการยกเลิกอัตโนมัติเมื่อผิดนัด | FR-03, BR-02, DR-01 | US-03, US-04, UC-02, AC-03, AC-04 | Partial (Policy TBD) |
| `CAP-05` Equipment Dispatch & Return Inspection | การส่งมอบ ตรวจรับคืน และบันทึกสภาพอุปกรณ์ | FR-05, BR-03, DR-04 | US-05, UC-03, AC-05 | Detailed |
| `CAP-06` Audit Logging & Compliance | การบันทึกหลักฐานเหตุการณ์ระบบที่ห้ามแก้ไขย้อนหลัง | NFR-01, BR-05, DR-05 | US-09, UC-05, AC-09 | Detailed |

### 2.4 Constraints and Assumptions

| ID | Type | Statement | Source | Status/next action |
|---|---|---|---|---|
| `CT-01` | Technical Constraint | ระบบต้องพัฒนาในรูปแบบ Responsive Web Application รองรับการแสดงผลทั้ง Desktop และ Mobile Browser | CASE_CARD.md | Confirmed |
| `CT-02` | Scope Constraint | ระบบเฟสแรกต้องไม่มีระบบชำระเงินออนไลน์ และไม่มีการเชื่อมต่อกลอนประตู IoT | CASE_CARD.md | Confirmed |
| `CT-03` | Security Constraint | ข้อมูลบันทึกเหตุการณ์ (Audit Log) ต้องเป็นแบบ Append-Only ไม่อนุญาตให้แก้ไขหรือลบผ่าน UI หรือ API ใดๆ | NFR-01 / W05 Backlog | Confirmed |
| `AS-01` | Operational Assumption | ผู้ใช้งานทุกคนมีบัญชีผู้ใช้ของสถาบัน และสามารถเข้าสู่ระบบผ่านการ Authentication กลางได้ | W04 Assumption | Confirmed |
| `AS-02` | Policy Assumption | การผิดนัดไม่มาใช้บริการ (No-show) เกิน 15 นาที ระบบจะตัดสิทธิ์และปลดล็อกห้องให้ผู้อื่นทันที | TD-Policy / W05 Backlog | Pending Owner Sign-off |

### 2.5 External Interfaces

| ID | System | Data/direction | Core/Extension | TBD/failure concern |
|---|---|---|---|---|
| `EXT-01` | Institutional Email Service | ส่งข้อความแจ้งเตือนผลการจอง/การยกเลิก (Outbound SMTP/API) | Supporting | มีแผนรองรับ In-App Notification หากบริการ Email ล่าช้าหรือขัดข้อง (OI-02) |
| `EXT-02` | Central Authentication System | ตรวจสอบสิทธิ์และดึงข้อมูลพื้นฐานผู้ใช้ (Inbound/SSO) | Core | หากระบบล่ม ผู้ใช้จะไม่สามารถเข้าสู่ระบบได้ ต้องมีแผนสำรองใน Week 08 |

---

## 3. Functional Requirements

จัดกลุ่มตาม Capability และคง ID ตาม `docs/05-requirement-backlog.md`

| FR | Requirement | Source | Priority/admission | BR/NFR/DR | US/UC/AC | Status |
|---|---|---|---|---|---|---|
| `FR-01` | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่เลือกภายใน 3 วินาที และส่งคำขอจองได้สำเร็จพร้อมแสดงรหัสคำขอจอง | E-01, E-02 → RC-01 | Must / Core | BR-01, BR-02, DR-01, DR-02, DR-03 | US-01, US-02; UC-01; AC-01, AC-02 | Detailed |
| `FR-02` | ระบบต้องมีหน้าจอให้เจ้าหน้าที่กดอนุมัติหรือปฏิเสธคำขอจองห้อง พร้อมบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที | E-03, C-01 → RC-02 | Must / Core | BR-01, DR-01, DR-05 | US-06; UC-03; AC-06 | Detailed |
| `FR-03` | ระบบต้องยกเลิกคำขอจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาเช็กอินเข้าใช้พื้นที่ภายใน 15 นาทีหลังจากถึงเวลาจอง | E-06, C-02, C-03 → RC-05 | Could / Supporting | BR-02, DR-01 | US-04; UC-02; AC-04 | Partial (Policy Detail in OI-01) |
| `FR-04` | ระบบต้องส่งข้อความแจ้งเตือนสถานะคำขอจอง (อนุมัติ/ปฏิเสธ/ยกเลิก) ให้ผู้ใช้งานทราบผ่าน Web Notification และ Email สถาบันภายใน 5 วินาทีหลังเกิดเหตุการณ์ | E-07, C-04 → RC-06 | Should / Supporting | DR-01, EXT-01 | US-06; UC-03; AC-06 | Partial (Format & API in OI-02) |
| `FR-05` | ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนที่เจ้าหน้าที่ส่งมอบและรับคืนอุปกรณ์หน้าเคาน์เตอร์ | E-08 → RC-07 | Must / Core | BR-03, DR-04 | US-05; UC-03; AC-05 | Detailed |
| `FR-06` | ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการเข้าใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติผู้ไม่มาตามนัด (No-show) สำหรับผู้บริหาร | E-10 → RC-09 | Could / Extension | DR-01, DR-04 | US-08; UC-05; AC-08 | Partial (KPI Metrics in OI-04) |

---

### Detailed Requirement Records (Deep Specification)

#### Record 1: FR-01 ค้นหาและส่งคำขอจองห้องพร้อมอุปกรณ์

| Field | Value |
|---|---|
| Requirement ID | `FR-01` |
| Statement | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องทำงานกลุ่มและอุปกรณ์การเรียนรู้ตามช่วงเวลาที่ผู้ใช้ระบุได้แบบเรียลไทม์ และรองรับการส่งคำขอจองห้องพร้อมระบุอุปกรณ์เสริมในขั้นตอนเดียว โดยออกรหัสการจอง (Booking ID) ทันทีที่ทำรายการสำเร็จ |
| Rationale/Goal | `G-01`, `G-02` ขจัดปัญหาการจองคิวซ้ำซ้อน และลดความยุ่งยากในการประสานงานหลายช่องทาง |
| Source | E-01 (นักศึกษาต้องการรู้ห้องว่างทันที), E-02 (ต้องการจองอุปกรณ์พร้อมห้อง) |
| Priority/Admission | Must / Core |
| Trigger | ผู้ใช้งานระบุวัน เวลา จำนวนคน และกดค้นหา หรือกดปุ่ม "ยืนยันการจอง" ในหน้าสรุปข้อมูล |
| Preconditions/guards | 1. ผู้ใช้งานผ่านการ Login เข้าสู่ระบบแล้ว <br> 2. ช่วงเวลาที่เลือกต้องไม่เกิน 3 ชั่วโมง/วัน และไม่เกิน 7 วันล่วงหน้า (ตาม BR-02) <br> 3. ไม่มีคำขอจองอื่นที่ได้รับอนุมัติในห้องและช่วงเวลาเดียวกันอยู่ก่อนหน้า |
| Expected result | 1. ระบบแสดงตารางห้องและอุปกรณ์ที่ว่างตรงตามเงื่อนไข <br> 2. เมื่อยืนยันการจอง ระบบจะสร้างเรคอร์ดคำขอจองในสถานะ `Pending_Approval` (สำหรับห้อง) หรือ `Confirmed` (สำหรับอุปกรณ์ Auto-approve) <br> 3. ระบบแสดงหน้าจอยืนยันสำเร็จพร้อมรหัส Booking ID และ QR Code สำหรับเตรียม Check-in |
| BR/NFR/DR links | BR-01, BR-02; NFR-03 (Concurrency Guard), NFR-04; DR-01, DR-02, DR-03 |
| US/UC/AC links | US-01, US-02; UC-01; AC-01, AC-02 |
| Verification | **Method:** Scenario Test + Demonstration <br> **Scenario:** ทดสอบผู้ใช้ล็อกอิน ค้นหาห้องในอีก 2 วันข้างหน้า เลือกห้อง Study Room 1 พร้อมไมโครโฟน 1 ตัว กดยืนยัน ระบบต้องบันทึกคำขอ ออกรหัส Booking ID และเปลี่ยนสถานะห้องในปฏิทินทันที |
| Status/TBD | Ready for Design (ข้อมูลฟอร์มขั้นต่ำสรุปแล้วใน DR-01) |

---

#### Record 2: FR-02 การพิจารณาอนุมัติหรือปฏิเสธคำขอจองห้องโดยเจ้าหน้าที่

| Field | Value |
|---|---|
| Requirement ID | `FR-02` |
| Statement | ระบบต้องจัดเตรียมหน้าจอสำหรับเจ้าหน้าที่ผู้ดูแล (Staff) เพื่อตรวจสอบรายการคำขอจองห้องที่รอดำเนินการ และรองรับการกด "อนุมัติ (Approve)" หรือ "ปฏิเสธ (Reject)" โดยต้องบันทึกเหตุผลประกอบและเปลี่ยนสถานะคำขอภายใน 3 วินาที |
| Rationale/Goal | `G-01` ป้องกันการใช้ห้องผิดวัตถุประสงค์ และให้เจ้าหน้าที่สามารถจัดสรรห้องพิเศษได้อย่างเหมาะสม |
| Source | E-03 (เจ้าหน้าที่ต้องการระบบคัดกรองคำขอ), C-01 (ข้อตกลงเรื่องการอนุมัติ) |
| Priority/Admission | Must / Core |
| Trigger | เจ้าหน้าที่เปิดหน้ารายการรอดำเนินการ (Pending Queue) และกดปุ่ม "อนุมัติ" หรือ "ปฏิเสธ" ในรายการคำขอ |
| Preconditions/guards | 1. เจ้าหน้าที่ต้องมีสิทธิ์บทบาท `Staff` หรือ `Admin` <br> 2. คำขอจองนั้นต้องอยู่ในสถานะ `Pending_Approval` <br> 3. กรณีปฏิเสธ เจ้าหน้าที่ต้องระบุเหตุผล (เลือกจาก Dropdown หรือกรอกข้อความ) |
| Expected result | 1. สถานะคำขอเปลี่ยนเป็น `Confirmed` (เมื่ออนุมัติ) หรือ `Rejected` (เมื่อปฏิเสธ) <br> 2. ระบบบันทึกเวลาที่อนุมัติและผู้ทำรายการ <br> 3. ปฏิทินการใช้ห้องได้รับการอัปเดต และระบบส่งสัญญาณแจ้งเตือนไปยังผู้จอง |
| BR/NFR/DR links | BR-01, BR-02; NFR-01 (Audit Log), NFR-03; DR-01, DR-05 |
| US/UC/AC links | US-06; UC-03; AC-06 |
| Verification | **Method:** Demonstration + Negative Test <br> **Scenario:** ทดสอบเจ้าหน้าที่กดอนุมัติคำขอ สถานะเปลี่ยนเป็น Confirmed; ทดสอบกดปฏิเสธโดยไม่กรอกเหตุผล ระบบต้องไม่อนุญาตให้บันทึก |
| Status/TBD | Ready for Design |

---

#### Record 3: FR-05 การบันทึกตรวจรับ-ส่งมอบ และตรวจสภาพอุปกรณ์

| Field | Value |
|---|---|
| Requirement ID | `FR-05` |
| Statement | ระบบต้องรองรับการสแกนหรือบันทึกรหัสครุภัณฑ์ (Asset ID) และบันทึกผลการตรวจสอบสภาพอุปกรณ์ (ปกติ / ชำรุด / สูญหาย) ในขั้นตอนที่เจ้าหน้าที่ทำการส่งมอบอุปกรณ์ให้ผู้ยืม และในขั้นตอนการรับคืนอุปกรณ์หน้าเคาน์เตอร์ |
| Rationale/Goal | `G-03` ติดตามผู้รับผิดชอบอุปกรณ์ที่แท้จริง ป้องกันอุปกรณ์สูญหาย และคัดแยกอุปกรณ์ชำรุดออกจากสต็อก |
| Source | E-08 (ปัญหาการคืนอุปกรณ์ล่าช้าและไม่มีบันทึกหลักฐานสภาพของ) |
| Priority/Admission | Must / Core |
| Trigger | เจ้าหน้าที่เปิดรายการยืม-คืนอุปกรณ์ และบันทึกการส่งมอบ (Dispatch) หรือรับคืน (Return) |
| Preconditions/guards | 1. ผู้ยืมต้องมีคำขอจองอุปกรณ์ในสถานะ `Confirmed` <br> 2. เจ้าหน้าที่ต้องระบุสภาพอุปกรณ์เป็น `Normal` หรือ `Damaged` ก่อนกดยืนยันการรับคืน |
| Expected result | 1. ในขั้นตอนส่งมอบ: สถานะอุปกรณ์เปลี่ยนเป็น `In_Use` และสร้างเรคอร์ดการยืมระบุเวลาและผู้รับผิดชอบ <br> 2. ในขั้นตอนรับคืน: สถานะอุปกรณ์เปลี่ยนเป็น `Available` (กรณีปกติ) หรือ `Under_Maintenance` (กรณีชำรุด) พร้อมบันทึกข้อความรายละเอียดความเสียหาย |
| BR/NFR/DR links | BR-03; NFR-01; DR-03, DR-04, DR-05 |
| US/UC/AC links | US-05; UC-03; AC-05 |
| Verification | **Method:** Scenario Test <br> **Scenario:** เจ้าหน้าที่บันทึกการรับคืน Webcam รหัส CAM-001 ระบุสถานะ "Damaged" พร้อมระบุสายขาด ระบบต้องเปลี่ยนสถานะ Webcam เป็น Under_Maintenance และลงบันทึกในประวัติผู้ยืม |
| Status/TBD | Ready for Design (ชุดฟิลด์และตัวเลือกสภาพอุปกรณ์กำหนดชัดใน DR-04) |

---

## 4. Business Rules

| BR | Rule | Authority/source | Affected FR/UC | Status |
|---|---|---|---|---|
| `BR-01` | **การจองล่วงหน้าและระบบแสดงผลเรียลไทม์:** ผู้ใช้สามารถจองพื้นที่และอุปกรณ์ล่วงหน้าได้สูงสุดไม่เกิน 7 วัน และข้อมูลสถานะความว่างต้องเป็นปัจจุบัน (Real-time Availability) | กฎระเบียบศูนย์การเรียนรู้ / TD-01 | FR-01; UC-01; AC-01 | Confirmed |
| `BR-02` | **โควตาเวลาและเกณฑ์ No-Show:** ผู้ใช้แต่ละคนจองห้องทำงานกลุ่มได้รวมกันไม่เกิน 3 ชั่วโมงต่อวัน และหากไม่มาสแกน Check-in ภายใน 15 นาทีหลังจากถึงเวลาเริ่มจอง ระบบจะยกเลิกคำขออัตโนมัติ (Auto-cancellation) เพื่อปล่อยสิทธิ์ให้ผู้อื่น | มติที่ประชุมทีมและผู้จัดการพื้นที่ / TD-02 | FR-01, FR-03; UC-01, UC-02; AC-02, AC-04 | Confirmed for Core (Penalty detail in OI-01) |
| `BR-03` | **การรับผิดชอบและการคืนอุปกรณ์:** ผู้ยืมต้องเป็นผู้รับมอบและส่งคืนอุปกรณ์ด้วยตนเองหน้าเคาน์เตอร์ หากอุปกรณ์ชำรุดหรือสูญหาย ระบบจะบันทึกสถานะ Under_Maintenance และระงับสิทธิ์การจองชั่วคราวของผู้ยืมจนกว่าจะได้รับการตรวจสอบ | กฎหมายครุภัณฑ์สถาบัน / TD-03 | FR-05; UC-03; AC-05 | Confirmed |
| `BR-04` | **การบังคับใช้กฎของระบบ:** การเปลี่ยนแปลงพารามิเตอร์การจอง (เช่น โควตาเวลา หรือระยะเวลาผ่อนปรน No-Show) โดยผู้ดูแลระบบ จะมีผลบังคับใช้เฉพาะรายการจองที่สร้างขึ้นใหม่หลังจากการบันทึกเท่านั้น | ข้อกำหนดด้านความคงสภาพของข้อมูล / TD-04 | FR-01; UC-04; AC-07 | Confirmed |
| `BR-05` | **ความสมบูรณ์ของบันทึกประวัติ (Audit Immutability):** ทุกการเปลี่ยนสถานะคำขอ (Submit, Approve, Reject, Cancel, Check-in, Return) ต้องสร้างเรคอร์ดใน Audit Log เสมอ และห้ามลบหรือแก้ไขเรคอร์ดไม่ว่ากรณีใดๆ | นโยบายความปลอดภัยสารสนเทศ / TD-05 | NFR-01; UC-05; AC-09 | Confirmed |

---

## 5. Non-functional Requirements

| NFR | Quality statement | Context/stimulus | Response/measure | Source | Verification | Status/TBD |
|---|---|---|---|---|---|---|
| `NFR-01` | **ความปลอดภัยและความคงสภาพของข้อมูล (Auditability):** ระบบต้องบันทึก Audit Log ทุกรายการจอง/อนุมัติ/ยกเลิก/คืนอุปกรณ์ พร้อม Timestamp, User ID, Action และไม่อนุญาตให้แก้ไขหรือลบย้อนหลัง | มีการกระทำใดๆ ที่เปลี่ยนสถานะของคำขอจองหรือข้อมูลสต็อก | Audit Log ถูกสร้างขึ้นแบบ Append-only 100% ไม่สามารถลบผ่าน API/UI | E-09 / W05 Backlog | Inspection + DB Trigger Review | Ready |
| `NFR-02` | **การควบคุมสิทธิ์การเข้าถึง (RBAC):** ระบบต้องจำกัดการเข้าถึงฟังก์ชันและข้อมูลตามบทบาท (Student, Staff, Admin, Executive) อย่างเคร่งครัด | ผู้ใช้พยายามเรียกดูข้อมูลหรือยิงคำสั่ง API ข้ามบทบาท | ปฏิเสธการเข้าถึง (403 Forbidden) และไม่เปิดเผยข้อมูลเกินสิทธิ์ | W06 Security Model | Security Penetration / Negative Test | Ready |
| `NFR-03` | **ความถูกต้องของตารางเวลาพร้อมกัน (Concurrency Guard):** ระบบต้องป้องกันไม่ให้เกิดการยืนยันคำขอจองในห้องเดียวกันและช่วงเวลาเดียวกันซ้ำซ้อน (Double Booking) แม้จะมีการกดจองเข้ามาพร้อมกันในเสี้ยววินาที | ผู้ใช้ 2 คนกดส่งคำขอจองห้องเดียวกัน เวลาเดียวกันในจังหวะเดียวกัน | มีเพียงคำขอเดียวที่สำเร็จ อีกคำขอต้องได้รับข้อความแจ้งเตือนห้องถูกจองแล้ว | G-01 / W04 Risk | Concurrent Load Simulation | Ready |
| `NFR-04` | **ประสิทธิภาพการตอบสนอง (Response Time):** ระบบต้องแสดงผลหน้าจอค้นหาสถานะความว่างของห้องและอุปกรณ์ภายในไม่เกิน 3 วินาที ภายใต้การใช้งานพร้อมกันของผู้ใช้ระดับปกติ | ผู้ใช้กดค้นหาตารางว่างในหน้าค้นหา | Render หน้าจอเสร็จสิ้นภายใน $\le 3$ วินาที ที่ 95th Percentile | W05 Backlog FR-01 | Performance Benchmark Test | Ready |
| `NFR-05` | **การรองรับอุปกรณ์ที่หลากหลาย (Usability & Responsiveness):** ระบบต้องแสดงผลและใช้งานฟังก์ชันหลักได้อย่างสมบูรณ์บนทั้งหน้าจอ Desktop และ Mobile Browser (หน้าจอตั้งแต่ 375px ขึ้นไป) | ผู้ใช้เปิดหน้าเว็บผ่านสมาร์ตโฟนเพื่อจองหรือแสดง QR Code | หน้าจอไม่ล้น ไม่ต้องซูม และกดปุ่มเมนูหลักได้อย่างสะดวก | CASE_CARD.md Constraint | Cross-device Walkthrough | Ready |

---

## 6. Data Requirements

กำหนด Conceptual Data Requirements เพื่อระบุโครงสร้างและนิยามข้อมูลหลักของระบบ (ยังไม่ใช่ Physical Database Schema)

| DR | Concept | Requirement / Minimum Data | Relationships | Classification | Source | Status |
|---|---|---|---|---|---|---|
| `DR-01` | `BookingRequest` | ข้อมูลคำขอจองพื้นที่หรืออุปกรณ์ ประกอบด้วย: `bookingId`, `requesterId`, `spaceId` (optional), `startDateTime`, `endDateTime`, `purpose`, `status` (Pending, Confirmed, Rejected, Cancelled, In_Use, Completed, No_Show), `createdAt` | 1 BookingRequest มีได้ 1 GroupSpace และมีได้ 0..* `EquipmentBorrowRecord` | Core Business Transaction | FR-01, FR-02, FR-03 | Ready |
| `DR-02` | `GroupSpace` | ข้อมูลพื้นที่หรือห้องทำงานกลุ่ม ประกอบด้วย: `spaceId`, `name`, `capacity`, `location`, `facilitiesList`, `operationalStatus` (Available, Closed, Maintenance) | 1 GroupSpace สามารถมีประวัติการจองได้หลาย `BookingRequest` | Master Resource Data | FR-01, UC-01 | Ready |
| `DR-03` | `LearningEquipment` | ข้อมูลชนิดและรายการอุปกรณ์การเรียนรู้ ประกอบด้วย: `equipmentId`, `name`, `category`, `totalQuantity`, `availableQuantity`, `isAutoApprove` | 1 LearningEquipment เชื่อมโยงกับ 0..* `EquipmentItem` (ครุภัณฑ์รายชิ้น) | Master Resource Data | FR-01, FR-05 | Ready |
| `DR-04` | `EquipmentBorrowRecord` | ข้อมูลรายการยืม-คืนอุปกรณ์รายชิ้น ประกอบด้วย: `borrowRecordId`, `bookingId`, `assetId` (รหัสครุภัณฑ์), `dispatchTime`, `dispatchStaffId`, `returnTime`, `returnStaffId`, `conditionOnReturn` (Normal, Damaged, Lost) | N EquipmentBorrowRecord อ้างถึง 1 BookingRequest และ 1 Asset ID | Operational Record | FR-05, UC-03 | Ready |
| `DR-05` | `AuditLog` | บันทึกประวัติเหตุการณ์และการเปลี่ยนสถานะ ประกอบด้วย: `logId`, `timestamp`, `actorId`, `actorRole`, `actionType`, `targetEntity`, `targetId`, `previousState`, `newState`, `ipAddress` | เชื่อมโยงแบบอ้างอิงรหัส (Reference) กับ Entity ต่างๆ ในระบบ | System Audit Record (Immutable) | NFR-01, US-09 | Ready |

---

## 7. Behavioral Model References

| Model | IDs/version | Requirement anchors | Coverage/gap | SRS use |
|---|---|---|---|---|
| User Stories | `US-01` ถึง `US-10` (v1.0) | FR-01 ถึง FR-06, BR-01 ถึง BR-06, NFR-01, NFR-02 | ครอบคลุม Actor ครบทั้ง 4 กลุ่ม | ใช้กำหนดพฤติกรรมและความต้องการในมุมมองผู้ใช้ (หัวข้อ 3) |
| Use Cases | `UC-01` ถึง `UC-06` (v1.0) | FR-01 ถึง FR-06, BR-01 ถึง BR-05 | UC-01, UC-02, UC-03 เป็น Detailed Core Flow; UC-04, 05, 06 เป็น Admin Flow | ใช้อธิบาย Main Flow และ Exception Flow (หัวข้อ 3) |
| Acceptance Criteria | `AC-01` ถึง `AC-10` (v1.0) | FR-01 ถึง FR-06, BR-01 ถึง BR-05 | กำหนดเงื่อนไข Given-When-Then ตรวจสอบได้ครบทุกฟังก์ชันหลัก | ใช้อ้างอิงใน Verification Plan (หัวข้อ 11) |

### 7.1 Lifecycle Rules

#### ก. วงจรสถานะคำขอจองพื้นที่ (Booking Request Lifecycle)

| From State | Trigger / Event | To State | Guard / Condition | Source |
|---|---|---|---|---|
| `[Initial]` | ผู้ใช้กดยืนยันการจอง | `Pending_Approval` | ข้อมูลการจองถูกต้อง และผ่านการตรวจเงื่อนไข BR-01, BR-02 | FR-01 / UC-01 |
| `Pending_Approval` | เจ้าหน้าที่กด "อนุมัติ" | `Confirmed` | ตรวจสอบห้องว่างซ้ำ ณ เวลาอนุมัติ และเจ้าหน้าที่ระบุผลอนุมัติ | FR-02 / UC-03 |
| `Pending_Approval` | เจ้าหน้าที่กด "ปฏิเสธ" | `Rejected` | เจ้าหน้าที่ต้องระบุเหตุผลในการปฏิเสธ | FR-02 / UC-03 |
| `Pending_Approval` หรือ `Confirmed` | ผู้ใช้กดยกเลิกคำขอ | `Cancelled` | ขอยกเลิกล่วงหน้าก่อนถึงเวลาเริ่มจองอย่างน้อย 30 นาที | US-03 / UC-02 |
| `Confirmed` | ผู้ใช้สแกน QR Code เพื่อ Check-in | `In_Use` | สแกนตรงจุดบริการภายในช่วงเวลาจอง (ไม่เกิน 15 นาทีหลังเริ่ม) | US-04 / UC-02 |
| `Confirmed` | เวลาเริ่มจองล่วงเลยเกิน 15 นาที | `No_Show` | ผู้ใช้ไม่ทำการสแกน Check-in ตามเกณฑ์ BR-02 (ระบบตัดสิทธิ์อัตโนมัติ) | FR-03 / UC-02 |
| `In_Use` | สิ้นสุดช่วงเวลาจอง หรือผู้ใช้กด Check-out | `Completed` | สิ้นสุดการใช้งานพื้นที่ และส่งคืนอุปกรณ์ครบถ้วน | US-04 / UC-02 |

#### ข. วงจรสถานะอุปกรณ์การเรียนรู้รายชิ้น (Equipment Item Lifecycle)

| From State | Trigger / Event | To State | Guard / Condition | Source |
|---|---|---|---|---|
| `Available` | เจ้าหน้าที่ส่งมอบอุปกรณ์ให้ผู้ยืม | `In_Use` | ผู้ยืมมีคำขอจองในสถานะ `Confirmed` และบันทึกรหัส Asset ID | FR-05 / UC-03 |
| `In_Use` | ผู้ยืมนำอุปกรณ์มาคืนหน้าเคาน์เตอร์ | `Available` | เจ้าหน้าที่ตรวจสภาพแล้วพบว่าอยู่ในสภาพปกติ (`Normal`) | FR-05 / UC-03 |
| `In_Use` | ผู้ยืมนำอุปกรณ์มาคืนหน้าเคาน์เตอร์ | `Under_Maintenance` | เจ้าหน้าที่ตรวจสภาพแล้วพบว่าชำรุด (`Damaged`) ต้องส่งซ่อม | FR-05 / UC-03 |

---

## 8. External Interface Requirements

| Interface | Requirement / Data | Direction | Owner | Failure / Privacy concern | Status |
|---|---|---|---|---|---|
| `EXT-01` Web User Interface | หน้าจอ Responsive UI รองรับการแสดงผลผ่าน Desktop (1366x768 ขึ้นไป) และ Mobile (375x667 ขึ้นไป) | In / Out | ทีมพัฒนาระบบ | การแสดงผลผิดเพี้ยนบนอุปกรณ์หน้าจอขนาดเล็ก ต้องทดสอบ Cross-browser | Core / Ready |
| `EXT-02` Email Gateway Service | ส่งอีเมลยืนยันผลการอนุมัติ/ปฏิเสธคำขอจองไปยังอีเมลสถาบันของผู้ใช้ (`@rmutl.ac.th`) | Outbound | ผู้ให้บริการ Email ของสถาบัน | หาก Mail Server ล่มหรือติด Spam ผู้ใช้อาจไม่ทราบผลการจอง (แก้ปัญหาด้วย In-App Status) | Supporting / TBD (OI-02) |
| `EXT-03` Authentication Interface | รับข้อมูลยืนยันตัวตน (User ID, Role, Full Name) จากระบบล็อกอินสถาบัน | Inbound | ศูนย์คอมพิวเตอร์สถาบัน | หากระบบยืนยันตัวตนล่ม ต้องมีข้อความแจ้งผู้ใช้ชัดเจน | Core / Ready |

---

## 9. Traceability and Coverage

| Source | W05 Requirement | W06 Model | SRS Section | Verification | Coverage |
|---|---|---|---|---|---|
| E-01, E-02 | `FR-01` จองห้องและอุปกรณ์เรียลไทม์ | US-01, US-02; UC-01; AC-01, AC-02 | หัวข้อ 3 (FR-01) | VF-01 (Demonstration + Test) | Fully Covered |
| E-03, C-01 | `FR-02` เจ้าหน้าที่อนุมัติ/ปฏิเสธ | US-06; UC-03; AC-06 | หัวข้อ 3 (FR-02) | VF-02 (Demonstration) | Fully Covered |
| E-06, C-02 | `FR-03` ตัดสิทธิ์ No-Show อัตโนมัติ | US-04; UC-02; AC-04 | หัวข้อ 3 (FR-03) | VF-03 (Automated Job Test) | Covered with OI-01 |
| E-07, C-04 | `FR-04` การแจ้งเตือนสถานะคำขอ | US-06; UC-03; AC-06 | หัวข้อ 3 (FR-04) | VF-04 (Inspection) | Covered with OI-02 |
| E-08 | `FR-05` บันทึกตรวจรับ-คืนและสภาพ | US-05; UC-03; AC-05 | หัวข้อ 3 (FR-05) | VF-05 (Scenario Test) | Fully Covered |
| E-10 | `FR-06` Dashboard สถิติสำหรับผู้บริหาร | US-08; UC-05; AC-08 | หัวข้อ 3 (FR-06) | VF-06 (Inspection) | Covered with OI-04 |
| E-04, C-01 | `BR-01` อุปกรณ์ยืมอัตโนมัติ / จองล่วงหน้า | US-01; UC-01; AC-01 | หัวข้อ 4 (BR-01) | VF-01 (Scenario Test) | Covered with OI-03 |
| E-05 | `BR-02` โควตา 3 ชม./วัน และล่วงหน้า 7 วัน | US-02, US-04; UC-01, UC-02 | หัวข้อ 4 (BR-02) | VF-01, VF-03 (Negative Test) | Fully Covered |
| E-09 | `NFR-01` Audit Log ป้องกันการแก้ไขย้อนหลัง | US-09; UC-05; AC-09 | หัวข้อ 5 (NFR-01) | VF-05 (DB Inspection) | Fully Covered |

---

## 10. Open Issues

| OI | Question / TBD | Affected IDs | Owner | Next action | Expected evidence | Needed by |
|---|---|---|---|---|---|---|
| `OI-01` | มาตรการบทลงโทษกรณี No-show สะสม (เช่น ขาดกี่ครั้งจะถูกระงับสิทธิ์ชั่วคราวกี่วัน) ยังไม่ได้รับลายลักษณ์อักษรจากผู้จัดการศูนย์ | FR-03, BR-02 | วรสิทธิ์ บุญยปรีดี | นำส่งร่างข้อเสนอบทลงโทษ (ขาด 3 ครั้ง ระงับ 14 วัน) ให้ผู้จัดการพื้นที่พิจารณา | บันทึกข้อความอนุมัตินโยบาย No-show Policy | Week 08 (Architecture Design) |
| `OI-02` | ข้อกำหนดทางเทคนิคและสิทธิ์การเชื่อมต่อ SMTP/API ของระบบอีเมลสถาบัน รวมถึงนโยบายการจำกัดอัตราส่ง (Rate Limit) | FR-04, EXT-02 | ปริษฎา สุทธดุก | ทำหนังสือขอข้อมูลสเปก API และ Credential ทดสอบจากสำนักวิทยบริการ | สเปกเอกสาร API และ Test Account | Week 08 (Architecture Design) |
| `OI-03` | รายการอุปกรณ์การเรียนรู้ที่จะกำหนดให้อนุมัติอัตโนมัติ (Auto-Approve) เทียบกับอุปกรณ์ที่ต้องรอเจ้าหน้าที่อนุมัติเป็นรายกรณี | BR-01, FR-01 | วรสิทธิ์ บุญยปรีดี | ประชุมร่วมกับเจ้าหน้าที่ประจำห้องเพื่อแยกหมวดหมู่อุปกรณ์ (เช่น สายแปลง = Auto, กล้อง = Manual) | ตาราง Equipment Classification Matrix | Week 08 (System Design) |
| `OI-04` | ตัวชี้วัดเชิงสถิติ (KPIs) ที่ผู้บริหารต้องการดูบนหน้า Dashboard ในเฟสแรก | FR-06 | ปริษฎา สุทธดุก | สัมภาษณ์อาจารย์ผู้ดูแลพื้นที่เพื่อสรุป 3 กราฟหลักที่ต้องแสดงผล | ร่าง Dashboard Mockup พร้อมระบุสูตรคำนวณสถิติ | Week 10 (Midterm Progress) |

---

## 11. Verification Plan

| VF | Method | Target IDs | Procedure / Evidence | Owner | Status |
|---|---|---|---|---|---|
| `VF-01` | Demonstration + Negative Test | FR-01, BR-01, BR-02 | ทดสอบสร้างคำขอจองห้องและอุปกรณ์: 1) จองเวลาปกติ 2) จองเกิน 3 ชั่วโมง 3) จองล่วงหน้าเกิน 7 วัน และ 4) จองซ้อนเวลาที่มีคนจองแล้ว เพื่อตรวจการตอบสนองและข้อความแจ้งเตือน | วรสิทธิ์ บุญยปรีดี | Planned for W08 Prototype |
| `VF-02` | Demonstration | FR-02 | ทดสอบบทบาท Staff เข้าดูคิวคำขอและกดอนุมัติ/ปฏิเสธ ตรวจสอบการเปลี่ยนสถานะและการบังคับใส่เหตุผลเมื่อปฏิเสธ | ปริษฎา สุทธดุก | Planned for W08 Prototype |
| `VF-03` | Automated Scheduled Test | FR-03, BR-02 | จำลองสถานการณ์คำขอที่ Confirmed แล้วไม่มีการ Check-in ภายใน 15 นาที ระบบ Background Worker ต้องรันตัดสิทธิ์เป็น No-Show และคืนสถานะห้องว่าง | วรสิทธิ์ บุญยปรีดี | Planned for Implementation |
| `VF-04` | Inspection | FR-04, EXT-02 | ตรวจสอบการยิง Event แจ้งเตือนเมื่อสถานะเปลี่ยนไปยัง Web Notification Console และ Log การส่ง Mail | ปริษฎา สุทธดุก | Planned for Integration |
| `VF-05` | Inspection + DB Trigger Review | FR-05, NFR-01, BR-03 | ตรวจสอบฟิลด์การบันทึกสภาพอุปกรณ์ และทดสอบคำสั่ง Update/Delete บนตาราง `AuditLog` ในระดับฐานข้อมูล เพื่อยืนยันคุณสมบัติ Append-Only | ปริษฎา สุทธดุก | Planned for DB Baseline |
| `VF-06` | Demonstration | FR-06 | ตรวจสอบความถูกต้องของตัวเลขสรุปบนหน้า Dashboard เทียบกับข้อมูลจริงในฐานข้อมูล | วรสิทธิ์ บุญยปรีดี | Planned for Milestone 2 |

---

## 12. Review Gate Checklist

- [x] **Completeness:** ครบถ้วนทุกหัวข้อ 0–12 ตาม `ENGSE206_Week07_Student_SRS_Template_TH.md`
- [x] **Backlog Admission:** ข้อกำหนดทุกข้อจาก W05 Backlog (`FR-01..06`, `BR-01..02`, `NFR-01`) ได้รับการแจกแจง Disposition ครบถ้วนใน Appendix A
- [x] **Traceability:** สามารถสืบค้นย้อนกลับไปยัง W05 Backlog, W06 Models (US, UC, AC) และหลักฐานสัมภาษณ์ W04 ได้อย่างสมบูรณ์
- [x] **Deep Specification:** มี FR อย่างน้อย 2–3 ข้อ (`FR-01`, `FR-02`, `FR-05`) และ BR อย่างน้อย 1–2 ข้อ (`BR-01`, `BR-02`, `BR-03`) ที่เขียนเจาะลึกครบทุกฟิลด์มาตรฐาน
- [x] **Quality & Data:** มี NFR ที่ระบุเงื่อนไขและวิธีตรวจสอบชัดเจนอย่างน้อย 1 ข้อ (`NFR-01`) และ Conceptual Data Requirements ครบ 5 เอนทิตีหลัก
- [x] **Open Issues:** เปิดเผยข้อค้างคา (Gaps/TBDs) อย่างโปร่งใส พร้อมระบุ Owner, แผนการหาหลักฐาน และกำหนดเวลาที่ต้องได้คำตอบ
- [x] **Status:** ระบุสถานะเอกสารเป็น **Baseline Candidate** พร้อมสำหรับการตรวจประเมินของ Week 07

---

## Appendix A — Requirement Disposition

ตารางแจกแจงสถานะการรับเข้าของ Requirement ทุกข้อจาก `docs/05-requirement-backlog.md` เข้าสู่โครงสร้าง SRS ฉบับนี้

| Backlog ID | Priority | Admission | Disposition | Coverage | SRS Section | Reason / Source |
|---|---|---|---|---|---|---|
| `FR-01` | Must | Core | Included | Detailed | หัวข้อ 3 (FR-01) | เป็นหัวใจหลักในการจองพื้นที่และยืมอุปกรณ์ ป้องกันปัญหาจองชนกัน (E-01, E-02) |
| `FR-02` | Must | Core | Included | Detailed | หัวข้อ 3 (FR-02) | ฟังก์ชันหลักของเจ้าหน้าที่ในการจัดสรรห้องและคัดกรองการใช้งาน (E-03, C-01) |
| `FR-03` | Could | Supporting | Included (with TBD) | Partial | หัวข้อ 3 (FR-03) | กลไกจัดการ No-show จำเป็นต่อการบริหารทรัพยากร แต่รอนโยบายบทลงโทษชัดเจน (E-06, OI-01) |
| `FR-04` | Should | Supporting | Included (with TBD) | Partial | หัวข้อ 3 (FR-04) | จำเป็นต่อประสบการณ์ผู้ใช้ รอยืนยันสเปก API ระบบอีเมลสถาบัน (E-07, OI-02) |
| `FR-05` | Must | Core | Included | Detailed | หัวข้อ 3 (FR-05) | ระบบควบคุมครุภัณฑ์และตรวจสภาพอุปกรณ์เพื่อความโปร่งใส (E-08, E-09) |
| `FR-06` | Could | Extension | Deferred to Phase 2 | Partial | หัวข้อ 3 (FR-06) | สถิติและ Dashboard รอสรุปชุดตัวชี้วัดของผู้บริหาร ไม่บล็อก Core Workflow (E-10, OI-04) |
| `BR-01` | Should | Supporting | Included | Detailed | หัวข้อ 4 (BR-01) | กฎการจองล่วงหน้า 7 วัน และรายการยืมอุปกรณ์อัตโนมัติ (E-04, C-01) |
| `BR-02` | Must | Core | Included | Detailed | หัวข้อ 4 (BR-02) | กฎโควตาเวลาไม่เกิน 3 ชั่วโมง/วัน และเวลาผ่อนปรน No-show 15 นาที (E-05, E-06) |
| `NFR-01` | Must | Core | Included | Detailed | หัวข้อ 5 (NFR-01) | นโยบายความปลอดภัยและตรวจสอบย้อนหลัง ต้องมี Audit Log ที่ห้ามแก้ไข (E-09) |

---

## Appendix B — Review and Revision

| Item | Before (v0.1 Template) | After (v1.0 Baseline Candidate) | Reason / Source | Reviewer |
|---|---|---|---|---|
| Section 1–2 | โครงร่างว่างเปล่า `[กรอก]` | เติมเต็มข้อมูล Purpose, Problem, Scope In/Out, Context, Actor, Constraints ครบถ้วน | ดึงข้อมูลจาก Case Card และเอกสารช่วง W01–W04 ให้ตรงตามบริบทเคส | ปริษฎา สุทธดุก |
| Section 3 | ตารางเปล่า 1 บรรทัด | ลงรายการ FR-01 ถึง FR-06 พร้อมตาราง Deep Specification ละเอียด 3 ข้อ (FR-01, FR-02, FR-05) | ปฏิบัติตามเกณฑ์ Student Core ของรายวิชาและ Reconcile ตรงกับ W05 Backlog | วรสิทธิ์ บุญยปรีดี |
| Section 4–6 | ตารางตัวอย่างเปล่า | ระบุ BR-01 ถึง BR-05, NFR-01 ถึง NFR-05 และ Data Concepts 5 ตัว (DR-01 ถึง DR-05) | เพื่อระบุกฎเกณฑ์ คุณภาพระบบ และโครงสร้างข้อมูลเชิงมโนทัศน์ให้ชัดเจน | ปริษฎา สุทธดุก |
| Section 7–11 | ลิงก์ว่าง `[link]` | เชื่อมโยง Model W06, วงจรสถานะ, External Interfaces, ตาราง Traceability, Open Issues 4 ข้อ และแผน Verification 6 ข้อ | เชื่อมโยงทุกองค์ประกอบให้ตรวจสอบย้อนกลับได้สองทิศทาง (Bi-directional Trace) | วรสิทธิ์ บุญยปรีดี |

---

## Appendix C — AI Use Disclosure

| Activity | AI Assistance | Human Verification / Change | Evidence |
|---|---|---|---|
| โครงร่างและจัดตาราง SRS ตามมาตรฐาน Week07 | ใช้ Antigravity (Gemini) ช่วยแปลงโครงสร้างจาก `ENGSE206_Week07_Student_SRS_Template_TH.md` และผสานเนื้อหาจาก W01–W06 | สมาชิกทีมตรวจสอบความสอดคล้องของ ID ทุกตัว (FR, BR, NFR, US, UC, AC) เทียบกับ Backlog เดิม ตรวจความถูกต้องของบริบทการจองห้อง และตัดฟังก์ชันที่อยู่นอก Scope ออก | `docs/07-srs-v1.md`, `evidence/week-07/ai_disclosure.csv` |
| ร่างรายละเอียด Deep Specification (Trigger, Guard, Result) | ใช้ AI ช่วยจัดระเบียบตาราง Field-Value และร่างขั้นตอน Scenario | ตรวจสอบและแก้ไขเงื่อนไขเวลาให้ตรงตามมติเคส เช่น ปรับเกณฑ์ No-show เป็น 15 นาที และโควตาไม่เกิน 3 ชม./วัน | `docs/07-srs-v1.md` Section 3 |
| ตรวจสอบความถูกต้องและจัดทำตาราง Disposition/Traceability | ใช้ AI รวบรวม Traceability Matrix จากไฟล์ W04, W05, W06 | ตรวจสอบความถูกต้องของ Source Link และจัดเก็บลงไฟล์ CSV แยกใน `evidence/week-07/` | `evidence/week-07/traceability.csv`, `disposition.csv` |
