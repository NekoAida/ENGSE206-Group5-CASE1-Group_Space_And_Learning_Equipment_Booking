# 05 — Requirement Backlog and Prioritization

> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้  
> **Source:** Week04 Candidate: `RC-01..RC-09`  
> **Goal:** จัดประเภท จัดลำดับ และเชื่อมโยง Traceability จากหลักฐานสู่ความต้องการ

## 1. Project Metadata
| Field | Value |
|---|---|
| Course / Week | ENGSE206 / Week05 |
| Team | Group 5 |
| Case | Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้ |
| Source Week04 file | `04-evidence-log.md` |
| Backlog version | `v1.2 (Baseline Locked - CR-02 Applied)` |
| Date | 2026-08-18 |

## 2. Prioritization Method
ใช้ MoSCoW โดยประเมินจาก 4 มิติ (Value, Risk, Urgency, Dependency)

| Dimension | วิธีใช้ในงานนี้ |
|---|---|
| Value | ช่วยให้ผู้ใช้งานสามารถค้นหา/จองพื้นที่และอุปกรณ์ได้ 24 ชม. และเจ้าหน้าที่บริหารจัดการทรัพยากรได้สะดวก |
| Risk | หากขาด requirement นี้จะเกิดความผิดพลาดในการจอง ข้อมูลสูญหาย การจองซ้ำซ้อน หรือคุมสต็อกผิดพลาด |
| Urgency | จำเป็นต้องมีในระบบเวอร์ชันแรกเพื่อให้ Core Workflow การจองและอนุมัติทำงานได้ |
| Dependency | ต้องรอการตัดสินใจเชิงนโยบาย (Policy) หรือข้อมูลยืนยันจากผู้ดูแล (Stakeholders) ก่อนหรือไม่ |

## 3. Requirement Backlog

| Req | ข้อความ requirement | Priority | Stakeholder | Evidence → Need | Status | Open Question | Week06 Use |
|---|---|---|---|---|---|---|---|
| FR-01 | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่เลือกภายใน 3 วินาที และส่งคำขอจองได้สำเร็จพร้อมแสดงรหัสคำขอจอง | Must | นักศึกษา | E-01, E-02 → RC-01 | Ready for Week06 | ข้อมูลขั้นต่ำที่ต้องกรอกในฟอร์มการจองคืออะไร | Use Case + User Story |
| FR-02 | ระบบต้องมีหน้าจอให้เจ้าหน้าที่กดอนุมัติหรือปฏิเสธคำขอจองห้อง พร้อมบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที | Must | เจ้าหน้าที่ดูแล (Staff) | E-03, C-01 → RC-02 | Ready for Week06 | เหตุผลการปฏิเสธมีตัวเลือกอะไรบ้าง (Dropdown หรือ Text) | Use Case + User Story |
| BR-01 | ระบบต้องอนุมัติการจองอุปกรณ์การเรียนรู้ทั่วไปแบบอัตโนมัติ (Auto-approve) ตามลำดับคิวเมื่อมีอุปกรณ์ว่างในระบบ | Should | เจ้าหน้าที่ / นักศึกษา | E-04, C-01 → RC-03 | Needs Follow-up | รายการอุปกรณ์ใดบ้างที่เข้าข่าย Auto-approve | Use Case Rule + AC |
| BR-02 | ระบบต้องตรวจสอบเงื่อนไขนโยบายการจอง โดยจำกัดระยะเวลาจองห้องไม่เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน พร้อมแสดงข้อความเตือนเมื่อเกินโควตา | Must | ผู้จัดการพื้นที่ | E-05 → RC-04 | Ready for Week06 | ข้อความ Error เมื่อผู้ใช้เลือกเวลาเกินโควตาคืออะไร | Use Case Rule + AC |
| FR-03 | ระบบต้องยกเลิกคำขอจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาเช็กอินเข้าใช้พื้นที่ภายใน 15 นาทีหลังจากถึงเวลาจอง | Could | ผู้จัดการพื้นที่ / เจ้าหน้าที่ | E-06, C-02, C-03 → RC-05 | Hold | ผู้จัดการพื้นที่ยืนยันเกณฑ์ No-show และบทลงโทษอย่างไร | Follow-up only |
| FR-04 | ระบบต้องส่งข้อความแจ้งเตือนสถานะคำขอจอง (อนุมัติ/ปฏิเสธ/ยกเลิก) ให้ผู้ใช้งานทราบผ่าน Web Notification และ Email สถาบันภายใน 5 วินาทีหลังเกิดเหตุการณ์ | Should | นักศึกษา / เจ้าหน้าที่ | E-07, C-04 → RC-06 | Needs Follow-up | รูปแบบข้อความและการเชื่อมต่อ API ระบบ Email สถาบัน | User Story + Event List |
| FR-05 | ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนที่เจ้าหน้าที่ส่งมอบและรับคืนอุปกรณ์หน้าเคาน์เตอร์ | Must | เจ้าหน้าที่ดูแล (Staff) | E-08 → RC-07 | Ready for Week06 | ฟิลด์สภาพอุปกรณ์ที่ต้องบันทึกมีตัวเลือกอะไรบ้าง | Use Case + AC |
| NFR-01 | ระบบต้องบันทึก Audit Log ทุกรายการจอง/อนุมัติ/ยกเลิก/คืนอุปกรณ์ โดยบันทึก Timestamp, User ID, Action, IP Address และไม่อนุญาตให้แก้ไขหรือลบ Log ย้อนหลัง | Must | ผู้ดูแลระบบ (Admin) | E-09 → RC-08 | Needs Follow-up | โครงสร้างการเก็บ Audit Log และระยะเวลาการเข้าถึงข้อมูล | Quality Scenario + Constraint |
| FR-06 | ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการเข้าใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติผู้ไม่มาตามนัด (No-show) สำหรับผู้บริหาร | Could | ผู้บริหาร / ผู้จัดการ | E-10 → RC-09 | Hold | ตัวชี้วัดสถิติที่ผู้บริหารและผู้จัดการต้องการดูคืออะไร | Follow-up only |

