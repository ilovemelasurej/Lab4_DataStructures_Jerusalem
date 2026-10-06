students = ["JERUSALEM_S1", "JERUSALEM_S2", "JERUSALEM_S3", "JERUSALEM_S4", "JERUSALEM_S5"]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]
records = [
    {"student": "JERUSALEM_S1", "subject": "PROGRAMMING", "score": 92},
    {"student": "JERUSALEM_S2", "subject": "MATHEMATICS", "score": 85},
    {"student": "JERUSALEM_S3", "subject": "ELECTRONICS", "score": 88},
    {"student": "JERUSALEM_S1", "subject": "PROGRAMMING", "score": 92},
    {"student": "JERUSALEM_S5", "subject": "ENGLISH", "score": None}
]

organized_perf = {}
for r in records:
    st = r["student"]
    if st not in organized_perf:
        organized_perf[st] = {}
    organized_perf[st][r["subject"]] = r["score"]

def get_category(score):
    if score is None: return "INCOMPLETE"
    return "PASSED" if score >= 75 else "FAILED"

seen_recs = set()
repeated_recs = []
incomplete_recs = []
for r in records:
    if r["score"] is None:
        incomplete_recs.append(r)
    tup = (r["student"], r["subject"], r["score"])
    if tup in seen_recs:
        repeated_recs.append(r)
    else:
        seen_recs.add(tup)

ordered_perf = sorted([r for r in records if r["score"] is not None], key=lambda x: x["score"], reverse=True)

print("--- ASSESSMENT DATA ---")
print("1. Generated Performance Records:", records)
print("2. Organized Data:", organized_perf)
print("3. Repeated Records:", repeated_recs)
print("4. Incomplete Records:", incomplete_recs)
print("5. Performance Categories Evaluated for all valid scores.")
print("6. Ordered Results:", ordered_perf)

print("\n--- FINAL OUTPUT ---")
print("Final Student Performance Report:")
for r in records:
    cat = get_category(r['score'])
    print(f"Student: {r['student']} | Subject: {r['subject']} | Score: {r['score']} | Status: {cat}")