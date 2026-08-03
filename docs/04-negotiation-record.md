# Week 04 — Conflict and Negotiation Record

## 1. Negotiation method

แต่ละประเด็นแยก Position (สิ่งที่แต่ละฝ่ายเรียกร้อง) ออกจาก Interest (เหตุผลหรือผลลัพธ์ที่ต้องการ) ตรวจ authority/constraint แล้วเปรียบเทียบ options ด้วยเกณฑ์ร่วม ได้แก่ usability, operational effort, fairness, traceability, privacy และ feasibility

## 2. Negotiation register

### N-01 — Quick issue reporting vs complete information

| Field | Record |
|---|---|
| Evidence | E-04, E-12 |
| Position A — นักศึกษา / ผู้พบปัญหา / อาจารย์ | ต้องการแจ้งปัญหาได้รวดเร็ว |
| Interest A | แจ้งได้ทันที ไม่เสียเวลาหาผู้รับผิดชอบ และมีผู้รับเรื่องเร็ว |
| Position B — เจ้าหน้าที่อาคาร / เจ้าหน้าที่เทคนิค / แม่บ้าน / ผู้ดูแลความปลอดภัย / ผู้ดูแลระบบ | ต้องการข้อมูลครบถ้วนและถูกต้องก่อนรับเรื่อง |
| Interest B | วิเคราะห์ปัญหาได้ ลดการถามกลับ ลดข้อมูลซ้ำ จัดลำดับความสำคัญได้ และตรวจสอบย้อนหลังได้ |

| Option | Description | Usability | Operational effort | Traceability/Risk |
|---|---|---:|---:|---|
| A | ปฏิเสธคำขอทันทีเมื่อข้อมูลไม่ครบ | Low | Medium | ชัดเจน แต่ผู้ใช้อาจเริ่มใหม่หลายครั้ง |
| B | รับคำขอเป็น Draft/Incomplete โดยยังไม่กันทรัพยากรจนข้อมูลขั้นต่ำครบ | High | Medium | ต้องแสดงสถานะและรายการที่ขาดชัดเจน |
| C | กันทรัพยากรทันทีแม้ข้อมูลไม่ครบ | High | High | เสี่ยงกักทรัพยากรและเกิด no-show |

**Decision/status:** เลือก Option B เป็น Provisional เพราะตอบสนอง interest ของทั้งสองฝ่ายและมีความสามารถตรวจสอบย้อนหลังได้  
**Rationale:** E-04 แสดงว่า cost ของคำขอที่ไม่ครบข้อมูลค่อนข้างสูง ในขณะที่ E-12 แสดงความต้องการความรวดเร็ว; การใช้ Draft จึงช่วยแยกการเริ่มคำขอออกจากการยืนยันการจองทรัพยากร  
**Unresolved:** required fields, ระยะเวลาคงอยู่ของ Draft และผู้มีสิทธิ์แก้ไข  
**Derived candidates:** RC-02, RC-03

### N-02 — Learning schedule/urgent activity vs existing request

| Field | Record |
|---|---|
| Evidence | E-07, E-11 |
| Position A — นักศึกษา | คำขอที่ยืนยันแล้วไม่ควรถูกยกเลิกโดยไม่แจ้งและไม่มีเหตุผล |
| Interest A | ความคาดการณ์ได้และความเป็นธรรม |
| Position B — อาจารย์ / เจ้าหน้าที่อาคาร / เจ้าหน้าที่เทคนิค / แม่บ้าน / ผู้ดูแลความปลอดภัย | กิจกรรมการเรียนหรือเหตุจำเป็นอาจต้องใช้ทรัพยากร |
| Interest B | รักษาภารกิจการเรียนและจัดการกรณีเร่งด่วนหรือ exception ได้ |
| Authority/constraint | ต้องมีผู้มีสิทธิ์พิจารณาและอนุมัติ exception รวมทั้งต้องมีการเชื่อมต่อกับตารางเวลาและนโยบายที่ชัดเจน; ST-04 ยังไม่กำหนด policy |

