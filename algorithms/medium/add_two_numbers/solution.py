# Definition for singly-linked list node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        """
        Initialize a linked list node.
        :param val: Value of the node (default is 0).
        :param next: Reference to the next node (default is None).
        """
        self.val = val  # The value stored in this node
        self.next = next  # The reference to the next node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by two linked lists in reverse order.
        
        :param l1: ListNode - First linked list
        :param l2: ListNode - Second linked list
        :return: ListNode - The sum as a new linked list
        """
        
        # Step 1: Initialize a dummy node to start the result linked list
        dummy = ListNode(0)  # Placeholder node to start building the result
        current = dummy      # Pointer to add new nodes to the result
        carry = 0            # Carry starts at 0, as no addition has happened yet
        
        # Step 2: Traverse the linked lists until both are done and there's no carry
        while l1 or l2 or carry:
            # Step 3: Extract the current digit from each list, or use 0 if the list has no more nodes
            val1 = l1.val if l1 else 0  # If l1 is not None, use l1.val; otherwise, use 0
            val2 = l2.val if l2 else 0  # If l2 is not None, use l2.val; otherwise, use 0

            # Step 4: Add the two digits along with any carry from the previous step
            total = val1 + val2 + carry  # Total sum of current digits and carry
            carry = total // 10          # Update carry for the next step (e.g., 15 -> carry = 1)
            value = total % 10           # The digit to store in the current node (e.g., 15 -> value = 5)

            # Step 5: Create a new node with the calculated value and attach it to the result
            current.next = ListNode(value)
            current = current.next  # Move the pointer to the new node

            # Step 6: Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Step 7: Return the result list, skipping the dummy node
        return dummy.next


# Helper functions for testing the solution
def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    :param values: List[int] - A list of integers representing node values.
    :return: ListNode - The head of the linked list.
    """
    dummy = ListNode(0)  # Dummy node to simplify list creation
    current = dummy
    for value in values:
        current.next = ListNode(value)  # Create a new node and attach it
        current = current.next
    return dummy.next  # Return the head of the list (skipping the dummy node)


def print_linked_list(node):
    """
    Helper function to print the linked list in a readable format.
    :param node: ListNode - The head of the linked list.
    """
    while node:
        print(node.val, end=" -> ")  # Print the value of each node
        node = node.next
    print("NULL")


# Example Usage:
if __name__ == "__main__":
    # Test case 1: l1 = [2, 4, 3], l2 = [5, 6, 4]
    l1 = create_linked_list([2, 4, 3])  # Represents 342
    l2 = create_linked_list([5, 6, 4])  # Represents 465
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)  # Expected output: 7 -> 0 -> 8
    
    print("Result of adding two numbers:")
    print_linked_list(result)
