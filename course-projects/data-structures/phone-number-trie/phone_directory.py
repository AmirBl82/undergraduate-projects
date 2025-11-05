class Contact:
    def __init__(self, full_name, nickname, phone_number, email, job_info):
        self.full_name = full_name
        self.nickname = nickname
        self.phone_number = phone_number
        self.email = email
        self.job_info = job_info

    def __str__(self):
        return f"Name: {self.full_name} ({self.nickname})\nPhone: {self.phone_number}\nEmail: {self.email}\nJob: {self.job_info}"


class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False
        self.contact = None


class PhoneNumberTree:
    def __init__(self):
        self.root = TreeNode()
        self.root.children['0'] = TreeNode()
        self.root.children['0'].children['9'] = TreeNode()

    def insert(self, phone_number, contact):
        node = self.root
        for digit in phone_number:
            if digit not in node.children:
                node.children[digit] = TreeNode()
            node = node.children[digit]
        node.is_end_of_number = True
        node.contact = contact

    def search(self, phone_number):
        node = self.root
        for digit in phone_number:
            if digit not in node.children:
                return None
            node = node.children[digit]
        if node.is_end_of_number:
            return node.contact
        return None

    def update(self, phone_number, new_contact):
        node = self.root
        for digit in phone_number:
            if digit not in node.children:
                return False, "Phone number not found"
            node = node.children[digit]
        if node.is_end_of_number:
            node.contact = new_contact
            return True, "Contact updated successfully"
        return False, "Phone number not found"

    def delete(self, phone_number):
        def delete_helper(node, phone_number, depth):
            if depth == len(phone_number):
                if node.is_end_of_number:
                    node.is_end_of_number = False
                    node.contact = None
                    return not node.children
                return False
            digit = phone_number[depth]
            if digit in node.children and delete_helper(node.children[digit], phone_number, depth + 1):
                del node.children[digit]
                return not node.children and not node.is_end_of_number
            return False

        delete_helper(self.root, phone_number, 0)


tree = PhoneNumberTree()

contact1 = Contact("Ali Yas", "Ali", "09121139567", "aliyas@yahoo.com", "Software Engineer")
contact2 = Contact("Max Davies", "Max", "09132567980", "max.dave@outlook.com", "Cloud Developer")
contact3 = Contact("Elise Anderson", "Elise", "09178754921", "el.anderson@gmail.com", "DevOps Engineer")

tree.insert("09121139567", contact1)
tree.insert("09132567980", contact2)

print("\nInsert done.\n")

result = tree.search("09121139567")
if result:
    print("Search successful:", result)
else:
    print("Search failed: Contact not found")

result = tree.search("0000000000")
if result:
    print("Search successful:", result)
else:
    print("Search failed: Contact not found")

new_contact_info = Contact("Ali Yas", "Ali", "09121139567", "aliyas@yahoo.com", "Senior Engineer")
success, message = tree.update("09121139567", new_contact_info)
if success:
    print("\nUpdate successful:", tree.search("09121139567"))
else:
    print("\nUpdate failed:", message)

tree.delete("09132567980")
result = tree.search("09132567980")
if result:
    print("\nDelete failed: Contact still exists")
else:
    print("\nDelete successful: Contact removed")

tree.insert("09178754921", contact3)
result = tree.search("09178754921")
if result:
    print("\nNew contact found:", result)
else:
    print("\nNew contact not found")



