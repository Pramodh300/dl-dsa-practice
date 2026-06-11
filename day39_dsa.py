#Solve 0/1 Knapsack Manually with Code
# Task 5: Solve 0/1 Knapsack Manually with Code

# Item Data
weights = [3, 2, 1]
values = [40, 30, 20]

# Item Names
laptop_weight = weights[0]
camera_weight = weights[1]
book_weight = weights[2]

laptop_value = values[0]
camera_value = values[1]
book_value = values[2]

capacity = 4

print("========== Individual Items ==========")

print(f"Laptop  -> Weight: {laptop_weight}, Value: {laptop_value}")
print(f"Camera  -> Weight: {camera_weight}, Value: {camera_value}")
print(f"Book    -> Weight: {book_weight}, Value: {book_value}")

print("\n========== Item Combinations ==========")

# Laptop + Book
lb_weight = laptop_weight + book_weight
lb_value = laptop_value + book_value

print(f"Laptop + Book   -> Weight: {lb_weight}, Value: {lb_value}")

# Camera + Book
cb_weight = camera_weight + book_weight
cb_value = camera_value + book_value

print(f"Camera + Book   -> Weight: {cb_weight}, Value: {cb_value}")

# Find best valid combination
best_name = ""
best_value = 0

if lb_weight <= capacity and lb_value > best_value:
    best_name = "Laptop + Book"
    best_value = lb_value

if cb_weight <= capacity and cb_value > best_value:
    best_name = "Camera + Book"
    best_value = cb_value

print("\n========== Final Answer ==========")
print("Best Combination:", best_name)
print("Maximum Value:", best_value)



#Generate All Subsets (Take or Skip)
# Task 6: Generate All Subsets (Take or Skip)

arr = [1, 2, 3]

def generate_subsets(index, current_subset):

    # Base case
    if index == len(arr):
        print(current_subset)
        return

    # Choice 1: Take the current element
    generate_subsets(
        index + 1,
        current_subset + [arr[index]]
    )

    # Choice 2: Skip the current element
    generate_subsets(
        index + 1,
        current_subset
    )

# Start recursion
generate_subsets(0, [])



#Recursive 0/1 Knapsack

def knapsack(weights, values, capacity, n):

    # Base Case
    if n == 0 or capacity == 0:
        return 0

    # If current item is heavier than remaining capacity
    if weights[n - 1] > capacity:
        return knapsack(
            weights,
            values,
            capacity,
            n - 1
        )

    # Option 1: Take current item
    take = values[n - 1] + knapsack(
        weights,
        values,
        capacity - weights[n - 1],
        n - 1
    )

    # Option 2: Skip current item
    skip = knapsack(
        weights,
        values,
        capacity,
        n - 1
    )

    # Return better option
    return max(take, skip)


# Data
weights = [3, 2, 1]
values = [40, 30, 20]
capacity = 4

answer = knapsack(
    weights,
    values,
    capacity,
    len(weights)
)

print("Maximum Value:", answer)



#AI Backpack Optimizer

# Backpack Data
items = ["Laptop", "Camera", "Jacket", "Charger"]

weights = [3, 2, 2, 1]

# Assume these importance scores came from a simple AI model
importance_scores = [90, 70, 50, 30]

capacity = 5


# 0/1 Knapsack Function
def knapsack(weights, values, capacity, n):

    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)

    take = values[n - 1] + knapsack(
        weights,
        values,
        capacity - weights[n - 1],
        n - 1
    )

    skip = knapsack(
        weights,
        values,
        capacity,
        n - 1
    )

    return max(take, skip)


# Function to reconstruct selected items
def find_selected_items(weights, values, capacity, n):

    selected = []

    while n > 0 and capacity > 0:

        if knapsack(weights, values, capacity, n) != \
           knapsack(weights, values, capacity, n - 1):

            selected.append(items[n - 1])
            capacity -= weights[n - 1]

        n -= 1

    return selected


# Run Optimizer
max_score = knapsack(
    weights,
    importance_scores,
    capacity,
    len(items)
)

selected_items = find_selected_items(
    weights,
    importance_scores,
    capacity,
    len(items)
)

# Calculate total weight
total_weight = 0

for item in selected_items:
    index = items.index(item)
    total_weight += weights[index]

# Print Results
print("========== AI Backpack Optimizer ==========")

print("\nSelected Items:")
for item in selected_items:
    print("-", item)

print("\nTotal Weight:", total_weight, "kg")
print("Total Importance Score:", max_score)