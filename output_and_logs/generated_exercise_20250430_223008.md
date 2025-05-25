<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" stores information about its books in a database.  Each book entry includes details such as title, author, ISBN, genre, publication year, and a list of keywords associated with the book. The company wants to implement a new search functionality that allows customers to find books based on a combination of keywords.
</scenario>

<problem>
# 1. Task (25 Points)

Develop an algorithm that efficiently searches the book database and returns all books that match a given set of keywords.  A book is considered a match if it contains *all* the keywords provided in the search query, regardless of their order in the book's keyword list.
</problem>

<data_elements>
The following class definition represents a book in the database:

@startuml
class Book {
- title : String
- author : String
- isbn : String
- genre : String
- publicationYear : Integer
- keywords : List<String>
}
@enduml

Public access methods (get/set) are available for each attribute.  The `keywords` attribute is a `List` of `String` objects, representing the keywords associated with the book.  Assume standard `List` operations like `contains(String s)` (returns `true` if the list contains the string `s`, `false` otherwise) and `size()` (returns the number of elements in the list) are available.


Example Book data:

| Title | Author | ISBN | Genre | Publication Year | Keywords |
|---|---|---|---|---|---|
| The Lord of the Rings | J.R.R. Tolkien | 978-0544003415 | Fantasy | 1954 |  "fantasy", "adventure", "middle-earth", "magic" |
| The Hitchhiker's Guide to the Galaxy | Douglas Adams | 978-0345391803 | Science Fiction | 1979 | "science fiction", "comedy", "space", "guide" |
| Pride and Prejudice | Jane Austen | 978-0141439518 | Romance | 1813 | "romance", "classic", "society", "love" |


The search query is represented as a `List<String>` where each string is a keyword.

Example search query:  `"fantasy", "magic"`
</data_elements>

<pseudocode_task>
Create a function `findMatchingBooks(books: List<Book>, searchKeywords: List<String>): List<Book>` that takes a list of `Book` objects and a list of search keywords as input. The function should return a new list containing only the `Book` objects that match the search criteria (i.e., contain all the keywords in `searchKeywords`).

`findMatchingBooks(books: List<Book>, searchKeywords: List<String>): List<Book>`
</pseudocode_task>