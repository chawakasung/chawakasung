# RDS Breakpoints — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_breakpoints.scss` > **Mixin**: `@include m.rds-media('{name}')` via `@use '@rds/core/styles/abstracts/mixins' as m`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_breakpoints.scss`

---

## Table of Contents

- [Breakpoint Scale](#breakpoint-scale)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Breakpoint Scale

| Name  | min-width                   |
| ----- | --------------------------- |
| `s`   | 0px (mobile first, default) |
| `m`   | 768px                       |
| `l`   | 1024px                      |
| `xl`  | 1440px                      |
| `xxl` | 1672px                      |

RDS uses a **mobile-first** approach — `s` is the base, larger breakpoints override upward.

---

## Usage Guide

### SCSS — `rds-media()` mixin (recommended)

```scss
@use '@rds/core/styles/abstracts/mixins' as m;
@use '@rds/core/styles/abstracts/functions' as f;

.my-component {
  padding: f.rds-spacing(3); // 8px (mobile)

  @include m.rds-media(m) {
    padding: f.rds-spacing(5);
  } // 16px
  @include m.rds-media(l) {
    padding: f.rds-spacing(7);
  } // 24px
}
```

Shorthand mixins are also available:

```scss
@include m.rds-media-s { ... }  // mobile only (max-width)
@include m.rds-media-m { ... }  // ≥ 768px
@include m.rds-media-l { ... }  // ≥ 1024px
@include m.rds-media-xl { ... } // ≥ 1440px
@include m.rds-media-xxl { ... } // ≥ 1672px
```

### Utility classes (spacing/layout responsive suffixes)

Breakpoint names are used as infixes in utility classes:

```html
<div class="pt-m-5 pt-l-9">...</div>
<!-- padding-top 16px at m, 32px at l -->
<div class="lm-xl-10">...</div>
<!-- layout-margin 40px at xl -->
```

See `SKILL-spacing.md` and `SKILL-layout.md` for full utility class syntax.

---

## Anti-patterns

❌ Raw media queries with hardcoded px:

```scss
@media (min-width: 768px) { ... }
```

✅ Use the mixin:

```scss
@include m.rds-media(m) { ... }
```

❌ `max-width` media queries (not mobile-first):

```scss
@media (max-width: 1023px) { ... }
```

✅ Mobile-first with `min-width` via mixin:

```scss
@include m.rds-media(l) { ... } // ≥ 1024px
```

❌ Custom breakpoints:

```scss
@media (min-width: 900px) { ... }
```

✅ Always use RDS breakpoints — pick the closest (`m` = 768px or `l` = 1024px).

---

## Decision Rules

| Scenario                              | Use                                      |
| ------------------------------------- | ---------------------------------------- |
| Responsive styling in SCSS            | `@include m.rds-media('{name}') { ... }` |
| Shorthand for single breakpoint       | `@include m.rds-media-m { ... }`         |
| Responsive utility classes in HTML    | `{class}-{breakpoint}-{size}` suffix     |
| Custom breakpoint not in scale        | ❌ Don't — always use RDS breakpoints    |
| `max-width` media queries             | ❌ Avoid — RDS is mobile-first           |
| Raw `@media (min-width: ...)` in SCSS | ❌ Use `rds-media()` mixin instead       |
