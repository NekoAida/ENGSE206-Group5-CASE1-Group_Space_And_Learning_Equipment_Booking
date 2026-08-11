# 04 — Evidence, Conflict, Negotiation and Requirement Candidates

> **Week 04 | AI role output is simulation evidence, not an approved real-world fact.**  
> **Team:** Group 5 — Group Space And Learning Equipment Booking System  
> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้

## 1. Evidence Tags

`CF` case fact · `SN` simulated need · `CT` constraint/rule · `OP` opinion · `AS` assumption · `PS` proposed solution · `OQ` open question

---

## 2. Evidence Log

| E-ID | Source/role/session | Tag | Statement / observed event | Context | Confidence + reason | Related/conflicting E-ID | Follow-up/owner |
|---|---|---|---|---|---|---|---|
| E-01 | S-00 Case Card | CF | ปัจจุบันใช้วิธีพูดคุยผ่านแชตส่วนตัวหรือเดินมาถาม ทำให้ข้อมูลไม่เป็น Real-time และเกิดปัญหาจองซ้ำซ้อน | Current process | High (Case Card) | E-02 | ใช้เป็นข้อมูลตั้งต้นโครงงาน |
| E-02 | S-01 นักศึกษา | SN | นักศึกษาต้องการค้นหา ดูตารางเวลาว่าง และส่งคำขอจองพื้นที่/อุปกรณ์ผ่านหน้าเว็บไซต์ได้ตลอด 24 ชม. | Search & Booking | Medium (Simulation) | E-01, E-03 | ยืนยัน UI/UX การเลือกช่วงเวลา |
| E-03 | S-02 เจ้าหน้าที่ดูแลห้อง | SN | การจองพื้นที่ (Space) ต้องให้เจ้าหน้าที่กดอนุมัติก่อนเสมอ เพราะผู้ใช้อาจไม่มาจริงหรือมีอาจารย์ขอแทรก | Approval Workflow | Medium (Simulation) | E-02, E-04 | ยืนยันสิทธิ์ Manual Approve |
| E-04 | S-02 เจ้าหน้าที่ดูแลห้อง | SN | การยืมอุปกรณ์การเรียนรู้ (เช่น สาย HDMI, Webcam) ต้องการความรวดเร็ว หากรออนุมัติทุกชิ้นจะเกิดงานค้าง | Equipment Booking | Medium (Simulation) | E-03 | ยืนยันการ Auto-approve อุปกรณ์ |
| E-05 | S-05 ผู้จัดการพื้นที่ | CT | กำหนดข้อบังคับสถาบัน: นักศึกษาจองใช้ห้องได้ไม่เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน | Usage Constraint | High (Policy Doc) | E-02 | นำไปตั้งค่า Validation Rule บนเว็บ |
| E-06 | S-02 เจ้าหน้าที่ดูแลห้อง | SN | หากจองแล้วไม่มาเช็กอินภายใน 15 นาที ระบบควรกดยกเลิกสิทธิ์ทันทีเพื่อเปิดโอกาสให้ผู้อื่น | No-show Policy | Medium (Simulation) | E-07 | ยืนยันระบบ Auto-cancellation |
| E-07 | S-01 นักศึกษา | SN | ต้องการได้รับการแจ้งเตือนสถานะการจอง (อนุมัติ/ปฏิเสธ/ใกล้ถึงเวลา) ผ่านอีเมลสถาบันหรือหน้าเว็บ | Notification | Medium (Simulation) | E-06 | ยืนยันรูปแบบการส่งข้อความ notification |
| E-08 | S-02 เจ้าหน้าที่ดูแลห้อง | SN | เจ้าหน้าที่ต้องกรอกรหัสครุภัณฑ์ (Asset ID) และบันทึกสภาพอุปกรณ์ลงบนหน้าเว็บเมื่อมีการรับ-คืน | Inventory Tracking | Medium (Simulation) | E-04 | ออกแบบฟอร์มหน้าจอจัดการรับ-คืน |
| E-09 | S-05 ผู้จัดการพื้นที่ | SN | ผู้บริหาร/ผู้จัดการต้องการดูสถิติตารางการจอง อัตราการใช้ห้อง และรายงานผู้ไม่มาตามนัด (No-show) บน Dashboard | Dashboard & Report | Medium (Simulation) | E-05, E-06 | ยืนยันข้อมูลฟิลด์รายงานที่ต้องการ |

