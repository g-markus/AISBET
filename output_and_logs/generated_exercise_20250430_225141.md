<scenario>
# The task relates to the following initial situation:

A large online retailer maintains a vast warehouse network. Each warehouse stocks a variety of products, each identified by a unique product ID.  The retailer wants to optimize its inventory management system to ensure efficient order fulfillment.
</scenario>

<problem>
# 1. Task (25 points)

The retailer needs a system to quickly determine the total quantity of a specific product available across all its warehouses.  Given a product ID and a list of warehouses, the system should calculate the total quantity of that product currently in stock.
</problem>

<data_elements>

A `Warehouse` class already exists that stores information about the inventory of each warehouse. There is also a `WarehouseNetwork` class that maintains a list of all warehouses.

## Warehouse Class:

@startuml
class Warehouse {
- id : Integer
- inventory : Map<Integer, Integer>
+ getQuantity(productId : Integer) : Integer
}
@enduml

The `inventory` is a map where the key is the product ID and the value is the quantity of that product in the warehouse.  The `getQuantity` method returns the quantity of a given product in the warehouse, or 0 if the product is not stocked.


## WarehouseNetwork Class:

@startuml
class WarehouseNetwork {
- warehouses : List<Warehouse>
+ getTotalQuantity(productId : Integer) : Integer
}
@enduml


The `warehouses` list contains `Warehouse` objects.  You can access the warehouses through appropriate public getter methods.



## Example Data:

Assume the following data for two warehouses:

**Warehouse 1 (id: 1):**

Inventory:
* Product ID 123: Quantity 10
* Product ID 456: Quantity 5
* Product ID 789: Quantity 12

**Warehouse 2 (id: 2):**

Inventory:
* Product ID 123: Quantity 8
* Product ID 456: Quantity 0
* Product ID 999: Quantity 20


</data_elements>

<pseudocode_task>
Create a function `getTotalQuantity(productId : Integer) : Integer` within the `WarehouseNetwork` class.  This function should take a product ID as input and return the total quantity of that product available across all warehouses in the network.  Utilize the existing `getQuantity` method of the `Warehouse` class for retrieving individual warehouse quantities.

`getTotalQuantity(productId : Integer) : Integer`
</pseudocode_task>