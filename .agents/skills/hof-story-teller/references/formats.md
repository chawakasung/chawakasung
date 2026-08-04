# Formats

Four outputs. Each is the same five-beat spine (object → work → making → living → ask)
compressed to a different budget. Placeholders are written `«…»`; unknown facts are written
`[CONFIRM: …]` and left in the draft.

---

## 1. `LISTING.txt` — FB Marketplace

Lives at `fb-marketplace/<SKU>/LISTING.txt`. Its absence is what `rebuild.py` flags.

Header lines are for the person pasting into Marketplace fields; everything after `---` is
the description body. Budget: **120–200 Thai words**.

```
TITLE: «ชื่อภาพ» «ศิลปิน» — ภาพพิมพ์ใส่กรอบ «ขนาด»
PRICE: «ราคา» บาท
CATEGORY: Home Goods / Home Decor
CONDITION: New
SKU: «SKU»
---
«เปิดด้วยตัวชิ้นงาน — สิ่งที่ลูกค้าจะได้จริง ๆ 1–2 ประโยค»

«ภาพนี้คืออะไร ไม่เกิน 2 ประโยค — เฉพาะที่ทำให้มองภาพเปลี่ยนไป»

รายละเอียด
• ภาพ: «ชื่อภาพ» — «ศิลปิน», «ปี»
• งานพิมพ์: [CONFIRM: กระดาษ/หมึก]
• กรอบ: [CONFIRM: วัสดุ สี ขนาดขอบ]
• ขนาดรวมกรอบ: «กว้าง × สูง» ซม.
• พร้อมแขวน มีอุปกรณ์แขวนให้

«ประโยคปิด — ภาพนี้ไปอยู่ตรงไหนของบ้าน»

ราคา «ราคา» บาท
[CONFIRM: จัดส่ง/นัดรับ] · ทักแชทได้เลย
```

### Worked example

Art-historical content is real; every specification is a placeholder, which is exactly how a
first draft should look before the specs are confirmed.

```
TITLE: The Starry Night — Vincent van Gogh — ภาพพิมพ์ใส่กรอบ «ขนาด»
PRICE: «ราคา» บาท
CATEGORY: Home Goods / Home Decor
CONDITION: New
SKU: «SKU»
---
ภาพพิมพ์คุณภาพสูง ใส่กรอบเรียบร้อย พร้อมแขวนออกจากกล่องได้เลย
ไม่ต้องหาร้านกรอบเพิ่ม

แวนโก๊ะวาดภาพนี้ในปี 1889 ตอนอยู่ในสถานพยาบาลที่แซ็ง-เรมี
เป็นวิวจากหน้าต่างห้องตัวเอง ที่เขาวาดซ้ำอยู่หลายครั้ง

รายละเอียด
• ภาพ: The Starry Night — Vincent van Gogh, 1889
• งานพิมพ์: [CONFIRM: กระดาษ/หมึก]
• กรอบ: [CONFIRM: วัสดุ สี ขนาดขอบ]
• ขนาดรวมกรอบ: «กว้าง × สูง» ซม.
• พร้อมแขวน มีอุปกรณ์แขวนให้

สีน้ำเงินของภาพคุมโทนห้องได้ทั้งห้อง เหมาะกับผนังหัวเตียง
หรือมุมโต๊ะทำงานที่ยังว่างอยู่

ราคา «ราคา» บาท
[CONFIRM: จัดส่ง/นัดรับ] · ทักแชทได้เลย
```

---

## 2. Social caption — IG / FB

The image carries beats 1 and 4, so the caption spends itself on 2 and 3. Budget:
**50–90 Thai words**, then hashtags on their own lines.

```
«ประโยคเปิดที่หยุดนิ้วได้ — เริ่มจากภาพหรือจากผนัง ไม่ใช่จากชื่อศิลปิน»

«เรื่องของภาพ 1–2 ประโยค»

«กรอบ/งานพิมพ์ 1 ประโยค — สิ่งที่เห็นได้จากรูป detail»

«ปิดด้วยคำชวนคุย หรือชวนดูขนาดอื่น»

#HallOfFrame #«ศิลปิน» #ภาพติดผนัง #ของแต่งบ้าน #กรอบรูป
```

Rules: no wall of hashtags in the first line, no emoji chain, one call to action.

---

## 3. Gallery blurb — website

Sits under the piece on the site, where the buyer is already browsing and does not need the
ask. Beats 2 and 3 only. Budget: **40–60 Thai words**, no bullet list, no price.

```
«ภาพนี้คืออะไร และทำไมถึงยังถูกพูดถึง — 2 ประโยค»
«กรอบและงานพิมพ์ทำให้มันกลายเป็นของในบ้านยังไง — 1 ประโยค»
```

---

## 4. Brand story — About

Answers "who is Hall of Frame and why should I trust the framing?". Written once, revised
rarely. Budget: **150–250 Thai words**.

Structure — a Before → After → Bridge:

1. **Before:** you find a painting you love, and then the framing is the hard part —
   cost, wait, guessing at proportions.
2. **After:** it arrives framed, matched, ready to hang.
3. **Bridge:** how that is done — the collections, how frames are chosen for each image,
   what is printed on, what it costs.

State plainly in the About text that these are reproductions. Doing it here means individual
listings do not have to carry the whole disclosure, and it is the single highest-trust
sentence on the site.

---

## Checklist before handing over

- [ ] The painting and painter are named.
- [ ] Nothing implies an original, an authorised edition, or a numbered run.
- [ ] Every specification is either confirmed or marked `[CONFIRM: …]` — none invented.
- [ ] Nothing is claimed that the four images do not show.
- [ ] Art history is two sentences or fewer, and accurate.
- [ ] No scarcity or urgency claim that is not true.
- [ ] Within the length budget for its format.
- [ ] The buyer's question at every beat is answered, in image order.
- [ ] Read aloud once: no sentence exists only to sound expensive.
- [ ] `LISTING.txt` written to `fb-marketplace/<SKU>/`, so `rebuild.py` stops flagging it.
