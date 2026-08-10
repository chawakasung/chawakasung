# RDS Spacing — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_spacings.scss` > **Sass function**: `f.rds-spacing(N)` via `@use '@rds/core/styles/abstracts/functions' as f`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_spacings.scss`

---

## Table of Contents

- [Core Principle](#core-principle)
- [Spacing Scale](#spacing-scale)
- [Utility Class Format](#utility-class-format)
- [Special Values](#special-values)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Core Principle

All **component-level** spacing uses predefined tokens. Never use arbitrary px or rem values — always pick the closest token from the scale.

This skill covers spacing **inside components and between elements within a component** (padding, gaps). For page-level section spacing, see `SKILL-layout.md`.

---

## Spacing Scale

| Suffix | px  |
| ------ | --- |
| 0      | 0   |
| 1      | 2   |
| 2      | 4   |
| 3      | 8   |
| 4      | 12  |
| 5      | 16  |
| 6      | 20  |
| 7      | 24  |
| 8      | 28  |
| 9      | 32  |
| 10     | 40  |
| 11     | 48  |
| 12     | 56  |

---

## Utility Class Format

**Without breakpoint:** `{property}{side}-{size}`
**With breakpoint:** `{property}{side}-{breakpoint}-{size}`

**Property** (`m` = margin, `p` = padding):

| Class | Sets                    |
| ----- | ----------------------- |
| `m`   | margin (spacing scale)  |
| `p`   | padding (spacing scale) |

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

Applies to margin only (`m`, not `p`):

| Value     | Effect                                                 |
| --------- | ------------------------------------------------------ |
| `auto`    | `margin: auto` — e.g. `mx-auto` to center horizontally |
| `n{size}` | Negative margin — e.g. `mt-n3` = `-8px`                |

---

## Usage Guide

### HTML Utility Classes

```html
<div class="p-5">...</div>
<!-- padding all sides: 16px -->
<div class="mt-9">...</div>
<!-- margin top: 32px -->
<div class="px-7">...</div>
<!-- padding horizontal: 24px -->
<div class="mx-auto">...</div>
<!-- center horizontally -->
<div class="mt-n3">...</div>
<!-- negative top margin: -8px -->
<div class="pt-m-5 pt-l-9">...</div>
<!-- responsive: 16px on medium, 32px on large -->
```

### SCSS Utility Function

```scss
@use '@rds/core/styles/abstracts/functions' as f;

.my-component {
  padding: f.rds-spacing(5); // 16px
  gap: f.rds-spacing(3); // 8px
  margin-bottom: f.rds-spacing(7); // 24px
}
```

---

## Anti-patterns

❌ Arbitrary px values:

```scss
.card {
  padding: 15px;
  gap: 1.5rem;
}
```

✅ Use spacing tokens:

```scss
.card {
  padding: f.rds-spacing(5);
  gap: f.rds-spacing(7);
} // 16px, 24px
```

❌ Layout tokens for component-level gaps:

```scss
.list-item {
  margin-bottom: f.rds-layout(1);
} // 16px — wrong scale
```

✅ Use spacing tokens inside components:

```scss
.list-item {
  margin-bottom: f.rds-spacing(5);
} // 16px
```

---

## Decision Rules

| Scenario                          | Use                                                      |
| --------------------------------- | -------------------------------------------------------- |
| Padding inside a component        | `p-{size}` / `rds-spacing()`                             |
| Gap between items in a list/grid  | `mt-{size}` or CSS `gap` with `rds-spacing()`            |
| Space between major page sections | **Use `SKILL-layout.md`** (`lm-{size}` / `rds-layout()`) |
| Need `margin: auto` for centering | `mx-auto` or `my-auto`                                   |
| Overlapping elements              | Negative margin: `mt-n{size}`                            |
| Value between two steps           | Round **up** to the larger token                         |
| Arbitrary px value in SCSS        | ❌ Replace with closest `rds-spacing()` variable         |
