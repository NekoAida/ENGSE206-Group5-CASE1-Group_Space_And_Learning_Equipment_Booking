# AI Use Log

> บันทึกเฉพาะการใช้ AI ที่มีผลต่อข้อความ การวิเคราะห์ รูปภาพ หรือโครงสร้างชิ้นงาน เพื่อความโปร่งใสและการตรวจสอบย้อนกลับ

| Date | Tool | Purpose | Input Summary (ไม่ใส่ข้อมูลลับ) | Output Used | Human Verification / Revision | Related File |
|---|---|---|---|---|---|---|
| [date] | [tool] | brainstorm / proofread / diagram idea | [สรุป] | [ใช้ส่วนใด] | [ตรวจ/แก้อย่างไร] | `docs/...` |
| 2026-10-02 | ZCode (GLM) | ร่างโครงเอกสาร + ตาราง + ไดอะแกรม + ไฟล์ Word | สรุปโจทย์ Lab W11 และข้อมูลจาก SRS/Backlog ของทีม (ไม่มีข้อมูลลับ) | โครง 11 หัวข้อตาม Lab, context/container diagram (.drawio+.png), ฟอร์ม Word W11, การแปลง SRS W07 เป็น Word, Design Spine | สมาชิกต้องตรวจ ID ทุกตัว (FR/BR/NFR/OI/UC/AC) เทียบ SRS, ตรวจว่าไม่มีการเดาค่า TBD (ทุก TBD ชี้ DD-01–06), ตรวจรูปกับป้ายลูกศร ก่อน commit | `design/11-*`, `diagrams/architecture/*`, `docs/07-srs-v1.docx`, `design/00-design-spine.md` |
