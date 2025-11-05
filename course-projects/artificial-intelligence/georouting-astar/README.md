# GeoRouting System using A-Star Algorithm

A Python project that performs geographic pathfinding using the **A\*** algorithm with real driving distances from **OpenRouteService**.  
The script reads nodes from a GeoJSON file, builds a weighted graph using ORS driving distances, computes Haversine heuristics, and returns the optimal route between two user-selected nodes.

──────────────────────────────

## 📌 Overview

This project demonstrates an end-to-end pipeline for geospatial route finding:

- Load and parse a GeoJSON file of nodes (IDs + coordinates).  
- Clean node IDs (remove prefixes like `node/`) and collect coordinates.  
- Query OpenRouteService to get *real driving distances* between node pairs (edge weights).  
- Compute Haversine (great-circle) distances as the heuristic for A\*.  
- Build a weighted graph with `networkx`.  
- Run A\* to find the shortest path between a chosen start and target node.  
- Print node list, cost matrix (pairwise driving distances), heuristic values, and the final path.

──────────────────────────────

## 🗂 Input

- A `.geojson` file containing point features with:
  - `properties['@id']` (e.g. `"node/12345"`)  
  - `geometry.coordinates` (lon, lat)

> The script uses a GUI file picker (`tkinter`) so you can choose the GeoJSON interactively.

──────────────────────────────

## 📊 Sample Visuals / Outputs

- **Extracted Nodes:** printed mapping of node IDs → (lon, lat)  
- **Cost Matrix:** printed pairwise driving distances (meters) retrieved from ORS  
- **Heuristic Table:** Haversine distance from every node to the chosen target  
- **Shortest Path:** printed ordered list of node IDs from start → target

You can optionally add map visualizations (e.g., using `folium`) to show nodes and the resulting path.  
(Example placeholders:)
- `Full-Graph-Map.png` — visualized nodes & edges  
- `Shortest-Route-Map.png` — highlighted optimal route

──────────────────────────────

## 🧩 Technologies & Libraries

- Python 3.8+  
- `openrouteservice` — ORS HTTP client for routing/directions  
- `networkx` — graph creation & traversal  
- `tkinter` — file picker (standard library)  
- `math` (Haversine implementation)  
- `queue.PriorityQueue` — A* frontier

Install dependencies:

```bash
pip install openrouteservice networkx
```

──────────────────────────────

## 🚀 How to Run

1. Set your OpenRouteService API key. **Do not** commit your real key to a public repo.

**Option A — environment variable (recommended):**
```bash
# macOS / Linux
export ORS_API_KEY="your-api-key"

# Windows (PowerShell)
setx ORS_API_KEY "your-api-key"
```

And in the script:
```python
import os
api_key = os.getenv("ORS_API_KEY")
```

**Option B — directly in script (for private use only):**
```python
api_key = "your-own-api-key-here"
```

2. Run the script:
```bash
python Geo_Routing.py
```

3. In the file picker, select your `.geojson`.  
4. Copy start and target node IDs from the printed `Extracted Nodes:` list and enter them when prompted.  
5. Review printed outputs: cost matrix, heuristic values, and the resulting shortest path.

──────────────────────────────

## 🧠 Design Notes

- **Heuristic (Haversine)** is admissible (never overestimates driving distance) in most cases, making A\* optimal.  
- **Edge weights** use ORS driving distances, so the path respects real-world roads, not just "as-the-crow-flies".  
- For many nodes, ORS pairwise queries can be slow and API-rate limited — caching or batching is recommended.

──────────────────────────────

## 🎯 Learning Outcomes

- Implementing the **A-Star (A\*) search algorithm** for real-world geographic data.  
- Working with **GeoJSON** structures and geospatial APIs.  
- Computing **Haversine distances** for heuristic estimation.  
- Applying **graph theory** to practical pathfinding scenarios.  
- Integrating external APIs (OpenRouteService) into Python applications.  
- Understanding **cost matrices** and **weighted graph traversal**.
