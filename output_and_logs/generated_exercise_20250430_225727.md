<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" is experiencing rapid growth.  They need to optimize their warehouse management system to handle the increasing volume of orders and diverse book formats.  Currently, books are stored on shelves identified by a unique alphanumeric code. Each shelf has a limited weight capacity.
</scenario>

<problem>
# 1. Task (25 points)

Bookworm Delights needs to implement a system for efficiently assigning books to shelves.  Given a list of incoming books, each with its weight and a preferred shelf code (if available),  develop an algorithm to assign each book to a suitable shelf.  The system should prioritize placing books on their preferred shelf if the shelf has sufficient capacity. If the preferred shelf is full or no preference is given, the system should find the first available shelf with sufficient capacity. If no shelf has enough capacity for a given book, the book should be marked as "unassigned".
</problem>

<data_elements>
## Book Class:

@startuml
class Book {
- isbn: String
- weight: Double
- preferredShelf: String
- assignedShelf: String
}
@enduml

Public access methods (set/get) are available for each attribute.  Initially, `assignedShelf` is null.

## Shelf Class:

@startuml
class Shelf {
- shelfCode: String
- capacity: Double
- currentWeight: Double
}
@enduml

Public access methods (set/get) are available for each attribute. Initially, `currentWeight` is 0.

## Input Data:

The input data is provided as two arrays: `books` (an array of `Book` objects) and `shelves` (an array of `Shelf` objects).

**Example:**

**books:**

| isbn | weight | preferredShelf |
|---|---|---|
| 978-0321765723 | 0.5 | A12 |
| 978-0596517748 | 0.7 | B23 |
| 978-1491950296 | 1.2 | A12 |
| 978-0132350884 | 0.9 | null |


**shelves:**

| shelfCode | capacity |
|---|---|
| A12 | 1.0 |
| B23 | 2.0 |
| C34 | 1.5 |


## Output Data:

The algorithm should update the `assignedShelf` attribute of each `Book` object.  Books that cannot be assigned to any shelf should have their `assignedShelf` attribute set to "unassigned".

</data_elements>

<pseudocode_task>
Create a function `assignBooks(books: Book[], shelves: Shelf[]): void` that assigns each book in the `books` array to a suitable shelf in the `shelves` array, following the logic described in the problem statement. The function should modify the `books` array in place, updating the `assignedShelf` attribute of each `Book` object.

assignBooks(books: Book[], shelves: Shelf[]): void
</pseudocode_task>