# ==========================================
# PHASE 2: FUNCTIONAL ENCAPSULATION & SCOPE
# ==========================================

# Task 4: Identity-Based Computational Seed
LAST_NAME = "Jerusalem"  #[cite: 7]
STUDENT_ID = "TUPM-26-1131"  #[cite: 7]

# Derive computational parameters[cite: 7]
seed_digit = int(STUDENT_ID[-1])  #[cite: 7]
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())  #[cite: 7]
vector_dim = len(LAST_NAME)  #[cite: 7]

# Encapsulate state into a Dictionary (Associative Map)[cite: 7]
sys_config = {
    "operator": LAST_NAME,  #[cite: 7]
    "auth_id": STUDENT_ID,  #[cite: 7]
    "base_seed": seed_digit,  #[cite: 7]
    "checksum": id_checksum,  #[cite: 7]
    "vector_dim": vector_dim,  #[cite: 7]
    "status": "INITIALIZED"  #[cite: 7]
}

# Display system state[cite: 7]
print("=== SYSTEM CONFIGURATION ===")  #[cite: 7]
for key, value in sys_config.items():  #[cite: 7]
    print(f"{key.upper()}: {value}")  #[cite: 7]

print("\n" + "="*40 + "\n")

# ==========================================
# PHASE 3: MUTABLE SEQUENCES (LISTS)
# ==========================================

# Task 5: Dynamic List Operations
# Initialize a list using the system configuration[cite: 7]
base_val = sys_config["base_seed"]  #[cite: 7]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]  #[cite: 7]

print(f"Initial Sequence: {number_sequence}")  #[cite: 7]

# Append a new value to the sequence[cite: 7]
number_sequence.append(base_val + 20)  #[cite: 7]
print(f"After Append: {number_sequence}")  #[cite: 7]
# ==========================================
# Task 6: Sequential Operations
# ==========================================
new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]  #[cite: 8]
number_sequence.extend(new_numbers)  #[cite: 8]
print(f"After Extend: {number_sequence}")  #[cite: 8]

# Count occurrences of the base value[cite: 8]
base_count = number_sequence.count(base_val)  #[cite: 8]
print(f"Occurrences of {base_val}: {base_count}")  #[cite: 8]

# Sort the sequence in ascending order[cite: 8]
number_sequence.sort()  #[cite: 8]
print(f"Sorted Sequence: {number_sequence}")  #[cite: 8]

print("\n" + "="*40 + "\n")

# ==========================================
# PHASE 4: IMMUTABLE RECORDS & ASSOCIATIVE MAPPING
# ==========================================

# Task 7: Immutable Sequences (Tuples)
# Define an immutable tuple using system parameters[cite: 8]
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 0)  #[cite: 8]
print(f"Fixed Coordinates: {fixed_coordinates}")  #[cite: 8]

# Unpack the tuple into individual variables[cite: 8]
x_val, y_val, z_val = fixed_coordinates  #[cite: 8]
print(f"Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}")  #[cite: 8]

# Attempt to modify the tuple (Expected to fail)[cite: 8]
print("\nAttempting modification...")  #[cite: 8]
try:
    fixed_coordinates[0] = 99  #[cite: 8]
except TypeError as error_msg:
    print(f"Modification Error: {error_msg}")  #[cite: 8]

print("\n" + "="*40 + "\n")

# Task 8: Key-Value Mappings (Dictionaries)
# Create a dictionary representing a structured data payload[cite: 9]
data_payload = {
    "identifier": sys_config["auth_id"],  #[cite: 9]
    "dimension": sys_config["vector_dim"],  #[cite: 9]
    "status": "active"  #[cite: 9]
}

# Iterate and display key-value pairs[cite: 9]
print("--- Payload Data ---")  #[cite: 9]
for key, value in data_payload.items():  #[cite: 9]
    print(f"{key.capitalize()}: {value}")  #[cite: 9]

# Add a new key-value pair dynamically[cite: 9]
data_payload["efficiency_rating"] = 98.5  #[cite: 9]
print(f"\nUpdated Payload: {data_payload}")  #[cite: 9]

