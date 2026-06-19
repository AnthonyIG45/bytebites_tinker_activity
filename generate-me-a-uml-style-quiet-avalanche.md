# UML-Style Class Diagram — ByteBites

## Context
The user wants a UML-style class diagram derived from `Bytebites_spec.md`. No Python files exist yet — this is a greenfield project. The diagram captures the four candidate classes, their attributes, methods, and relationships before any code is written.

---

## Class Diagram

```
┌─────────────────────────────────┐
│            Customer             │
├─────────────────────────────────┤
│ - name: str                     │
│ - purchase_history: list[Order] │
├─────────────────────────────────┤
│ + verify_user() → bool          │
│ + add_to_history(t: Transaction)│
└────────────────┬────────────────┘
                 │ places
                 ▼
┌─────────────────────────────────┐
│           Transaction           │
├─────────────────────────────────┤
│ - items: list[MenuItem]         │
├─────────────────────────────────┤
│ + compute_total() → float       │
│ + add_item(item: MenuItem)      │
└────────────────┬────────────────┘
                 │ contains
                 ▼
┌─────────────────────────────────┐
│            MenuItem             │
├─────────────────────────────────┤
│ - name: str                     │
│ - price: float                  │
│ - category: str                 │
│ - popularity_rating: float      │
├─────────────────────────────────┤
│ + get_details() → dict          │
└─────────────────────────────────┘
                 ▲
                 │ manages
┌─────────────────────────────────┐
│              Menu               │
├─────────────────────────────────┤
│ - items: list[MenuItem]         │
├─────────────────────────────────┤
│ + add_item(item: MenuItem)      │
│ + filter_by_category(c: str)    │
│   → list[MenuItem]              │
└─────────────────────────────────┘
```

## Relationships
| From        | To          | Type        | Description                              |
|-------------|-------------|-------------|------------------------------------------|
| Customer    | Transaction | Association | A customer places one or more transactions |
| Transaction | MenuItem    | Aggregation | A transaction holds a list of menu items  |
| Menu        | MenuItem    | Aggregation | The menu manages the full item collection |

## Attribute / Method Rationale
- **Customer.verify_user()** — spec says the system must "verify they are real users"; this is the simplest hook for that check.
- **Transaction.compute_total()** — spec explicitly asks the transaction to "compute the total cost."
- **Menu.filter_by_category()** — spec says the menu must "filter by category such as 'Drinks' or 'Desserts'."

## Verification
No code execution needed — this is a design artifact. Review the diagram against each bullet in `Bytebites_spec.md` to confirm all four classes and every named attribute/behaviour are represented.
