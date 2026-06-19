# ByteBites — UML Class Diagram (Draft)

## Classes

```
┌───────────────────────────────────────┐
│               Customer                │
├───────────────────────────────────────┤
│ - name: str                           │
│ - purchase_history: list[Transaction] │
├───────────────────────────────────────┤
│ + verify_user() → bool                │
│ + add_to_history(t: Transaction)      │
└──────────────────┬────────────────────┘
                   │ places
                   ▼
┌───────────────────────────────────────┐
│             Transaction               │
├───────────────────────────────────────┤
│ - items: list[MenuItem]               │
├───────────────────────────────────────┤
│ + add_item(item: MenuItem)            │
│ + compute_total() → float             │
└──────────────────┬────────────────────┘
                   │ contains
                   ▼
┌───────────────────────────────────────┐
│              MenuItem                 │
├───────────────────────────────────────┤
│ - name: str                           │
│ - price: float                        │
│ - category: str                       │
│ - popularity_rating: float            │
├───────────────────────────────────────┤
│ + get_details() → dict                │
└───────────────────────────────────────┘
                   ▲
                   │ manages
┌───────────────────────────────────────┐
│               Menu                    │
├───────────────────────────────────────┤
│ - items: list[MenuItem]               │
├───────────────────────────────────────┤
│ + add_item(item: MenuItem)            │
│ + filter_by_category(c: str)          │
│     → list[MenuItem]                  │
└───────────────────────────────────────┘
```

## Relationships

| Class       | Related To  | Relationship | Notes                                      |
|-------------|-------------|--------------|--------------------------------------------|
| Customer    | Transaction | Association  | A customer places one or more transactions |
| Transaction | MenuItem    | Aggregation  | A transaction groups one or more items     |
| Menu        | MenuItem    | Aggregation  | The menu holds the full item catalog       |

## Attribute Notes

| Attribute                  | Type              | Source in Spec                                 |
|----------------------------|-------------------|------------------------------------------------|
| Customer.name              | str               | "tracking their names"                         |
| Customer.purchase_history  | list[Transaction] | "their past purchase history"                  |
| MenuItem.name              | str               | "name … for every item we sell"                |
| MenuItem.price             | float             | "price … for every item we sell"               |
| MenuItem.category          | str               | "category … for every item we sell"            |
| MenuItem.popularity_rating | float             | "popularity rating for every item we sell"     |
| Menu.items                 | list[MenuItem]    | "a digital list that holds all items"          |
| Transaction.items          | list[MenuItem]    | "group them into a single transaction"         |

## Method Notes

| Method                | Class       | Reason                                                      |
|-----------------------|-------------|-------------------------------------------------------------|
| verify_user()         | Customer    | Spec: "verify they are real users"                          |
| add_to_history(t)     | Customer    | Keeps purchase_history updated after each transaction       |
| add_item(item)        | Transaction | Adds items to the transaction one at a time                 |
| compute_total()       | Transaction | Spec: "compute the total cost"                              |
| get_details()         | MenuItem    | Convenient read access to all item fields                   |
| add_item(item)        | Menu        | Builds up the item catalog                                  |
| filter_by_category(c) | Menu        | Spec: "filter by category such as 'Drinks' or 'Desserts'"   |

## Scope Reminder
Per `ByteBites_Design_Reference.md`: no authentication logic, no database layer,
and no features beyond the spec above.
