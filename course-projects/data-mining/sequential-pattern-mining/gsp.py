import pandas as pd
from collections import defaultdict

pd.set_option('display.max_rows', None)  # نمایش همه ردیف‌ها

def generate_candidates(frequent_sequences):
    candidates = set()
    for seq1 in frequent_sequences:
        for seq2 in frequent_sequences:
            if seq1[1:] == seq2[:-1]:
                candidates.add(seq1 + (seq2[-1],))
    return list(candidates)

def count_support(dataset, candidates):
    candidate_counts = defaultdict(lambda: {"support": 0, "seq_ids": []})
    for t_idx, transaction in enumerate(dataset):
        for candidate in candidates:
            idx = 0
            for itemset in transaction:
                itemset = set(itemset) if isinstance(itemset, list) else {itemset}
                if idx < len(candidate) and set(candidate[idx]).issubset(itemset):
                    idx += 1
                if idx == len(candidate):
                    candidate_counts[candidate]["support"] += 1
                    candidate_counts[candidate]["seq_ids"].append(t_idx + 1)
                    break
    return candidate_counts

def prune_candidates(candidate_counts, min_support):
    return {seq: data for seq, data in candidate_counts.items() if data["support"] >= min_support}

def gsp_algorithm(dataset, min_support):
    single_items = set(
        item if isinstance(item, str) else tuple(sorted(item))
        for transaction in dataset
        for itemset in transaction
        for item in (itemset if isinstance(itemset, list) else [itemset])
    )
    frequent_sequences = [((item,),) for item in single_items]

    results = []
    k = 1
    all_possible_combinations = set()

    while frequent_sequences:
        frequent_sequences_sorted = sorted(frequent_sequences)
        print(f"\nFrequent patterns of length {k}:")
        for seq in frequent_sequences_sorted:
            print(f"  {seq}")

        for seq1 in frequent_sequences_sorted:
            for seq2 in frequent_sequences_sorted:
                if seq1[1:] == seq2[:-1]:
                    combination = seq1 + (seq2[-1],)
                    all_possible_combinations.add(combination)

        candidates = generate_candidates(frequent_sequences)
        candidate_counts = count_support(dataset, candidates)
        frequent_sequences = list(prune_candidates(candidate_counts, min_support).keys())
        results.append(prune_candidates(candidate_counts, min_support))
        k += 1

    return results, all_possible_combinations

dataset = [
    [['B', 'D'], 'C', 'B', ['A', 'C']],
    [['B', 'F'], ['C', 'E'], 'B', ["F", "G"]],
    [['A', 'H'], ['B', 'F'], 'A', 'B', 'F'],
    [['B', 'E'], ['C', 'E'], 'D'],
    ['A', ['B', 'D'], 'B', 'C', 'B', ['A', 'D', 'E']]
]

min_support = 2
frequent_patterns, all_possible_combinations = gsp_algorithm(dataset, min_support)

all_results = []
for level, patterns in enumerate(frequent_patterns, start=1):
    for pattern, data in patterns.items():
        all_results.append({
            "Pattern": pattern,
            "Support": data["support"],
            "Seq_IDs": data["seq_ids"]
        })

results_df = pd.DataFrame(all_results)

all_combinations_results = []
for comb in all_possible_combinations:
    found_in_dataset = comb in [key for pattern_dict in frequent_patterns for key in pattern_dict.keys()]
    all_combinations_results.append({
        "Pattern": comb,
        "In Dataset": "✅" if found_in_dataset else "❌"
    })

combinations_df = pd.DataFrame(all_combinations_results)

print("\nAll Possible Combinations (with check for dataset presence):")
print(combinations_df.sort_values(by='Pattern').reset_index(drop=True))