## 4. Priority Summary
| Priority | Count | Requirement IDs | เหตุผลรวม |
|---|---:|---|---|
| Must | 4 | FR-01, FR-02, BR-02, FR-05, NFR-01 | เป็นฟังก์ชันหลักของการจอง การอนุมัติ การจำกัดโควตา คุมสต็อกอุปกรณ์ และความปลอดภัยของข้อมูล |
| Should | 2 | BR-01, FR-04 | มีคุณค่าสูงในการลดงานเจ้าหน้าที่และการแจ้งเตือน แต่มี Dependency หรือรอยยืนยันการเชื่อมต่อระบบ |
| Could | 2 | FR-03, FR-06 | เป็นส่วนเสริม (Auto-cancel และ Dashboard) รอความชัดเจนเชิงนโยบายและ KPI |
| Won't yet | 0 | - | - |

## 5. Ready / Follow-up / Hold
| Status | Requirement IDs | สิ่งที่ต้องทำต่อ |
|---|---|---|
| Ready for Week06 | FR-01, FR-02, BR-02, FR-05 | พร้อมนำไปทำ User Story / Use Case / Acceptance Criteria |
| Needs Follow-up | BR-01, FR-04, NFR-01 | ต้องถาม Stakeholder เรื่องรายการอุปกรณ์ Auto-approve, ช่องทาง Email และนโยบาย Audit Log |
| Hold | FR-03, FR-06 | เก็บเป็น Issue ไว้ก่อนจนกว่าจะได้ความชัดเจนเรื่อง Policy (No-show) และ Metrics สำหรับ Report |

## 6. Review Checklist
- [x] มีคอลัมน์ `Req`, `ข้อความ requirement`, `Priority`, `Stakeholder`, `Evidence → Need` ตรงตามรูปแบบตารางมาตรฐาน
- [x] ทุก requirement อ้างอิง Evidence และ Need Trace สอดคล้องกับ `04-evidence-log.md` และ `04-requirement-candidates.md`
- [x] Priority ประเมินโดยอ้างอิงจาก Value, Risk, Urgency และ Dependency (อัปเดตตรงตาม CR-02)
- [x] มีแผนการนำไปทำ Model ใน Week06 อย่างชัดเจน

## 7. Week06 Handoff
| Week06 artefact | Input ที่เหมาะสม |
|---|---|
| User Story | FR-01, FR-02, FR-05 |
| Use Case | FR-01 เป็น main flow; FR-02, FR-05 เป็น operational flow |
| Acceptance Criteria | BR-02 เรื่องโควตา |
| Quality Scenario | NFR-01 เรื่อง Audit Log (ร่างโครงสร้างเบื้องต้น รอผล Verify) |