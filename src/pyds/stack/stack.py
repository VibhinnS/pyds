from __future__ import annotations
from typing import Generic, TypeVar
from pyds.linkedlist.node import SLLNode
Type = TypeVar("Type")




class AStack(Generic[Type]):
    """
    Array based stack. Allows only Memory efficient, but O(n) for worst case insertion and deletion.
    """
    
    def __init__(self, data_type, size: int = 5):
        """By default stack size set to 5. Add the size in argument if needed"""
        self.__stack: list[Type] = []
        self.size = size
        self.data_type = data_type
        
    def __bool__(self) -> bool:
        return bool(self.__stack)
    
    
    def __str__(self) -> str:
        return str(self.__stack)
    
    def __iter__(self):
        return iter(self.__stack)
    
    def push(self, data: Type) -> None:
        if not isinstance(data, self.data_type):
            raise TypeError(f"Data type must be {self.data_type}")        
        if len(self.__stack) >= self.size:
            raise StackOverFlowError("Stack is full")
        self.__stack.append(data)
        
        
    def pop(self):
        if len(self.__stack) == 0:
            raise StackUnderFlowError("Stack is empty")
        return self.__stack.pop()
    
    def peek(self) -> Type:
        if not self.__stack:
            raise StackUnderFlowError("Stack is empty")
        return self.__stack[-1]
    
    def empty(self) -> bool:
        """
        Checks if stack is empty or not.
        """
        return not bool(self.__stack)
    
    def search(self, data: Type) -> int:
        """
        Returns 1 based index of the element. If element is not found, returns -1
        """
        try:
            return self.__stack.index(data) + 1
        except ValueError:
            return -1
    
    




class LLStack(Generic[Type]):
    """
    Linked List based stack. O(1) for worst case insertion and deletion, but memory inefficient.
    """

    def __init__(self, data_type, size:int = 5):
        """
        By default stack size set to 5. Add the size in argument if needed
        """
        self.top:SLLNode | None = None
        self.data_type = data_type
        self.size = size
        
    
    def __iter__(self):
        current_node = self.top
        while current_node:
            yield current_node.data
            current_node = current_node.next
            
    def __str__(self):
        return "->".join([str(i) for i in self])
    
    def __len__(self):
        return sum([1 for _ in self])
    
    def push(self, value: Type) -> None:
        if not isinstance(value, self.data_type):
            raise TypeError(f"Data type must be {self.data_type}")
        
        if len(self) >=  self.size:
            raise StackOverFlowError("Stack is full")
        
        new_node:SLLNode = SLLNode(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
    def pop(self) -> Type:
        if len(self) == 0 or not self:
            raise StackUnderFlowError("Stack is empty")
        assert isinstance(self.top, SLLNode)
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data
    
    def peeK(self) -> Type:
        if len(self) == 0 or not self:
            raise StackUnderFlowError("Stack is empty")
        assert self.top is not None
        return self.top.data
    
    def clear(self) -> None:
        self.top = None
    
    
class StackOverFlowError(BaseException):
    pass

class StackUnderFlowError(BaseException):
    pass
