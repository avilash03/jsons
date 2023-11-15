import json
import random

# Generate a list of 3000 JSON objects
data = []

for i in range(1, 500001):
    product = {
        "Product Name": f"Product {i}",
        "Quantity": random.randint(1, 100),
        "Price": round(random.uniform(10, 2000), 2)
    }
    data.append(product)

# Write the data to a JSON file
with open('products500000.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file with 3000 objects generated: products.json")
