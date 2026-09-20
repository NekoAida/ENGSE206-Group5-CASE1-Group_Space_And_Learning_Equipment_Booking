# Week 07 Submission — SRS Authoring Studio

- **Assignment:** W07-v1.0
- **Case ID และทีม:** Case 01 — Group 5 (Group Space and Learning Equipment Booking Website)
- **สมาชิก:**
  1. นายวรสิทธิ์ บุญยปรีดี (68543210017-8) — Requirements Lead & Facilitator
  2. นางสาวปริษฎา สุทธดุก (68543210015-2) — Quality Checker & Scribe
- **SRS Document ID / Version:** `CASE01-SRS-W07-v1` / `0.1-draft`
- **Status:** Baseline Candidate
- **W05/W06 Source Snapshot:**
  - W05 Backlog: `docs/05-requirement-backlog.md` (v1.2 Baseline Locked - CR-02 Applied, 2026-08-18)
  - W06 Models: `docs/06-requirement-models.md` (W06 Baseline Candidate, 2026-08-25)
- **Submission Date:** 2026-09-19
- **Commit Message:** `submit(w07): SRS draft v1`
- **Commit Hash:** [กรอกหลัง push git จริง]

---

## 1. File Manifest

| Artifact | Path / Link ที่เปิดได้ | Version / Date | หมายเหตุ |
|---|---|---|---|
| **SRS หลัก (หัวข้อ 0–12)** | [`../docs/07-srs-v1.md`](../docs/07-srs-v1.md) | v1.0 / 2026-09-19 | เอกสารข้อกำหนดความต้องการซอฟต์แวร์ฉบับสมบูรณ์ |
| **Requirement Disposition** | [`../evidence/week-07/disposition.csv`](../evidence/week-07/disposition.csv) | 2026-09-19 | บันทึกการรับเข้าของทุก Backlog ID (Appendix A) |
| **Traceability Matrix** | [`../evidence/week-07/traceability.csv`](../evidence/week-07/traceability.csv) | 2026-09-19 | ตาราง Traceability สองทาง (W04->W05->W06->SRS->VF) |
| **Open Issues Register** | [`../evidence/week-07/open_issues.csv`](../evidence/week-07/open_issues.csv) | 2026-09-19 | ทะเบียนข้อค้างคาพร้อม Owner และ Due Date |
| **Peer Review Record** | [`../evidence/week-07/peer_review.csv`](../evidence/week-07/peer_review.csv) | 2026-09-19 | บันทึกการตรวจทานระหว่างสมาชิกในทีม |
| **Revision Record** | [`../evidence/week-07/revision.csv`](../evidence/week-07/revision.csv) | 2026-09-19 | บันทึกประวัติการปรับแก้ข้อความ (Before/After) |
| **AI Use Disclosure** | [`../evidence/week-07/ai_disclosure.csv`](../evidence/week-07/ai_disclosure.csv) | 2026-09-19 | รายงานความโปร่งใสในการใช้ AI ช่วยจัดทำเอกสาร |
| **Worklog รายบุคคล** | [`../evidence/week-07/worklog.csv`](../evidence/week-07/worklog.csv) | 2026-09-19 | บันทึกเวลาและกิจกรรมของสมาชิกทุกคน |
| **Exit Tickets ทุกคน** | [`../evidence/week-07/exit_ticket.md`](../evidence/week-07/exit_ticket.md) | 2026-09-19 | คำตอบประเมินตนเองรายบุคคลครบทุกคน |

---

## 2. Student Core Checks

