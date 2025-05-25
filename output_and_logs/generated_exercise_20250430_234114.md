<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" is experiencing rapid growth and needs to optimize its warehouse management system.  Currently, books are stored on shelves identified by a unique alphanumeric code.  However, the retrieval process is inefficient because there is no systematic organization based on book categories.  The company wants to implement a category-based system to speed up order fulfillment.
</scenario>

<problem>
# 1. Task (25 points)

Bookworm Delights needs a function to categorize books based on their genre and assign them to appropriate warehouse shelves within those categories. Each category has a limited shelf capacity.  The function should ensure that books of the same genre are placed together on shelves within the category, and if a shelf within a category is full, the next available shelf within that category should be used.  If all shelves within a category are full, the book should be marked as "Unplaced."
</problem>

<data_elements>

## Book Class:

@startuml
class Book {
- title : String
- genre : String
- shelfCode : String
}
@enduml

Public access methods (set/get) are available for each attribute.


## Shelf Class:

@startuml
class Shelf {
- shelfCode : String
- category : String
- capacity : Integer
- currentOccupancy : Integer
}
@enduml

Public access methods (set/get) are available for each attribute.

## Input Data:

The function will receive two inputs:

1. `books`: A list of `Book` objects. Initially, the `shelfCode` attribute of each `Book` object is empty.
2. `shelves`: A list of `Shelf` objects representing available shelves.  Assume shelves are pre-sorted by category, and within each category, by shelf code.


## Output Data:

The function should update the `shelfCode` attribute of each `Book` object to reflect its assigned shelf. If a book cannot be placed, its `shelfCode` should be set to "Unplaced." The function should return the updated list of `Book` objects.

## Example:

Let's say we have the following simplified data:

**Books:**

| Title | Genre | Shelf Code |
|---|---|---|
| "The Hobbit" | "Fantasy" |  |
| "Pride and Prejudice" | "Romance" |  |
| "1984" | "Sci-Fi" |  |
| "The Lord of the Rings" | "Fantasy" |  |

**Shelves:**

| Shelf Code | Category | Capacity | Current Occupancy |
|---|---|---|---|
| "F1" | "Fantasy" | 2 | 0 |
| "F2" | "Fantasy" | 2 | 0 |
| "R1" | "Romance" | 1 | 0 |
| "SF1" | "Sci-Fi" | 1 | 0 |


**Expected Output (Books after processing):**

| Title | Genre | Shelf Code |
|---|---|---|
| "The Hobbit" | "Fantasy" | "F1" |
| "Pride and Prejudice" | "Romance" | "R1" |
| "1984" | "Sci-Fi" | "SF1" |
| "The Lord of the Rings" | "Fantasy" | "F2" |

</data_elements>

<pseudocode_task>
Create a function `categorizeBooks(books: List<Book>, shelves: List<Shelf>): List<Book>` that assigns books to shelves according to their genre and the available shelf capacity.  The function should return the updated list of `Book` objects with their assigned `shelfCode`.
</pseudocode_task>