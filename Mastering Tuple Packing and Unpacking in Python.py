# Sample Order Data
sample_orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Function to input customer orders
def input_orders():
    """
    Function to input customer orders from the user.
    Returns a list of tuples, each representing a customer's order.
    """
    orders = []
    while True:
        # Input customer name
        customer_name = input("Enter customer name (or 'done' to finish): ")
        if customer_name.lower() == 'done':
            break
        
        # Input product ordered
        product = input("Enter product ordered: ")
        
        # Input quantity ordered
        quantity = int(input("Enter quantity ordered: "))
        
        # Append the order as a tuple to the orders list
        orders.append((customer_name, product, quantity))
    
    return orders

# Function to process and print orders
def process_orders(order_list):
    """
    Function to iterate over the list of orders, unpack each tuple,
    and print the order details in a user-friendly format.
    """
    for order in order_list:
        # Unpack the tuple into customer_name, product, and quantity
        customer_name, product, quantity = order
        
        # Format and print the order details
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Input orders from the user
user_orders = input_orders()

# Combine sample orders and user input orders
all_orders = sample_orders + user_orders

# Call the function with the combined order data
process_orders(all_orders)
