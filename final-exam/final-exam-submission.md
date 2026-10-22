# ใบส่งงานสอบปลายภาค — ส่วน ก งานกลุ่ม (Change-to-Design)

> วางไฟล์นี้ที่ `final-exam/final-exam-submission.md` ใน branch `final-exam` ของ Team Repo

| รายการ | กรอก |
|---|---|
| กลุ่ม / Case | กลุ่ม 5 · Case 01 (ENGSE206-Group5-CASE1) |
| ชื่อระบบ | Group Space and Learning Equipment Booking System |
| CR เสริมที่เลือก | CR-01 (การปรับเกณฑ์เวลา Soft Lock สำหรับผู้พิการทางสายตาเป็น 10 นาที) |
| Branch | `final-exam` |
| Pull Request | `submit(final): change-to-design take-home` |
| Commit hash สุดท้าย (ก่อน T0 + 24 ชั่วโมง) | `a8f3b21c4e9d7e6f` |
| สถานะ SRS ที่ใช้เป็นฐาน | Baseline Candidate — *ไม่อ้างว่า Approved* |

## งานเดิมที่ใช้เป็นฐาน

| งาน | ไฟล์และ commit หรือวันที่ |
|---|---|
| SRS (W07) | `docs/07-srs-v1.md` (Commit: `3c1a9d0` · 2026-08-28) |
| งาน W08 (review · trace · CR) | `docs/08-requirements-traceability-and-change.md` (Commit: `4f2b1c8` · 2026-09-04) |
| Design Strategy + Design Spine (W10) | `docs/10-design-strategy.md` & `design/00-design-spine.md` (Commit: `7e9a2b4` · 2026-09-18) |
| Conceptual Architecture (W11) | `design/11-conceptual-architecture.md` (Commit: `9b8c7d6` · 2026-09-25) |

## ไฟล์ที่ส่ง

- [x] `final-exam/final-exam-group-answer.docx`
- [x] `final-exam/diagrams/context-after.drawio` + `.png`
- [x] `final-exam/diagrams/container-after.drawio` + `.png`
- [x] `final-exam/final-exam-submission.md` (ไฟล์นี้)
- [x] `final-exam/ai-use-log.md`

## สมาชิกและส่วนที่รับผิดชอบ

| ชื่อ–สกุล | รหัส | รับผิดชอบ (G / ข้อ) | หลักฐาน (commit หรือส่วนในไฟล์) |
|---|---|---|---|
| วรสิทธิ์ บุญยปรีดี | 68543210017-8 | G1, G2 (Impact Analysis & C4 Container Architecture) | Commit: `a8f3b21` · Section G1, G2 ใน `final-exam-group-answer.docx` |
| วรสิทธิ์ บุญยปรีดี | 68543210017-8 | G3 (Design Drivers & Concurrency Control Strategy) | Commit: `b7e2c10` · Section G3 ใน `final-exam-group-answer.docx` |
| ปริษฎา สุทธดุก | 68543210015-2 | G4 (Sequence Diagram & Component Interactions) | Commit: `c1d2e3f` · Section G4 ใน `final-exam-group-answer.docx` |
| ปริษฎา สุทธดุก | 68543210015-2 | G5 (Traceability & Open Decisions Verification) | Commit: `d4e5f6a` · Section G5 & `ai-use-log.md` |

## รับรอง

- [x] สมาชิกทุกคนอ่านคำตอบทั้งฉบับ และอธิบายส่วนใดก็ได้ใน oral spot-check
- [x] ไม่มีตัวเลข นโยบาย หรือ protocol ที่แต่งขึ้น — ค่าที่ไม่รู้เป็น TBD และมี OI หรือ DD รองรับ
- [x] ไม่อ้างว่า SRS หรือ CR ใด Approved
- [x] ไม่ได้แก้ไฟล์งานเดิมของแต่ละสัปดาห์ — ทุกอย่างอยู่ใน `final-exam/`
```
