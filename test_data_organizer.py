categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]
raw_records = [
    {"source": "JERUSALEM_T1", "category": "TEMPERATURE", "value": 25.5},
    {"source": "JERUSALEM_T2", "category": "VOLTAGE", "value": 12.0},
    {"source": "JERUSALEM_T3", "category": "CURRENT", "value": 1.5},
    {"source": "JERUSALEM_T4", "category": "PRESSURE", "value": 101.3},
    {"source": "JERUSALEM_T5", "category": "SPEED", "value": 60.0},
    {"source": "JERUSALEM_T1", "category": "TEMPERATURE", "value": 25.5}
]

organized_data = {}
for r in raw_records:
    src, cat = r["source"], r["category"]
    if src not in organized_data:
        organized_data[src] = {}
    organized_data[src][cat] = r["value"]

seen = set()
repeated = []
distinct = []
for r in raw_records:
    item_tuple = (r["source"], r["category"], r["value"])
    if item_tuple in seen:
        repeated.append(r)
    else:
        seen.add(item_tuple)
        distinct.append(r)

total_values = len(raw_records)
avg_value = sum(r["value"] for r in raw_records) / total_values
ordered_results = sorted(raw_records, key=lambda x: x["source"])

print("--- ASSESSMENT DATA ---")
print("1. Generated Test Data:", raw_records)
print("2. Organized Test Data:", organized_data)
print("3. Repeated Data:", repeated)
print("4. Summaries (Total Count, Avg):", total_values, avg_value)
print("5. Processed Results (Count):", len(ordered_results))
print("6. Ordered Results:", ordered_results)

print("\n--- FINAL OUTPUT ---")
print("Final Organized and Summarized Test Dataset:")
for k, v in organized_data.items():
    print(f"Source: {k} -> Measurements: {v}")