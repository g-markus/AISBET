<scenario>
# The task relates to the following initial situation:

The online retailer "Bookworm Delights" is experiencing rapid growth and needs to optimize its warehouse management system.  Currently, books are stored across multiple warehouse sections, and retrieving them for order fulfillment involves significant manual effort.  The company wants to implement an automated system to guide robots in efficiently collecting books for individual orders.
</scenario>

<problem>
# 1. Task (25 points)

Develop an algorithm to determine the optimal route for a robot to collect all books for a given order. The robot starts at a designated charging station and must visit each warehouse section containing a book from the order, returning to the charging station at the end. The goal is to minimize the total distance traveled by the robot.
</problem>

<data_elements>
The warehouse layout is represented as a two-dimensional grid, where each cell represents a location.  The charging station is located at cell (0, 0).  Each warehouse section is assigned a unique identifier and coordinates (x, y) within the grid.

The following class defines a warehouse section:

@startuml
class WarehouseSection {
- id : Integer
- x : Integer
- y : Integer
}
@enduml

Public access methods (get/set) are available for each attribute.

Order information is provided as a list of book IDs.  A helper function `getSectionForBook(bookId: Integer): WarehouseSection` returns the `WarehouseSection` object corresponding to the given `bookId`.

The distance between two locations (x1, y1) and (x2, y2) is calculated using the Manhattan distance: `|x1 - x2| + |y1 - y2|`.

The result should be a list of `WarehouseSection` IDs representing the order in which the robot should visit the sections.
</data_elements>

<pseudocode_task>
Create an algorithm in pseudocode for a function that determines the optimal route for the robot.

`calculateRoute(bookIds: List of Integer): List of Integer`
</pseudocode_task>