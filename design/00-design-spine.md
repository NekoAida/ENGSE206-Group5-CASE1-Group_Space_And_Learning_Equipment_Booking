# 00 — Design Spine (เส้นโครงหลักของระบบ)

> **สถานะการจัดทำ:** ไฟล์นี้ควรสร้างตั้งแต่ Week 10 แต่ `design/10-design-strategy.md` ของทีมยังเป็นเทมเพลต ทีมจึงถอด Scope / Design Drivers / Spine จาก **SRS v1 (docs/07-srs-v1.md — Baseline Candidate, ไม่ใช่ Approved)** โดยตรงใน Week 11 ตามกติกา Lab (ห้ามเดาค่า — ทุกขั้นอ้าง ID ของ SRS)
> คอลัมน์ W12–W13 เว้นว่างไว้ตามคำสั่ง Lab (ห้ามเติมล่วงหน้า)

## 1. Scope ที่รับมา (จาก SRS §1.3, §3)

- **Build now:** ค้นหา/จอง (FR-01), อนุมัติ/ปฏิเสธ (FR-02), Check-in/No-show (FR-03), แจ้งเตือน (FR-04), รับ-คืนอุปกรณ์ (FR-05)
- **Overview:** Dashboard สถิติ (FR-06 — รอ OI-03)
- **นอกขอบเขต:** ระบบชำระเงิน, IoT/กลอนอัจฉริยะ (CT-02), ระบบแนะนำ AI (Future Scope มติ W06)

## 2. Design Drivers (Proposed — ถอดจาก SRS ใน W11)

| ID | Driver | ที่มา |
|---|---|---|
| **D1** | ห้าม Double Booking — ไม่มีรายการ Confirmed ซ้ำในห้อง/ช่วงเวลาเดียวกัน แม้ผู้ใช้กดพร้อมกัน | FR-01, BR-01, NFR-03, AC-02 |
| **D2** | กฎ สิทธิ์ และ Audit บังคับฝั่งเซิร์ฟเวอร์เท่านั้น | FR-02, BR-02–BR-04, NFR-01, NFR-02, CT-03 |
| **D3** | ใช้งานได้จริงทุกอุปกรณ์ (Responsive ≥375px) และตอบสนอง ≤ 3 วินาที | CT-01, NFR-04, NFR-05 |

## 3. Spine — เดินแต่ละขั้นผ่าน Container Diagram (คอลัมน์ W11)

| # | ขั้นตอน | UC | FR / AC | ระดับ | เส้นทางผ่าน Container (W11) |
|---|---|---|---|---|---|
| 1 | ค้นหาสถานะว่างของห้อง/อุปกรณ์ตามวัน-เวลา-จำนวนคน | UC-01 | FR-01, AC-01 | Build now | Web → API (นับ Confirmed + block) → DB |
| 2 | สร้างคำขอจองห้องพร้อมอุปกรณ์เสริม → ได้ Booking ID + QR | UC-01 | FR-01, AC-02, BR-01, BR-02 | Build now | Web → API (ตรวจ BR + recheck + ออก ID/QR) → DB |
| 3 | เจ้าหน้าที่อนุมัติ/ปฏิเสธ (ปฏิเสธต้องระบุเหตุผล) | UC-03 | FR-02, AC-06 | Build now | Web (Staff) → API (recheck + เปลี่ยนสถานะ + AuditLog ใน transaction เดียว) → DB |
| 4 | Check-in ด้วย QR / ตัดสิทธิ์ No-show อัตโนมัติหลัง 15 นาที | UC-02 | FR-03, AC-04, BR-02 | Build now | Web (สแกน) → API (ตรวจเวลา) → DB · **Scheduled Job → API** (ตัด No_Show เป็นรอบ — ความถี่ DD-03) |
| 5 | แจ้งเตือนสถานะคำขอ (อนุมัติ/ปฏิเสธ/ยกเลิก) | UC-03 | FR-04 | Build now | API → Web Notification (in-app) · API → EXT-02 Email (สเปก TBD = OI-02) |
| 6 | บันทึกการรับ-คืนอุปกรณ์ พร้อมสภาพอุปกรณ์ | UC-03 | FR-05, AC-05, BR-03 | Build now | Web (Staff) → API (บันทึกสภาพ + AuditLog) → DB |
| 7 | Dashboard สถิติการใช้งาน + Export | UC-05 | FR-06, AC-08 | Overview (รอ OI-03) | Web → API (aggregate) → DB |
| — | **Cross-cutting:** ตรวจสิทธิ์ RBAC ทุก action + เขียน AuditLog Append-Only | ทุก UC | NFR-01, NFR-02, FR-12 | Build now | ตรวจที่ API ทุกขั้นตอน · เขียนลง DB |

**ผลการเดิน Spine:** ทุกขั้นเดินผ่าน Web → API → Database ได้ครบ; กฎสำคัญ (D1 กันซ้ำ, BR-01–BR-04, RBAC, Audit) ถูกบังคับฝั่งเซิร์ฟเวอร์ทั้งหมดตาม D2 — ความซับซ้อนอยู่ใน API (zoom เป็น component ใน W13)

## 4. คอลัมน์สำหรับภายหลัง (ยังไม่เติม)

| # | ขั้นตอน | W12 (UX/UI — หน้าจอ + API ที่เรียก) | W13 (Detailed Design — component/sequence) |
|---|---|---|---|
| 1–7 | (ตามตารางข้างบน) | ห้ามเติมล่วงหน้า | ห้ามเติมล่วงหน้า |
