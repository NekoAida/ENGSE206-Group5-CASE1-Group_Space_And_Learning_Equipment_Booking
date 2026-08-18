# ใบตรวจ Cross-Review (Peer Review Form)

> **กิจกรรม:** Requirement Baseline Review & Readiness Gate (Week 05)  
> **ทีมผู้ถูกตรวจ:** Group 5 — Group Space And Learning Equipment Booking System  
> **วันที่:** 2026-08-18  
> **ผู้ตรวจทาน:** Peer Cross-Review Team / Internal Quality Auditor

---

## 1. ผลการตรวจทานตาม Checklist (Cross-Review Checklist)

| สิ่งที่ตรวจ | ผลการตรวจ | ข้อสังเกต / ข้อเสนอแนะ (อ้าง ID) | การดำเนินการแก้ไขของทีม (Action Taken) |
|---|:---:|---|---|
| **1. ทุก Must มีสาย traceable ครบ**<br>(Problem → Evidence → Need → FR/NFR → Priority) | ✅ ผ่าน | ตรวจสอบสายครบทั้ง 5 รายการ (FR-01, FR-02, BR-02, FR-05, NFR-01) สามารถลากสายกลับไปถึง Problem Brief (PP-01, PP-03, F-01, F-03) และ Evidence (E-01..E-09) ได้ครบ 100% | จัดทำตาราง Traceability Matrix ฉบับเต็มลงใน `docs/08-validation-traceability.md` เรียบร้อยแล้ว |
| **2. FR/NFR วัด/ทดสอบได้ และไม่กำกวม** | ✅ ผ่าน | ข้อความเดิมของ FR-01 และ FR-02 มีคำว่า "Real-time" และไม่ได้ระบุความเร็วของการตอบสนอง ทำให้ตรวจรับยาก | ปรับปรุงถ้อยคำโดยเพิ่มเกณฑ์เวลาเชิงตัวเลข เช่น "แสดงผลภายใน 3 วินาที" และ "ส่งแจ้งเตือนภายใน 5 วินาที" ลงใน `docs/05` |
| **3. ไม่มี requirement ซ้ำ / ขัดกันเอง** | ✅ ผ่าน | พบความขัดแย้งเดิมระหว่าง Backlog และ Prioritization Rationale เรื่องระดับ MoSCoW ของ BR-01, FR-05, FR-03 | ซิงก์รหัส Req ID และปรับ MoSCoW ให้ตรงกันทุกไฟล์ (BR-01 = Should, FR-05 = Must, FR-03 = Could) |
| **4. Scope ตรงกับ Case Card ไม่บวมเกิน** | ✅ ผ่าน | ขอบเขตฟังก์ชันครอบคลุมการจองห้องและยืมอุปกรณ์ ไม่พบการเพิ่มระบบชำระเงินออนไลน์หรืออุปกรณ์ IoT ที่อยู่นอก Scope | ยืนยันขอบเขต In Scope / Out of Scope ตาม `CASE_CARD.md` และ `docs/02` |
| **5. MoSCoW มีเหตุผลรองรับ** | ✅ ผ่าน | ทุก Requirement มีการแจกแจงตามมิติ Value, Risk, Urgency และ Dependency ชัดเจน | บันทึกรายละเอียดใน `docs/05-prioritization-rationale.md` และ `project-management/decision-log.md` |

---

## 2. สรุปความเห็นและข้อเสนอแนะจากผู้ตรวจทาน

1. **จุดเด่น:** สาย Traceability มีความชัดเจน มีการแยกกระบวนการอนุมัติระหว่างห้อง (Manual Approve) และอุปกรณ์ทั่วไป (Auto-approve) อย่างสมเหตุสมผลเพื่อลดภาระงานของเจ้าหน้าที่
2. **คำแนะนำสำหรับการต่อยอดใน Week 06:** ควรเตรียม Acceptance Criteria ของ Business Rules (BR-02) ในกรณีผู้ใช้งานพยายามจองห้องซ้อนทับเวลาเดิม เพื่อใช้เป็น Test Scenarios ในขั้นตอนถัดไป

**ผลการตรวจสรุป:** ✅ **ผ่านการตรวจทาน (Passed)**
