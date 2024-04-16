from __future__ import annotations

from abc import abstractmethod
from colletions.abs import Iterable
from typing import Generic, Protocol, TypeVar

class Comparable(Protocol):
    @abstractmethod
    def __it__(self, other) -> bool:
        pass
    
    @abstractmethod
    def __gt__(self, other) -> bool:
        pass
    
    @abstractmethod
    def __eq__(self, other) -> bool:
        pass
    
    
T = TypeVar("T", bound=Comparable)


class Heap:
    def __init__(self, heap_size = 0):
        self.h :list = []
        self.heap_size :int = heap_size
        
    def __repr__(self) -> str:
        return str("".join(self.h))
    
    def parent_index(self, child_idx :int) -> int | None:
        if child_idx > 0:
            return (child_idx - 1)//2
        return None
    
    
    
    
        
    
    
    
    