---

## 3. Issue and Conflict List

| ID | Evidence-linked issue/conflict | Parties + authority | Positions | Interests/constraints | Status |
|---|---|---|---|---|---|
| C-01 | กระบวนการอนุมัติการจองอุปกรณ์การเรียนรู้ (E-03, E-04) | นักศึกษา vs เจ้าหน้าที่ผู้ดูแล | นักศึกษาต้องการยืมได้ทันที แต่เจ้าหน้าที่กังวลเรื่องการคุมสต็อกอุปกรณ์ | ความสะดวกสะดวกรวดเร็ว vs ความถูกต้องของจำนวนอุปกรณ์ | Decided |
| C-02 | ระยะเวลาในการตัดสิทธิ์ผู้ไม่มาตามนัด (No-show) (E-06) | เจ้าหน้าที่ vs นักศึกษา | เจ้าหน้าที่ต้องการตัดสิทธิ์ใน 10 นาที แต่นักศึกษาขอขยายเป็น 30 นาที | การเปิดโอกาสให้คนอื่นใช้พื้นที่ vs ข้อจำกัดการเดินทางของผู้ใช้ | Decided |
| C-03 | บทลงโทษกรณี No-show ติดต่อกันหลายครั้ง (E-06, E-09) | ผู้จัดการพื้นที่ vs นักศึกษา | ผู้จัดการต้องการตัดสิทธิ์ทันที แต่นักศึกษาขอให้ตักเตือนก่อน | ความเป็นระเบียบของนโยบาย vs ความยืดหยุ่นต่อผู้ใช้งาน | Decided |
| C-04 | ช่องทางการส่งแจ้งเตือนสถานะคำขอ (E-07) | ผู้ดูแลระบบ IT vs นักศึกษา | นักศึกษาต้องการ LINE Notify แต่ผู้ดูแล IT ให้ใช้ Web+Email สถาบัน | ค่าใช้จ่าย/ขอบเขตเทคนิค vs ความสะดวกในการรับข่าวสาร | Decided |

---

## 4. Negotiation Record

| Conflict | Options considered | Evaluation criteria | Decision/status | Rationale + evidence | Follow-up |
|---|---|---|---|---|---|
| **C-01** | A: อนุมัติอัตโนมัติ (Auto-approve)<br>B: ต้องรอเจ้าหน้าที่กดอนุมัติทุกรายการ | Usability / Staff Burden | **Decided** (เลือก A สำหรับอุปกรณ์, เลือก B สำหรับพื้นที่) | การจองห้อง (Space) ต้องรออนุมัติจากเจ้าหน้าที่เสมอ ส่วนอุปกรณ์ให้ Auto-approve แล้วรับของตามคิวหน้าเคาน์เตอร์เพื่อลดภาระงาน (E-03, E-04) | ออกแบบ Logic บนหน้าเว็บไซต์ให้แยกประเภททรัพยากร |
| **C-02** | A: ตัดสิทธิ์ภายใน 10 นาที<br>B: ตัดสิทธิ์ภายใน 15 นาที<br>C: ตัดสิทธิ์ภายใน 30 นาที | Fairness / Resource Utilization | **Decided** (เลือก B) | ระยะเวลา 15 นาทีมีความสมดุลที่สุด ไม่นานเกินไปจนเสียโอกาสการใช้ห้อง และไม่กระชั้นชิดเกินไปสำหรับผู้เดินทาง (E-06) | เขียนเงื่อนไข Auto-cancellation บนระบบหลังบ้าน |
| **C-03** | A: ตัดสิทธิ์การจองทันที 7 วัน<br>B: เตือนผ่านระบบก่อนครบ 3 ครั้ง แล้วค่อยระงับสิทธิ์ 7 วัน | Compliance / Fairness | **Decided** (เลือก B) | ทางเลือก B ช่วยป้องกันกรณีเกิดเหตุสุดวิสัย และเพิ่มความโปร่งใสโดยแสดงสถิติเตือนบนหน้าเว็บผู้ใช้ (E-06, E-09) | ออกแบบระบบนับจำนวน No-show ในฐานข้อมูล |
| **C-04** | A: ส่งผ่าน Email สถาบัน + Web Notification<br>B: เชื่อมต่อ LINE Official Account | Feasibility / Cost / Scope | **Decided** (เลือก A) | ทางเลือก B มีค่าใช้จ่ายและอยู่นอกขอบเขต (Out of Scope) โครงงาน การแจ้งผ่าน Web + Email บนบัญชีสถาบันเหมาะสมที่สุด (E-07) | เชื่อมระบบ Mail Service จำลองบนหน้าเว็บ |

