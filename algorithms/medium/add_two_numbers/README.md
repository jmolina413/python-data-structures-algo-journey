# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in **reverse order**, and each node contains a single digit.  

Add the two numbers and return the sum as a **linked list**.

---

## Example 1:
**Input**:  
`l1 = [2, 4, 3]`  
`l2 = [5, 6, 4]`  

**Output**: `[7, 0, 8]`  

**Explanation**:  
342 + 465 = 807.

---

## Approach
1. Traverse both linked lists while handling **carry-over** values.  
2. Use a dummy node to build the result list.  
3. Add corresponding digits and manage the carry:
   - `total = val1 + val2 + carry`
   - `carry = total // 10`
   - `value = total % 10`
4. Continue until both lists are traversed and carry becomes `0`.

---

## Complexity
- **Time Complexity**: O(max(m, n))  
- **Space Complexity**: O(max(m, n))

---

## Python Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            value = total % 10
            
            current.next = ListNode(value)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next