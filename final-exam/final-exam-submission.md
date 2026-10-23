# ใบส่งงานสอบปลายภาค ส่วน ก งานกลุ่ม

| รายการ | ข้อมูล |
|---|---|
| กลุ่ม / Case | กลุ่ม 5 · Case 1 |
| ชื่อระบบ | Group Space and Learning Equipment Booking System |
| CR หลัก / เสริม | CR-FX-01 + CR-FX-02A (Pending; decision เป็น Proposed) |
| Branch | `final-exam` |
| Pull Request | [submit(final): change-to-design take-home](https://github.com/NekoAida/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/pull/4) · `final-exam` → `main` · Open |
| กำหนดส่งล่าสุด | 23 ตุลาคม 2569 เวลา 23:59 น. (Asia/Bangkok, UTC+07:00) ตามข้อมูลล่าสุดที่ผู้ส่งงานแจ้ง |
| T0 ตาม README รายวิชา | 20 ตุลาคม 2569 เวลา 09:00 น.; กำหนดส่งล่าสุดข้างต้นเป็นข้อมูลเพิ่มเติมจากผู้ส่งงาน ไม่อ้างว่าเป็น T0 + 24 ชั่วโมงตาม README |
| Commit งานคำตอบสุดท้าย | `e0b7b4abe36c9c1bf7ca384a0b5c6015e1e93bf8` — รวม Word, diagrams และข้อมูลรับรอง; commit ถัดมาบันทึก PR/hash ในใบส่งงานเท่านั้น |
| Commit ล่าสุดของการส่ง | ดู hash ล่าสุดใน [PR commits](https://github.com/NekoAida/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/pull/4/commits); hash HEAD หลังบันทึกใบส่งงานระบุในรายละเอียด PR |
| Snapshot ที่ใช้ทบทวนฐาน | `da4c30ac84a7b1189b3bdedffe84bc3d2ed2a06d` (snapshot ของฐานก่อนแก้คำตอบ) |
| สถานะ SRS | Baseline Candidate ตามไฟล์เดิม ไม่อ้างอนุมัติ |

## งานเดิมที่ใช้เป็นฐาน

ไฟล์ต่อไปนี้อ้าง snapshot ด้านบน ไม่แก้ไฟล์งานเดิม:

| งาน | Path |
|---|---|
| SRS W07 | `docs/07-srs-v1.md` |
| Models W06 | `docs/06-requirement-models.md` |
| W08 | `docs/08-validation-traceability.md` |
| W10 / Spine | `design/10-design-strategy.md` ยังเป็น template จึงใช้ `design/00-design-spine.md` ที่ถอดจาก SRS ใน W11 |
| W11 | `design/11-conceptual-architecture.md` และ `design/11-conceptual-architecture-v0.1.docx` |

## ไฟล์ที่ส่ง

- [x] `final-exam/final-exam-group-answer.docx` (G1–G6 และภาพฝัง)
- [x] `final-exam/diagrams/context-after.drawio` + `context-after.drawio.png`
- [x] `final-exam/diagrams/container-after.drawio` + `container-after.drawio.png`
- [x] `final-exam/final-exam-submission.md`
- [x] `final-exam/ai-use-log.md`

## การมีส่วนร่วม

สมาชิกทั้งสองอ่านฉบับแก้และยืนยันการมีส่วนร่วมกับ AI log แล้ว ตามการยืนยันของผู้ส่งงานในแชต; อ้างหลักฐานเป็นส่วนในไฟล์ ไม่อ้างชื่อ commit ที่ตรวจไม่ได้

| สมาชิก | ส่วนที่รับผิดชอบ | หลักฐานที่อ้างได้ |
|---|---|---|
| วรสิทธิ์ บุญยปรีดี 68543210017-8 | G1, G2, G4 | ส่วน G1/G2/G4 ใน Word; สมาชิกยืนยันแล้ว |
| ปริษฎา สุทธดุก 68543210015-2 | G3, G5, G6 และภาพ | ส่วน G3/G5/G6 และภาพท้าย G4; สมาชิกยืนยันแล้ว |

## ตรวจและรับรองก่อนส่ง

- [x] ข้อเสนอใหม่ใช้ ID ที่มี FX แยกจาก baseline
- [x] ค่าที่ยังไม่ตกลงเป็น TBD พร้อม OI-FX/DD-FX; ใช้ stack เดิม
- [x] CR Pending และ decision Proposed; ไม่อ้าง SRS/CR Approved
- [x] แก้เฉพาะไฟล์ใน `final-exam/`
- [x] สมาชิกทั้งสองอ่านฉบับแก้และยืนยันตารางการมีส่วนร่วม/AI log ตามจริง ตามการยืนยันของผู้ส่งงาน
- [x] commit/push ผ่านบัญชี NekoAida และกรอก hash งานคำตอบจริง; ประวัติมี NekoAida และ ThunderXD11 ไม่แก้ชื่อผู้เขียนย้อนหลัง
- [x] เปิด PR #4 ชื่อถูกต้องจาก `final-exam` เข้า `main` เมื่อ 22 ตุลาคม 2569 ก่อนกำหนดล่าสุด 23 ตุลาคม 2569 เวลา 23:59 น. ตามข้อมูลผู้ส่งงาน; ไม่อ้างว่าส่งทัน T0 + 24 ชั่วโมงตาม README เดิม

## แหล่งอ้างอิงวิธีส่ง

[README สัปดาห์ 15 ของรายวิชา](https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-15-final-exam/README.md) ระบุให้ส่งส่วน ก ผ่าน PR จาก `final-exam` เข้า `main` ชื่อ `submit(final): change-to-design take-home`; กำหนดส่งวันที่ 23 ตุลาคม 2569 เวลา 23:59 น. ใช้ตามข้อมูลล่าสุดจากผู้ส่งงาน
