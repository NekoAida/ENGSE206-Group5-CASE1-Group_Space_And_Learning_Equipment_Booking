# Decision Log

> ใช้สำหรับการตัดสินใจที่มีผลต่อ scope, requirement, architecture, UX/UI หรือ detailed design

| ID | Date | Decision | Options Considered | Rationale | Impacted Artefacts | Owner |
|---|---|---|---|---|---|---|
| **D-01** | 2026-08-18 | ล็อก Baseline v1.0 สำหรับชุดความต้องการ เพื่อเตรียมเข้าสู่การทำ Requirement Modeling ใน Week 06 | A: ปรับเพิ่ม requirement ใหม่<br>B: ล็อกชุดเดิมและปรับปรุงคุณภาพความชัดเจน (เลือก B) | เพื่อให้มีชุดความต้องการตั้งต้นที่นิ่ง ทดสอบได้ และมีสาย Traceability ครบถ้วนก่อนเริ่มออกแบบ | `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md` | วรสิทธิ์ บุญยปรีดี |
| **D-02** | 2026-08-18 | ปรับระดับ MoSCoW ให้สอดคล้องกันทุกไฟล์ (BR-01 เป็น Should, FR-05 เป็น Must, FR-03 เป็น Could) | A: คงตามร่างแรกที่ขัดแย้งกัน<br>B: ซิงก์ให้ตรงกันตามเกณฑ์ Value/Risk/Dependency (เลือก B) | ขจัดความขัดแย้งของข้อมูล โดยจัดลำดับตามความจำเป็นของ Core Workflow และความพร้อมของ Policy | `docs/05-requirement-backlog.md`, `docs/05-prioritization-rationale.md` | ปริษฎา สุทธดุก |
| **D-03** | 2026-08-11 | แยก Workflow การอนุมัติการจอง: การจองห้องต้องรอเจ้าหน้าที่อนุมัติ (Manual) ส่วนอุปกรณ์ทั่วไปให้อนุมัติอัตโนมัติ (Auto-approve) | A: รออนุมัติทุกรายการ<br>B: Auto-approve ทั้งหมด<br>C: แยกตามประเภททรัพยากร (เลือก C) | ช่วยลดภาระงานค้างของเจ้าหน้าที่ในส่วนอุปกรณ์ และยังคงการคัดกรองการใช้พื้นที่ห้องเพื่อความเหมาะสม | `docs/04-evidence-log.md`, `docs/05-requirement-backlog.md` | วรสิทธิ์ บุญยปรีดี |
| **D-04** | 2026-08-18 | จัดลำดับฟังก์ชัน Auto-cancel No-show 15 นาที (FR-03) ให้อยู่ในกลุ่ม Could (Hold) ชั่วคราว | A: บังคับเป็น Must ทันที<br>B: เก็บเป็น Could/Hold รอ Policy ชัดเจน (เลือก B) | ป้องกันการสร้างกฎตัดสิทธิ์/บทลงโทษจากสมมติฐานของทีมเอง ต้องรอระเบียบที่แน่ชัดจากผู้จัดการพื้นที่ | `docs/05-requirement-backlog.md`, `docs/05-open-questions-and-issues.md` | ปริษฎา สุทธดุก |
