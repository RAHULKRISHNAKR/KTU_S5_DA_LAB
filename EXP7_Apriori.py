import pandas as pd

# Set minimum support and confidence thresholds
min_sup = 3
min_conf = 0.6

# Load dataset
df = pd.read_csv('Data/Apriori.csv')
transactions = df.values.tolist()

# Step 1: Generate 1-itemsets
# Extract unique items from transactions
items = set(item for transaction in transactions for item in transaction)

# Create initial candidate itemsets with single items
candidates = [{item} for item in items]

# Step 2: Filter candidates by support
frequent_itemsets = []
for candidate in candidates:
    # Count the number of transactions containing the candidate itemset
    count = sum(1 for transaction in transactions if candidate.issubset(transaction))
    # If the count meets or exceeds the minimum support, add to frequent itemsets
    if count >= min_sup:
        frequent_itemsets.append(candidate)

# Store all frequent itemsets
all_frequent_itemsets = frequent_itemsets.copy()
k = 2

# Step 3: Generate higher-order itemsets
while frequent_itemsets:
    candidates = []
    n = len(frequent_itemsets)
    for i in range(n):
        for j in range(i + 1, n):
            # Generate candidate itemsets by taking the union of pairs of frequent itemsets
            candidate = frequent_itemsets[i].union(frequent_itemsets[j])
            # Only consider itemsets of length k
            if len(candidate) == k:
                candidates.append(candidate)
    
    frequent_itemsets = []
    for candidate in candidates:
        # Count the number of transactions containing the candidate itemset
        count = sum(1 for transaction in transactions if candidate.issubset(transaction))
        # If the count meets or exceeds the minimum support, add to frequent itemsets
        if count >= min_sup:
            frequent_itemsets.append(candidate)
    
    # Add the new frequent itemsets to the list of all frequent itemsets
    all_frequent_itemsets.extend(frequent_itemsets)
    k += 1

# Display frequent itemsets
print("Frequent Itemsets:\n")
for itemset in all_frequent_itemsets:
    print(itemset)

# Step 4: Generate and display association rules
print("\nAssociation Rules:")

# Iterate over all frequent itemsets
for itemset in all_frequent_itemsets:
    # Only consider itemsets with more than one item
    if len(itemset) > 1:
        # Generate all possible subsets of the itemset
        subsets = [frozenset([item]) for item in itemset]
        # Iterate over each subset
        for antecedent in subsets:
            # The consequent is the itemset minus the antecedent
            consequent = itemset - antecedent
            
            # Only consider non-empty consequents
            if consequent:
                # Calculate support for the itemset
                itemset_support_count = sum(1 for transaction in transactions if itemset.issubset(transaction))
                support = itemset_support_count / len(transactions)
                
                # Calculate support for the antecedent
                antecedent_support_count = sum(1 for transaction in transactions if antecedent.issubset(transaction))
                antecedent_support = antecedent_support_count / len(transactions)
                
                # Calculate confidence
                confidence = support / antecedent_support
                
                # Only consider rules that meet the minimum confidence
                if confidence >= min_conf:
                    # Convert frozenset to regular set for display
                    antecedent = set(antecedent)
                    consequent = set(consequent)
                    print(f"{antecedent} -> {consequent} (support: {support}, confidence: {confidence})")
