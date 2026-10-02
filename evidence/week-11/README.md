# Evidence — Week 11: Conceptual Architecture

- วันที่: 2026-10-02 (จัดทำล่วงหน้าก่อนคาบ — รอ Checkpoint 1–2 และ Miro review ในคาบ)
- กิจกรรม: Workshop "Context & Container (180 min)" — สร้าง C4 Level 1/2, NFR mapping, Decision Cards, เดิน Spine
- ผู้เข้าร่วม/บทบาท: วรสิทธิ์ บุญยปรีดี (Architecture Owner / Drawer), ปริษฎา สุทธดุก (Quality Checker / Scribe) — ร่างด้วยความช่วยเหลือ AI และรอสมาชิกตรวจก่อน commit
- หลักฐานที่เก็บ: ไดอะแกรม .drawio + .png, ฟอร์ม Word 11 หัวข้อ, Design Spine — รายการอยู่ด้านล่าง
- สิ่งที่ค้นพบ: FR-03/BR-02 (ตัดสิทธิ์ No-show "อัตโนมัติ") + VF-03 ("Background Worker") บังคับให้ต้องมี container ที่ 4 = Scheduled Job (DEC-03) ส่วนความถี่รอบสแกนเป็น TBD (DD-03) ห้ามเดาค่า
- ผลกระทบต่อ artefact: `design/11-conceptual-architecture.md`, `design/00-design-spine.md` (สร้างใหม่), `diagrams/architecture/*`

## Files

- [x] `context-diagram.drawio` / `context-diagram.png` — C4 Level 1 (ระบบเดียว + 4 actors + 2 external systems)
- [x] `container-diagram.drawio` / `container-diagram.png` — C4 Level 2 (Web + API + DB + Scheduled Job + ขอบเขต trust boundary)
- [x] `../design/11-conceptual-architecture-v0.1.docx` — ฟอร์ม 11 หัวข้อพร้อมภาพที่ 1–2
- [ ] Miro "Group 5 — W11" frame: ภาพก่อน/หลังแก้ตาม feedback เพื่อน (ถ่าย/ส่งออกแล้ววางที่โฟลเดอร์นี้หลังคาบ)
- [ ] ภาพถ่าย worksheet (ถ้ามี)
