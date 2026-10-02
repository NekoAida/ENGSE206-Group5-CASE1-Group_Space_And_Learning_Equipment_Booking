# Week 11 Submission — Conceptual Architecture

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W11-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/tree/main/weeks/week-11-conceptual-architecture |
| Course version/commit read | main @ 2026-10-02 (lab.html + assignment-contract + index ตัวอย่าง CRBS) |
| Date checked | 2026-10-02 |
| Case ID / Case URL | Case No. 01 — Group Space and Learning Equipment Booking · https://github.com/NekoAida/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **Architecture View + Rationale** (Context C4 L1 + Container C4 L2 + NFR mapping + Decision Cards + Spine walk)

Expected paths: `design/11-conceptual-architecture.md`, `design/11-conceptual-architecture-v0.1.docx`, `design/00-design-spine.md`, `diagrams/architecture/`, `submissions/week-11-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| ฟอร์ม Word 11 หัวข้อ (ภาพที่ 1–2 ฝังในเล่ม) | `design/11-conceptual-architecture-v0.1.docx` | วรสิทธิ์ บุญยปรีดี (ร่างด้วยความช่วยเหลือ AI — ดู §6 และ AI Use Log) | Submitted (Proposed v0.1) |
| สรุปฉบับ Markdown | `design/11-conceptual-architecture.md` | วรสิทธิ์ บุญยปรีดี | Submitted |
| Context diagram (C4 L1) | `diagrams/architecture/context-diagram.drawio` + `.png` | วรสิทธิ์ บุญยปรีดี | Submitted |
| Container diagram (C4 L2) | `diagrams/architecture/container-diagram.drawio` + `.png` | วรสิทธิ์ บุญยปรีดี | Submitted |
| Design Spine + คอลัมน์ W11 | `design/00-design-spine.md` | ทีม (ถอดจาก SRS) | Submitted |
| Worklog + AI use log | `project-management/team-worklog.md`, `project-management/ai-use-log.md` | ปริษฎา สุทธดุก | Updated 2026-10-02 |

## 3. Evidence and Quality Check

- [x] มี source file ที่แก้ไขได้ (`.drawio` 2 ไฟล์ + `.md`)
- [x] diagram มี `.drawio` และ export `.png` ครบทั้ง 2 รูป
- [x] evidence อ้างอิงกลับไปยัง artefact ได้ (`evidence/week-11/README.md`)
- [x] อัปเดต worklog และ AI use log แล้ว
- [ ] peer/instructor feedback ถูกบันทึกแล้ว *(รอ Checkpoint 1–2 ในคาบ — ยังไม่ได้ทำ Miro review จริง เมื่อทำแล้วแนบภาพ before/after ที่ `evidence/week-11/`)*
- [x] ไม่มีข้อมูลส่วนบุคคล/secret

## 4. Team Contribution

| Member | Role / Work completed | Evidence (commit/file) |
|---|---|---|
| วรสิทธิ์ บุญยปรีดี | Architecture Owner — ถอด drivers/spine จาก SRS, กำหนด container + NFR mapping + decision cards, ตรวจความถูกของ ID | `design/11-*`, `design/00-design-spine.md`, `diagrams/architecture/` |
| ปริษฎา สุทธดุก | Quality Checker & Scribe — ตรวจ ID ทุกตัวเทียบ SRS, จัดการ evidence + worklog + AI use log, จัดทำไฟล์ Word คู่ | `evidence/week-11/`, `project-management/*`, `design/11-conceptual-architecture-v0.1.docx` |

> หมายเหตุความโปร่งใส: ร่างแรกของเอกสาร/ไดอะแกรมจัดทำด้วยความช่วยเหลือของ AI (ZCode/GLM) และ**ต้อง**ได้รับการตรวจสอบโดยสมาชิกก่อน commit ตามกติกาทีม — ดู `project-management/ai-use-log.md` และหัวข้อ 11 ของฟอร์ม Word

## 5. Tabletop / Review Summary

- สิ่งที่นำเสนอ: (แผน) ภาพที่ 1–2 + คำถามบังคับ "driver ที่ห้ามพลาด (D1 กันจองซ้ำ) อยู่ container ไหน" → คำตอบ: **API + Database** (DEC-01, DEC-02)
- Feedback ที่ได้รับ: รอ Checkpoint ในคาบ (ยังไม่ได้ทำจริง — จะบันทึกเพิ่มหลังคาบ)
- สิ่งที่แก้ก่อนส่ง: ตามผล Done Checklist หัวข้อ 10 ของฟอร์ม Word (ผ่านครบ 6 ข้อตามที่ตรวจเอง ณ 2026-10-02)

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w11): conceptual architecture` |
| Commit hash | [กรอกหลัง push] |
| Submitted at | [YYYY-MM-DD HH:MM] |
| Known limitations / open questions | DD-01 โปรโตคอลยืนยันตัวตน (AS-01) · DD-02 กลไกกันจองซ้ำระดับ DB · DD-03 ความถี่รอบสแกน No-show · DD-04 Email API (OI-02) · DD-05 บทลงโทษ No-show สะสม (OI-01) · DD-06 KPI Dashboard (OI-03) — ทั้งหมดเป็น TBD ที่ชี้ปลายทางชัดเจน ไม่มีการเดาค่า |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| | | | |
