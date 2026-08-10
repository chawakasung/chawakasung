# RDS Typography — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_typography.scss` > **Mixin**: `@include m.rds-typography('<class-name>')` via `@use '@rds/core/styles/abstracts/mixins' as m`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_typography.scss`

---

## Table of Contents

- [Core Principle](#core-principle)
- [Two Systems: ui vs article](#two-systems-ui-vs-article)
- [UI Type Scale](#ui-type-scale)
- [Article Type Scale](#article-type-scale)
- [Responsive Breakpoint Override](#responsive-breakpoint-override)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Core Principle

Never set `font-size`, `line-height`, `font-weight`, `letter-spacing`, or `font-family` manually. Always use RDS utility classes or the `rds-typography()` mixin.

- **Roche Sans** — all UI text (headings, body, labels, overlines)
- **Roche Serif** — quotes only (`ui-quote`, `article-quote-*`)

---

## Two Systems: ui vs article

| System      | Use when                                               |
| ----------- | ------------------------------------------------------ |
| `ui-*`      | Application interfaces — dashboards, forms, navigation |
| `article-*` | Editorial / long-form reading content — docs, articles |

Default to `ui-*`. Use `article-*` only for long-form content pages.

---

## UI Type Scale

### Headings (responsive)

| Class               | Weight  |
| ------------------- | ------- |
| `ui-heading-1`      | Light   |
| `ui-heading-1-bold` | Regular |
| `ui-heading-2`      | Light   |
| `ui-heading-2-bold` | Regular |
| `ui-heading-3`      | Regular |
| `ui-heading-3-bold` | Medium  |
| `ui-heading-4`      | Regular |
| `ui-heading-4-bold` | Medium  |

### Body

| Class            | Weight  | Responsive |
| ---------------- | ------- | ---------- |
| `ui-body-l`      | Light   | ✅         |
| `ui-body-l-bold` | Regular | ✅         |
| `ui-body-m`      | Light   | ✅         |
| `ui-body-m-bold` | Regular | ✅         |
| `ui-body-s`      | Light   | ❌         |
| `ui-body-s-bold` | Regular | ❌         |

### Labels (NOT responsive)

| Class             | Weight  |
| ----------------- | ------- |
| `ui-label-l`      | Light   |
| `ui-label-l-bold` | Regular |
| `ui-label-m`      | Light   |
| `ui-label-m-bold` | Regular |
| `ui-label-s`      | Light   |
| `ui-label-s-bold` | Regular |

### Overlines (NOT responsive, uppercase)

| Class           |
| --------------- |
| `ui-overline-m` |
| `ui-overline-s` |

### Component Text (NOT responsive)

| Class                 |
| --------------------- |
| `ui-component-text-m` |
| `ui-component-text-s` |

### Quote (Roche Serif, responsive)

| Class      |
| ---------- |
| `ui-quote` |

---

## Article Type Scale

### Display (responsive)

| Class               | Weight |
| ------------------- | ------ |
| `article-display-l` | Light  |
| `article-display-m` | Light  |

### Headings (responsive)

| Class                    | Weight    |
| ------------------------ | --------- |
| `article-heading-1`      | Light     |
| `article-heading-1-bold` | Regular   |
| `article-heading-2`      | Light     |
| `article-heading-2-bold` | Regular   |
| `article-heading-3`      | Light     |
| `article-heading-3-bold` | Regular   |
| `article-heading-4`      | Regular   |
| `article-heading-4-bold` | Semi-bold |
| `article-heading-5`      | Regular   |
| `article-heading-5-bold` | Semi-bold |
| `article-heading-6`      | Regular   |
| `article-heading-6-bold` | Semi-bold |

### Quotes (Roche Serif, responsive)

| Class             | Weight |
| ----------------- | ------ |
| `article-quote-m` | Light  |
| `article-quote-s` | Light  |

### Lead (responsive)

| Class          | Weight |
| -------------- | ------ |
| `article-lead` | Light  |

### Body (responsive)

| Class                 | Weight  |
| --------------------- | ------- |
| `article-body-m`      | Light   |
| `article-body-m-bold` | Regular |
| `article-body-s`      | Light   |
| `article-body-s-bold` | Regular |

### Caption (responsive)

| Class             |
| ----------------- |
| `article-caption` |

### Non-responsive

| Class              |
| ------------------ |
| `article-kpi`      |
| `article-footnote` |

---

## Responsive Breakpoint Override

Responsive classes automatically scale across breakpoints (`s`, `m`, `l`, `xl`, `xxl`).

To apply typography at a **specific breakpoint only**, use the `--{breakpoint}` suffix:

**Format:** `{class}--{breakpoint}` (e.g., `ui-heading-1--l`, `ui-body-m--s`)

Breakpoints can be combined: `ui-heading-1--xl-xxl`, `ui-heading-1--m-l`, `ui-heading-1--s`

### UI (responsive)

- `ui-heading-1` … `ui-heading-4` (+ `-bold`)
- `ui-body-l` / `ui-body-l-bold`, `ui-body-m` / `ui-body-m-bold`
- `ui-quote`

> **Not responsive:** `ui-body-s` / `-bold`, `ui-label-*`, `ui-overline-*`, `ui-component-text-*`

### Article (responsive)

- `article-display-l`, `article-display-m`
- `article-heading-1` … `article-heading-6` (+ `-bold`)
- `article-quote-m`, `article-quote-s`
- `article-lead`
- `article-body-m` / `-bold`, `article-body-s` / `-bold`
- `article-caption`

> **Not responsive:** `article-kpi`, `article-footnote`

---

## Usage Guide

### HTML Utility Classes

```html
<!-- Page title (responsive by default) -->
<h1 class="ui-heading-1">Dashboard</h1>

<!-- At specific breakpoint -->
<h1 class="ui-heading-1--m-l">Dashboard</h1>

<!-- Section heading -->
<h2 class="ui-heading-3-bold">Recent Activity</h2>

<!-- Body text -->
<p class="ui-body-m">Description text here.</p>

<!-- Form label -->
<span class="ui-label-s">Email address</span>

<!-- Overline -->
<p class="ui-overline-m">Category</p>

<!-- Quote -->
<blockquote class="ui-quote">Doing now what patients need next.</blockquote>
```

### SCSS Mixin

```scss
@use '@rds/core/styles/abstracts/mixins' as m;

.my-heading {
  @include m.rds-typography(ui-heading-2-bold);
}

.my-label {
  @include m.rds-typography(ui-label-s);
}
```

---

## Anti-patterns

❌ Manual font properties:

```scss
.title {
  font-size: 24px;
  font-weight: 500;
  line-height: 32px;
}
```

✅ Use the typography mixin:

```scss
.title {
  @include m.rds-typography(ui-heading-3-bold);
}
```

❌ System fonts:

```scss
.body {
  font-family: Arial, sans-serif;
}
```

✅ Use RDS utility class (Roche Sans applied automatically):

```html
<p class="ui-body-m">...</p>
```

❌ Manual letter-spacing:

```scss
.overline {
  letter-spacing: 1px;
  text-transform: uppercase;
}
```

✅ Already baked into the token:

```scss
.overline {
  @include m.rds-typography(ui-overline-m);
}
```

---

## Decision Rules

| Scenario                                   | Use                                                                |
| ------------------------------------------ | ------------------------------------------------------------------ |
| Page / section headings                    | `ui-heading-1` … `ui-heading-4` (+ `-bold`)                        |
| Running body text                          | `ui-body-m` (default), `ui-body-l` (larger), `ui-body-s` (smaller) |
| Form labels, small UI elements             | `ui-label-s` or `ui-label-m`                                       |
| Category / section labels (uppercase)      | `ui-overline-m` or `ui-overline-s`                                 |
| Text inside chips, badges, tags            | `ui-component-text-m` or `ui-component-text-s`                     |
| Long-form editorial content                | `article-*` classes                                                |
| Quote or testimonial                       | `ui-quote` or `article-quote-*` (Roche Serif)                      |
| Manual `font-size` / `font-weight` in SCSS | ❌ Replace with `rds-typography()` mixin                           |
| System fonts (`Arial`, `Helvetica`)        | ❌ Always use Roche Sans via RDS classes                           |
| `letter-spacing` manually                  | ❌ Baked into the token classes                                    |
