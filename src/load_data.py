import pandas as pd

# 1. Data load karna
file_path = "data/support_tickets.csv"
df = pd.read_csv(file_path)

print("--- 1. Poora Dataset ---")
print(df)
print("\n" + "="*40 + "\n")

# 2. Total Tickets ki counting
total_tickets = len(df)
print(f"Total Tickets ki tadaad: {total_tickets}")
print("\n" + "="*40 + "\n")

# 3. Sirf HIGH priority wale tickets filter karna
high_priority_df = df[df['priority'] == 'High']
print("--- 2. Sirf High Priority Tickets ---")
print(high_priority_df)
print("\n" + "="*40 + "\n")

# 4. Har category mein kitne tickets hain check karna
category_counts = df['category'].value_counts()
print("--- 3. Har Category Mein Total Tickets ---")
print(category_counts)
