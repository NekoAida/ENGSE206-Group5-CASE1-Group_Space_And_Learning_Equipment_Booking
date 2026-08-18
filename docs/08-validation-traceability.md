# 08 — Validation, Traceability and Change Management

> **Version:** baseline-v1.0 | **Date:** 2026-08-18 | **Status:** Baseline Locked (Week 05 Requirement Baseline Review)

---

## 1. Validation Plan

| Validation Activity | Artefact | Participants | Criteria | Evidence |
|---|---|---|---|---|
| Artefact Health Check | docs/01–05 | สมาชิกทีม Group 5 (ปริษฎา, วรสิทธิ์) | Completeness, consistency, no dangling placeholders | `../evidence/week-05/baseline-review/artefact-health-check.md` |
| Peer Cross-Review | docs/05, docs/08 | ทีม Group 5 & Peer Reviewer | Traceability, atomic/measurable criteria, MoSCoW rationale | `../evidence/week-05/baseline-review/cross-review.md` |
| Quality & MoSCoW Check | docs/05-requirement-backlog.md | Quality Checker & Traceability Auditor | Verifiable, Unambiguous, Atomic, Traceable, Scope constraint | `../evidence/week-05/baseline-review/` |

---

## 2. Requirements Quality Checklist

| Check | Result | Evidence / Note |
|---|---|---|
| Requirement มี ID และไม่ซ้ำกัน | Pass | ใช้มาตรฐาน `FR-01..06`, `BR-01..02`, `NFR-01` สอดคล้องกันทุกไฟล์ |
| ใช้ถ้อยคำชัดเจน ไม่กำกวม | Pass | ระบุเงื่อนไข ตัวเลขเวลา (3 วินาที / 5 วินาที / 15 นาที / 7 วัน) หลีกเลี่ยงคำว่า "เร็ว/สะดวก" ลอยๆ |
| ตรวจรับหรือวัดผลได้ | Pass | กำหนด Response time (≤3 วินาที) และ Notification latency (≤5 วินาที) |
| มี source/rationale | Pass | ทุก Requirement อ้างอิง Evidence E-ID และ Stakeholder Need ชัดเจน |
| Scope เหมาะสม | Pass | ตรงตาม Case Card No.1 ไม่มีส่วนเกิน Out of Scope (ไม่มี Online Payment / IoT) |
| เป็น Atomic (หนึ่งข้อหนึ่งเรื่อง) | Pass | แยกการจองห้องและการยืมอุปกรณ์ออกจากกัน ไม่มัดรวม Workflow |

---

## 3. Traceability Matrix

| Problem / Pain Point | Stakeholder | Evidence / Negotiation | Need / Candidate | Requirement ID & Statement | Priority |
|---|---|---|---|---|---|
| **PP-01** (ไม่ทราบสถานะห้อง/อุปกรณ์) | นักศึกษา | E-01, E-02 | RC-01 | **FR-01**: ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่เลือกภายใน 3 วินาที และส่งคำขอจองพื้นที่หรืออุปกรณ์ได้สำเร็จพร้อมแสดงรหัสคำขอจอง | Must |
| **PP-03** (ภาระงานเอกสาร/จัดการมือ) | เจ้าหน้าที่ดูแล (Staff) | E-03, C-01 | RC-02 | **FR-02**: ระบบต้องมีหน้าจอให้เจ้าหน้าที่กดอนุมัติหรือปฏิเสธคำขอจองห้อง พร้อมบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที | Must |
| **PP-02, PP-03** (ความล่าช้าในการยืม) | เจ้าหน้าที่ / นักศึกษา | E-04, C-01 | RC-03 | **BR-01**: ระบบต้องอนุมัติการจองอุปกรณ์การเรียนรู้ทั่วไปแบบอัตโนมัติ (Auto-approve) ตามลำดับคิวเมื่อมีอุปกรณ์ว่างในระบบ | Should |
| **F-03** (ทรัพยากรห้องมีจำกัด) | ผู้จัดการพื้นที่ | E-05 | RC-04 | **BR-02**: ระบบต้องตรวจสอบเงื่อนไขนโยบายการจอง โดยจำกัดระยะเวลาจองห้องไม่เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน พร้อมแสดงข้อความเตือนเมื่อเกินโควตา | Must |
| **F-02, OQ-02** (ปัญหา No-show/จองกัก) | ผู้จัดการพื้นที่ / เจ้าหน้าที่ | E-06, C-02, C-03 | RC-05 | **FR-03**: ระบบต้องยกเลิกคำขอจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาเช็กอินเข้าใช้พื้นที่ภายใน 15 นาทีหลังจากถึงเวลาจอง | Could |
| **PP-01, PP-03** (ไม่ทราบผลคำขอจอง) | นักศึกษา / เจ้าหน้าที่ | E-07, C-04 | RC-06 | **FR-04**: ระบบต้องส่งข้อความแจ้งเตือนสถานะคำขอจอง (อนุมัติ/ปฏิเสธ/ยกเลิก) ให้ผู้ใช้งานทราบผ่าน Web Notification และ Email สถาบันภายใน 5 วินาทีหลังเกิดเหตุการณ์ | Should |
| **F-01, A-02** (ขาดการบันทึกติดตาม) | เจ้าหน้าที่ดูแล (Staff) | E-08 | RC-07 | **FR-05**: ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนที่เจ้าหน้าที่ส่งมอบและรับคืนอุปกรณ์หน้าเคาน์เตอร์ | Must |
| **ความปลอดภัย/ความโปร่งใส** | ผู้ดูแลระบบ (Admin) | E-09 | RC-08 | **NFR-01**: ระบบต้องบันทึก Audit Log ทุกรายการจอง/อนุมัติ/ยกเลิก/คืนอุปกรณ์ โดยบันทึก Timestamp, User ID, Action, IP Address และไม่อนุญาตให้แก้ไขหรือลบ Log ย้อนหลัง | Must |
| **G-03, F-03** (วางแผนทรัพยากร) | ผู้บริหาร / ผู้จัดการ | E-10, E-12 | RC-09 | **FR-06**: ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการเข้าใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติผู้ไม่มาตามนัด (No-show) สำหรับผู้บริหาร | Could |

