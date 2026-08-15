# 🌴 مولد عذق التمر — Date Palm Bunch Generator

إضافة بلندر تولّد عذوق تمر واقعية بضغطة زر: شماريخ من كيرفات قابلة للتحريك، حبات تمر بتجاعيد ديسبلاسمنت حقيقية، 23 صنف تمر سعودي، وحارس تصادم يمنع تداخل الحبات مهما غيّرت الإعدادات.

A Blender addon that generates realistic date palm bunches in one click — animatable curve strands, displacement-wrinkled fruits, 23 Saudi date varieties, and a built-in collision guard so fruits never intersect.

> يتطلب بلندر 4.2 أو أحدث — Requires Blender 4.2+

---

## 🟢 دليل المبتدئ: التثبيت خطوة بخطوة

### الطريقة 1 — تثبيت الإضافة (الأسهل والأفضل)

1. حمّل ملف **`date_palm_bunch.zip`** من هذا المستودع (زر Code الأخضر ثم Download ZIP، أو من صفحة Releases)
2. افتح بلندر واذهب إلى: **Edit ← Preferences ← Add-ons**
3. اضغط السهم الصغير أعلى يمين النافذة واختر **Install from Disk...**
4. اختر ملف `date_palm_bunch.zip` واضغط تثبيت
5. فعّل علامة ✔ جنب **"Date Palm Bunch Generator - مولد عذق التمر"**
6. أغلق النافذة. خلاص! ✅

### كيف تضيف عذق؟

1. في نافذة العرض ثلاثية الأبعاد اضغط **Add ← Curve ← Date Bunch (عذق تمر)**
2. بيظهر العذق مكان مؤشر البلندر (الدائرة الحمراء البيضاء)
3. **قبل ما تضغط أي شي ثاني**: افتح اللوحة الصغيرة أسفل يسار الشاشة (أو اضغط F9) وعدّل:
   - **Strands** عدد الشماريخ (الأغصان)
   - **Shape Seed** غيّر الرقم = شكل عشوائي جديد
   - **Spread** اتساع العذق
   - **Overall Size** الحجم الكلي
   - **Variety** الصنف (0 إلى 22 — القائمة تحت)

### التحكم الكامل بعد الإضافة

حدد العذق وافتح تبويب **المفتاح 🔧 (Modifiers)** — كل شي سلايدرات:

| السلايدر | وظيفته |
|---|---|
| Strands x | مضاعفة عدد الشماريخ (1-4) |
| Date Spacing | المسافة بين الحبات (أصغر = حبات أكثر) |
| Date Size | حجم الحبة |
| Dates Start | من وين تبدأ الحبات على الشمراخ |
| Stalk Radius / Resolution | سماكة ونعومة الشمراخ |
| Knob Size | حجم العُقد الصغيرة على الشماريخ |
| Fruit Wrinkles / Lumps / Micro | قوة تجاعيد الحبة (ديسبلاسمنت حقيقي) |
| Fruit Resolution | دقة الحبة (0-3) |
| Color Seed | توزيعة ألوان جديدة |
| Variety | الصنف (0-22) |

**🛡️ ضمانة عدم التداخل:** الحبات تفحص بعضها داخل النودز — أي حبة تلامس حبة ثانية تنحذف تلقائياً. زد Strands x أو كبّر الحبات أو عدّل الكيرف يدوياً — ما بيصير تداخل أبداً.

### الطريقة 2 — بدون تثبيت (Append)

1. افتح ملفك في بلندر
2. **File ← Append**
3. تصفح لملف `date_bunch_assets.blend`
4. ادخل مجلد **Object** واختر **DateBunch**
5. اضغط Append — بيجيب معه كل شي تلقائياً (الحبة، المواد، النودز)

---

## 🌴 قائمة الأصناف — Varieties (Variety slider)

| # | الصنف | # | الصنف |
|---|---|---|---|
| 0 | المجدول (الافتراضي) | 12 | سكري أحمر |
| 1 | العجوة | 13 | سكرة ينبع |
| 2 | الصقعي | 14 | سبع |
| 3 | الخلاص | 15 | زوندي |
| 4 | السكري | 16 | زبنة |
| 5 | البرحي | 17 | شكيري |
| 6 | زاملي | 18 | شكل |
| 7 | ريق البنات | 19 | شقراء |
| 8 | دهني | 20 | سيقان البنات |
| 9 | دهامة | 21 | سندي |
| 10 | دكيني | 22 | سلج قطار |
| 11 | سكرية الشريف | | |

💡 **نصيحة:** الأصناف من 6 إلى 22 (مرحلة البسر) ملساء لامعة بطبيعتها — نزّل Fruit Wrinkles إلى 0.05 وFruit Lumps إلى 0.05 معها.

## 🎬 التحريك — Animation

الشماريخ كيرفات حقيقية: حدد العذق وادخل **Edit Mode (Tab)** وحرّك أي نقطة — الحبات تتبع تلقائياً بدون تداخل. للأنميشن أضف **Hooks** لنقاط الكيرف أو استخدم أي مودفاير تشويه.

---

## English Quick Start

1. Download `date_palm_bunch.zip` → Blender: Edit > Preferences > Add-ons > Install from Disk
2. Enable "Date Palm Bunch Generator"
3. Add > Curve > Date Bunch — tweak strands/seed/variety in the F9 panel
4. All controls live on the `DateBunchGN` modifier (23 varieties, wrinkle strength, resolution, color seed)
5. Fruits are guaranteed collision-free: a built-in geometry-nodes guard removes any intersecting date, even after manual curve edits

Or without installing: File > Append > `date_bunch_assets.blend` > Object > `DateBunch`.

## License

MIT — free for any use, including commercial.
