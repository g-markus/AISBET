<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" is experiencing rapid growth and needs to optimize its warehouse management system.  Currently, books are stored on shelves identified by a unique alphanumeric code.  However, the retrieval process is inefficient as there is no systematic organization of books based on their genre.  This leads to increased search times and delays in order fulfillment.
</scenario>

<problem>
# 1. Task (25 points)

Bookworm Delights wants to reorganize its warehouse by grouping books of the same genre together on shelves.  Develop an algorithm to analyze the current warehouse inventory and generate a report detailing the number of shelves required for each genre, given a maximum capacity per shelf.
</problem>

<data_elements>
The warehouse inventory is represented by a list of `Book` objects.

@startuml
class Book {
- isbn : String
- title : String
- genre : String
}
@enduml

Public access methods (get/set) are available for each attribute.

The `inventory` list stores objects of the `Book` type. An example `inventory` list is shown below:

| isbn | title | genre |
|---|---|---|
| 978-0321765723 | The Lord of the Rings | Fantasy |
| 978-0743273565 | The Hitchhiker's Guide to the Galaxy | Science Fiction |
| 978-0451524935 | Nineteen Eighty-Four | Dystopian |
| 978-0553573428 | A Game of Thrones | Fantasy |
| 978-1400054386 | The Kite Runner | Historical Fiction |
| 978-0307474278 | The Da Vinci Code | Thriller |
| 978-0140430164 | Animal Farm | Dystopian |


The maximum capacity of each shelf is represented by the integer variable `shelfCapacity`.  Assume `shelfCapacity = 2` for this exercise.

The output report should be a list of `GenreShelfCount` objects.

@startuml
class GenreShelfCount {
- genre : String
- shelfCount : Integer
}
@enduml

Public access methods (get/set) are available for each attribute.
</data_elements>

<pseudocode_task>
Create a function `calculateShelves(inventory: List<Book>, shelfCapacity: Integer): List<GenreShelfCount>` that fulfills the following requirement:

* The function takes the inventory list and the shelf capacity as input.
* The function analyzes the inventory and calculates the number of shelves required for each genre based on the shelf capacity.
* The function returns a list of `GenreShelfCount` objects, where each object represents a genre and the corresponding number of shelves needed.
</pseudocode_task>