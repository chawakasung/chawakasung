---
name: rds-core-developer
description: RDS design tokens, SCSS abstracts (functions, mixins, variables), utility classes, and TypeScript constants/types for the Roche Design System. Trigger when styling components, choosing colors, setting typography, applying spacing/layout, building responsive layouts, or importing RDS constants and types.
metadata:
  author: Roche Design System
  version: '1.0'
---

# RDS Core — Skill Reference

> **Package**: `@rds/core`
>
> ⚠️ **Generated on**: 2026-04-24 | **Verify against**: `package.json` for current version

1. **Always use RDS design tokens** — never hardcode hex colors, px spacing, font sizes, or breakpoint values. Every visual property has a corresponding token accessed via Sass functions (`f.rds-color()`, `f.rds-spacing()`, `f.rds-layout()`) or mixins (`m.rds-typography()`, `m.rds-media()`). If no token fits, round to the nearest one.

2. **Read the relevant sub-skill before generating styles** in a specific domain. This file is the hub — detailed token tables, usage guides, and anti-patterns live in the domain-specific `SKILL-*.md` files linked in the [Sub-Skills](#sub-skills) section.

3. **Import TypeScript constants and types from `@rds/core`** — do not duplicate enum arrays or union types in application code. The canonical `RDS_*` arrays and `Rds*` types are the single source of truth for component variants, sizes, and defaults.

4. **Prefer semantic color tokens over primitives** — semantic tokens (`bg-base-1`, `high-contrast`, `informative`) adapt automatically to light/dark themes. Primitives (`600-roche-blue`) are theme-independent and should only be used when the color must never change.

5. **Use `@use` with namespaced aliases** — always import SCSS abstracts with `@use '@rds/core/styles/abstracts/functions' as f` and `@use '@rds/core/styles/abstracts/mixins' as m`. Do not use `@import` (deprecated in Sass) or un-namespaced `@use`.

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Sub-Skills](#sub-skills)
- [TypeScript Constants & Types](#typescript-constants--types)
- [Component SCSS Styles](#component-scss-styles)
- [Theming](#theming)
- [Anti-patterns](#anti-patterns)
- [Decision Rules](#decision-rules)

---

## Overview

`@rds/core` provides two pillars for building UIs with the Roche Design System:

1. **SCSS Design Tokens & Abstracts** — colors, typography, spacing, layout, breakpoints, grid, and utility classes exposed via Sass functions, mixins, and CSS custom properties.
2. **TypeScript Constants & Types** — strongly-typed enumerations, default values, and union types for every component domain (button variants, alert types, icon sizes, etc.).

Both pillars are framework-agnostic and consumed by `@rds/angular-components`, `@rds/react-components`, and any custom application code.

---

## Quick Start

### SCSS Imports

```scss
// Functions — rds-color(), rds-spacing(), rds-layout(), etc.
@use '@rds/core/styles/abstracts/functions' as f;

// Mixins — rds-typography(), rds-media(), rds-elevation(), etc.
@use '@rds/core/styles/abstracts/mixins' as m;

// Direct variable access (rarely needed — prefer functions)
@use '@rds/core/styles/abstracts/variables' as v;
```

### TypeScript Imports

```typescript
import { RDS_BUTTON_VARIANT, RdsButtonSize, RDS_ALERT_TYPE } from '@rds/core';
```

### Full Stylesheet

```scss
@use '@rds/core/styles/rds';
```

> See [Component SCSS Styles](#component-scss-styles) for details on base-only vs. full imports.

---

## Sub-Skills

Detailed domain-specific references. **Read the relevant sub-skill before working in that area.**

| Domain      | Description                                       | Reference                                                                       |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------- |
| Colors      | Color tokens, themes, CSS variables, primitives   | Read [SKILL-colors.md](SKILL-colors.md)           |
| Typography  | Type scale, fonts, utility classes, mixins        | Read [SKILL-typography.md](SKILL-typography.md)   |
| Spacing     | Component-level padding and gaps                  | Read [SKILL-spacing.md](SKILL-spacing.md)         |
| Layout      | Page-level section spacing                        | Read [SKILL-layout.md](SKILL-layout.md)           |
| Breakpoints | Responsive breakpoints, media query mixins        | Read [SKILL-breakpoints.md](SKILL-breakpoints.md) |
| Grid        | Grid system, containers, columns                  | Read [SKILL-grid.md](SKILL-grid.md)               |
| Elevation   | Box-shadow depth levels, transition helpers       | Read [SKILL-elevation.md](SKILL-elevation.md)        |
| Utilities   | Utility classes (flex, display, visibility, etc.) | Read [SKILL-utilities.md](SKILL-utilities.md)     |

---

## TypeScript Constants & Types

Every component domain in `@rds/core` follows a consistent pattern:

```typescript
// 1. Const array with all allowed values
export const RDS_BUTTON_VARIANT = ['primary', 'warning', 'secondary', ...] as const;

// 2. Union type derived from the array
export type RdsButtonVariant = (typeof RDS_BUTTON_VARIANT)[number];

// 3. Default value (where applicable)
export const RDS_BUTTON_DEFAULT_SIZE: RdsButtonSize = 'm';
```

### Available Domains

Import any of these from `@rds/core`:

#### Forms & Inputs

| Domain           | Example exports                                           |
| ---------------- | --------------------------------------------------------- |
| Checkbox         | `RDS_CHECKBOX_*` constants, `RdsCheckbox*` types          |
| Input            | `RDS_INPUT_*` constants, `RdsInput*` types                |
| Input with Chips | `RDS_INPUT_WITH_CHIPS_*` constants                        |
| Label            | `RDS_LABEL_*` constants, `RdsLabel*` types                |
| Radio Button     | `RDS_RADIO_BUTTON_*` constants, `RdsRadioButton*` types   |
| Search           | `RDS_SEARCH_*` constants, `RdsSearch*` types              |
| Select           | `RDS_SELECT_*` constants, `RdsSelect*` types              |
| Toggle Button    | `RDS_TOGGLE_BUTTON_*` constants, `RdsToggleButton*` types |

#### Layout & Navigation

| Domain      | Example exports                                       |
| ----------- | ----------------------------------------------------- |
| Accordion   | `RDS_ACCORDION_*` constants, `RdsAccordion*` types    |
| Anchor Menu | `RDS_ANCHOR_MENU_*` constants, `RdsAnchorMenu*` types |
| Divider     | `RDS_DIVIDER_*` constants, `RdsDivider*` types        |
| Drawer      | `RDS_DRAWER_*` constants, `RdsDrawer*` types          |
| List Item   | `RDS_LIST_ITEM_*` constants, `RdsListItem*` types     |
| Menu        | `RDS_MENU_*` constants, `RdsMenu*` types              |
| Paginator   | `RDS_PAGINATOR_*` constants, `RdsPaginator*` types    |
| Stepper     | `RDS_STEPPER_*` constants, `RdsStepper*` types        |
| Tab         | `RDS_TAB_*` constants, `RdsTab*` types                |
| Tree        | `RDS_TREE_*` constants, `RdsTree*` types              |

#### Feedback & Overlays

| Domain      | Example exports                                       |
| ----------- | ----------------------------------------------------- |
| Alert       | `RDS_ALERT_*` constants, `RdsAlert*` types            |
| Dialog      | `RDS_DIALOG_*` constants, `RdsDialog*` types          |
| Dropdown    | `RDS_DROPDOWN_*` constants, `RdsDropdown*` types      |
| Empty State | `RDS_EMPTY_STATE_*` constants, `RdsEmptyState*` types |
| Popover     | `RDS_POPOVER_*` constants, `RdsPopover*` types        |
| Tooltip     | `RDS_TOOLTIP_*` constants, `RdsTooltip*` types        |

#### Data Display

| Domain | Example exports                            |
| ------ | ------------------------------------------ |
| Badge  | `RDS_BADGE_*` constants, `RdsBadge*` types |
| Card   | `RDS_CARD_*` constants, `RdsCard*` types   |
| Chips  | `RDS_CHIPS_*` constants, `RdsChips*` types |
| Table  | `RDS_TABLE_*` constants, `RdsTable*` types |

#### UI Elements

| Domain | Example exports                                                     |
| ------ | ------------------------------------------------------------------- |
| Avatar | `RDS_AVATAR_*` constants, `RdsAvatar*` types                        |
| Button | `RDS_BUTTON_*`, `RDS_ICON_BUTTON_*`, `RDS_SPLIT_BUTTON_*` constants |
| Icon   | `RDS_ICON_*` constants, `RdsIcon*` types                            |
| Link   | `RDS_LINK_*` constants, `RdsLink*` types                            |

#### Foundation & Shared

| Domain     | Example exports                                                     |
| ---------- | ------------------------------------------------------------------- |
| Color      | Color-related constants and types                                   |
| Common     | `RdsPlacement*` types, `RdsTouch*` types (shared across components) |
| Typography | Typography-related constants and types                              |
| Utils      | Shared utility types and helpers                                    |

### Usage Example

```typescript
import { RDS_BUTTON_VARIANT, RdsButtonVariant, RDS_BUTTON_DEFAULT_SIZE } from '@rds/core';

// Use the const array for validation or iteration
if (RDS_BUTTON_VARIANT.includes(incomingVariant)) { ... }

// Use the type for type-safe props
function renderButton(variant: RdsButtonVariant) { ... }

// Use the default when no value is provided
const size = userSize ?? RDS_BUTTON_DEFAULT_SIZE; // 'm'
```

---

## Component SCSS Styles

Pre-built component styles live under `styles/library/`. These are consumed internally by `@rds/angular-components` and `@rds/react-components`. To include all component styles in your app:

```scss
@use '@rds/core/styles/rds'; // base + all component styles
```

Or import only the core stylesheet (base styles, no components):

```scss
@use '@rds/core/styles/core'; // base styles only
```

---

## Theming

RDS supports **light** (default) and **dark** themes via semantic color tokens that swap automatically.

### Activating Dark Theme

Add the `rds-theme="dark"` attribute to any ancestor element:

```html
<!-- Entire page -->
<html rds-theme="dark">
  <!-- Scoped section -->
  <div rds-theme="dark">
    <!-- All RDS semantic tokens resolve to dark palette inside here -->
  </div>
</html>
```

No code changes needed — semantic tokens (`bg-base-1`, `high-contrast`, etc.) automatically resolve to the correct palette. See [SKILL-colors.md](SKILL-colors.md) for the full token list.

> ⚠️ Primitive tokens (e.g., `600-roche-blue`) do **not** change between themes. Use them only when a color must remain constant regardless of theme.

---

## Anti-patterns

❌ **Hardcoded hex/rgb values** — breaks theming and design consistency:

```scss
.card {
  background: #f5f5f5;
  color: #333;
}
```

✅ Use semantic color tokens:

```scss
.card {
  background: f.rds-color(bg-base-2);
  color: f.rds-color(high-contrast);
}
```

---

❌ **Arbitrary px/rem for spacing** — diverges from the spacing scale:

```scss
.section {
  padding: 15px;
  gap: 1.5rem;
}
```

✅ Use spacing tokens:

```scss
.section {
  padding: f.rds-spacing(5); // 16px
  gap: f.rds-spacing(7); // 24px
}
```

---

❌ **Manual font properties** — misses responsive scaling and font consistency:

```scss
.title {
  font-size: 24px;
  font-weight: 500;
  font-family: Arial;
}
```

✅ Use the typography mixin:

```scss
.title {
  @include m.rds-typography(ui-heading-3-bold);
}
```

---

❌ **Raw media queries with hardcoded px** — inconsistent breakpoints:

```scss
@media (min-width: 768px) { ... }
```

✅ Use the breakpoint mixin:

```scss
@include m.rds-media(m) { ... }
```

---

❌ **Duplicating constants** instead of importing from `@rds/core`:

```typescript
const BUTTON_SIZES = ['s', 'm', 'l']; // duplicated!
```

✅ Import the canonical constant:

```typescript
import { RDS_BUTTON_SIZE } from '@rds/core';
```

---

## Decision Rules

| Scenario                                | Action                                                                   |
| --------------------------------------- | ------------------------------------------------------------------------ |
| Need a color value                      | Use `f.rds-color()` or `var(--rds-color-*)` — see SKILL-colors.md        |
| Need typography styling                 | Use `m.rds-typography()` or utility class — see SKILL-typography.md      |
| Need padding / gap inside a component   | Use `f.rds-spacing()` or `p-*` / `m-*` classes — see SKILL-spacing.md    |
| Need space between page sections        | Use `f.rds-layout()` or `lm-*` classes — see SKILL-layout.md             |
| Need responsive style changes           | Use `m.rds-media()` mixin — see SKILL-breakpoints.md                     |
| Need a page grid / columns              | Use `.rds-container` + `.rds-row` + `.rds-col-*` — see SKILL-grid.md     |
| Need box-shadow / depth                 | Use `m.rds-elevation()` or `.rds-shadow-*` — see SKILL-elevation.md      |
| Need flex/display/visibility helpers    | Use utility classes — see SKILL-utilities.md                             |
| Need component variant/size types in TS | Import `RDS_*` / `Rds*` from `@rds/core`                                 |
| Need dark theme                         | Add `rds-theme="dark"` attribute — semantic tokens swap automatically    |
| Value not in the token scale            | Round to the nearest token — do **not** use arbitrary values             |
| Unsure which sub-skill to read          | Start with this hub file, then follow the link to the relevant sub-skill |