---

## 4. Change Request Log

| CR-ID | Date | Requested Change | Reason / Evidence | Impacted Artefacts | Decision | Owner |
|---|---|---|---|---|---|---|
| CR-01 | 2026-08-18 | ปรับปรุงถ้อยคำ FR-01/02 และ NFR-01 ให้ระบุตัวเลขวัดผลได้ (Verifiable & Atomic) | ผลการตรวจ Quality Check ใน Baseline Review พบความกำกวม | `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md` | Accepted | วรสิทธิ์ บุญยปรีดี |
| CR-02 | 2026-08-18 | ปรับระดับ MoSCoW ของ BR-01 เป็น Should, FR-05 เป็น Must, FR-03 เป็น Could และ NFR-01 เป็น Must ให้สอดคล้องกันทุกไฟล์ | แก้ไขข้อขัดแย้งระหว่าง Backlog และ Prioritization Rationale | `docs/05-prioritization-rationale.md`, `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md` | Accepted | ปริษฎา สุทธดุก |

---
## 5. Open Questions / Assumptions (Gap Traceability)

| Req ID / Issue | มาจาก Evidence (E-xx) | ผูกกับ Stakeholder | Need/Candidate (RC) | ลากครบ? |
|---|---|---|---|---|
| OQ-01 (เงื่อนไข Auto-approve) | E-04, C-01 | ST-02 (เจ้าหน้าที่) | RC-03 | [ ]  ครบ |
| OQ-02 (เกณฑ์อุทธรณ์ No-show) | E-06, C-02, C-03 | ST-03 (ผู้จัดการพื้นที่) | RC-05 | [ ]  ครบ |
| OQ-03 (โครงสร้าง Audit Log / PDPA) | E-09 | ST-04 (ผู้ดูแลระบบ) | RC-08 | [ ]  ครบ |

เหตุผลและคำอธิบาย Open Questions / Assumptions

* **OQ-01 (รายการอุปกรณ์ Auto-approve):**
  * **Rationale:** แม้จะมีข้อตกลง `C-01` ให้ Auto-approve อุปกรณ์ทั่วไป แต่ยังไม่มีหลักฐานระบุชัดเจนว่าอุปกรณ์ประเภทใดบ้างเข้าข่าย
  * **Assumption:** กำหนดเบื้องต้นให้สายแปลงและปลั๊กพ่วงเป็น Auto-approve ส่วนโน้ตบุ๊ก/กล้องถ่ายภาพต้องรออนุมัติ และตั้งเป็นประเด็นไปถามต่อใน Week 06

* **OQ-02 (เงื่อนไขขอยกเว้นและอุทธรณ์ No-show):**
  * **Rationale:** จาก `C-02` และ `C-03` ตกลงใช้เกณฑ์ตัดสิทธิ์ที่ 15 นาที และระบบ Strike เตือน 3 ครั้ง แต่ยังขาดนโยบายรองรับกรณีสุดวิสัย (เช่น ระบบมหาวิทยาลัยล่ม)
  * **Assumption:** ตั้ง Assumption ให้ผู้จัดการพื้นที่เป็นผู้มีอำนาจ Override ปลดล็อกสิทธิ์ผ่านระบบได้ โดยเก็บเป็น Issue ไว้คุยต่อโดยไม่ลบ Requirement ทิ้ง

* **OQ-03 (นโยบาย Audit Log และ PDPA):**
  * **Rationale:** `E-09` กำหนดให้เก็บ Audit Log ย้อนหลังอย่างน้อย 90 วัน แต่ยังต้องรอการยืนยันโครงสร้าง DB และนโยบาย PDPA ร่วมกับฝ่าย IT สถาบัน
  * **Assumption:** กำหนดให้บันทึกข้อมูลพื้นฐาน (Timestamp, User ID, Action, IP) ไปก่อนเพื่อรอ Verify ในสัปดาห์ถัดไป
---

## 6. Baseline Decision

- **Baseline Name:** `baseline-v1.0`
- **Date:** 2026-08-18
- **Approved/Reviewed by:** ทีมโครงงาน Group 5 (ปริษฎา สุทธดุก, วรสิทธิ์ บุญยปรีดี)
- **Status:** Approved for Week 06 Requirement Modeling
- **Remaining Open Issues:** 6 ข้อ (บันทึกใน [`docs/05-open-questions-and-issues.md`](05-open-questions-and-issues.md) และ [`evidence/week-05/baseline-review/open-questions.md`](../evidence/week-05/baseline-review/open-questions.md))

---

## 7. Follow-up Backlog for Week 06

- [x] ตรวจสอบความสอดคล้องของ Priority ระหว่าง `05-requirement-backlog.md` และ `08-validation-traceability-and-change-management.md`
- [ ] แปลง **FR-01**, **FR-02**, **FR-05** เป็น User Stories และ Use Cases พร้อม Flow การทำงาน
- [ ] กำหนด Acceptance Criteria สำหรับ **BR-02** (โควตาเวลา 3 ชม./วัน และล่วงหน้า 7 วัน)
- [ ] ร่าง Quality Scenario และ Data Schema สำหรับ **NFR-01** (Audit Log)
- [ ] นำรายการ Open Questions ใน `evidence/week-05/baseline-review/open-questions.md` ไปสอบถามอาจารย์ในคาบเรียน Week 06