import time

# --- Simulated "Workerless Company Operating System" Components ---

# Component 1: Inventory Management Service
# Manages product stock without human intervention.
INVENTORY = {
    "Laptop": {"stock": 10, "price": 1200},
    "Mouse": {"stock": 50, "price": 25},
    "Keyboard": {"stock": 30, "price": 75},
}

def check_inventory(item_name, requested_quantity):
    """
    Automated check of product availability.
    """
    if item_name in INVENTORY and INVENTORY[item_name]["stock"] >= requested_quantity:
        return True, INVENTORY[item_name]["price"]
    return False, 0

def update_inventory(item_name, quantity_change):
    """
    Automated update of inventory after an order.
    """
    if item_name in INVENTORY:
        INVENTORY[item_name]["stock"] += quantity_change
        print(f"  [Inventory Service] Updated {item_name}: New stock = {INVENTORY[item_name]['stock']}")
        return True
    return False

# Component 2: Order Processing Service
# Processes incoming orders, calculates totals, and makes approval decisions.
def process_order(order_id, customer_name, items):
    """
    Automated processing of an order, including inventory check and decision making.
    This simulates the "decision-making processes" mentioned in the article.
    """
    print(f"\n[Order Processing Service] Processing Order #{order_id} for {customer_name}...")
    total_cost = 0
    all_items_available = True
    processed_items = []

    for item_name, quantity in items:
        available, item_price = check_inventory(item_name, quantity)
        if not available:
            print(f"  [Order Processing Service] Item '{item_name}' (qty {quantity}) not available in sufficient stock.")
            all_items_available = False
            break
        else:
            total_cost += item_price * quantity
            processed_items.append((item_name, quantity))
            print(f"  [Order Processing Service] Item '{item_name}' (qty {quantity}) available. Price: ${item_price:.2f}")

    if all_items_available:
        # Simulate payment processing (always successful for this demo)
        payment_successful = True # This is an automated decision point
        if payment_successful:
            print(f"  [Order Processing Service] Payment successful for Order #{order_id}. Total: ${total_cost:.2f}")
            # This is where the "operating system" makes a decision to approve
            print(f"  [Order Processing Service] Order #{order_id} APPROVED.")
            for item_name, quantity in processed_items:
                update_inventory(item_name, -quantity) # Deduct from stock
            return "APPROVED", total_cost
        else:
            print(f"  [Order Processing Service] Payment failed for Order #{order_id}.")
            return "REJECTED_PAYMENT", 0
    else:
        print(f"  [Order Processing Service] Order #{order_id} REJECTED due to insufficient stock.")
        return "REJECTED_STOCK", 0

# Component 3: Notification Service
# Sends automated notifications to customers.
def send_notification(order_id, customer_name, status, total_cost=0):
    """
    Automated sending of order status notifications.
    """
    if status == "APPROVED":
        message = f"Dear {customer_name}, your Order #{order_id} has been APPROVED and will be shipped soon. Total: ${total_cost:.2f}"
    else:
        message = f"Dear {customer_name}, your Order #{order_id} has been {status}. Please contact support for details."
    print(f"  [Notification Service] Sending email to {customer_name}: '{message}'")

# --- Main "Workerless Company Operating System" Execution Flow ---

def run_workerless_system():
    """
    Simulates the continuous operation of the workerless company system.
    """
    print("--- Workerless Company Operating System Initialized ---")
    print("Current Inventory:")
    for item, details in INVENTORY.items():
        print(f"  {item}: {details['stock']} in stock, ${details['price']:.2f}")
    print("-" * 50)

    # Simulate incoming orders
    orders_to_process = [
        {"id": "ORD001", "customer": "Alice Smith", "items": [("Laptop", 1), ("Mouse", 1)]},
        {"id": "ORD002", "customer": "Bob Johnson", "items": [("Keyboard", 2)]},
        {"id": "ORD003", "customer": "Charlie Brown", "items": [("Laptop", 1), ("Monitor", 1)]}, # Monitor not in stock
        {"id": "ORD004", "customer": "Diana Prince", "items": [("Mouse", 60)]}, # Not enough stock
        {"id": "ORD005", "customer": "Eve Adams", "items": [("Keyboard", 1)]},
    ]

    for order_data in orders_to_process:
        order_id = order_data["id"]
        customer = order_data["customer"]
        items = order_data["items"]

        # Step 1: Order is "received" by the system
        print(f"\n[System Core] New Order Received: #{order_id} from {customer}")

        # Step 2: Order Processing Service takes over
        status, total = process_order(order_id, customer, items)

        # Step 3: Notification Service takes over based on processing outcome
        send_notification(order_id, customer, status, total)

        print("-" * 50)
        time.sleep(0.5) # Simulate some processing time

    print("\n--- Workerless Company Operating System Shutting Down ---")
    print("Final Inventory:")
    for item, details in INVENTORY.items():
        print(f"  {item}: {details['stock']} in stock, ${details['price']:.2f}")
    print("-" * 50)

if __name__ == "__main__":
    run_workerless_system()
