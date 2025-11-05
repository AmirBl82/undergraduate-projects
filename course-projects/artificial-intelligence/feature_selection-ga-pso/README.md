# 🧬 Feature Selection using Genetic Algorithm (GA) and Particle Swarm Optimization (PSO)

This project implements **feature selection** for machine learning using
two powerful optimization algorithms:
- **Genetic Algorithm (GA)**
- **Particle Swarm Optimization (PSO)**

Both methods are compared on the **Breast Cancer dataset** from
scikit-learn using a **Random Forest classifier** and evaluated with
**Stratified Cross-Validation**.

──────────────────────────────

## 📌 Overview

Feature selection is critical for improving machine learning models by:
- Reducing dimensionality
- Avoiding overfitting
- Speeding up training
- Improving model generalization

This project explores how GA and PSO can optimize the selection of the
most informative subset of features.

──────────────────────────────

## ⚙️ Algorithms Implemented

### 1️⃣ Genetic Algorithm (GA)
- Uses **binary chromosomes** to represent selected features  
- Operators: **Tournament Selection**, **Crossover**, **Mutation**, **Elitism**  
- Evaluates fitness using Random Forest accuracy with cross-validation  

### 2️⃣ Particle Swarm Optimization (PSO)
- Represents feature subsets as binary **particle positions**  
- Updates particle velocities & positions using **cognitive** and **social** components  
- Converts velocity to probability via a **sigmoid transfer function**  
- Evaluates fitness using the same Random Forest setup  

──────────────────────────────

## 🧠 Dataset

-   Dataset: `load_breast_cancer()` from scikit-learn
-   Binary classification (Malignant vs Benign tumors)
-   30 numerical features (real-valued measurements)

──────────────────────────────

## 📊 Output

The program reports:
- Best feature subset and its **Cross-Validation accuracy**
- **Execution time** of each algorithm
- **Comparison** between GA and PSO in terms of performance and speed

Example output:

    === Genetic Algorithm ===
    Generation 40: Best Fitness = 0.9649
    GA - Best Chromosome: [1 0 1 ... 0 1]
    GA - Best Fitness (CrossVal): 0.9649
    GA - Execution Time: 12.3456 seconds

    === Particle Swarm Optimization ===
    Iteration 40: gbest_score = 0.9614
    PSO - Best Position: [1 1 0 ... 1 0]
    PSO - Best Fitness (CrossVal): 0.9614
    PSO - Execution Time: 10.9876 seconds

    === Comparison ===
    Genetic Algorithm performed better on this dataset.

──────────────────────────────

## 🛠 Technologies Used

-   Python 3.x
-   scikit-learn
-   NumPy

──────────────────────────────

## 🚀 How to Run

1. Install dependencies:  
```bash
pip install scikit-learn numpy
```

2. Run the main script:  
```bash
python main.py
```

──────────────────────────────

## 🎯 Learning Outcomes

- Applying **Genetic Algorithms** and **Particle Swarm Optimization** for feature selection.  
- Understanding **metaheuristic optimization** concepts.  
- Implementing **Random Forest** as an evaluation model.  
- Using **Stratified Cross-Validation** for reliable performance metrics.  
- Comparing algorithmic efficiency in real-world machine learning tasks.  
