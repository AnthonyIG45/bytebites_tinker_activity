# ByteBites — Implementation Plan

## Context
The UML design is finalized in `AI_UML.md`. The user wants a high-level plan for
implementing the four classes in `models.py`. No database, no auth — pure Python
classes with simple algorithms per the design reference.

---

## File to Modify
`bytebites_tinker_activity/models.py` (currently empty)

---

## Implementation Order

### 1. `MenuItem`
Implement first — it has no dependencies on other classes.

**Attributes (all set in `__init__`):**
- `name: str`
- `price: float`
- `category: str`
- `popularity_rating: float`

**Methods:**
- `get_details() → dict` — return all four attributes as a dictionary

---

### 2. `Menu`
Depends only on `MenuItem`.

**Attributes:**
- `items: list` — starts as an empty list

**Methods:**
- `add_item(item: MenuItem)` — append to `self.items`
- `filter_by_category(category: str) → list` — list comprehension filtering
  `item.category == category`

---

### 3. `Transaction`
Depends only on `MenuItem`.

**Attributes:**
- `items: list` — starts as an empty list

**Methods:**
- `add_item(item: MenuItem)` — append to `self.items`
- `compute_total() → float` — `sum(item.price for item in self.items)`

---

### 4. `Customer`
Implement last — depends on `Transaction`.

**Attributes:**
- `name: str`
- `purchase_history: list` — starts as an empty list

**Methods:**
- `verify_user() → bool` — return `True` if `len(self.purchase_history) > 0`,
  otherwise `False` (proves the customer has prior activity; no auth logic)
- `add_to_history(transaction: Transaction)` — append to `self.purchase_history`

---

## Verification
After writing the classes, run a quick smoke test in the Python REPL or a test file:
1. Create two `MenuItem` objects in different categories
2. Add both to a `Menu`, call `filter_by_category()` and confirm correct subset returned
3. Create a `Transaction`, add both items, call `compute_total()` and check arithmetic
4. Create a `Customer`, call `verify_user()` (should be `False`), add the transaction
   via `add_to_history()`, call `verify_user()` again (should be `True`)
