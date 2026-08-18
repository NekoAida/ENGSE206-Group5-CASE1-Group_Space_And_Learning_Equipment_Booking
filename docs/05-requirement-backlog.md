# 05 — Requirement Backlog and Prioritization

> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้  
> **Source:** Week04 Candidate: `RC-01..RC-09`  
> **Goal:** จัดประเภท จัดลำดับ และแยกสิ่งที่พร้อมใช้ต่อ Week06 ออกจากสิ่งที่ยังต้องถามต่อ

## 1. Project Metadata
| Field | Value |
|---|---|
| Course / Week | ENGSE206 / Week05 |
| Team | Group 5 |
| Case | Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้ |
| Source Week04 file | `04-evidence-log.md` |
| Backlog version | `v1.0` |
| Date | 2026-08-11 |

## 2. Prioritization Method
ใช้ MoSCoW โดยประเมินจาก 4 มิติ (Value, Risk, Urgency, Dependency)

| Dimension | วิธีใช้ในงานนี้ |
|---|---|
| Value | ช่วยให้ผู้ใช้งานสามารถค้นหา/จองพื้นที่และอุปกรณ์ได้ 24 ชม. และเจ้าหน้าที่บริหารจัดการทรัพยากรได้สะดวก |
| Risk | หากขาด requirement นี้จะเกิดความผิดพลาดในการจอง ข้อมูลสูญหาย การจองซ้ำซ้อน หรือคุมสต็อกผิดพลาด |
| Urgency | จำเป็นต้องมีในระบบเวอร์ชันแรกเพื่อให้ Core Workflow การจองและอนุมัติทำงานได้ |
| Dependency | ต้องรอการตัดสินใจเชิงนโยบาย (Policy) หรือข้อมูลยืนยันจากผู้ดูแล (Stakeholders) ก่อนหรือไม่ |

## 3. Requirement Backlog
| Req ID | Source RC | Evidence / Need Trace | Requirement Statement | Type | Priority | Rationale | Status | Open Question | Week06 Use |
|---|---|---|---|---|---|---|---|---|---|
| FR-01 | RC-01 | E-01, E-02 | ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่เลือกภายใน 3 วินาที และส่งคำขอจองพื้นที่หรืออุปกรณ์ได้สำเร็จพร้อมแสดงรหัสคำขอจอง | Functional | Must | เป็นฟังก์ชันหลัก (Core capability) ของระบบเพื่อให้เกิดการใช้งาน | Ready for Week06 | ข้อมูลขั้นต่ำที่ต้องกรอกในฟอร์มการจองคืออะไร | Use Case + User Story |
| FR-02 | RC-02 | E-03, C-01 | ระบบต้องมีหน้าจอให้เจ้าหน้าที่กดอนุมัติหรือปฏิเสธคำขอจองห้อง พร้อมบันทึกเหตุผลและเปลี่ยนสถานะคำขอภายใน 3 วินาที | Functional / Workflow | Must | จำเป็นต่อการบริหารจัดการและคัดกรองการใช้พื้นที่ทำงานกลุ่มโดยเจ้าหน้าที่ | Ready for Week06 | เหตุผลการปฏิเสธมีตัวเลือกอะไรบ้าง (Dropdown หรือ Text) | Use Case + User Story |
| BR-01 | RC-03 | E-04, C-01 | ระบบต้องอนุมัติการจองอุปกรณ์การเรียนรู้ทั่วไปแบบอัตโนมัติ (Auto-approve) ตามลำดับคิวเมื่อมีอุปกรณ์ว่างในระบบ | Business Rule | Should | ลดภาระงานเจ้าหน้าที่ แต่ต้องยืนยันหมวดหมู่อุปกรณ์ที่เปิดให้อนุมัติอัตโนมัติ | Needs Follow-up | รายการอุปกรณ์ใดบ้างที่เข้าข่าย Auto-approve | Use Case Rule + AC |
| BR-02 | RC-04 | E-05 | ระบบต้องตรวจสอบเงื่อนไขนโยบายการจอง โดยจำกัดระยะเวลาจองห้องไม่เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน พร้อมแสดงข้อความเตือนเมื่อเกินโควตา | Business Rule | Must | จำเป็นต่อการควบคุมโควตาเพื่อกระจายสิทธิ์การใช้งานอย่างเท่าเทียม | Ready for Week06 | ข้อความ Error เมื่อผู้ใช้เลือกเวลาเกินโควตาคืออะไร | Use Case Rule + AC |
| FR-03 | RC-05 | E-06, C-02 | ระบบต้องยกเลิกคำขอจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาเช็กอินเข้าใช้พื้นที่ภายใน 15 นาทีหลังจากถึงเวลาจอง | Functional / Policy | Could | แก้ปัญหา Ghost Booking แต่มี Dependency สูงเรื่องกลไกเช็กอินและนโยบายระงับสิทธิ์ | Hold | ผู้จัดการพื้นที่ยืนยันเกณฑ์ No-show และบทลงโทษอย่างไร | Follow-up only |
| FR-04 | RC-06 | E-07, C-04 | ระบบต้องส่งข้อความแจ้งเตือนสถานะคำขอจอง (อนุมัติ/ปฏิเสธ/ยกเลิก) ให้ผู้ใช้งานทราบผ่าน Web Notification และ Email สถาบันภายใน 5 วินาทีหลังเกิดเหตุการณ์ | Functional | Should | เพิ่ม Usability แต่ต้องเช็คเรื่องการต่อ Email Service ของสถาบัน | Needs Follow-up | รูปแบบข้อความและการเชื่อมต่อ API ระบบ Email สถาบัน | User Story + Event List |
| FR-05 | RC-07 | E-08 | ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนที่เจ้าหน้าที่ส่งมอบและรับคืนอุปกรณ์หน้าเคาน์เตอร์ | Functional / Inventory | Must | จำเป็นต่อการติดตามทรัพย์สินของสถาบัน ป้องกันอุปกรณ์สูญหาย | Ready for Week06 | ฟิลด์สภาพอุปกรณ์ที่ต้องบันทึกมีตัวเลือกอะไรบ้าง | Use Case + AC |
| NFR-01 | RC-08 | E-09 | ระบบต้องบันทึก Audit Log ทุกรายการจอง/อนุมัติ/ยกเลิก/คืนอุปกรณ์ โดยบันทึก Timestamp, User ID, Action, IP Address และไม่อนุญาตให้แก้ไขหรือลบ Log ย้อนหลัง | Security / NFR | Must | จำเป็นต่อความปลอดภัย ความโปร่งใส และการตรวจสอบย้อนหลัง | Needs Follow-up | โครงสร้างการเก็บ Audit Log และระยะเวลาการเข้าถึงข้อมูล | Quality Scenario + Constraint |
| FR-06 | RC-09 | E-10 | ระบบต้องมีหน้า Dashboard สรุปสถิติอัตราการเข้าใช้พื้นที่ อัตราการยืมอุปกรณ์ และสถิติผู้ไม่มาตามนัด (No-show) สำหรับผู้บริหาร | Functional / Reporting | Could | เป็นส่วนเสริมสำหรับบริหาร ยังไม่จำเป็นต่อ Core Workflow ในระยะแรก | Hold | ตัวชี้วัดสถิติที่ผู้บริหารและผู้จัดการต้องการดูคืออะไร | Follow-up only |

