from __future__ import annotations
from typing import Generic, TypeVar, Any
from dataclasses import dataclass
from .node import SLLNode
Type = TypeVar("Type")


class SinglyLL(Generic[Type]):
    def __init__(self):
        self.head: SLLNode | None = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
        
    def __len__(self):
        return sum(1 for _ in self)
    
    def __str__(self) -> str:
        return "->".join(str(i) for i in self)
    
    def add(self, data: Type):
        """Add at end of the list (append)"""
        if self.head is None:
            self.head = SLLNode(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = SLLNode(data)
        
    def addAtPosition(self, data: Type, position: int):
        """Append at specified position of the list. Provide position as 0 based indexing."""
        if position < 0:
            raise ValueError("Position cannot be negative")

        if position == 0:
            new_node:SLLNode = SLLNode(data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position):
            if current is None or current.next is None:
                raise IndexError("Can't add! Index out of range")
            current = current.next

        new_node = SLLNode(data)
        if current:
            current.next = new_node
            new_node.next = current.next
    
    def addFirst(self, data: Type):
        """Add at first position of the list"""
        new_head = SLLNode(data)
        new_head.next = self.head
        self.head = new_head
    
    def clear(self):
        """Clears the list"""
        self.head = None
    
    def copy(self):
        """Makes a copy of the list"""
        new_list = SinglyLL()
        for element in self:
            new_list.add(SLLNode(element))
        return new_list
    
    def get_head(self) -> Type:
        """Returns the data of the first element of the list"""
        if self.head is None:
            raise Exception("List is empty")
        return self.head.data
