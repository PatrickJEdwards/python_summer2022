# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:42:25 2022

@author: edwar
"""

## OVERVIEW.
### 1.  __init__(self, value)
### 2.  length(self)
### 3.  addNode(self, new_value)
### 4.  addNodeAfter(self, new_value, after_node)
### 5.  addNodeBefore(self, new_value, before_node)
### 6.  removeNode(self, node_to_remove)
### 7.  removeNodesByValue(self, value)
### 8.  reverse(self)
### 9.  __str(self)__
### 10. hasCycle(self)

# TASKS/STEPS.
#%% Pre_1. Starter definition for `Node` class.
class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)


#%%
class LinkedList():

### 1.  __init__(self, value). (FINISHED!)
#####   Computational Complexity. O(1)
#####   Creating the list/initial node takes the same amount of time no matter how long the list will grow. 
#####   Thus, this function is constant over time.
    def __init__(self, value = None):
        # Require value to only be integer.
        if not ((value is None) or isinstance(value, int)):
            raise Exception("ERROR! Input `value` must be integer or None")
        self.head_node = Node(_value = value)
        self.num_nodes = 1
    
### 2.  length(self): (FINISHED!)
#####   Computational Complexity. O(1) (I think?)
#####   I included a list size/length ticker in all the other functions addings/removing nodes.
#####   As a result, this function remains the same no matter the length of the list. 
#####   It thus has constant time.
    def length(self):
        length = self.num_nodes
        return length

### 3.  addNode(self, new_value). [FINISHED!]
#####   Computational Complexity. O(n)
#####   This function must 'traverse' the entire list one node at a time to add a new tail node.
#####   Because 'traversing' the list requires linearly increasing computational energy as the list grows longer,
#####   this function requires linearly increasing time.
    def addNode(self, new_value):
        # Create error if new_value isn't integer.
        if not isinstance(new_value, int):
            raise Exception("ERROR! Input `new_value` must be integer or None")
        self.num_nodes += 1 # Update for length function.
        added_node = Node(_value = new_value) # Create new node.
        # STRATEGY. use loop to move down linked list until we reach the tail, then add next node.
        node_iteration = self.head_node
        while node_iteration.next != None:
            node_iteration = node_iteration.next # Moves down linked list until last node.
        node_iteration.next = added_node # Adds node to end of linked list.

### 4.  addNodeAfter(self, new_value, after_node): [FINISHED!]
#####   Computational Complexity. O(n).
#####   Like the addNode function, this function 'traverses' the list one node at a time until it reaches the desired node.
#####   For the same reason, this function requires linearly increasing time.
    def addNodeAfter(self, new_value, after_node):
        # Create error if 'after_node' isn't integer.
        if not isinstance(after_node, int):
            raise Exception("ERROR! Input `after_node` must be integer or None")
        # Creates error if after_node integer is longer than the linked list itself.
        if after_node > self.num_nodes:
            raise Exception("ERROR! Input `after_node` specifies a node that doesn't exist! The linked list is not that long.")
        # Create error if new_value isn't integer.
        if not isinstance(new_value, int):
            raise Exception("ERROR! Input `new_value` must be integer or None")
        # Run `addNode` function if the node specified by `after_node` is the last one.
        # This simply adds the new node onto the end of the linked list.
        if after_node == self.num_nodes:
            self.addNode(new_value)
        # STRATEGY: use 'while' loop to 'traverse' list to node, then add node afterwards.
        else:
            node_iterate = self.head_node
            iteration_counter = 1
            # When we reach after_node #, while loop breaks.
            while iteration_counter < after_node:
                iteration_counter += 1
                node_iterate = node_iterate.next
            # Attach node following after_node to next of new_node.
            tempnode = node_iterate.next
            # Create new node with tempnode (previously after_node's next node) as next node.
            node_iterate.next = Node(new_value, tempnode)
            # Update for length function.
            self.num_nodes += 1

### 5.  addNodeBefore(self, new_value, before_node). [FINISHED]
#####   Computational Complexity. O(n).
#####   This function is basically a slight modification to the 'addNodeAfter' function.
#####   For the same reason, it requires linearly increasing time.
    def addNodeBefore(self, new_value, before_node):
        # Create error if new_value isn't integer.
        if not isinstance(new_value, int):
            raise Exception("ERROR! Input `new_value` must be integer or None")
        # STRATEGY: I'm basically repeating adNodeafter but tweaking it.
        # Create error if 'before_node' isn't integer.
        if not isinstance(before_node, int):
            raise Exception("ERROR! Input `before_node` must be integer or None")
        # Creates error if before_node integer is longer than the linked list itself.
        if before_node > self.num_nodes:
            raise Exception("ERROR! Input `before_node` specifies a node that doesn't exist! The linked list is not that long.")
        # Check if before_node = 1, i.e., the head node.
        if before_node == 1:
            oldhead = self.head_node
            self.head_node = Node(new_value, oldhead)
            self.num_nodes += 1
        # STRATEGY: use 'while' loop to 'traverse' list to node just before specified one, then add node beforehand.
        else:
            node_iterate = self.head_node
            iteration_counter = 2 # Only crucial difference.
            # When we reach after_node #, while loop breaks.
            while iteration_counter < before_node:
                iteration_counter += 1
                node_iterate = node_iterate.next
            # Attach node following before_node to next of new_node.
            tempnode = node_iterate.next
            # Create new node with tempnode (previously before_node's next node) as next node.
            node_iterate.next = Node(new_value, tempnode)
            # Update for length function.
            self.num_nodes += 1
        
### 6.  removeNode(self, node_to_remove): [FINISHED!]
#####   Computational Complexity. O(n)
#####   This function traverses every node until it reaches the one that's to be removed.
#####   For the same reason as the last several functions, this one has linearly increasing time.
    def removeNode(self, node_to_remove):
        # Standard error messages blah blah blah.
        if not isinstance(node_to_remove, int):
            raise Exception("ERROR! Input `node_to_remove` must be integer or None")
        if node_to_remove < 1 or node_to_remove > self.num_nodes:
            raise Exception("ERROR! Input 'node_to_remove' is out of bounds. It doesn't correspond to an existing node.")
        # Remove first node if node_to_remove = 1.
        if node_to_remove == 1:
            self.head_node = self.head_node.next
        # Make while loop that traverses list until node just before one to remove.
        else:
            node_ticker = 1
            node_iterate = self.head_node
            while node_ticker < node_to_remove - 1:
                node_iterate = node_iterate.next
                node_ticker += 1
            # Map out the nodes before and after the one being removed.
            prev_node = node_iterate
            soon_removed_node = prev_node.next
            subsequent_node = soon_removed_node.next
            # "Unlink" the to-be-removed node by setting the prev_node's next node as the subsequent_node.
            prev_node.next = subsequent_node 
            # Voila! 
        self.num_nodes -= 1 # Update for length function.

### 7.  removeNodesByValue(self, value): [FINISHED!]
#####   Computational Complexity. O(n).
#####   This function uses pointers to 'traverse' the function removing nodes that contain the specified value when it finds them.
#####   Since it goes through nodes one at a time, I think it uses linear time
    def removeNodesByValue(self, value):
        ## NEEDS self.num_nodes FUNCTIONALITY.
        # Create error if value isn't integer.
        if not isinstance(value, int):
            raise Exception("ERROR! Input `new_value` must be integer or None")
        # Remove if value in head_node.
        if self.head_node.value == value:
            self.head_node = self.head_node.next
            self.num_nodes -= 1
        # Check if tail has value.    
        current_it = self.head_node
        prior_it = None
        while current_it.next != None:
            prior_it = current_it
            current_it = current_it.next
        if current_it.value == value:
            prior_it.next = None
            self.num_nodes -= 1
        # STRATEGY: continue looking with a while loop.
        current_it = self.head_node
        while current_it.next != None:
            if current_it.next.value == value:
                removable_node = current_it.next 
                # Remove if next node is tail.
                if removable_node.next != None:
                    subsequent_node = removable_node.next
                    current_it.next = subsequent_node
                    self.num_nodes -= 1
            current_it = current_it.next
        
### 8.  reverse(self): [FINISHED!]
#####   Computational Complexity. O(n)
#####   This function 'traverses' the list one node at a time and reverses their connection to the other nodes.
#####   Because the computational effort increases linearly with increasing list size, this function requires linear time.
    def reverse(self):
        # STRATEGY: go down the linked list and switch all nodes around so that their prior node is now their next node.
        ########### KEEP TRACK of prior, present, and subsequent nodes.
        prior_node = None
        current_node = self.head_node
        # Run for-loop that gathers 'subsequent_node' information, then switched 'current_node' to have 'prior_node' as next value.
        while current_node != None: # This occurs after the tail node.
            # Capture subsequent_node information.
            subsequent_node = current_node.next 
            # Flip the current_node's 'next' argument around so that now 'prior_node' is the 'next' node in the list.
            current_node.next = prior_node
            # Finally, update prior_node and current_node information to continue 'traversing' original list.
            prior_node = current_node
            current_node = subsequent_node
        # For full reversal, the tail node has to be the head node.
        ## The 'tail' node is now the prior_node. This is because the current_node is empty as there was no subsequent_node.
        ## So set this as the list's head_node
        self.head_node = prior_node
        # This should've completely flipped around the list.

### 9.  __str(self)__. [FINISHED]
#####   Computational Complexity. O(n).
#####   As with the others, this function traverses the list one node at a time. 
#####   Thus, it's computational complexity increases linearly with the size of the list.
    def __str__(self):
        # STRATEGY: start at head, then gather node information in while loop.
        # Start print statement.
        list_string = "Singly Linked List:\n"
        node_counter = 0 # Starting with head node
        # Create object that 'traverses' down list.
        node_iterate = self.head_node
        # Create while loop that pushed 'node_iterate' down list and scoops up printable information.
        while node_iterate is not None:
            node_counter += 1
            list_string += f"Node {node_counter}: {node_iterate.value}\n"
            node_iterate = node_iterate.next # Moves down linked list until last node.
        return list_string




#%%
# TESTING GROUND.

# 1. Initialization.
testlist = LinkedList(5) # Runs
type(testlist)
dir(testlist)
# Check errors.
LinkedList(5.5) # Fails
LinkedList([5]) # Fails
LinkedList({5:5}) # Fails

# 2. Return length of list.
testlist.length() # Works properly.

# 3. Test adding node to end of list.
testlist.addNode(12)
testlist.length() # Now 2 nodes.
testlist.head_node.value # Correct, 5.
testlist.head_node.next.value # Correct, 12.
# Check errors.
testlist.addNode(12.5) # Fails.
testlist.addNode([12]) # Fails.
testlist.addNode({12:12}) # Fails.

# 4. Check addNodeAfter.
testlist = LinkedList(1)
testlist.addNode(2)
testlist.addNodeAfter(3, 2)
testlist.addNodeAfter(100, 2)
testlist.addNodeAfter(50, 1)
print(testlist) #WORKS!
testlist.length()

# 5. check addNodeBefore.
testlist = LinkedList(1)
testlist.addNode(2)
testlist.addNodeAfter(3, 2)
testlist.addNodeBefore(100, 1)
print(testlist) 
testlist.length()

# 6. Check removeNode.
testlist = LinkedList(1)
testlist.addNode(2)
testlist.addNodeAfter(3, 2)
testlist.addNodeBefore(100, 1)
testlist.removeNode(1)
testlist.removeNode(3)
print(testlist) 
testlist.length()

# 7. Check removeNodesByValue.
testlist = LinkedList(1)
testlist.addNode(2)
testlist.addNodeAfter(4, 2)
testlist.addNodeBefore(3, 3)
testlist.addNode(5)
testlist.addNode(2)
testlist.addNode(5)
testlist.removeNodesByValue(1) # Removes head node.
testlist.removeNodesByValue(2) # Removes from middle
testlist.removeNodesByValue(5)
print(testlist) 
testlist.length()

# 8. Check/test reverse function.
testlist = LinkedList(1)
testlist.addNode(2)
testlist.addNodeAfter(4, 2)
testlist.addNodeBefore(3, 3)
testlist.addNode(5)
testlist.reverse()
print(testlist)  # WORKS!
testlist.length()


# 9. Test print statement
testlist = LinkedList(5) # Add a couple nodes.
testlist.addNode(12)
testlist.addNodeAfter(5, 3)


print(testlist)