print("\n" + "="*40 + "\n")

# ==========================================
# PHASE 5: UNIQUE COLLECTIONS (SETS)
# ==========================================

# Task 9: Data De-duplication
base_val = sys_config["base_seed"]  #[cite: 9]

# Initialize a list with deliberate duplicate values[cite: 9]
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]  #[cite: 9]
print(f"Raw List (with duplicates): {raw_data}")  #[cite: 9]

# Convert the list to a Set to remove duplicates[cite: 9]
unique_data = set(raw_data)  #[cite: 10]
print(f"Unique Set: {unique_data}")  #[cite: 10]

print("\n" + "="*40 + "\n")

# Task 10: Mathematical Set Operations
# Define a secondary reference set for comparison[cite: 10]
reference_set = {base_val, base_val + 10, base_val + 20}  #[cite: 10]
print(f"Reference Set: {reference_set}")  #[cite: 10]

# Perform mathematical intersections and unions[cite: 10]
common_elements = unique_data.intersection(reference_set)  #[cite: 10]
combined_elements = unique_data.union(reference_set)  #[cite: 10]

print(f"Intersection (Common): {common_elements}")  #[cite: 10]
print(f"Union (Combined): {combined_elements}")  #[cite: 10]

print("\n" + "="*40 + "\n")

# ==========================================
# PHASE 6: ADVANCED ITERATIONS
# ==========================================

# Task 11: Homogeneous Arrays
import array  #[cite: 10]

# Initialize an integer array using the type code 'i'[cite: 10]
number_array = array.array('i', [sys_config["base_seed"], sys_config["vector_dim"], 100])  #[cite: 10]
print(f"Integer Array: {number_array}")  #[cite: 10]

# Attempt to append a non-integer data type (Expected to fail)[cite: 10]
print("\nAttempting to append a string...")  #[cite: 10]
try:
    number_array.append("invalid")  #[cite: 10]
except TypeError as error_msg:
    print(f"Type Error: {error_msg}")  #[cite: 10]
    # ==========================================
# Task 12: List Comprehensions
# ==========================================
base_val = sys_config["base_seed"]  #[cite: 10]

# Generate a sequence dynamically[cite: 10]
generated_list = [(x * base_val) for x in range(1, 6)]  #[cite: 10]
print(f"Generated Comprehension: {generated_list}")  #[cite: 10]

# Filter the generated sequence[cite: 10]
filtered_list = [x for x in generated_list if x > 15]  #[cite: 10]
print(f"Filtered Comprehension (Values > 15): {filtered_list}")  #[cite: 10]

print("\n" + "="*40 + "\n")

# ==========================================
# PHASE 7: SPECIALIZED COLLECTIONS
# ==========================================

# Task 13: Double-Ended Queues (Deque)
from collections import deque  #[cite: 10]

# Initialize a double-ended queue[cite: 10]
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])  #[cite: 10]
print(f"Initial Deque: {data_queue}")  #[cite: 10]

# Append to both ends[cite: 10]
data_queue.append(100)  #[cite: 10]
data_queue.appendleft(200)  #[cite: 10]
print(f"After Appends: {data_queue}")  #[cite: 10]

# Remove from the left side[cite: 10]
data_queue.popleft()  #[cite: 10]
print(f"Final Deque (After Popleft): {data_queue}")  #[cite: 10]

print("\n" + "="*40 + "\n")

# Task 14: Fault-Tolerant Key Mappings (Defaultdict)
from collections import defaultdict  #[cite: 10]

# Initialize with a default integer factory (creates a 0 for missing keys)[cite: 10]
default_data = defaultdict(int)  #[cite: 10]

# Assign a known key[cite: 10]
default_data['active_key'] = sys_config["vector_dim"]  #[cite: 10]

print(f"Existing Key Value: {default_data['active_key']}")  #[cite: 10]
# Accessing an uninitialized key will not throw a KeyError[cite: 10]
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key']}")  #