# class Stack:
#     def __init__(self):
#         self.stack = []

#     def insert(self, value):
#         self.stack.append(value)

#     def delete(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return "Stack is empty!"

#     def display(self):
#         if not self.is_empty():
#             print("Stack:", self.stack)
#         else:
#             print("Stack is empty!")

#     def is_empty(self):
#         return len(self.stack) == 0


# class Queue:
#     def __init__(self):
#         self.queue = []

#     def insert(self, value):
#         self.queue.append(value)

#     def delete(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             return "Queue is empty!"

#     def display(self):
#         if not len(self.queue) == 0:
#             print("Queue:", self.queue)
#         else:
#             print("Queue is empty!")

#     def is_empty(self):
#         return len(self.queue) == 0



class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, value):
        self.stack.append(value)

    def delete(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def display(self):
        if not self.is_empty():
            print("Stack:", self.stack)
        else:
            print("Stack is empty!")

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def display(self):
        if not self.is_empty():
            print("Queue:", self.queue)
        else:
            print("Queue is empty!")

    def is_empty(self):
        return len(self.queue) == 0

# -------> Common functions <---------


def insert_item(ob):
    value = input("Enter value to insert: ")
    ob.insert(value)
    print(f"{value} inserted.")

def delete_item(ob):
    result = ob.delete()
    print(f"Deleted: {result}")

def display_items(ob):
    ob.display()

def data_structure_menu(ob, ds_name):
    while True:
        print(f"\n{ds_name} Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Back")
        operation = input("Choose an operation (1/2/3/4): ")

        if operation == '1':
            insert_item(ob)
        elif operation == '2':
            delete_item(ob)
        elif operation == '3':
            display_items(ob)
        elif operation == '4':
            break
        else:
            print("Invalid operation!")
