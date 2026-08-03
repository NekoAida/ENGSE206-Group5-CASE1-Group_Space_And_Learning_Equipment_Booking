# Week 04 — Evidence Log

> **Team:** Group 5 — Group Space And Learning Equipment Booking System  
> **Case:** Case No. 1 — เว็บไซต์จองพื้นที่ทำงานกลุ่มและอุปกรณ์การเรียนรู้  
> **Assignment:** `W04-v2.0`  
> **Version:** v1.0 — Completed Evidence Log  
> **Inputs:** Week 03 Elicitation Plan and revised Interview Guide

---

## 1. Evidence policy

บันทึกนี้แยก **สิ่งที่แหล่งข้อมูลกล่าว/ระบุ (Statement / Observed Event)** ออกจาก **การตีความของทีม (Interpretation)** คำตอบจาก AI stakeholder panel หรือการสัมภาษณ์จำลองเป็นข้อมูลจำลอง (`SN`) ไม่ใช่นโยบายจริง และทุกข้อที่ไม่มี source/authority ชัดเจนต้องคงสถานะ provisional หรือ unresolved

---

## 2. Source and session register

| Session | Source/role | Objectives | Control used | Limitation |
|---|---|---|---|---|
| **S-00** | Case Card / Problem Brief | ใช้เป็นข้อมูลตั้งต้น (CF) และขอบเขตของระบบเว็บไซต์ | อ้างอิง Problem Brief (`01-problem-brief-v0.1.md`) | ให้ข้อมูลเฉพาะบริบทเบื้องต้น |
| **S-01** | นักศึกษา / ผู้ใช้งานระบบ | EO-01, EO-02, EO-03 | Interview Guide, Scenario-based questions | เป็นข้อมูลจำลอง ไม่มี authority ด้านนโยบายสถาบัน |
| **S-02** | เจ้าหน้าที่ผู้ดูแลห้อง / เจ้าหน้าที่อุปกรณ์ | EO-01, EO-03, EO-04 | Workflow walkthrough, Interview Guide | สะท้อนกระบวนการทำงานจำลองหน้าเคาน์เตอร์ |
| **S-03** | ผู้จัดการพื้นที่ / ผู้ดูแลนโยบาย | EO-02, EO-03 | Document Analysis, Policy questions | ข้อกำหนดต้องยืนยันกับเอกสารระเบียบคณะจริง |
| **S-04** | ผู้ดูแลระบบ IT (SysAdmin) | EO-04 | Security and System Constraint check | ไม่สามารถกำหนด Business Policy ของพื้นที่ได้ |

---

## 3. Tagging and confidence rules

| Tag | Use | Confidence rule |
|---|---|---|
| `CF` | ข้อเท็จจริงจาก Case Card หรือเอกสารที่ได้รับอนุมัติ | **High** เมื่ออ้างอิงแหล่งข้อมูลได้ชัดเจน |
| `CT` | ข้อกำหนดหรือข้อจำกัดที่มีแหล่งอ้างอิงหรือผู้มีอำนาจยืนยัน | **High–Medium** ตามความน่าเชื่อถือของแหล่งข้อมูล |
| `SN` | ข้อมูลหรือความต้องการจากการจำลอง Stakeholder | **Medium** ต้องยืนยันกับผู้ใช้งานหรือเอกสารจริง |
| `OP` | ความคิดเห็นหรือความชอบของ Stakeholder | ไม่ใช้เป็น Requirement โดยตรง |
| `AS` | สมมติฐานของทีม | ต้องมีแผนตรวจสอบหรือผู้รับผิดชอบ |
| `PS` | แนวทางแก้ไขหรือข้อเสนอที่ Stakeholder เสนอ | ต้องหาความต้องการที่แท้จริง (Underlying Need) ก่อนสร้าง Requirement |
| `OQ` | ประเด็นที่ยังไม่มีคำตอบหรือข้อมูลยืนยัน | ห้ามสรุปหรือสร้างข้อมูลขึ้นเอง ต้องติดตามตรวจสอบเพิ่มเติม |

---

## 4. Evidence table

