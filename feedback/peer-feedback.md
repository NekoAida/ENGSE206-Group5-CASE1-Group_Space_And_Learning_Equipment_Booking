# Peer Feedback & Requirement Baseline Review Summary

**Repository:** `NekoAida/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking`  
**Review Date:** 2026-08-18  
**Activity:** Requirement Baseline Review & Readiness Gate (Week 05)  
**Overall Status:** **ผ่านแบบมีจุดต้องแก้ก่อนส่ง (Pass with Required Fixes)**  
**Evaluation Score:** **8.5 / 10**

---

## 1. ตารางสรุปข้อเสนอแนะภาพรวม (Peer Feedback Matrix)

| Date | Reviewer | Artefact / Target ID | Strengths | Questions / Suggestions / Points to Fix | Action Taken |
|---|---|---|---|---|---|
| 2026-08-18 | External Reviewer / Peer Audit | [docs/05-requirement-backlog.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/05-requirement-backlog.md) | มีการจัดลำดับความสำคัญ MoSCoW พร้อมระบุ Rationale ชัดเจน | ตาราง Priority Summary ระบุ `Must \| 4` แต่แสดงรายการ 5 ข้อ (`FR-01`, `FR-02`, `BR-02`, `FR-05`, `NFR-01`) ขัดกับ assertion เรื่อง consistency 100% | แก้ไขตัวเลขจำนวน Must จาก `4` เป็น `5` ในสรุปตาราง Priority Summary ให้ถูกต้องตรงกัน |
| 2026-08-18 | External Reviewer / Peer Audit | `FR-01` ([docs/05-requirement-backlog.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/05-requirement-backlog.md)) | กำหนดเงื่อนไขเวลาตอบสนอง (3 วินาที) ได้ชัดเจนวัดผลได้ | `FR-01` ยังไม่ Atomic เนื่องจากรวม 2 Capabilities ไว้ในข้อเดียว (1. ตรวจ Availability, 2. ส่งคำขอจองพร้อมแสดงรหัส) | แยก `FR-01` เป็น 2 ข้อย่อย `FR-01A` (การตรวจสถานะว่าง) และ `FR-01B` (การส่งคำขอจอง) เพื่อความชัดเจนในการเขียน Test Case |
| 2026-08-18 | External Reviewer / Peer Audit | [cross-review.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/evidence/week-05/baseline-review/cross-review.md) | มีโครงสร้าง Checklist และ Action Taken ตรงตามข้อกำหนดของ Studio | ระบุ Reviewer เพียง "Peer Cross-Review Team / Internal Quality Auditor" ทำให้ Evidence Provenance ไม่ชัดเจน | ระบุชื่อทีมที่ตรวจข้ามทีม (Reviewer Team) หรือรายชื่อผู้ตรวจจริงให้ตรวจสอบย้อนกลับได้ |
| 2026-08-18 | External Reviewer / Peer Audit | [docs/08-validation-traceability.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/08-validation-traceability.md) | Traceability Matrix เชื่อมโยง Problem → Evidence → Need → Req ได้สมบูรณ์ และมี Open Questions | ยังขาดตาราง Readiness Gate Checklist 5 ข้อพร้อม Evidence Mapping ที่ผูกลิงก์หลักฐานชัดเจน | เพิ่มตาราง Readiness Gate Checklist (5 Criteria) พร้อมแนบไฟล์หลักฐาน/ commit ref ในเอกสาร |

---

## 2. รายละเอียดผลการตรวจตามเกณฑ์ Studio (6 Phases Review)

### 2.1 Artefact Health Check (ช่วงที่ 1)
- **สถานะ:** **ผ่าน (แบบมีข้อสังเกตเรื่อง Inconsistency)**
- **ข้อค้นพบ:** เอกสารหลักครบถ้วนตามโครงสร้าง repo (`docs/01` ถึง `docs/05` และ `evidence/week-05/baseline-review/artefact-health-check.md`)
- **จุดที่ต้องแก้:** ใน `artefact-health-check.md` อ้างว่า *"ซิงก์ MoSCoW ตรงกัน 100%"* แต่ใน [docs/05-requirement-backlog.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/05-requirement-backlog.md) สรุป `Must | 4` แต่นับรายการได้ 5 ข้อ (`FR-01, FR-02, BR-02, FR-05, NFR-01`)
- **แนวทางแก้ไข:** ปรับตัวเลขจำนวน Must ในตาราง Priority Summary ให้ตรงกับจำนวน Requirement จริง

### 2.2 Traceability Audit (ช่วงที่ 2)
- **สถานะ:** **ผ่าน**
- **ข้อค้นพบ:** มีการเดินสาย Traceability ครบถ้วน (`PP-01 → Student → E-01/E-02 → RC-01 → FR-01 → Must` เป็นต้น)
- **จุดแข็ง:** ไม่มีการลบ Requirement ที่ยังขัดแย้ง แต่บันทึกเป็น Open Questions (เช่น Auto-approve, No-show appeal, PDPA/Audit Log) ไว้อย่างเป็นระบบ

