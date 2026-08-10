# RDS Layout — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_layouts.scss` > **Sass function**: `f.rds-layout(N)` via `@use '@rds/core/styles/abstracts/functions' as f`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_layouts.scss`

---

## Table of Contents

- [Core Principle](#core-principle)
- [Layout Scale](#layout-scale)
- [Utility Class Format](#utility-class-format)
- [Special Values](#special-values)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Core Principle

Layout tokens define spacing **between major sections and layout-level elements** — not inside components. Never use arbitrary px or rem values.

This skill covers **page-level spacing** (margins between sections, large content blocks). For spacing inside components, see `SKILL-spacing.md`.

---

## Layout Scale

| Suffix | px  |
| ------ | --- |
| 0      | 0   |
| 1      | 16  |
| 2      | 24  |
| 3      | 32  |
| 4      | 48  |
| 5      | 64  |
| 6      | 72  |
| 7      | 96  |
| 8      | 120 |

---

## Utility Class Format

**Without breakpoint:** `{property}{side}-{size}`
**With breakpoint:** `{property}{side}-{breakpoint}-{size}`

**Property** (`lm` = layout margin, `lp` = layout padding):

| Class | Sets                   |
| ----- | ---------------------- |
| `lm`  | margin (layout scale)  |
| `lp`  | padding (layout scale) |

**Side** (optional):

| Side      | Property                          |
| --------- | --------------------------------- |
| `t`       | top                               |
| `b`       | bottom                            |
| `s`       | start (left in LTR, right in RTL) |
| `e`       | end (right in LTR, left in RTL)   |
| `x`       | horizontal (left + right)         |
| `y`       | vertical (top + bottom)           |
| _(blank)_ | all 4 sides                       |

**Breakpoint** (optional): `s` · `m` · `l` · `xl` · `xxl`

---

## Special Values

Applies to margin only (`lm`, not `lp`):

| Value     | Effect                                    |
| --------- | ----------------------------------------- |
| `auto`    | `margin: auto` — e.g. `lmx-auto`          |
| `n{size}` | Negative margin — e.g. `lmt-n4` = `-48px` |

---

## Usage Guide

### HTML Utility Classes

```html
<section class="lmb-4">...</section>
<!-- layout margin bottom: 48px -->
<div class="lpx-5">...</div>
<!-- layout padding horizontal: 64px -->
<section class="lmb-m-3 lmb-l-5">...</section>
<!-- responsive: 32px on medium, 64px on large -->
<div class="lmx-auto">...</div>
<!-- center layout block -->
```

### SCSS Utility Function

```scss
@use '@rds/core/styles/abstracts/functions' as f;

.page-section {
  margin-bottom: f.rds-layout(4); // 48px
  padding: f.rds-layout(3); // 32px
}
```

---

## Anti-patterns

❌ Arbitrary px values for section spacing:

```scss
.page-section {
  margin-bottom: 50px;
}
```

✅ Use layout tokens:

```scss
.page-section {
  margin-bottom: f.rds-layout(4);
} // 48px
```

❌ Spacing tokens for page-level gaps:

```scss
.section-gap {
  margin-bottom: f.rds-spacing(11);
} // 48px — wrong scale
```

✅ Use layout tokens between sections:

```scss
.section-gap {
  margin-bottom: f.rds-layout(4);
} // 48px
```

---

## Decision Rules

| Scenario                                    | Use                                                       |
| ------------------------------------------- | --------------------------------------------------------- |
| Space between page sections                 | `lmb-{size}` / `rds-layout()`                             |
| Page horizontal gutters / container padding | `lpx-{size}` / `rds-layout()`                             |
| Padding inside a component                  | **Use `SKILL-spacing.md`** (`p-{size}` / `rds-spacing()`) |
| Gap between list items                      | **Use `SKILL-spacing.md`** (`rds-spacing()`)              |
| Gap ≥ 48px between distinct content blocks  | Layout token                                              |
| Gap < 48px inside a component               | Spacing token                                             |
| Value between two layout steps              | Round **up** to the larger token                          |
| Arbitrary px in SCSS for sections           | ❌ Replace with `rds-layout()` function                   |