| E-ID | Source/role/session | Tag | Statement / observed | Context | Confidence + reason | Related/conflicting E-ID | Follow-up/owner |
|---|---|---|---|---|---|---|---|
| **E-01** | S-00 Case Description | CF | ผู้ใช้ปัจจุบันต้องเดินมาถามหน้าเคาน์เตอร์หรือส่งแชตถาม ทำให้ไม่ทราบตารางเวลาว่างจริง | Current Process | High (Case Card) | E-02 | ใช้เป็นข้อมูลตั้งต้นโครงงาน |
| **E-02** | S-01 นักศึกษา | SN | นักศึกษาต้องการค้นหา ตรวจสอบตารางเวลาว่าง และส่งคำขอจองพื้นที่/อุปกรณ์ผ่านหน้าเว็บได้ตลอด 24 ชม. | Search & Booking | Medium (Simulation) | E-01, E-03 | ยืนยัน UI ตารางเวลาบนหน้าเว็บ (วรสิทธิ์) |
| **E-03** | S-02 เจ้าหน้าที่ดูแลห้อง | SN | การจองพื้นที่ (Space) ต้องผ่านการกดอนุมัติจากเจ้าหน้าที่ก่อนเสมอ เพื่อคัดกรองความเหมาะสม | Space Approval | Medium (Simulation) | E-02, E-04 | ยืนยัน Workflow การอนุมัติ (ปริษฎา) |
| **E-04** | S-02 เจ้าหน้าที่ดูแลห้อง | SN | การยืมอุปกรณ์การเรียนรู้เกิดขึ้นบ่อย หากต้องกดอนุมัติทีละรายการจะเกิดงานค้างสะสม | Equipment Booking | Medium (Simulation) | E-03 | ยืนยันสิทธิ์ Auto-approve (วรสิทธิ์) |
| **E-05** | S-03 ผู้จัดการพื้นที่ | CT | ระเบียบคณะกำหนดให้นักศึกษาใช้งานห้องเรียนกลุ่มได้ไม่เกิน 3 ชม./วัน และจองล่วงหน้าได้ไม่เกิน 7 วัน | Resource Constraint | High (Policy Doc) | E-02 | กำหนด Validation Rule บนเว็บ (วรสิทธิ์) |
| **E-06** | S-02 เจ้าหน้าที่ดูแลห้อง | SN | ถ้านักศึกษาไม่มาเช็กอินภายใน 15 นาที ระบบควรกดยกเลิกสิทธิ์อัตโนมัติเพื่อเปิดโอกาสให้คนอื่น | No-show Policy | Medium (Simulation) | E-07 | ยืนยันระบบ Auto-cancellation (ปริษฎา) |
| **E-07** | S-01 นักศึกษา | SN | ผู้จองต้องการรับแจ้งเตือนสถานะการจอง (อนุมัติ/ปฏิเสธ) ผ่านทางอีเมลสถาบันและบนหน้าเว็บ | Notification | Medium (Simulation) | E-06 | ยืนยันรูปแบบการแจ้งเตือน (ปริษฎา) |
| **E-08** | S-02 เจ้าหน้าที่ดูแลห้อง | SN | เจ้าหน้าที่ต้องบันทึกรหัสครุภัณฑ์ (Asset ID) และสภาพอุปกรณ์ลงบนหน้าเว็บเมื่อมีการรับ-คืน | Inventory Tracking | Medium (Simulation) | E-04 | ออกแบบฟอร์มบันทึกรับ-คืน (ปริษฎา) |
| **E-09** | S-04 ผู้ดูแลระบบ IT | SN | ระบบต้องบันทึก Audit Log ประวัติการจอง การอนุมัติ และการยกเลิกทั้งหมดเพื่อใช้ตรวจสอบย้อนหลัง | Audit & Security | Medium (Simulation) | E-08 | ยืนยันตาราง Audit Log (วรสิทธิ์) |
| **E-10** | S-03 ผู้จัดการพื้นที่ | SN | ผู้บริหารและผู้จัดการต้องการดูสถิติอัตราการใช้ห้อง อุปกรณ์ยอดฮิต และรายงาน No-show บน Dashboard | Reporting & Dashboard | Medium (Simulation) | E-05, E-06 | ออกแบบหน้ารายงาน Dashboard (วรสิทธิ์) |

