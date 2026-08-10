# RDS Utilities — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_utilities.scss`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_utilities.scss`

---

## Table of Contents

- [Core Principle](#core-principle)
- [Display](#display)
- [Flex](#flex)
- [Width & Height](#width--height)
- [Position](#position)
- [Opacity & Visibility](#opacity--visibility)
- [Text](#text)
- [Vertical Align](#vertical-align)
- [Float](#float)
- [Gap](#gap)
- [Spacing & Layout Utilities](#spacing--layout-utilities)
- [Responsive Suffix](#responsive-suffix)
- [Anti-patterns](#anti-patterns)

---

## Core Principle

Use utility classes directly in HTML instead of writing custom SCSS. All utilities are derived from RDS tokens — never use arbitrary values.

Responsive utilities follow the pattern: `{class}-{breakpoint}-{value}` (e.g. `d-m-flex`).

---

## Display

Class: `d-{value}`  
Responsive: yes

| Class            | CSS                     |
| ---------------- | ----------------------- |
| `d-inline`       | `display: inline`       |
| `d-inline-block` | `display: inline-block` |
| `d-block`        | `display: block`        |
| `d-grid`         | `display: grid`         |
| `d-flex`         | `display: flex`         |
| `d-inline-flex`  | `display: inline-flex`  |
| `d-table`        | `display: table`        |
| `d-table-row`    | `display: table-row`    |
| `d-table-cell`   | `display: table-cell`   |
| `d-none`         | `display: none`         |

```html
<div class="d-flex">
  <div class="d-m-none d-l-block"><!-- hidden on m, visible on l+ --></div>
</div>
```

---

## Flex

All flex utilities are responsive.

### Direction

| Class                 | CSS                              |
| --------------------- | -------------------------------- |
| `flex-row`            | `flex-direction: row`            |
| `flex-column`         | `flex-direction: column`         |
| `flex-row-reverse`    | `flex-direction: row-reverse`    |
| `flex-column-reverse` | `flex-direction: column-reverse` |

### Wrap

| Class               | CSS                       |
| ------------------- | ------------------------- |
| `flex-wrap`         | `flex-wrap: wrap`         |
| `flex-nowrap`       | `flex-wrap: nowrap`       |
| `flex-wrap-reverse` | `flex-wrap: wrap-reverse` |

### Grow & Shrink

| Class           | CSS              |
| --------------- | ---------------- |
| `flex-grow-0`   | `flex-grow: 0`   |
| `flex-grow-1`   | `flex-grow: 1`   |
| `flex-shrink-0` | `flex-shrink: 0` |
| `flex-shrink-1` | `flex-shrink: 1` |
| `flex-fill`     | `flex: 1 1 auto` |

### Justify Content

Class: `justify-content-{value}` — Responsive: yes

| Value     | CSS             |
| --------- | --------------- |
| `start`   | `flex-start`    |
| `end`     | `flex-end`      |
| `center`  | `center`        |
| `between` | `space-between` |
| `around`  | `space-around`  |
| `evenly`  | `space-evenly`  |

### Align Items

Class: `align-items-{value}` — Responsive: yes

`start` · `end` · `center` · `baseline` · `stretch`

### Align Content

Class: `align-content-{value}` — Responsive: yes

`start` · `end` · `center` · `between` · `around` · `stretch`

### Align Self

Class: `align-self-{value}` — Responsive: yes

`auto` · `start` · `end` · `center` · `baseline` · `stretch`

### Order

Class: `order-{value}` — Responsive: yes

`first` (−1) · `0` · `1` · `2` · `3` · `4` · `5` · `last` (6)

---

## Width & Height

### Width

| Class        | CSS                |
| ------------ | ------------------ |
| `w-25`       | `width: 25%`       |
| `w-50`       | `width: 50%`       |
| `w-75`       | `width: 75%`       |
| `w-100`      | `width: 100%`      |
| `w-auto`     | `width: auto`      |
| `mw-100`     | `max-width: 100%`  |
| `vw-100`     | `width: 100vw`     |
| `min-vw-100` | `min-width: 100vw` |

### Height

| Class        | CSS                 |
| ------------ | ------------------- |
| `h-25`       | `height: 25%`       |
| `h-50`       | `height: 50%`       |
| `h-75`       | `height: 75%`       |
| `h-100`      | `height: 100%`      |
| `h-auto`     | `height: auto`      |
| `mh-100`     | `max-height: 100%`  |
| `vh-100`     | `height: 100vh`     |
| `min-vh-100` | `min-height: 100vh` |

---

## Position

Class: `position-{value}`

`static` · `relative` · `absolute` · `fixed` · `sticky`

### Offset helpers

| Class                                   | CSS                     |
| --------------------------------------- | ----------------------- |
| `top-0`                                 | `top: 0`                |
| `top-50`                                | `top: 50%`              |
| `top-100`                               | `top: 100%`             |
| `bottom-0` / `bottom-50` / `bottom-100` | analogous               |
| `start-0` / `start-50` / `start-100`    | `left: 0 / 50% / 100%`  |
| `end-0` / `end-50` / `end-100`          | `right: 0 / 50% / 100%` |

---

## Opacity & Visibility

### Opacity

Class: `opacity-{value}`

| Class         | CSS             |
| ------------- | --------------- |
| `opacity-0`   | `opacity: 0`    |
| `opacity-25`  | `opacity: 0.25` |
| `opacity-50`  | `opacity: 0.5`  |
| `opacity-75`  | `opacity: 0.75` |
| `opacity-100` | `opacity: 1`    |

### Visibility

| Class       | CSS                   |
| ----------- | --------------------- |
| `visible`   | `visibility: visible` |
| `invisible` | `visibility: hidden`  |

---

## Text

### Alignment — Responsive: yes

| Class         | CSS                  |
| ------------- | -------------------- |
| `text-start`  | `text-align: left`   |
| `text-end`    | `text-align: right`  |
| `text-center` | `text-align: center` |

### Decoration

| Class                          | CSS                             |
| ------------------------------ | ------------------------------- |
| `text-decoration-none`         | `text-decoration: none`         |
| `text-decoration-underline`    | `text-decoration: underline`    |
| `text-decoration-line-through` | `text-decoration: line-through` |

### Transform

| Class             | CSS                          |
| ----------------- | ---------------------------- |
| `text-lowercase`  | `text-transform: lowercase`  |
| `text-uppercase`  | `text-transform: uppercase`  |
| `text-capitalize` | `text-transform: capitalize` |

### Wrap

| Class         | CSS                                             |
| ------------- | ----------------------------------------------- |
| `text-wrap`   | `white-space: normal`                           |
| `text-nowrap` | `white-space: nowrap`                           |
| `text-break`  | `word-wrap: break-word; word-break: break-word` |

---

## Vertical Align

Class: `align-{value}`

`baseline` · `top` · `middle` · `bottom` · `text-bottom` · `text-top`

---

## Float

Class: `float-{value}` — Responsive: yes

| Class         | CSS            |
| ------------- | -------------- |
| `float-start` | `float: left`  |
| `float-end`   | `float: right` |
| `float-none`  | `float: none`  |

---

## Gap

Responsive: yes

| Class        | Source                          |
| ------------ | ------------------------------- |
| `gap-{0–12}` | spacing scale (`$rds-spacings`) |
| `lgap-{0–8}` | layout scale (`$rds-layouts`)   |

```html
<div class="d-flex gap-5">
  <!-- flex gap 16px -->
  <div class="d-grid lgap-6"><!-- grid gap from layout scale --></div>
</div>
```

See `SKILL-spacing.md` and `SKILL-layout.md` for scale values.

---

## Spacing & Layout Utilities

Margin (`m`, `mx`, `my`, `mt`, `me`, `mb`, `ms`) and padding (`p`, `px`, `py`, `pt`, `pe`, `pb`, `ps`) utilities — with spacing and layout variants (`lm*`, `lp*`) — are documented in:

- **`SKILL-spacing.md`** — spacing scale (component-level)
- **`SKILL-layout.md`** — layout scale (section/page-level)

---

## Responsive Suffix

All utilities marked "Responsive: yes" accept a breakpoint infix:

```
{class}-{breakpoint}-{value}
```

Breakpoints: `s` · `m` · `l` · `xl` · `xxl` — see `SKILL-breakpoints.md`.

```html
<div class="d-none d-m-flex">
  <!-- hidden on s, flex on m+ -->
  <div class="flex-column flex-l-row">
    <!-- column on s/m, row on l+ -->
    <div class="text-center text-l-start"><!-- centered on s/m, left on l+ --></div>
  </div>
</div>
```

---

## Anti-patterns

❌ Custom CSS for flex layout:

```scss
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

✅ Use utility classes:

```html
<div class="d-flex justify-content-center align-items-center">...</div>
```

❌ Arbitrary width values:

```scss
.panel {
  width: 48%;
}
```

✅ Use width utilities:

```html
<div class="w-50">...</div>
```
