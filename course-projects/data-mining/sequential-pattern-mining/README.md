# 📈 Sequential Pattern Mining using GSP Algorithm

This project implements the **GSP (Generalized Sequential Pattern)** algorithm to find frequent sequential patterns in transactional datasets. The algorithm identifies frequent sequences based on a minimum support threshold and also generates possible combinations of patterns of length 3 and 4.

──────────────────────────────

## 📌 Overview
The GSP algorithm works in multiple steps:
- Extract single items as **initial frequent sequences**.
- Iteratively generate candidate sequences from the previous frequent ones.
- Count their support in the dataset.
- Prune candidates that do not meet the **minimum support threshold**.
- Generate and check **all possible pattern combinations**.

──────────────────────────────

## 🧠 Dataset
The dataset is represented as a list of transactions, where:
- Each transaction is a sequence of **itemsets** (either single items or a list of items).
- Example:

```python
dataset = [
    [['B', 'D'], 'C', 'B', ['A', 'C']],  
    [['B', 'F'], ['C', 'E'], 'B', ["F", "G"]],  
    [['A', 'H'], ['B', 'F'], 'A', 'B', 'F'],  
    [['B', 'E'], ['C', 'E'], 'D'],  
    ['A', ['B', 'D'], 'B', 'C', 'B', ['A', 'D', 'E']]  
]
```

──────────────────────────────

## ⚙️ Algorithm Steps
1. **Generate Candidates** – From frequent sequences of length *k*, generate candidates for length *k+1*.
2. **Count Support** – Count how many transactions contain each candidate.
3. **Prune** – Remove candidates with support less than `min_support`.
4. **Iterate** – Repeat until no new frequent sequences are found.
5. **Generate All Possible Combinations** – Create length 3 and 4 combinations from frequent sequences.

──────────────────────────────

## 📊 Output
The algorithm produces:
- **Frequent patterns per iteration** with their support count and sequence IDs.
- **All possible combinations** and a check whether they exist in the frequent pattern set (`✅` or `❌`).

Example output of combinations:
```
Pattern                           In Dataset
--------------------------------  ----------
(('A',), ('B',), ('C',))          ✅
(('B',), ('D',), ('E',))          ❌
...
```

──────────────────────────────

## 🛠 Technologies Used
- Python 3.x
- pandas
- collections (defaultdict)

──────────────────────────────

## 🚀 How to Run

1. Install dependencies:
```bash
pip install pandas
```
2. Run the Python script:
```bash
python GSP.py
```

──────────────────────────────

## 🎯 Learning Outcomes

- Implementing the **GSP (Generalized Sequential Pattern)** algorithm from scratch.  
- Understanding **sequential pattern mining** and **support counting**.  
- Applying **pattern pruning** and **candidate generation** techniques.  
- Working with **Python data structures** for efficient sequence analysis.  
- Strengthening practical skills in **data mining and algorithmic design**.
