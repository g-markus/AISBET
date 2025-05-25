<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" stores information about its books in a database.  Each book entry includes the title, author, ISBN, genre, and publication year. The company wants to implement a new search feature that allows customers to find books based on various criteria.
</scenario>

<problem>
# 1. Task (25 points)

Bookworm Delights needs an algorithm to search for books based on a partial match of the title and author.  The search should be case-insensitive and return all books where both the title and author contain the provided search strings.
</problem>

<data_elements>
The book data is stored in an array of `Book` objects. The `Book` class is defined as follows:

@startuml
class Book {
- title : String
- author : String
- isbn : String
- genre : String
- publicationYear : Integer
}
@enduml

Public getter methods (`getTitle()`, `getAuthor()`, etc.) are available for each attribute. The array of `Book` objects is named `books`.

Helper function `containsIgnoreCase(text: String, searchString: String): Boolean` is available. This function returns `true` if `text` contains `searchString` irrespective of case, and `false` otherwise.  You do not need to implement this helper function.
</data_elements>

<pseudocode_task>
Create a function `searchBooks(books: Array of Book, titleSearch: String, authorSearch: String): Array of Book` that searches the `books` array for books matching the provided `titleSearch` and `authorSearch` strings.  The function should return an array containing only the matching `Book` objects.

searchBooks(books: Array of Book, titleSearch: String, authorSearch: String): Array of Book
</pseudocode_task>