- [x] **โครงสร้าง SRS:** หัวข้อ 0–12 ครบถ้วนตาม Student SRS Template และทุก Backlog ID ใน W05 มี Disposition ครบถ้วน
- [x] **Deep Specification:** มี FR เจาะลึก 3 ข้อ (`FR-01`, `FR-02`, `FR-05`) และ BR ที่เกี่ยวข้อง 3 ข้อ (`BR-01`, `BR-02`, `BR-03`)
- [x] **Behavior References:** อ้างอิงและเชื่อมโยง User Stories (`US-01..10`), Use Cases (`UC-01..06`) และ Acceptance Criteria (`AC-01..10`) จาก W06
- [x] **Quality & Data:** มี NFR ด้าน Auditability (`NFR-01`) และ Concurrency (`NFR-03`) พร้อม Conceptual Data Concepts 5 ตัว (`DR-01..05`)
- [x] **Traceability & Open Issues:** Trace ไป-กลับสมบูรณ์ และเปิดเผยสถานะ Partial/Extension/TBD ใน Open Issues (`OI-01..04`) ตามจริง
- [x] **Review Evidence:** มีหลักฐาน Review, Revision, Worklog, AI Disclosure และ Exit Tickets ครบทั้ง 2 คน
- [x] **ความซื่อสัตย์ทางวิชาการ:** ไม่มีการอ้าง Approved Baseline หรือ Test Passed โดยไม่มีหลักฐานรองรับจริง

---

## 3. Review Result และ Week 08 Handoff

- **ผู้ตรวจ / Version ที่ตรวจ:** นายวรสิทธิ์ บุญยปรีดี, นางสาวปริษฎา สุทธดุก (Peer Review / Draft v0.1 สู่ Baseline Candidate v1.0)
- **Gate Result:** **Passed Gate** — เหมาะสมในการใช้เป็น Baseline Candidate สำหรับการนำไปออกแบบ System & Architecture Design ใน Week 08
- **Open Issues ที่กระทบการออกแบบใน Week 08:**
  - `OI-01`: นโยบายบทลงโทษ No-show (กระทบการออกแบบ Database Schema สถานะผู้ใช้ และ Background Job)
  - `OI-02`: สเปกการเชื่อมต่อ Email SMTP/API สถาบัน (กระทบการออกแบบ Notification Service และ Fallback Architecture)
  - `OI-03`: รายการอุปกรณ์ที่ Auto-approve (กระทบ Logic การสร้าง Booking และ State Transition)
- **สิ่งที่ต้องทำต่อก่อนส่ง Week 08:**
  - ติดตามลายลักษณ์อักษรของ No-show Policy จากผู้จัดการพื้นที่
  - ทดสอบการเชื่อมต่อ Mail Server หรือสรุปการใช้ Mock Service สำหรับช่วงการพัฒนา Prototype

---

## 4. สรุปการมีส่วนร่วมของสมาชิก (Team Contribution)

| Member | Role / Work completed | Evidence (Commit / File) |
|---|---|---|
| **วรสิทธิ์ บุญยปรีดี** (68543210017-8) | Requirements Lead & Facilitator: ร่างโครงสร้าง SRS, Deep Spec FR-01/02, จัดทำ Traceability และตรวจสอบ Reconcile Backlog W05 | `docs/07-srs-v1.md`, `evidence/week-07/traceability.csv`, `evidence/week-07/worklog.csv`, `evidence/week-07/exit_ticket.md` |
| **ปริษฎา สุทธดุก** (68543210015-2) | Quality Checker & Scribe: Deep Spec FR-05, จัดทำ BR/NFR/Data Concepts, ลงทะเบียน Open Issues และบันทึก Review/Revision | `docs/07-srs-v1.md`, `evidence/week-07/open_issues.csv`, `evidence/week-07/peer_review.csv`, `evidence/week-07/exit_ticket.md` |

---

## 5. การเปิดเผยการใช้ AI (AI Use Disclosure)

| Activity | AI Assistance | Human Decision / Verification | Source / Evidence |
|---|---|---|---|
| ร่างและจัดโครงสร้าง SRS ตามเทมเพลต Week 07 | Antigravity (Gemini) ช่วยจัดรูปแบบ Markdown ตาราง และสกัดข้อความจากเอกสารเดิม | ตรวจสอบ Reconcile ID ทุกตัว ไม่ให้ตกหล่นหรือบิดเบือนความหมายเดิมของเคส | `docs/07-srs-v1.md`, `evidence/week-07/ai_disclosure.csv` |
| ตรวจสอบความสอดคล้องของ Trigger / Guard / Result | ให้ AI ช่วยทบทวนเงื่อนไขขอบเขตการทำงานของ Core Flow | ปรับแก้ระยะเวลา No-show ให้เป็น 15 นาทีตามหลักฐานเดิม และกำหนด Append-Only Log | `evidence/week-07/revision.csv` |
