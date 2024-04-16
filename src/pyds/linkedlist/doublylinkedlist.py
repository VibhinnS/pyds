from __future__ import annotations
from .node import DLLNode
from typing import Generic, TypeVar, Any

class DoublyLL:
    def __init__(self):
        self.head: DLLNode | None = None
        
    def __iter__(self) -> Any:
        node = self.head
        while node:
            yield node.data
            node = node.next
            
    def __len__(self) -> int:
        return sum(1 for _ in self)
    
    def __str__(self)-> str:
        return "<->".join(str(i) for i in self)
    
    def add(self, data: Any) -> None:
        """Append at the list end"""
        if self.head is None:
            self.head = DLLNode(data)
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = DLLNode(data)
        current.next.prev = current
        
    
    def addAtPosition(self, data: Any, position: int):
        """Append at specified position of the list. Provide position as 0 based indexing."""
        if position < 0:
            raise ValueError("Position cannot be negative")
        
        if position == 0:
            self.addFirst(data)
            return
        
        current = self.getNodeAtPosition(position - 1)
        self.insertAfterNode(current, data)
            
    def getNodeAtPosition(self, position: int) -> DLLNode | None:
        current = self.head
        for _ in range(position):
            if current is None or current.next is None:
                raise IndexError("Can't Add! Index out of range")
            current = current.next
        return current
    
    def insertAfterNode(self, node: DLLNode | None, data: Any):
        new_node = DLLNode(data)
        if node:
            new_node.next = node.next
            new_node.prev = node
            if node.next:
                node.next.prev = new_node
            node.next = new_node
        
    def addFirst(self, data: Any):
        """Add at first position of the list"""
        new_head = DLLNode(data)
        new_head.next = self.head
        if self.head:
            self.head.prev = new_head
        self.head = new_head
        
    
    def clear(self):
        """Clears the list."""
        self.head = None
        
    
    def copy(self):
        """Makes a list copy and return new object"""
        new_list = DoublyLL()
        for element in self:
            new_list.add(DLLNode(element))
        return new_list
    
    def delete(self, value: Any):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
