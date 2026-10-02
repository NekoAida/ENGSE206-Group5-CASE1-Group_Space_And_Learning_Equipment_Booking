# Architecture Diagrams

Week 11 — Conceptual Architecture (C4):

- `context-diagram.drawio` / `context-diagram.png` — System Context (C4 Level 1): ระบบเดียว + Actor 4 บทบาท (SRS §2.2) + External 2 ระบบ (EXT-01 Core ตาม AS-01, EXT-02 TBD รอ OI-02)
- `container-diagram.drawio` / `container-diagram.png` — Container (C4 Level 2): Web Application [React] · API Application [Node.js + Express] · Database [PostgreSQL] · Scheduled Job — No-show Sweeper [cron] ภายใต้ trust boundary ฝั่งเซิร์ฟเวอร์

อ้างอิง: `design/11-conceptual-architecture.md`, `design/11-conceptual-architecture-v0.1.docx`, `design/00-design-spine.md`

## Checklist

- [x] มี source file ที่แก้ไขได้ (`.drawio`)
- [x] มี PNG/PDF export สำหรับใช้ในเอกสาร (`.png`)
- [x] ชื่อไฟล์สื่อถึง purpose
- [x] เชื่อมโยงกับ requirement/design document
