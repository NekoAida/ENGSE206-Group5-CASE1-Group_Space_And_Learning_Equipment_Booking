# 03 — Elicitation Plan

> Week 03 | Team: Group 5 | Case: 01 — Group Space And Learning Equipment Booking System

## 1. Inputs from Week 02

- Problem Brief: [`01-problem-brief-v0.1.md`](01-problem-brief-v0.1.md)
- Stakeholder/Context/Scope: [`02-stakeholder-context-scope.md`](02-stakeholder-context-scope.md)

| OQ ID | Open Question | Impact if unresolved | Candidate source |
|---|---|---|---|
| OQ-01 | การแสดงผลตารางเวลาบนหน้าเว็บไซต์ ควรล็อกไม่ให้จองล่วงหน้าเกินกี่วัน และจำกัดจำนวนชั่วโมงต่อครั้งหรือไม่? | หากไม่มีการจำกัด อาจเกิดการจองผูกขาดข้ามสัปดาห์ ทำให้ผู้ใช้คนอื่นเสียโอกาสในการเข้าถึงทรัพยากรที่จำกัด | เจ้าหน้าที่ดูแล (Staff / Admin), นักศึกษา |
| OQ-02 | หากนักศึกษาจองผ่านเว็บไซต์แล้วไม่มาเช็กอินภายในเวลาที่กำหนด (No-show) ควรให้ระบบยกเลิกการจองอัตโนมัติในกี่นาที? | พื้นที่และอุปกรณ์จะถูกจองค้างไว้โดยไม่ได้ใช้งานจริง ทำให้สูญเสียประโยชน์และเสียโอกาสกลุ่มอื่น | เจ้าหน้าที่ดูแล (Staff / Admin) |

## 2. Elicitation Objectives

| EO ID | Objective: what must be learned | Related OQ | Decision/use | Expected evidence / exit criterion |
|---|---|---|---|---|
| EO-01 | ค้นหาข้อกำหนดเรื่องระยะเวลาการจองล่วงหน้า และระยะเวลาสูงสุดที่เหมาะสมต่อการใช้งานหนึ่งครั้ง | OQ-01 | เพื่อนำไปตั้งค่า Business Rules ในระบบสำหรับจำกัดระยะเวลาการจองและป้องกันการผูกขาด | บันทึกการสัมภาษณ์จากเจ้าหน้าที่ดูแล |
| EO-02 | กำหนดเงื่อนไขเวลาที่เหมาะสมในการยกเลิกการจองอัตโนมัติ (Auto-cancel) เมื่อผู้จองไม่มาแสดงตัว (No-show) | OQ-02 | เพื่อใช้ในการออกแบบระบบตัดสิทธิ์อัตโนมัติ และระบบบันทึกความประพฤติแทนการปรับเงิน | บันทึกการสัมภาษณ์และข้อตกลงจากเจ้าหน้าที่ดูแล |

## 3. Plan

| EO | Stakeholder/source | Technique + rationale | Evidence to record | Owner/time | Risk/mitigation | Exit criterion |
|---|---|---|---|---|---|---|
| EO-01 | เจ้าหน้าที่ดูแล (Staff / Admin) | Interview: เพื่อสอบถามข้อจำกัดจากประสบการณ์การทำงานจริง และความเหมาะสมในการจัดสรรทรัพยากร | บันทึกเสียงและบันทึกการสัมภาษณ์ | วรสิทธิ์ บุญยปรีดี / Week 03 | เจ้าหน้าที่ไม่มีเวลาให้สัมภาษณ์นาน / เตรียมคำถามให้กระชับและตรงประเด็น | ได้ข้อสรุปจำนวนวัน/ชั่วโมงที่ชัดเจน |
| EO-02 | เจ้าหน้าที่ดูแล (Staff / Admin) | Interview: เพื่อให้เข้าใจกระบวนการจัดการกับปัญหา No-show ในปัจจุบันและข้อจำกัดของเจ้าหน้าที่ | บันทึกเสียงและบันทึกการสัมภาษณ์ | ปริษฎา สุทธดุก / Week 03 | เจ้าหน้าที่อาจไม่มีนโยบายที่ชัดเจน / เสนอแนวทางเวลา (เช่น 15 นาที) เพื่อให้พิจารณา | ได้ตัวเลขนาทีสำหรับ Auto-cancel และบทลงโทษ |

## 4. Privacy and Responsible AI

- Data that must not be collected: ข้อมูลส่วนตัวที่ไม่เกี่ยวข้องกับระบบ (เช่น รหัสผ่านส่วนตัว, ข้อมูลทางการเงิน), ข้อมูลที่ระบุตัวตนของผู้ให้สัมภาษณ์หากไม่ได้รับอนุญาต
- Consent/opening statement: สวัสดีครับ พวกเราเป็นนักศึกษาจากรายวิชา ENGSE206 กำลังรวบรวมข้อมูลเพื่อพัฒนาระบบจองพื้นที่ทำงานกลุ่ม... ข้อมูลทั้งหมดจะถูกนำไปใช้เพื่อการเรียนรู้และออกแบบระบบเท่านั้น จะไม่มีการเปิดเผยข้อมูลส่วนบุคคลหรือข้อมูลที่เป็นความลับ
- How roles will be anonymized: แทนชื่อผู้ให้สัมภาษณ์ด้วย Role เช่น "เจ้าหน้าที่คนที่ 1"
- AI use permitted: การใช้ AI ในการถอดความเสียงสัมภาษณ์ สรุปประเด็น และจำลองการสัมภาษณ์ (Rehearsal)
- Human verification plan: สมาชิกในทีมจะตรวจสอบความถูกต้องของการถอดความและสรุปประเด็นจาก AI เทียบกับบันทึกเสียงและจดบันทึกการสัมภาษณ์ด้วยตนเอง

## 5. Team Roles

| Member | Workshop role | Responsibility/evidence |
|---|---|---|
| วรสิทธิ์ บุญยปรีดี | Presenter / Facilitator / Interviewer | ดำเนินการสัมภาษณ์และตั้งคำถาม |
| ปริษฎา สุทธดุก | Note taker / Evidence checker / Timekeeper | บันทึกผล จับเวลา และตรวจสอบความถูกต้องของข้อมูล |

## 6. Definition of Done

- [x] 3–5 high-impact OQs
- [x] EO–OQ–evidence–decision linkage
- [x] appropriate technique and stakeholder rationale
- [x] owner/time/risk/exit criteria
- [x] privacy/AI plan and team roles
