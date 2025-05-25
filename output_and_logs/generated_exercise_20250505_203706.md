<scenario>
# The task relates to the following initial situation:

The city of Hamburg is implementing a new bicycle sharing system called "StadtRAD Hamburg."  The system uses GPS-enabled bicycles and docking stations distributed throughout the city. Users can rent a bike at any station and return it to any other station.  Data about bike rentals, returns, and current bike availability at each station are constantly being collected and updated in the system's database.
</scenario>

<problem>
# 1. Task

StadtRAD Hamburg wants to implement a feature in their mobile app that suggests nearby docking stations with available bikes to users. To achieve this, the app needs an efficient algorithm to find the closest stations to the user's current location.  Furthermore, the app should only display stations that currently have at least one bike available.
</problem>

<data_elements>
The following class `Station` is used to represent a docking station:

@startuml
class Station {
- stationID : Integer
- latitude : double
- longitude : double
- availableBikes : Integer
}
@enduml

Public getter methods are available for all attributes (`getStationID()`, `getLatitude()`, `getLongitude()`, `getAvailableBikes()`).

The system maintains a list of all stations as a `List<Station>` called `allStations`.

The user's current location is represented by a `Location` object:

@startuml
class Location {
- latitude : double
- longitude : double
}
@enduml

Public getter methods are available for both attributes (`getLatitude()`, `getLongitude()`).

The following helper function `calculateDistance` calculates the distance between two locations:

@startuml
class DistanceCalculator {
+ {static} calculateDistance(loc1: Location, loc2: Location) : double
}
@enduml

This function takes two `Location` objects as input and returns the distance between them as a `double`. You can assume this function is already implemented and works correctly.
</data_elements>

<pseudocode_task>
Create an algorithm in pseudocode for a function `findNearestStations(userLocation: Location, allStations: List<Station>, maxDistance: double, minBikes: Integer): List<Station>` that takes the user's current location (`userLocation`), the list of all stations (`allStations`), a maximum search distance (`maxDistance`), and a minimum number of available bikes (`minBikes`) as input.  The function should return a `List<Station>` containing all stations within `maxDistance` of the user's location that have at least `minBikes` available, sorted by distance to the user (closest first).

findNearestStations(userLocation: Location, allStations: List<Station>, maxDistance: double, minBikes: Integer): List<Station>
</pseudocode_task>