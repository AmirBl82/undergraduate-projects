# 🛫 Flight Management System with AVL Tree

This project implements a **Flight Management System** using an **AVL
Tree** data structure in Python. The system efficiently manages flight
information with operations like insertion, search, deletion, updates,
and traversal, ensuring balanced performance for large datasets.

──────────────────────────────

## 📌 Overview

The system provides a menu-driven interface where users can:

-   Add flights with details (flight number, pilot, time, passengers,
    source, destination).\
-   Display all flights sorted by flight number (inorder traversal).\
-   Update flight time for a given flight.\
-   Search and display flights to a specific destination.\
-   Find and display the flight with the maximum number of passengers.\
-   Delete a flight by its flight number.\
-   Exit the program gracefully.

The AVL Tree ensures **logarithmic time complexity** for insertions,
deletions, and searches.

──────────────────────────────

## 🧠 Data Stored in Each Node

Each flight is stored as a node in the AVL Tree with the following
attributes:

-   ✈️ Flight Number\
-   👨‍✈️ Pilot Name\
-   ⏰ Flight Time (validated in `HH:MM AM/PM` format)\
-   🧳 Number of Passengers\
-   🌆 Source City\
-   🏙️ Destination City

──────────────────────────────

## 🛠️ Technologies Used

-   Python 3.x\
-   **AVL Tree** implementation for efficient data management\
-   Built-in modules:
    -   `datetime` → for time validation\
    -   `time` → for smooth exit transitions

──────────────────────────────

## 🚀 How to Run

1. Run the script:
``` bash
    python flight_management.py
```

2.  Use the menu options to interact with the system.

──────────────────────────────

## 🎯 Example Menu

    Menu:
    1. Add a flight
    2. Display all flights (sorted by flight number)
    3. Update flight time
    4. Display flights to a specific destination
    5. Display flight with the most passengers
    6. Delete a flight by flight number
    7. Exit

──────────────────────────────

## 📊 Key Features

-   ✅ Balanced AVL Tree for fast operations\
-   ✅ Input validation for reliability\
-   ✅ User-friendly interactive menu\
-   ✅ Handles flight updates and deletions gracefully

──────────────────────────────

## 🎯 Learning Outcomes

- Understanding **AVL Tree rotations** and balance factor management.  
- Implementing **efficient data structures** in real-world systems.  
- Applying **object-oriented programming** principles in Python.  
- Designing **menu-driven applications** with validated user input.  
- Managing **dynamic datasets** with reliable update and delete operations.
