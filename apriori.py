from itertools import combinations
from collections import defaultdict

def get_frequent_itemsets(transactions, min_support):
    itemsets = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            itemsets[frozenset([item])] += 1

    # Filter out itemsets that do not meet the minimum support threshold
    itemsets = {itemset: count for itemset, count in itemsets.items() if count >= min_support}
    return itemsets

def generate_candidates(prev_frequent_itemsets, k):
    candidates = set()
    itemsets_list = list(prev_frequent_itemsets)
    for i in range(len(itemsets_list)):
        for j in range(i+1, len(itemsets_list)):
            candidate = itemsets_list[i] | itemsets_list[j]
            if len(candidate) == k:
                subsets = list(combinations(candidate, k-1))
                if all(frozenset(subset) in prev_frequent_itemsets for subset in subsets):
                    candidates.add(candidate)
    return candidates

def apriori(transactions, min_support):
    transactions = list(map(set, transactions))
    itemsets = get_frequent_itemsets(transactions, min_support)
    all_frequent_itemsets = dict(itemsets)

    k = 2
    while itemsets:
        candidates = generate_candidates(itemsets, k)
        itemsets = defaultdict(int)

        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    itemsets[candidate] += 1

        # Filter out itemsets that do not meet the minimum support threshold
        itemsets = {itemset: count for itemset, count in itemsets.items() if count >= min_support}
        all_frequent_itemsets.update(itemsets)
        k += 1

    return all_frequent_itemsets

def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for antecedent in combinations(itemset, len(itemset) - 1):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                confidence = frequent_itemsets[itemset] / frequent_itemsets[antecedent]
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent, confidence))
    return rules

# Example Usage
transactions = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'egg'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola']
]

min_support = 2
min_confidence = 0.7

frequent_itemsets = apriori(transactions, min_support)
print("Frequent Itemsets:")
for itemset, count in frequent_itemsets.items():
    print(f"{set(itemset)}: {count}")

association_rules = generate_association_rules(frequent_itemsets, min_confidence)
print("\nAssociation Rules:")
for antecedent, consequent, confidence in association_rules:
    print(f"{set(antecedent)} -> {set(consequent)} (Confidence: {confidence:.2f})")
