# Import pandas, read parquet file, and convert to json
import pandas as pd
from sklearn.model_selection import train_test_split

# df = pd.read_parquet('test-00000-of-00001.parquet')
df  = pd.read_json('tempfile.jsonl')
# df.to_json('parquetOut.jsonl', orient='records', lines=True)


# 2. First split: Separate out the test set (e.g., 20% of total)
train_val, test = train_test_split(df, test_size=0.2, random_state=42)

# 3. Second split: Split the remaining data into train and validation (e.g., 25% of 80% is ~20% of total)
train, val = train_test_split(train_val, test_size=0.25, random_state=42)

# Verify sizes
print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")

# Save to JSONL files
train.to_json('humaneval_train_subset.jsonl', orient='records', lines=True)
val.to_json('humaneval_val_subset.jsonl', orient='records', lines=True)
test.to_json('humaneval_test_subset.jsonl', orient='records', lines=True)
