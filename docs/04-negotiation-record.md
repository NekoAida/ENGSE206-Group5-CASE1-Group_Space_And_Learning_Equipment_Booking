# Week 04 — Conflict and Negotiation Record

> **Team:** Group 5 — Group Space And Learning Equipment Booking System  
> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้  
> **Version:** v1.0 — Negotiation and Decision Record

---

## 1. Negotiation method

แต่ละประเด็นแยก Position (สิ่งที่แต่ละฝ่ายเรียกร้อง) ออกจาก Interest (เหตุผลหรือผลลัพธ์ที่ต้องการ) ตรวจ authority/constraint แล้วเปรียบเทียบ options ด้วยเกณฑ์ร่วม ได้แก่ usability, operational effort, fairness, traceability, privacy และ feasibility

---

## 2. Negotiation register

### C-01 — Manual Approval vs Auto-approval for Equipment

| Field | Record |
|---|---|
| Evidence | E-03, E-04 |
| Position A — นักศึกษา | ต้องการยืมอุปกรณ์ได้ทันทีหลังส่งคำขอ โดยไม่ต้องรอเจ้าหน้าที่กดอนุมัติ |
| Interest A | ความรวดเร็วในการใช้งานอุปกรณ์ ไม่ต้องเสียเวลารอนานหน้าเคาน์เตอร์ |
| Position B — เจ้าหน้าที่ดูแลห้อง/อุปกรณ์ | ต้องการตรวจสอบและควบคุมสต็อกอุปกรณ์ทุกชิ้นเพื่อป้องกันอุปกรณ์สูญหาย |
| Interest B | ความถูกต้องของจำนวนอุปกรณ์ และลดภาระงานคั่งค้างในระบบ |

| Option | Description | Usability | Operational effort | Traceability/Risk |
|---|---|---:|---:|---|
| A | อนุมัติอัตโนมัติ (Auto-approve) ทุกรายการ ทั้งพื้นที่และอุปกรณ์ | High | Low | เสี่ยงต่อการใช้พื้นที่ผิดวัตถุประสงค์ |
| B | ต้องรอเจ้าหน้าที่กดอนุมัติ (Manual Approve) ทุกรายการ | Low | High | เกิดคอขวดและงานค้างสะสมของเจ้าหน้าที่ |
| C | แยกประเภท: พื้นที่ (Space) ต้องรออนุมัติ ส่วนอุปกรณ์ทั่วไปให้ Auto-approve ตามสต็อก | High | Medium | สมดุลระหว่างการคัดกรองและการลดภาระงาน |

**Decision/status:** เลือก Option C เป็น **Decided**  
**Rationale:** E-03 แสดงว่าการใช้พื้นที่ต้องคัดกรองความเหมาะสม ส่วน E-04 แสดงว่าการยืมอุปกรณ์ทั่วไปเกิดขึ้นบ่อย การแยก Workflow ช่วยให้ผู้ใช้ได้รับความสะดวกรวดเร็วและเจ้าหน้าที่ไม่ทำงานซ้ำซ้อน  
**Derived candidates:** RC-02, RC-03

---

### C-02 — No-show Cancellation Timeout (10 min vs 15 min vs 30 min)

| Field | Record |
|---|---|
| Evidence | E-06 |
| Position A — เจ้าหน้าที่ผู้ดูแลห้อง | ต้องการตัดสิทธิ์ทันทีภายใน 10 นาทีหลังจากถึงเวลาจอง |
| Interest A | ป้องกัน Ghost Booking และคืนห้องให้ผู้ใช้กลุ่มอื่นได้รวดเร็ว |
| Position B — นักศึกษา | ขอขยายเวลาผ่อนผันเป็น 30 นาที |
| Interest B | ความยืดหยุ่นกรณีติดภารกิจการเรียนหรือการเดินทางในมหาวิทยาลัย |

| Option | Description | Fairness | Resource Utilization | Feasibility |
|---|---|---:|---:|---:|
| A | ยกเลิกอัตโนมัติภายใน 10 นาที | Low | High | High |
| B | ยกเลิกอัตโนมัติภายใน 15 นาที | High | High | High |
| C | ยกเลิกอัตโนมัติภายใน 30 นาที | High | Low | High |

**Decision/status:** เลือก Option B เป็น **Decided**  
**Rationale:** ระยะเวลา 15 นาทีมีความสมดุลที่สุด ไม่นานเกินไปจนเสียโอกาสการใช้ห้อง และไม่กระชั้นชิดเกินไปสำหรับผู้เดินทาง  
**Derived candidate:** RC-05

---

### C-03 — Penalty for Repeated No-shows (Immediate Suspension vs Strike System)

