<scenario>
# The task relates to the following initial situation:

A large botanical garden uses a sophisticated irrigation system to maintain optimal growing conditions for its diverse plant collection.  The system consists of numerous sprinkler heads located throughout the garden, each controlled by a central computer system.  Each sprinkler head has unique water requirements based on the plants in its vicinity.  The system needs to optimize water usage to conserve resources and minimize operating costs.
</scenario>

<problem>
# 1. Task

The botanical garden wants to implement a scheduling algorithm for its irrigation system that minimizes the total watering time while ensuring that all plants receive sufficient water.  The system should consider the water requirements of each sprinkler head and avoid conflicts where multiple sprinkler heads drawing from the same water source are active simultaneously.
</problem>

<data_elements>
## Sprinkler Head Class

@startuml
class SprinklerHead {
- id : Integer
- waterRequirement : Integer // in liters
- waterSourceId : Integer
- duration : Integer // watering duration in minutes
}
@enduml

Public getter methods are available for each attribute (`getId()`, `getWaterRequirement()`, `getWaterSourceId()`, `getDuration()`).

## Water Source Class

@startuml
class WaterSource {
- id : Integer
- capacity : Integer // liters per minute
}
@enduml

Public getter methods are available for each attribute (`getId()`, `getCapacity()`).


## Input Data

The sprinkler heads are stored in an array `sprinklerHeads` of type `SprinklerHead`.  The water sources are stored in an array `waterSources` of type `WaterSource`.

## Example Data

**sprinklerHeads:**

| id | waterRequirement | waterSourceId | duration |
|---|---|---|---|
| 1 | 50 | 1 | 10 |
| 2 | 100 | 2 | 20 |
| 3 | 75 | 1 | 15 |
| 4 | 25 | 2 | 5 |


**waterSources:**

| id | capacity |
|---|---|
| 1 | 100 |
| 2 | 50 |


## Output Format

The function should return a schedule, represented as a list of `WateringEvent` objects.

@startuml
class WateringEvent {
- sprinklerHeadId : Integer
- startTime : Integer // in minutes from the start of the day
}
@enduml

Public getter methods are available for each attribute (`getSprinklerHeadId()`, `getStartTime()`).


</data_elements>

<pseudocode_task>
Design an algorithm for a function

`createSchedule(sprinklerHeads: SprinklerHead[], waterSources: WaterSource[]): WateringEvent[]`

that creates an irrigation schedule that minimizes the total watering time while respecting water source capacity constraints.  The schedule should specify the start time for each sprinkler head.  Assume a 24-hour period (1440 minutes) for scheduling. If a valid schedule cannot be created (e.g., due to insufficient water source capacity), the function should return an empty array.

Represent the algorithm in pseudocode.

createSchedule(sprinklerHeads: SprinklerHead[], waterSources: WaterSource[]): WateringEvent[]
</pseudocode_task>