# RDS Elevation — Skill Reference

> **Source**: `libs/core/styles/abstracts/mixins/_elevation.scss` > **Mixin**: `@include m.rds-elevation($z)` via `@use '@rds/core/styles/abstracts/mixins' as m`
>
> ⚠️ **Generated on**: 2026-04-24 | **Verify against**: `libs/core/styles/abstracts/mixins/_elevation.scss`

---

## Table of Contents

- [Elevation Scale](#elevation-scale)
- [Usage Guide](#usage-guide)
- [Animated Transitions](#animated-transitions)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Elevation Scale

RDS uses a 3-level elevation scale. Each level produces a composite `box-shadow` with two layers (umbra + ambient) for realistic depth.

| Level | Umbra shadow      | Ambient shadow      | Use case                             |
| ----- | ----------------- | ------------------- | ------------------------------------ |
| `1`   | `0px 0px 1px 0px` | `0px 2px 4px 0px`   | Subtle lift — cards, list items      |
| `2`   | `0px 0px 1px 0px` | `0px 8px 20px 0px`  | Medium lift — dropdowns, popovers    |
| `3`   | `0px 0px 2px 0px` | `0px 12px 40px 0px` | High lift — dialogs, drawers, modals |

Shadow color defaults to `grey` (black with varying opacity per layer).

---

## Usage Guide

### SCSS — `rds-elevation()` mixin (recommended)

```scss
@use '@rds/core/styles/abstracts/mixins' as m;

.card {
  @include m.rds-elevation(1);
}

.dropdown-panel {
  @include m.rds-elevation(2);
}

.dialog {
  @include m.rds-elevation(3);
}
```

### SCSS — `rds-elevation()` function (for manual composition)

Use the function when you need the raw `box-shadow` value without the mixin wrapper:

```scss
@use '@rds/core/styles/abstracts/mixins' as m;

.card {
  box-shadow: m.rds-elevation(1);
}
```

### HTML — Utility classes

Pre-generated classes are available for all three levels:

```html
<div class="rds-shadow-1">Subtle shadow</div>
<div class="rds-shadow-2">Medium shadow</div>
<div class="rds-shadow-3">High shadow</div>
```

---

## Animated Transitions

To animate between elevation levels on hover or state changes, use the transition mixin:

```scss
@use '@rds/core/styles/abstracts/mixins' as m;

.card {
  @include m.rds-elevation(1);
  @include m.rds-elevation-transition();

  &:hover {
    @include m.rds-elevation(2);
  }
}
```

The transition defaults to `280ms` with a `cubic-bezier(0.4, 0, 0.2, 1)` easing. Override with custom values:

```scss
@include m.rds-elevation-transition(400ms, ease-in-out);
```

---

## Anti-patterns

❌ Hardcoded `box-shadow` values:

```scss
.card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
```

✅ Use the elevation mixin:

```scss
.card {
  @include m.rds-elevation(1);
}
```

---

❌ Elevation levels outside 1–3:

```scss
@include m.rds-elevation(0); // error
@include m.rds-elevation(5); // error
```

✅ Always use levels `1`, `2`, or `3`.

---

❌ Manual `box-shadow` transitions:

```scss
.card {
  transition: box-shadow 200ms ease;
}
```

✅ Use the elevation transition mixin:

```scss
.card {
  @include m.rds-elevation-transition();
}
```

---

❌ Using elevation utility classes in component SCSS (mixing concerns):

```scss
.card {
  @extend .rds-shadow-1;
}
```

✅ Use the mixin in SCSS, reserve utility classes for HTML:

```scss
.card {
  @include m.rds-elevation(1);
}
```

---

## Decision Rules

| Scenario                                  | Use                                                |
| ----------------------------------------- | -------------------------------------------------- |
| Static shadow on a component in SCSS      | `@include m.rds-elevation(1\|2\|3)`                |
| Shadow as a raw value (e.g., for compose) | `m.rds-elevation(1\|2\|3)` function                |
| Shadow via HTML class                     | `.rds-shadow-1`, `.rds-shadow-2`, `.rds-shadow-3`  |
| Animate shadow on hover / state change    | `@include m.rds-elevation-transition()`            |
| Custom transition duration or easing      | `@include m.rds-elevation-transition(400ms, ease)` |
| Shadow level not in scale (e.g., 0 or 4)  | ❌ Don't — always use `1`, `2`, or `3`             |
| Hardcoded `box-shadow` value              | ❌ Replace with `rds-elevation()` mixin            |
