# 🔥 Graph Algorithms: Dijkstra & Burning Number

This project implements **graph algorithms** including **Dijkstra's shortest path** and the **Burning Number algorithm** using Python and NetworkX.

──────────────────────────────

## 📌 Overview  
- Build a weighted undirected graph from user input.  
- Compute **shortest paths** from a source node using Dijkstra’s algorithm.  
- Determine the **burning number** and the **burning sequence** of the graph.  
- Visualize the graph with `matplotlib`.  

──────────────────────────────

## ⚙️ Features  
- ✅ User-defined graph creation (nodes & weighted edges).  
- ✅ Shortest path calculation with **Dijkstra**.  
- ✅ Graph burning process (find burning centers & burning number).  
- ✅ Graph visualization with labeled edges.  

──────────────────────────────

## 🚀 How to Run  

1. Install dependencies:  
```bash
pip install networkx numpy matplotlib
```

2. Run the script:  
```bash
python main.py
```

3. The program will ask for:
   - Number of nodes.
   - Edge weights between nodes.
   - Source node index for shortest path calculation.

──────────────────────────────

## 📊 Example Output  

```
Please enter the number of nodes: 4
Please enter the weight from 0 to 1: 5
Please enter the weight from 0 to 2: 3
Please enter the weight from 0 to 3: 7
Please enter the weight from 1 to 2: 2
Please enter the weight from 1 to 3: 6
Please enter the weight from 2 to 3: 4
Please enter the index of the source node: 0

Shortest path from A to B: ['A', 'C', 'B']
Shortest path from A to C: ['A', 'C']
Shortest path from A to D: ['A', 'C', 'D']
Burning number: 2
Burning sequences: ['A', 'C']
```

Graph will also be displayed with weighted edges.

──────────────────────────────

## 🛠️ Requirements  
- Python 3.8+  
- `networkx`  
- `numpy`  
- `matplotlib`  

──────────────────────────────

## 🎯 Expected Learning Outcomes  
- Understand graph construction and traversal.  
- Apply **Dijkstra’s algorithm** for shortest path problems.  
- Explore **graph burning number** concept in network theory.  
- Visualize and interpret graph structures.  
