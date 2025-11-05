import datetime
import time

class AVLNode:
    def __init__(self, flight_number, pilot_name, flight_time, passengers, source_city, destination_city):
        self.flight_number = flight_number
        self.pilot_name = pilot_name
        self.flight_time = flight_time
        self.passengers = passengers
        self.source_city = source_city
        self.destination_city = destination_city
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, flight_number, pilot_name, flight_time, passengers, source_city, destination_city):
        if not node:
            return AVLNode(flight_number, pilot_name, flight_time, passengers, source_city, destination_city)

        if flight_number < node.flight_number:
            node.left = self.insert(node.left, flight_number, pilot_name, flight_time, passengers, source_city, destination_city)
        elif flight_number > node.flight_number:
            node.right = self.insert(node.right, flight_number, pilot_name, flight_time, passengers, source_city, destination_city)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and flight_number < node.left.flight_number:
            return self.rotate_right(node)
        if balance < -1 and flight_number > node.right.flight_number:
            return self.rotate_left(node)
        if balance > 1 and flight_number > node.left.flight_number:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and flight_number < node.right.flight_number:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def add_flight(self, flight_number, pilot_name, flight_time, passengers, source_city, destination_city):
        self.root = self.insert(self.root, flight_number, pilot_name, flight_time, passengers, source_city, destination_city)

    def search_flight(self, node, flight_number):
        if not node or node.flight_number == flight_number:
            return node
        if flight_number < node.flight_number:
            return self.search_flight(node.left, flight_number)
        return self.search_flight(node.right, flight_number)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"Flight Number: {node.flight_number}, Pilot: {node.pilot_name}, Time: {node.flight_time}, "
                  f"Passengers: {node.passengers}, From: {node.source_city}, To: {node.destination_city}")
            self.inorder_traversal(node.right)

    def flights_to_destination(self, node, destination):
        flights = []
        if node:
            flights += self.flights_to_destination(node.left, destination)
            if node.destination_city == destination:
                flights.append(f"Flight Number: {node.flight_number}, Pilot: {node.pilot_name}, "
                               f"Time: {node.flight_time}, Passengers: {node.passengers}, "
                               f"From: {node.source_city}, To: {node.destination_city}")
            flights += self.flights_to_destination(node.right, destination)
        return flights

    def find_max_passengers(self, node):
        if not node:
            return None
        max_flight = node
        left_max = self.find_max_passengers(node.left)
        right_max = self.find_max_passengers(node.right)
        if left_max and left_max.passengers > max_flight.passengers:
            max_flight = left_max
        if right_max and right_max.passengers > max_flight.passengers:
            max_flight = right_max
        return max_flight

    def delete(self, node, flight_number):
        if not node:
            return node

        if flight_number < node.flight_number:
            node.left = self.delete(node.left, flight_number)
        elif flight_number > node.flight_number:
            node.right = self.delete(node.right, flight_number)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.get_min_node(node.right)
            node.flight_number = temp.flight_number
            node.pilot_name = temp.pilot_name
            node.flight_time = temp.flight_time
            node.passengers = temp.passengers
            node.source_city = temp.source_city
            node.destination_city = temp.destination_city
            node.right = self.delete(node.right, temp.flight_number)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

if __name__ == "__main__":
    tree = AVLTree()
    initial_flights = [
        (101, "Captain A", "10:00 AM", 150, "Tehran", "Mashhad"),
        (102, "Captain B", "12:00 PM", 200, "Isfahan", "Tabriz"),
        (103, "Captain C", "02:00 PM", 180, "Shiraz", "Tehran"),
        (104, "Captain D", "06:00 AM", 50, "Tehran", "Tabriz"),
    ]
    for flight in initial_flights:
        tree.add_flight(*flight)
    print("Initial flights added successfully.")

    while True:
        print("\nMenu:")
        print("1. Add a flight")
        print("2. Display all flights (sorted by flight number)")
        print("3. Update flight time")
        print("4. Display flights to a specific destination")
        print("5. Display flight with the most passengers")
        print("6. Delete a flight by flight number")
        print("7. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 7:
                    break
                print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if choice == 1:
            while True:
                try:
                    flight_number = int(input("Enter flight number: "))
                    break
                except ValueError:
                    print("Invalid input. Flight number must be a number.")
            while True:
                pilot_name = input("Enter pilot name: ")
                if pilot_name.strip() and all(c.isalpha() or c.isspace() for c in pilot_name):
                    break
                print("Invalid input. Please enter a valid pilot name.")
            while True:
                flight_time = input("Enter flight time (e.g., 10:00 AM): ")
                try:
                    datetime.datetime.strptime(flight_time, "%I:%M %p")
                    break
                except ValueError:
                    print("Invalid input. Flight time must be in the format HH:MM AM/PM.")
            while True:
                try:
                    passengers = int(input("Enter number of passengers: "))
                    if passengers > 0:
                        break
                    print("Number of passengers must be greater than zero.")
                except ValueError:
                    print("Invalid input. Number of passengers must be a number.")
            while True:
                source_city = input("Enter source city: ")
                if source_city.strip().isalpha():
                    break
                print("Invalid input. Please enter a valid city name.")
            while True:
                destination_city = input("Enter destination city: ")
                if destination_city.strip().isalpha():
                    break
                print("Invalid input. Please enter a valid city name.")

            tree.add_flight(flight_number, pilot_name, flight_time, passengers, source_city, destination_city)
            print("Flight added successfully.")

        elif choice == 2:
            print("All Flights:")
            tree.inorder_traversal(tree.root)

        elif choice == 3:
            while True:
                try:
                    flight_number = int(input("Enter flight number to update time: "))
                    break
                except ValueError:
                    print("Invalid input. Flight number must be a number.")
            flight = tree.search_flight(tree.root, flight_number)
            if flight:
                while True:
                    new_time = input("Enter new flight time (e.g., 10:00 AM): ")
                    try:
                        datetime.datetime.strptime(new_time, "%I:%M %p")
                        flight.flight_time = new_time
                        print("Flight time updated.")
                        break
                    except ValueError:
                        print("Invalid input. Flight time must be in the format HH:MM AM/PM.")
            else:
                print("Flight not found.")

        elif choice == 4:
            while True:
                destination = input("Enter destination city: ")
                if destination.strip().isalpha():
                    break
                print("Invalid input. Please enter a valid city name.")
            flights = tree.flights_to_destination(tree.root, destination)
            if flights:
                print(f"Flights to {destination}:")
                for flight in flights:
                    print(flight)
            else:
                print(f"No flights found to the destination {destination}.")

        elif choice == 5:
            max_flight = tree.find_max_passengers(tree.root)
            if max_flight:
                print(f"Flight Number: {max_flight.flight_number}, Pilot: {max_flight.pilot_name}, "
                      f"Time: {max_flight.flight_time}, Passengers: {max_flight.passengers}, "
                      f"From: {max_flight.source_city}, To: {max_flight.destination_city}")
            else:
                print("No flights available.")

        elif choice == 6:
            while True:
                try:
                    flight_number = int(input("Enter flight number to delete: "))
                    break
                except ValueError:
                    print("Invalid input. Flight number must be a number.")
            flight = tree.search_flight(tree.root, flight_number)
            if flight:
                tree.root = tree.delete(tree.root, flight_number)
                print(f"Flight with number {flight_number} deleted successfully.")
            else:
                print(f"No flight found with the number {flight_number}.")

        elif choice == 7:
            print("Exiting...", end="")
            time.sleep(2)
            print("\rHave a nice day!")
            break
