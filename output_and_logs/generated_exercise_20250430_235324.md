<scenario>
# The task relates to the following initial situation:

A large online retailer maintains a complex warehousing system with multiple warehouses across the country. Each warehouse stores a variety of products, and the retailer needs to efficiently manage inventory levels to meet customer demand.  Products are categorized by unique product IDs and stored in different sections within each warehouse.
</scenario>

<problem>
# 1. Task

The retailer needs a system to quickly determine the total quantity of a specific product available across all warehouses.  This system should take a product ID as input and return the sum of the quantities of that product found in all warehouses.
</problem>

<data_elements>
The inventory data is represented by a two-dimensional array called `warehouses`.  Each element within this array is an object of the `WarehouseSection` class. Each `WarehouseSection` represents a section within a warehouse and stores information about the products in that section.

## WarehouseSection Class

@startuml
class WarehouseSection {
- productId : Integer
- quantity : Integer
}
@enduml

Public getter methods (`getProductId()` and `getQuantity()`) are available for each attribute.

## Warehouses Array Structure

The `warehouses` array is structured as follows:

`warehouses[warehouse_index][section_index]`

where `warehouse_index` represents the index of the warehouse and `section_index` represents the index of the section within that warehouse.  Each element `warehouses[warehouse_index][section_index]` is a `WarehouseSection` object.

## Example Data

Consider the following simplified example with two warehouses:

Warehouse 0:
- Section 0:  productId = 123, quantity = 5
- Section 1:  productId = 456, quantity = 2
- Section 2:  productId = 123, quantity = 3

Warehouse 1:
- Section 0:  productId = 456, quantity = 1
- Section 1:  productId = 123, quantity = 7


In this example, `warehouses[0][0].getProductId()` would return 123, and `warehouses[0][0].getQuantity()` would return 5.

## Output Format

The function should return an integer representing the total quantity of the specified product across all warehouses.
</data_elements>

<pseudocode_task>
Design an algorithm for a function

`getTotalQuantity(warehouses: WarehouseSection[][], productId: Integer) : Integer`

that takes the `warehouses` array and a `productId` as input and returns the total quantity of that product across all warehouses. Represent the algorithm in pseudocode.


`get_total_quantity(warehouses: Warehouse_section[][], product_id: Integer) : Integer`
</pseudocode_task>