---

## 5. Triangulation and conflicts

| Topic | Supporting/contradicting E-IDs | Finding | Action |
|---|---|---|---|
| **การค้นหาและจองผ่านหน้าเว็บไซต์** | E-01, E-02 | ผู้ใช้ต้องการระบบจองออนไลน์ที่แสดงตารางเวลาว่างแบบ Real-time | สร้าง **RC-01** |
| **กระบวนการอนุมัติการจอง** | E-03, E-04 | การจองห้องต้องกดอนุมัติ (Manual) แต่การจองอุปกรณ์ควรอนุมัติอัตโนมัติ (Auto) | เปิดประเด็น **C-01** และสร้าง **RC-02, RC-03** |
| **ข้อจำกัดการใช้งานตามนโยบาย** | E-02, E-05 | ต้องคุมโควตาจองล่วงหน้าไม่เกิน 7 วัน และใช้ห้องไม่เกิน 3 ชม./วัน | สร้าง **RC-04** |
| **การจัดการ No-show และตัดสิทธิ์** | E-06, E-07 | ต้องการระบบตัดสิทธิ์อัตโนมัติใน 15 นาที พร้อมแจ้งเตือนผ่าน Email/Web | เปิดประเด็น **C-02, C-03** และสร้าง **RC-05, RC-06** |
| **การบันทึกยืม-คืนอุปกรณ์หน้าเคาน์เตอร์** | E-04, E-08 | เจ้าหน้าที่ต้องบันทึก Asset ID และสภาพอุปกรณ์ผ่านหน้าเว็บ | สร้าง **RC-07** |
| **การบันทึกประวัติและสรุปรายงาน** | E-09, E-10 | ต้องมี Audit Log ตรวจสอบย้อนหลัง และหน้า Dashboard สรุปสถิติสำหรับผู้บริหาร | สร้าง **RC-08, RC-09** |

---

## 6. Evidence quality check

- [x] ทุก Evidence มี E-ID และระบุ Session/Source ชัดเจน
- [x] แยก Statement ออกจาก Team Interpretation บนเอกสารอื่น ๆ
- [x] Simulation ถูกระบุแท็กเป็น `SN` อย่างถูกต้อง
- [x] ทุก Requirement Candidate อ้างอิง E-ID ย้อนกลับได้
- [x] ทุก Conflict/Issue เชื่อมโยงกับ Evidence Log
- [x] ไม่มีการอ้างว่าเป็นนโยบายจริงโดยไม่มีหลักฐานอ้างอิง

---

## 7. Handoff

- ใช้ **E-01, E-02** → สร้าง Candidate Requirement **RC-01** (ระบบค้นหาและตารางเวลาว่าง)
- ใช้ **E-03** → สร้าง Candidate Requirement **RC-02** (ระบบอนุมัติห้องทำงานกลุ่มโดยเจ้าหน้าที่)
- ใช้ **E-04** → สร้าง Candidate Requirement **RC-03** (ระบบอนุมัติอุปกรณ์อัตโนมัติ)
- ใช้ **E-05** → สร้าง Candidate Requirement **RC-04** (Validation Rule คุมเวลาจอง)
- ใช้ **E-06** → เปิดประเด็น **C-02** และสร้าง Candidate Requirement **RC-05** (Auto-cancellation 15 นาที)
- ใช้ **E-07** → เปิดประเด็น **C-04** และสร้าง Candidate Requirement **RC-06** (Web & Email Notification)
- ใช้ **E-08** → สร้าง Candidate Requirement **RC-07** (ฟอร์มบันทึก Asset ID ยืม-คืน)
- ใช้ **E-09, E-10** → สร้าง Candidate Requirement **RC-08, RC-09** (Audit Log และ Dashboard)
- Candidate ทั้งหมดอ้างอิง E-ID ตาม[Requirement Candidates](04-requirement-candidates.md)