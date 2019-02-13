class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back(self, val):
            if self.head == None:	# if the list is empty
                self.add_to_front(val)	# run the add_to_front method
            return self
            # let's make sure the rest of this function doesn't happen if we add to the front
            new_node = Node(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            return self



my_list = SList()
my_list.add_to_front("Are").add_to_front("I want this first").add_to_back("Thu coi").print_values()