## 4. Priority Summary
| Priority | Count | Requirement IDs | เหตุผลรวม |
|---|---:|---|---|
| Must | 5 | FR-01, FR-02, BR-02, FR-05, NFR-01 | เป็นฟังก์ชันหลักของการจอง การอนุมัติ การจำกัดโควตา คุมอุปกรณ์ และความปลอดภัยของระบบ |
| Should | 2 | BR-01, FR-04 | มีคุณค่าสูงในการลดงานเจ้าหน้าที่หรือเพิ่ม UX แต่ต้องยืนยันข้อมูลหรือเชิงเทคนิคเพิ่มเติม |
| Could | 2 | FR-03, FR-06 | เป็นส่วนเสริม (Dashboard, Auto-cancel) ต้องรอ Policy และรายละเอียดเพิ่มเติม |
| Won't yet | 0 | - | - |

## 5. Ready / Follow-up / Hold
| Status | Requirement IDs | สิ่งที่ต้องทำต่อ |
|---|---|---|
| Ready for Week06 | FR-01, FR-02, BR-02, FR-05 | พร้อมนำไปทำ User Story / Use Case / Acceptance Criteria |
| Needs Follow-up | BR-01, FR-04, NFR-01 | ต้องถาม Stakeholder เรื่องรายการอุปกรณ์ Auto-approve, ช่องทาง Email และนโยบาย Audit Log |
| Hold | FR-03, FR-06 | เก็บเป็น Issue ไว้ก่อนจนกว่าจะได้ความชัดเจนเรื่อง Policy (No-show) และ Metrics สำหรับ Report |

## 6. Review Checklist
- [x] ทุก requirement มี Source RC หรือ Evidence source
- [x] ทุก requirement อ้าง Evidence / Need Trace
- [x] Type แยกเป็น Functional / NFR / Business Rule / Constraint / Issue
- [x] Priority มี rationale จาก value/risk/urgency/dependency
- [x] Unknown หรือ policy issue ไม่ถูกยกระดับเป็น requirement โดยไม่มีหลักฐาน
- [x] มี Week06 Use สำหรับรายการที่พร้อมทำ model

## 7. Week06 Handoff
Week06 ควรเริ่มจาก requirement ที่พร้อมก่อน:

| Week06 artefact | Input ที่เหมาะสม |
|---|---|
| User Story | FR-01, FR-02, FR-05 |
| Use Case | FR-01 เป็น main flow; FR-02, FR-05 เป็น operational flow |
| Acceptance Criteria | BR-02 เรื่องโควตา |
| Quality Scenario | NFR-01 เรื่อง Audit Log (ร่างโครงสร้างเบื้องต้น รอผล Verify) |