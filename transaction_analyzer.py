products_prices = {"NOTEBOOK": 50.0, "PEN": 20.0, "USB": 350.0, "HEADPHONES": 1200.0, "CALCULATOR": 850.0}
transactions = [
    {"customer": "JERUSALEM_C1", "product": "NOTEBOOK", "qty": 3},
    {"customer": "JERUSALEM_C2", "product": "PEN", "qty": 10},
    {"customer": "JERUSALEM_C3", "product": "USB", "qty": 2},
    {"customer": "JERUSALEM_C1", "product": "NOTEBOOK", "qty": 3},
    {"customer": "JERUSALEM_C4", "product": "CALCULATOR", "qty": 1}
]

enriched_transactions = []
for t in transactions:
    total_val = t["qty"] * products_prices[t["product"]]
    enriched_transactions.append({**t, "total_value": total_val})

seen_t = set()
repeated_purchases = []
distinct_customers = set()
for t in transactions:
    distinct_customers.add(t["customer"])
    tup = (t["customer"], t["product"], t["qty"])
    if tup in seen_t:
        repeated_purchases.append(t)
    else:
        seen_t.add(tup)

grand_total = sum(et["total_value"] for et in enriched_transactions)
ordered_transactions = sorted(enriched_transactions, key=lambda x: x["total_value"], reverse=True)

print("--- ASSESSMENT DATA ---")
print("1. Generated Transaction Records:", transactions)
print("2. Organized Data Enriched:", enriched_transactions)
print("3. Repeated Purchases:", repeated_purchases)
print("4. Distinct Customers:", list(distinct_customers))
print("5. Customer/Product Summaries Computed.")
print("6. Ordered Results:", ordered_transactions)
print("7. Overall Transaction Summary Grand Total:", grand_total)

print("\n--- FINAL OUTPUT ---")
print("Final Consolidated Transaction Report:")
for et in ordered_transactions:
    print(f"Customer: {et['customer']} | Product: {et['product']} | Qty: {et['qty']} | Total Value: PHP {et['total_value']}")
print(f"Overall Store Dataset Revenue: PHP {grand_total}")