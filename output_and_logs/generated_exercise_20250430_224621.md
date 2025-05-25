<scenario>
# The task relates to the following initial situation:

The online retailer "Booktopia" stores information about its books in a database. Each book has a unique ISBN, a title, an author, a genre, and a publication year.  Booktopia wants to implement a new search feature that allows users to find books based on different criteria.
</scenario>

<problem>
# 1. Task (25 points)

Booktopia needs an algorithm to filter its book database based on specific search criteria. The search criteria can be a combination of ISBN, title, author, genre, and publication year.  The algorithm should return a list of books that match all provided criteria.  If a criterion is not specified, it should not be used for filtering.
</problem>

<data_elements>
The `Book` class is defined as follows:

@startuml
class Book {
- isbn : String
- title : String
- author : String
- genre : String
- publicationYear : Integer
}
@enduml

Public access methods (getISBN(), getTitle(), getAuthor(), getGenre(), getPublicationYear()) are available for each attribute.

The book database is represented as a `List<Book>`.

The search criteria are provided as a `SearchCriteria` object:

@startuml
class SearchCriteria {
- isbn : String
- title : String
- author : String
- genre : String
- publicationYear : Integer
}
@enduml

Public access methods (getISBN(), getTitle(), getAuthor(), getGenre(), getPublicationYear()) are available for each attribute.  A `null` value for an attribute indicates that the corresponding criterion should not be used for filtering.

Example `List<Book>` (bookDatabase):

| ISBN | Title | Author | Genre | Publication Year |
|---|---|---|---|---|
| 978-0321765723 | The Lord of the Rings | J.R.R. Tolkien | Fantasy | 1954 |
| 978-0743273565 | The Hitchhiker's Guide to the Galaxy | Douglas Adams | Science Fiction | 1979 |
| 978-1481482225| To Kill a Mockingbird | Harper Lee| Fiction | 1960 |
| ... | ... | ... | ... | ... |


Example `SearchCriteria` object (criteria):

```java
SearchCriteria criteria = new SearchCriteria();
criteria.setGenre("Fantasy");
criteria.setPublicationYear(1954);
```

This `SearchCriteria` object would filter for books in the "Fantasy" genre published in 1954.
</data_elements>

<pseudocode_task>
Create a function `filterBooks(bookDatabase: List<Book>, criteria: SearchCriteria): List<Book>` that takes a list of books and a `SearchCriteria` object as input and returns a new list containing only the books that match all provided criteria.

`filterBooks(bookDatabase: List<Book>, criteria: SearchCriteria): List<Book>`
</pseudocode_task>