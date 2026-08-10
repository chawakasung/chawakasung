# RDS Color Tokens — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_colors.scss` > **Sass accessor**: `f.rds-color(<token-name>)` via `@use '@rds/core/styles/abstracts/functions' as f` > **CSS variable prefix**: `--rds-color-`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_colors.scss`

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Primitive Tokens](#primitive-tokens)
- [Semantic Tokens](#semantic-tokens)
- [Component Tokens](#component-tokens)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Architecture Overview

Two layers:

1. **Primitive tokens** — raw hex/rgba values, theme-independent. Grouped by hue in `_colors.scss`.
2. **Semantic tokens** — purpose-driven aliases that swap between **light** and **dark** palettes automatically.

CSS custom properties are emitted on `:root` (light) and `[rds-theme="dark"]`.

Utility classes: `.bg-<token>` (background), `.c-<token>` (foreground) — no `rds-` prefix.

---

## Primitive Tokens

Primitives carry actual hex values and are **constant across themes**. For the full list of token names and hex values, see `_colors.scss`.

**Hue groups:** `black-and-white`, `blue`, `red`, `green`, `yellow`, `grey`, `neutral`, `orange`, `purple`, `brand`

> Use primitives only when you need a theme-independent color (rare). Prefer semantic tokens.

---

## Semantic Tokens

Always prefer semantic tokens — they adapt to light/dark automatically.

### Background

| Token                         | Purpose                               |
| ----------------------------- | ------------------------------------- |
| `bg-base-1`                   | Primary page background               |
| `bg-base-2`                   | Secondary surface (cards, sections)   |
| `bg-base-3`                   | Tertiary surface                      |
| `bg-base-box`                 | Boxed containers                      |
| `bg-base-elevated`            | Elevated surfaces (popovers, dialogs) |
| `bg-informative`              | Informative action backgrounds        |
| `bg-informative-hover`        | Informative hover state               |
| `bg-informative-hover-select` | Informative hover/select subtle state |
| `bg-informative-pressed`      | Informative pressed state             |
| `bg-success`                  | Success backgrounds                   |
| `bg-success-hover`            | Success hover state                   |
| `bg-success-pressed`          | Success pressed state                 |
| `bg-warning`                  | Warning backgrounds                   |
| `bg-warning-hover`            | Warning hover state                   |
| `bg-warning-pressed`          | Warning pressed state                 |
| `bg-error`                    | Error backgrounds                     |
| `bg-error-hover`              | Error hover state                     |
| `bg-error-pressed`            | Error pressed state                   |
| `bg-disabled`                 | Disabled element background           |
| `bg-disabled-2`               | Stronger disabled background          |
| `bg-solid-hover-select`       | Solid surface hover/select            |
| `bg-solid-pressed`            | Solid surface pressed                 |
| `bg-transparent-hover-select` | Transparent surface hover/select      |
| `bg-transparent-pressed`      | Transparent surface pressed           |
| `bg-overlay`                  | Modal/dialog overlay                  |
| `bg-gradient-1`               | Gradient stop 1                       |
| `bg-gradient-2`               | Gradient stop 2                       |
| `bg-gradient-3`               | Gradient stop 3                       |
| `bg-gradient-4`               | Gradient stop 4                       |
| `bg-gradient-5`               | Gradient stop 5                       |
| `bg-gradient-6`               | Gradient stop 6                       |
| `bg-gradient-7`               | Gradient stop 7                       |

### Foreground

| Token                      | Purpose                                |
| -------------------------- | -------------------------------------- |
| `high-contrast`            | Primary text / icons                   |
| `low-contrast`             | Secondary text / captions              |
| `high-contrast-reversed`   | Text on inverted surfaces              |
| `on-dark-surface`          | Text on permanently dark surfaces      |
| `on-light-surface`         | Text on permanently light surfaces     |
| `logo`                     | Logo color                             |
| `brand`                    | Brand accent                           |
| `accent`                   | Accent / decorative highlights         |
| `grey-1`                   | Subtle borders / dividers              |
| `grey-2`                   | Medium borders                         |
| `grey-3`                   | Stronger borders / icons               |
| `track`                    | Slider / progress track color          |
| `informative`              | Informative foreground (links, icons)  |
| `informative-hover`        | Informative hover                      |
| `informative-pressed`      | Informative pressed                    |
| `success`                  | Success foreground                     |
| `success-hover`            | Success hover                          |
| `success-pressed`          | Success pressed                        |
| `warning`                  | Warning foreground                     |
| `warning-hover`            | Warning hover                          |
| `warning-pressed`          | Warning pressed                        |
| `error`                    | Error foreground                       |
| `error-hover`              | Error hover                            |
| `error-pressed`            | Error pressed                          |
| `neutral`                  | Neutral accent foreground              |
| `secondary-link`           | Secondary link text                    |
| `secondary-link-hover`     | Secondary link hover                   |
| `secondary-link-pressed`   | Secondary link pressed                 |
| `disabled`                 | Disabled text / icons                  |
| `stroke-enabled`           | Default input / card stroke            |
| `stroke-selected-disabled` | Stroke for selected-but-disabled state |
| `stroke-hover`             | Stroke on hover                        |
| `stroke-active-focus`      | Stroke on focus / active               |

---

## Component Tokens

Scoped to individual components. Theme-aware (light/dark swap automatically).

| Token                                 | Component  |
| ------------------------------------- | ---------- |
| `alert-informative-bg`                | Alert      |
| `alert-success-bg`                    | Alert      |
| `alert-warning-bg`                    | Alert      |
| `alert-error-bg`                      | Alert      |
| `avatar-bg`                           | Avatar     |
| `avatar-stroke`                       | Avatar     |
| `badge-blue-bg`                       | Badge      |
| `badge-green-bg`                      | Badge      |
| `badge-red-bg`                        | Badge      |
| `badge-yellow-bg`                     | Badge      |
| `badge-neutral-bg`                    | Badge      |
| `badge-orange-bg`                     | Badge      |
| `badge-grey-bg`                       | Badge      |
| `badge-dark-grey-bg`                  | Badge      |
| `badge-purple-1-bg`                   | Badge      |
| `badge-purple-2-bg`                   | Badge      |
| `chips-bg-enabled`                    | Chips      |
| `chips-1-bg-pressed`                  | Chips      |
| `chips-1-text-pressed`                | Chips      |
| `chips-1-stroke-enabled`              | Chips      |
| `chips-1-stroke-hover`                | Chips      |
| `chips-2-bg-pressed`                  | Chips      |
| `chips-2-text-pressed`                | Chips      |
| `chips-2-stroke-enabled`              | Chips      |
| `chips-2-stroke-hover`                | Chips      |
| `datepicker-item-bg-hover`            | Datepicker |
| `datepicker-item-bg-comparison`       | Datepicker |
| `datepicker-item-bg-overlap`          | Datepicker |
| `datepicker-item-bg-overlap-selected` | Datepicker |
| `rating-star-filled`                  | Rating     |
| `rating-star-outline`                 | Rating     |
| `rating-star-empty`                   | Rating     |
| `switch-toggle`                       | Switch     |
| `switch-track`                        | Switch     |
| `switch-track-error`                  | Switch     |
| `tooltip-bg`                          | Tooltip    |

---

## Usage Guide

### SCSS (recommended)

```scss
@use '@rds/core/styles/abstracts/functions' as f;

.my-component {
  color: f.rds-color(high-contrast); // var(--rds-color-high-contrast)
  background: f.rds-color(bg-informative); // var(--rds-color-bg-informative)
  border: f.rds-color(600-roche-blue, $hex-color: true); // #0b41cd (primitive only!)
}
```

### CSS Custom Properties

```css
.my-element {
  color: var(--rds-color-high-contrast); /* semantic — theme-aware */
  border-color: var(--rds-color-600-roche-blue); /* primitive — constant */
}
```

### Utility Classes

```html
<div class="bg-informative">...</div>
<span class="c-high-contrast">...</span>
```

> ⚠️ No `rds-` prefix on utility classes — watch for CSS collisions with third-party frameworks.

### Theme Switching

```html
<div rds-theme="dark">...</div>
<!-- All semantic tokens resolve to dark palette -->
```

---

## Anti-patterns

❌ Hardcoded hex values:

```scss
.title {
  color: #544f4f;
}
```

✅ Use semantic tokens:

```scss
.title {
  color: f.rds-color(high-contrast);
}
```

❌ Primitive token for theme-dependent text (breaks in dark mode):

```scss
.title {
  color: f.rds-color(900-shade-grey);
}
```

✅ Semantic token adapts automatically:

```scss
.title {
  color: f.rds-color(high-contrast);
}
```

❌ `$hex-color: true` on semantic tokens (will error):

```scss
background: f.rds-color(bg-informative, $hex-color: true);
```

✅ `$hex-color` only works with primitives:

```scss
border: f.rds-color(600-roche-blue, $hex-color: true);
```

---

## Decision Rules

| Scenario                                  | Use                                                            |
| ----------------------------------------- | -------------------------------------------------------------- |
| Text, icons, links                        | Foreground tokens (`high-contrast`, `informative`, `error`, …) |
| Page / card / surface backgrounds         | Background tokens (`bg-base-1`, `bg-base-box`, …)              |
| Interactive state (hover / pressed)       | Matching `-hover` / `-pressed` variants                        |
| Disabled states                           | `bg-disabled` / `disabled`                                     |
| Component-specific styling                | Component tokens (`alert-*-bg`, `chips-*`, `switch-*`, …)      |
| Brand color that must NOT change on theme | Primitive: `f.rds-color(600-roche-blue, $hex-color: true)`     |
| WCAG contrast                             | Pair `high-contrast` / `low-contrast` with `bg-base-*`         |

---

## File Map

| File                                                | Role                                     |
| --------------------------------------------------- | ---------------------------------------- |
| `libs/core/styles/abstracts/variables/_colors.scss` | Defines primitives + light/dark palettes |
| `libs/core/styles/abstracts/functions/_colors.scss` | `rds-color()` Sass function              |
| `libs/core/styles/abstracts/mixins/_colors.scss`    | Generates CSS vars + utility classes     |