| Field | Record |
|---|---|
| Evidence | E-06, E-10 |
| Position A — ผู้จัดการพื้นที่ | ต้องการตัดสิทธิ์การจองทันที 7 วันเมื่อเกิด No-show |
| Interest A | สร้างวินัยในการใช้งานทรัพยากรส่วนรวมและลดสถิติห้องว่างทิ้ง |
| Position B — นักศึกษา | ขอให้มีการตักเตือนก่อนระงับสิทธิ์จริง |
| Interest B | ความเป็นธรรมและป้องกันผลกระทบจากเหตุจำเป็นสุดวิสัย |

| Option | Description | Fairness | Operational effort | Compliance |
|---|---|---:|---:|---|
| A | ตัดสิทธิ์การจองทันที 7 วันตั้งแต่ครั้งแรก | Low | Low | High |
| B | เตือนผ่านระบบก่อนครบ 3 ครั้ง แล้วค่อยระงับสิทธิ์ 7 วัน | High | Medium | High |
| C | ไม่มีการระงับสิทธิ์ ใช้เพียงการตักเตือน | High | Low | Low |

**Decision/status:** เลือก Option B เป็น **Decided** (เก็บเงื่อนไขอุทธรณ์เป็น Open Question OQ-03)  
**Rationale:** ทางเลือก B ช่วยป้องกันกรณีเกิดเหตุสุดวิสัย และเพิ่มความโปร่งใสโดยแสดงสถิติเตือนบนหน้าเว็บผู้ใช้  
**Derived candidate:** RC-05, OQ-03

---

### C-04 — Notification Channel (Web/Email vs LINE Official)

| Field | Record |
|---|---|
| Evidence | E-07 |
| Position A — นักศึกษา | ต้องการให้แจ้งเตือนผ่าน LINE Official Account / LINE Notify |
| Interest A | ความสะดวกในการเปิดอ่านข้อความบนมือถือ |
| Position B — ผู้ดูแลระบบ IT | ให้ใช้การแจ้งเตือนบนหน้าเว็บและส่ง Email บัญชีสถาบัน |
| Interest B | ควบคุมขอบเขตระบบ ไม่เพิ่มค่าใช้จ่าย และใช้ระบบความปลอดภัยของสถาบัน |

| Option | Description | Usability | Cost/Effort | Scope Alignment |
|---|---|---:|---:|---|
| A | แจ้งผ่าน Web Notification + Email สถาบัน | High | Low | In Scope |
| B | พัฒนาเชื่อมต่อ LINE Official Account API | High | High | Out of Scope |

**Decision/status:** เลือก Option A เป็น **Decided**  
**Rationale:** ทางเลือก B มีค่าใช้จ่ายและอยู่นอกขอบเขต (Out of Scope) ของโครงการ การแจ้งผ่าน Web + Email บนบัญชีสถาบันมีความเหมาะสมและทำได้จริง  
**Derived candidate:** RC-06

---

## 3. Decision summary

| Conflict ID | Status | Accepted direction | Explicitly not decided | Next owner |
|---|---|---|---|---|
| C-01 | Decided | แยก Workflow: พื้นที่ใช้ Manual Approve ส่วนอุปกรณ์ทั่วไปใช้ Auto-approve | รายการประเภทอุปกรณ์เฉพาะทางที่ต้องรออนุมัติ | เจ้าหน้าที่ดูแลห้อง/อุปกรณ์ |
| C-02 | Decided | Auto-cancel คำขอจองเมื่อ No-show เกิน 15 นาที | การนับเวลาในกรณีวันหยุดหรือช่วงปิดทำการ | ทีมพัฒนา / เจ้าหน้าที่ |
| C-03 | Decided | ระบบ Strike เตือน 3 ครั้งก่อนระงับสิทธิ์ 7 วัน | ช่องทางการยื่นอุทธรณ์และผู้มีอำนาจปลดล็อกสิทธิ์ (OQ-03) | ผู้จัดการพื้นที่ |
| C-04 | Decided | ส่งแจ้งเตือนผ่าน Web Notification และ Email สถาบัน | Template ข้อความแจ้งเตือนและการตั้งค่า SMTP | ทีมพัฒนา / IT สถาบัน |

---

## 4. Quality check

- [x] ทุก conflict มี E-ID และอย่างน้อย 2 options
- [x] แยก position / interest / authority / constraint ชัดเจน
- [x] ใช้เกณฑ์ร่วมและบันทึก rationale ตรงกับ Case 01
- [x] ข้อมูลสอดคล้องกับ `docs/04-evidence-log.md` 100%
- [x] สิ่งที่ยังไม่รู้มี owner และบันทึกเป็น Open Questions แล้ว