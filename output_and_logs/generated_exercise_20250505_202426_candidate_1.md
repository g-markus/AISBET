<scenario>
# The task relates to the following initial situation:

The online retailer "Booktopia" stores information about its books in a database.  Each book entry includes the title, author, ISBN, genre, publication year, and a list of customer reviews.  Booktopia wants to implement new features for its website, including personalized recommendations and enhanced search functionalities.
</scenario>

<problem>
# 1. Task (25 points)

Booktopia needs an algorithm to filter and sort its book collection based on specific criteria. The algorithm should be able to filter books by genre and then sort the filtered results by publication year in ascending order.
</problem>

<data_elements>
The `Book` class is defined as follows:

@startuml
class Book {
- title : String
- author : String
- isbn : String
- genre : String
- publicationYear : Integer
- reviews : List<Review>
}
@enduml

Public get methods are available for each attribute.  The `Review` class is not relevant for this task.

The book collection is stored in an array called `books` of type `Book`.

Example `books` array data:

| Title | Author | ISBN | Genre | Publication Year |
|---|---|---|---|---|
| The Hitchhiker's Guide to the Galaxy | Douglas Adams | 978-0345391803 | Science Fiction | 1979 |
| Pride and Prejudice | Jane Austen | 978-0141439518 | Romance | 1813 |
| To Kill a Mockingbird | Harper Lee | 978-0060935467 | Classic | 1960 |
| 1984 | George Orwell | 978-0451524935 | Dystopian | 1949 |
| The Martian | Andy Weir | 978-0553418026 | Science Fiction | 2011 |


The desired output is a new array containing only books of the specified genre, sorted by publication year.
</data_elements>

<pseudocode_task>
Create an algorithm in pseudocode for a function `filterAndSortBooks(books: Book[], genre: String): Book[]` that filters the `books` array by the given `genre` and sorts the filtered results by `publicationYear` in ascending order.  The function should return a new array containing only the filtered and sorted books.  You can assume access to standard array operations like creating new arrays and adding elements.

filterAndSortBooks(books: Book[], genre: String): Book[]
</pseudocode_task>