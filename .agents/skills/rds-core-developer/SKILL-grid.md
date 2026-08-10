# RDS Grid — Skill Reference

> **Source**: `libs/core/styles/abstracts/variables/_grid.scss`
>
> ⚠️ **Generated on**: 2026-04-23 | **Verify against**: `libs/core/styles/abstracts/variables/_grid.scss`

---

## Table of Contents

- [Core Principle](#core-principle)
- [Container Types](#container-types)
- [Standard Container](#standard-container)
- [Dashboard Container](#dashboard-container)
- [Usage Guide](#usage-guide)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Core Principle

RDS uses a **12-column grid**. Containers have responsive gutters and margins defined per breakpoint. Two container types exist: standard (editorial/marketing pages) and dashboard (data-dense UIs).

---

## Container Types

| Type      | Class                            | Use case                                     |
| --------- | -------------------------------- | -------------------------------------------- |
| Standard  | `.container`                     | Editorial, marketing, general pages          |
| Dashboard | `.container.container-dashboard` | Data-dense UIs with sidenav (tables, charts) |
| Fluid     | `.container.container-fluid`     | Full-width fluid layout                      |

---

## Standard Container

Per-breakpoint settings (`$rds-container-variables`):

| Breakpoint | `column-gutter` | `container-gutter` |
| ---------- | --------------- | ------------------ |
| `s`        | 0px             | 20px               |
| `m`        | 24px            | 32px               |
| `l`        | 24px            | 64px               |
| `xl`       | 32px            | 96px               |
| `xxl`      | 32px            | 96px               |

At `xxl`: `max-width: 1672px`, `margin-inline: auto` (centered).

---

## Dashboard Container

Per-breakpoint settings (`$rds-container-dashboard-variables`):

| Breakpoint | `column-gutter` | `container-spacing` |
| ---------- | --------------- | ------------------- |
| `s`        | 0px             | 0px                 |
| `m`        | 16px            | 20px                |
| `l`        | 16px            | 28px                |
| `xl`       | 16px            | 32px                |
| `xxl`      | 16px            | 32px                |

Use with sidenav (288px wide). Sidenav collapses to 72px on smaller viewports.

---

## Usage Guide

### HTML — grid classes

```html
<!-- Standard grid -->
<div class="container">
  <div class="row">
    <div class="col">equal column</div>
    <div class="col-6">6 of 12</div>
    <div class="col-auto">natural width</div>
  </div>
</div>

<div class="container container-dashboard">...</div>
<!-- Dashboard grid -->
<div class="container container-fluid">...</div>
<!-- Fluid grid -->

<div class="col-12 col-m-6 col-l-4 col-xl-3">...</div>
<!-- Responsive columns -->
<div class="offset-4 col-2">...</div>
<!-- Column offset -->
<div class="row row-cols-3">...</div>
<!-- Fixed columns per row -->
```

---

## Anti-patterns

❌ Custom column count:

```html
<div class="col-1-of-5">...</div>
```

✅ Use the 12-column system:

```html
<div class="col-2">...</div>
<!-- closest to 1/5 -->
```

❌ Hardcoded container max-width:

```scss
.wrapper {
  max-width: 1400px;
  margin: 0 auto;
}
```

✅ Use the container class:

```html
<div class="container">...</div>
<!-- max-width: 1672px at xxl -->
```

❌ Custom gutter values:

```scss
.row {
  gap: 18px;
}
```

✅ Use spacing scale for gutters:

```scss
.row {
  gap: f.rds-spacing(5);
} // 16px
```

---

## Decision Rules

| Scenario                           | Use                                                         |
| ---------------------------------- | ----------------------------------------------------------- |
| Standard page layout               | `.container`                                                |
| Data-dense / dashboard layout      | `.container.container-dashboard`                            |
| Full-width fluid layout            | `.container.container-fluid`                                |
| Equal-width columns                | `.col`                                                      |
| Specific column span               | `.col-{1–12}`                                               |
| Column width from content          | `.col-auto`                                                 |
| Responsive column span             | `.col-{breakpoint}-{1–12}`                                  |
| Column offset                      | `.offset-{1–11}`                                            |
| Fixed columns per row              | `.row-cols-{n}`                                             |
| Custom column count                | ❌ Don't — use the 12-column system                         |
| Custom gutter not in spacing scale | ❌ Replace with closest `rds-spacing()` value               |
| Container max width                | `$rds-breakpoint-xxl` (1672px) — see `SKILL-breakpoints.md` |
