import pandas as pd

# Create some test data
data = {
    "Province": ["Kabul", "Bamyan", "Herat"],
    "Beneficiaries": [120, 85, 150]
}

df = pd.DataFrame(data)

# Simple calculation
df["Status"] = "Completed"

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Python script completed successfully!")
print(df)