### 2.3 Quality & MoSCoW Check (ช่วงที่ 3)
- **สถานะ:** **ต้องแก้ไขเรื่อง Atomicity (`FR-01`)**
- **ข้อค้นพบ:**
  - `FR-01` รวม Capability สองเรื่อง: การแสดงสถานะว่าง/ไม่ว่างภายใน 3 วินาที และการส่งคำขอจองสำเร็จพร้อมแสดงรหัส
  - `FR-02` และ `BR-02` รวมหลายเงื่อนไข แต่ยังพอถือว่าเป็น Business Transaction / Business Rule เดียวกันได้
  - `FR-03 (Auto-cancel No-show)` ถูกปรับเป็น `Could / Hold` มีเหตุผลรองรับดี Scope ไม่บวม
- **แนวทางแก้ไข:** แยก `FR-01` ออกเป็น `FR-01A` และ `FR-01B` ดังนี้:
  - **FR-01A:** ระบบต้องแสดงสถานะว่าง/ไม่ว่างของห้องและอุปกรณ์ตามช่วงเวลาที่ผู้ใช้เลือกภายใน 3 วินาที
  - **FR-01B:** ระบบต้องให้ผู้ใช้ส่งคำขอจองพื้นที่หรืออุปกรณ์ และแสดงรหัสคำขอเมื่อบันทึกสำเร็จ

### 2.4 Peer Cross-Review Provenance (ช่วงที่ 4)
- **สถานะ:** **เนื้อหาผ่าน แต่ Evidence Provenance ยังอ่อน**
- **ข้อค้นพบ:** ใน [cross-review.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/evidence/week-05/baseline-review/cross-review.md) ระบุ Reviewer Vague
- **แนวทางแก้ไข:** ระบุ Reviewer Team / Reviewer Names (หรือ Internal Split Review Role A/B) ให้ชัดเจน

### 2.5 Baseline Lock & Commit Tag (ช่วงที่ 5)
- **สถานะ:** **ผ่าน**
- **ข้อค้นพบ:** ตรวจพบ Git Tag `baseline-v1.0` มี Decision Log และ Team Worklog ระบุบทบาทสมาชิกชัดเจน

### 2.6 Readiness Gate & Reflection (ช่วงที่ 6)
- **สถานะ:** **เกือบผ่าน (ต้องเพิ่ม Checklist ตาราง Gate)**
- **ข้อค้นพบ:** มี Individual Reflection ใน [15-individual-reflection.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/feedback/15-individual-reflection.md) ครบถ้วนแล้ว แต่ยังขาดตารางสรุป Readiness Gate Checklist 5 ข้อ

---

## 3. Readiness Gate Checklist (ตารางประเมินด่านความพร้อม)

| # | Gate Criterion | Status | Evidence Path / Reference |
|---|---|:---:|---|
| 1 | เอกสาร `docs/01–05` ครบและอัปเดตล่าสุด | **Pass** | [evidence/week-05/baseline-review/artefact-health-check.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/evidence/week-05/baseline-review/artefact-health-check.md) |
| 2 | ทุก Must requirement Traceable ถึง Evidence + Stakeholder | **Pass** | [docs/08-validation-traceability.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/08-validation-traceability.md) |
| 3 | FR/NFR ทุกข้อวัดผลได้ ไม่กำกวม และเป็น Atomic | **Pending Fix** | แยก `FR-01` เป็น `FR-01A/B` ใน [docs/05-requirement-backlog.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/docs/05-requirement-backlog.md) |
| 4 | ผ่าน Peer Cross-Review อย่างน้อย 1 รอบ | **Pass** | [evidence/week-05/baseline-review/cross-review.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/evidence/week-05/baseline-review/cross-review.md) |
| 5 | Commit + Tag `baseline-v1.0` และอัปเดต Worklog / Decision Log | **Pass** | [project-management/decision-log.md](file:///d:/Work/Code/RMUTL/ENGSE206-Group5-CASE1-Group_Space_And_Learning_Equipment_Booking/project-management/decision-log.md) & Git Tag `baseline-v1.0` |

---

## 4. รายการที่ต้องดำเนินการแก้ไขก่อนล็อก Baseline (Action Checklist)

1. [x] **สรุป Must Count:** แก้จำนวน `Must` ใน Priority Summary ของ `docs/05` จาก `4` เป็น `5`
2. [ ] **แยก Atomicity:** แยก `FR-01` เป็น `FR-01A` และ `FR-01B` ใน `docs/05` และอัปเดตอ้างอิงใน `docs/08`
3. [ ] **ระบุตัวตน Reviewer:** อัปเดตชื่อผู้ตรวจ/ทีมผู้ตรวจใน `cross-review.md`
4. [ ] **ฝัง Readiness Gate Table:** นำตาราง Readiness Gate Checklist ด้านบนไปใส่ใน `docs/08`
5. [ ] **ตรวจสอบ Consistency:** ตรวจคำว่า `100% Consistent` ไม่ให้ขัดกับข้อเท็จจริงในเอกสาร
6. [ ] **ยืนยัน Baseline Tag:** ตรวจสอบว่า Git Tag `baseline-v1.0` ชี้ไปยัง Commit ล่าสุดที่ทำการแก้ไขเรียบร้อยแล้ว

