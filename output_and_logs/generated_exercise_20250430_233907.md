<scenario>
# The task relates to the following initial situation:

A large online retailer maintains a complex warehousing system with multiple warehouses across the country. Each warehouse stores a variety of products, identified by unique product IDs.  Inventory management is crucial for efficient order fulfillment.  The system needs to track the quantity of each product available in each warehouse.
</scenario>

<problem>
# 1. Task (25 points)

The retailer needs a system to quickly determine the total quantity of a specific product across all warehouses.  Given a product ID, the system should return the sum of the quantities of that product available in all warehouses.  If the product is not found in any warehouse, the system should return 0.
</problem>

<data_elements>
The inventory data is stored in a two-dimensional array called `warehouseInventory`. Each row represents a warehouse, and each column represents a product.  The value at `warehouseInventory[i][j]` represents the quantity of product `j` in warehouse `i`.

The product IDs are integers starting from 0.  The number of warehouses and products is known and stored in the variables `numWarehouses` and `numProducts`, respectively.

Example `warehouseInventory` (3 warehouses, 4 products):

```
warehouseInventory = [
    [5, 10, 0, 3],  // Warehouse 0
    [2, 0, 7, 8],  // Warehouse 1
    [0, 4, 1, 0]   // Warehouse 2
]
numWarehouses = 3
numProducts = 4
```

In this example, there are 5 units of product 0 in warehouse 0, 10 units of product 1 in warehouse 0, and so on.
</data_elements>

<pseudocode_task>
Create a function `getTotalQuantity(productId: Integer, warehouseInventory: Integer[][], numWarehouses: Integer, numProducts: Integer): Integer` that calculates the total quantity of a given product across all warehouses.

The function should take the following inputs:
* `productId`: The ID of the product to query.
* `warehouseInventory`: The two-dimensional array representing the inventory.
* `numWarehouses`: The number of warehouses.
* `numProducts`: The number of products.

The function should return an integer representing the total quantity of the product across all warehouses.
</pseudocode_task>