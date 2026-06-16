def route_ticket(ticket_text):
    # Text ko lower case mein convert karna taakay spelling ka masla na ho
    text = ticket_text.lower()
    
    # Default values (agar kuch match na ho)
    category = "General"
    priority = "Low"
    
    # Rules for Category
    if "login" in text or "password" in text or "error" in text:
        category = "Technical"
    elif "refund" in text or "cancel" in text or "billing" in text or "price" in text:
        category = "Billing"
    elif "delayed" in text or "shipping" in text or "delivery" in text or "order" in text:
        category = "Shipping"
        
    # Rules for Priority
    if "urgent" in text or "not working" in text or "refund" in text:
        priority = "High"
    elif "reset" in text or "delayed" in text:
        priority = "Medium"
        
    return category, priority

# Test karne ke liye ek naya ticket
customer_ticket = "My order is delayed and I want a refund immediately"

# Function ko chalana
assigned_category, assigned_priority = route_ticket(customer_ticket)

print("--- AI Rule-Based Agent Output ---")
print(f"Customer Ticket: '{customer_ticket}'")
print(f"Auto Assigned Category: {assigned_category}")
print(f"Auto Assigned Priority: {assigned_priority}")