---

## 5. Requirement Candidates

| RC ID | Candidate statement | Rationale | Evidence E-ID | Status | Confidence | Verification / Follow-up |
|---|---|---|---|---|---|---|
| **RC-01** | ระบบหน้าเว็บต้องรองรับการค้นหา ตรวจสอบตารางเวลาว่าง และส่งคำขอจองพื้นที่ทำงานกลุ่มหรืออุปกรณ์การเรียนรู้ | เพื่อให้ผู้ใช้เห็นข้อมูลที่เป็น Real-time และลดการจองซ้ำซ้อน | E-01, E-02 | Candidate | High | ยืนยัน UI ตารางเวลาบนหน้าเว็บ |
| **RC-02** | ระบบต้องมีหน้าจอสำหรับเจ้าหน้าที่ในการตรวจสอบ และกดยอมรับ/ปฏิเสธ (Approve/Reject) คำขอจองพื้นที่ | เพื่อให้เจ้าหน้าที่คัดกรองความถูกต้องก่อนเปิดใช้ห้อง | E-03 | Candidate | High | ยืนยัน Workflow หน้าจอจัดการ |
| **RC-03** | ระบบต้องรองรับการอนุมัติการจองอุปกรณ์แบบอัตโนมัติ (Auto-approve) ตามลำดับคิวความพร้อมของอุปกรณ์ | ลดความล่าช้าในการยืมอุปกรณ์ และลดภาระงานเจ้าหน้าที่ | E-04 | Candidate | Medium | ตรวจสอบ Logic จำนวนสต็อกอุปกรณ์ |
| **RC-04** | ระบบต้องมี Validation Rule ตรวจสอบเงื่อนไขการจองไม่ให้เกิน 3 ชั่วโมง/วัน และจองล่วงหน้าไม่เกิน 7 วัน | บังคับใช้กฎนโยบายของสถาบันอย่างเป็นธรรม | E-05 | Candidate | High | ทดสอบเงื่อนไขการกรอกฟอร์ม |
| **RC-05** | ระบบต้องมียกเลิกการจองอัตโนมัติ (Auto-cancellation) หากผู้ใช้ไม่มาแสดงตนภายใน 15 นาทีหลังถึงเวลาจอง | ลดปัญหาทรัพยากรถูกจองทิ้งไว้โดยไม่มีผู้ใช้งานจริง | E-06 | Candidate | High | ยืนยันการทำงานของ Cron Job/Timer |
| **RC-06** | ระบบต้องรองรับการส่งแจ้งเตือนสถานะคำขอจองผ่านทาง Web Notification และ Email สถาบัน | เพื่อให้ผู้ใช้งานทราบความคืบหน้าของคำขอทันเวลา | E-07 | Candidate | Medium | ยืนยันการเชื่อมต่อ Mail API |
| **RC-07** | ระบบต้องรองรับการบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ในขั้นตอนการส่งมอบและรับคืน | เพิ่มความโปร่งใสและใช้เป็นหลักฐานติดตามอุปกรณ์ | E-08 | Candidate | High | ยืนยัน ฟอร์มบันทึกรับ-คืน |
| **RC-08** | ระบบต้องมีหน้า Dashboard แสดงรายงานสถิติการใช้งานห้อง อัตราการยืมอุปกรณ์ และประวัติ No-show สำหรับผู้บริหาร | เพื่อสนับสนุนการตัดสินใจและวางแผนจัดสรรงบประมาณ | E-09 | Candidate | Medium | ยืนยันรูปแบบ กราฟ/ตาราง บน Dashboard |

---

## 6. Quality Check

* [x] Statement and team interpretation are separated.
* [x] Every finding has source/tag/context/confidence.
* [x] Contradictions remain visible; no silent merging.
* [x] Conflict includes interests, authority and ≥2 options.
* [x] RCs cite E-IDs and do not claim real-world approval.
* [x] No personal/confidential data; AI use logged.