# 📞 Phone Number Trie

This project implements a **phone contact manager** using a **Trie (prefix tree)** data structure.  
It supports inserting, searching, updating, and deleting contacts based on their phone numbers with efficient digit-by-digit traversal.

──────────────────────────────

## 📌 Overview

The program manages a collection of contacts where each phone number is stored in a **Trie**.  
Key operations include:

- **Insert** a new contact.
- **Search** for a contact by phone number.
- **Update** an existing contact’s details.
- **Delete** a contact completely from the directory.
- **Handle** non-existent or duplicate phone numbers gracefully.

──────────────────────────────

## 🗂 Data Structure

- **`Contact` class** → stores:
  - Full Name
  - Nickname
  - Phone Number
  - Email
  - Job Information
- **`TreeNode` class** → represents each digit node in the Trie.
- **`PhoneNumberTree` class** → manages insert, search, update, and delete operations.

──────────────────────────────

## 📊 Features

### ➕ Insert
Adds a new phone number with its associated contact details.

### 🔍 Search
Looks up and returns the contact for a given phone number.

### ✏️ Update
Replaces the stored contact details for an existing number.

### ❌ Delete
Removes the contact and prunes unused nodes in the Trie.

──────────────────────────────

## 🧩 Technologies Used

- Python 3.x  
- Object-Oriented Programming (OOP)  
- Data Structure: **Trie / Prefix Tree**  
- Standard Python Collections

──────────────────────────────

## 🚀 How to Run

1. Run the script:
```bash
python Phone_Directory.py
```

2. The example usage in `main` demonstrates:
   - Inserting sample contacts
   - Searching for existing and missing numbers
   - Updating a contact
   - Deleting a contact

──────────────────────────────

## 📈 Sample Output

```
Insert done.

Search successful: Name: Ali Yas (Ali)
Phone: 09121139567
Email: aliyas@yahoo.com
Job: Software Engineer

Search failed: Contact not found

Update successful: Name: Ali Yas (Ali)
Phone: 09121139567
Email: aliyas@yahoo.com
Job: Senior Engineer

Delete successful: Contact removed

New contact found: Name: Elise Anderson (Elise)
Phone: 09178754921
Email: el.anderson@gmail.com
Job: DevOps Engineer
```

──────────────────────────────

## 🎯 Learning Outcomes

- Implementing a **Trie** for efficient key-based lookups.
- Using **OOP** principles to organize related data and behavior.
- Building **CRUD** (Create, Read, Update, Delete) operations in Python.
- Understanding **node-based data storage** for optimal search speed.