| Option | Description | Fairness | Feasibility | Auditability |
|---|---|---:|---:|---:|
| A | First-come-first-served โดยไม่มี exception | Medium | High | High |
| B | ผู้มีอำนาจส่ง exception request พร้อมเหตุผล ผลกระทบ และการแจ้งผู้ได้รับผล | High | Medium | High |
| C | Override อัตโนมัติจากตารางเรียน | Low–Medium | Unknown | Medium และเสี่ยงต่อข้อมูลผิด |

**Decision/status:** เลือก Option B เป็น Provisional; ไม่เลือก automatic override เพราะ E-11 ยังไม่ยืนยันการเชื่อมต่อกับระบบตารางเรียน  
**Rationale:** การรักษาสิทธิ์ในการตัดสินใจและ audit trail โดยไม่ยืนยันว่า exception ทุกกรณีได้รับอนุมัติ  
**Unresolved:** authority matrix, notice period, alternative resource และ appeal mechanism  
**Derived candidate:** RC-04

### N-03 — No-show control vs fair treatment

| Field | Record |
|---|---|
| Evidence | E-08, E-12, E-13 |
| Position A — เจ้าหน้าที่อาคาร / เจ้าหน้าที่เทคนิค / แม่บ้าน | ต้องลด no-show เพื่อไม่ให้ทรัพยากรถูกจองแล้วไม่ได้ใช้ |
| Interest A | เพิ่มการใช้ทรัพยากรและลดภาระงาน |
| Position B — นักศึกษา | ไม่ควรลงโทษเหมือนกันทุกกรณี โดยเฉพาะกรณีเหตุจำเป็น |
| Interest B | ความเป็นธรรมและมีโอกาสชี้แจง |
| Authority/constraint | ยังไม่มี policy source หรือตัวเลขที่ยืนยันจาก E-08 |

| Option | Description | Fairness | Operational effort | Evidence status |
|---|---|---:|---:|---|
| A | ลงโทษอัตโนมัติทุกกรณี no-show | Low | Low | Unsupported |
| B | บันทึกเหตุการณ์และแจ้งเตือน; ผลลัพธ์ตาม policy จะพิจารณาต่อไป | High | Medium | Supported at candidate level |
| C | ไม่บันทึกและไม่ดำเนินการ | Medium | Low | ไม่ตอบสนอง operational need |

**Decision/status:** ยัง Unresolved ในส่วน penalty/suspension; ยอมรับเพียงแนวทาง Option B ในเรื่องการบันทึกเหตุการณ์และแจ้งสถานะเป็น candidate  
**Rationale:** E-08 ยืนยันเพียงว่ายังไม่มีนโยบายที่อนุญาตให้ทีมกำหนดบทลงโทษโดยอัตโนมัติ  
**Unresolved owner:** ผู้ดูแลระบบ / ผู้มีอำนาจกำหนดนโยบาย; ต้องทบทวนใน Week 05 ก่อนการพิจารณา prioritization  
**Derived candidate:** RC-05 เฉพาะเรื่อง cancellation/status; penalty ไม่สร้างเป็น RC

## 3. Decision summary

| N-ID | Status | Accepted direction | Explicitly not decided | Next owner |
|---|---|---|---|---|
| N-01 | Provisional | Draft/Incomplete โดยไม่กันทรัพยากรจนข้อมูลขั้นต่ำครบ | required fields และ draft lifetime | ST-02 / ST-03 |
| N-02 | Provisional | exception request พร้อม authority, rationale และการแจ้งผู้ได้รับผลกระทบ | automatic override และ notice period | ST-03 + schedule owner |
| N-03 | Unresolved | บันทึก event/status ได้ | penalty/suspension/appeal rule | Authorized policy owner |

## 4. Quality check

- [x] ทุก conflict มี E-ID และอย่างน้อย 2 options
- [x] แยก position / interest / authority / constraint
- [x] ใช้เกณฑ์ร่วมและบันทึก rationale
- [x] status ไม่ overclaim ว่า Approved
- [x] สิ่งที่ยังไม่รู้มี owner และไม่ถูกเติมด้วยสมมติฐาน