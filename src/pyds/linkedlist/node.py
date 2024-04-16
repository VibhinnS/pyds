from __future__ import annotations
from typing import TypeVar, Any
from dataclasses import dataclass
Type = TypeVar("Type")


@dataclass(slots=True)
class SLLNode:
    """
    Use SLLNode(integer argument) to implement to head node of the singly linked list. Add new nodes by using head.next = SLLNode(integer argument)."""
    data: Any
    next: SLLNode | None = None
    
       
@dataclass(slots=True)    
class DLLNode:
    """
    Use DLLNode(integer argument) to implement to head node of the doubly linked list. Add new nodes by using head.next = DSLLNode(integer argument). Connect new nodes to previous ones by new_node.prev = previous_node.
    """
    data: Any
    prev: DLLNode | None = None
    next: DLLNode | None = None
        

@dataclass(slots=True)
class TreeNode:
    """
    Use TreeNode(integer argument) to implement to root node of the binary tree.
    Use root.left and root.right for adding further nodes.
    """
    data: Any
    left: TreeNode | None = None
    right: TreeNode | None = None
       

@dataclass(slots=True)  
class GraphNode:
    """
    Use GraphNode(integer argument) to implement to head node of the graph. Add new nodes by using head.next = GraphNode(integer argument). Connect new nodes to previous ones by new_node.prev = previous_node.
    """
    visited: bool 
    adjacency_list: list[int]
    data: Any
    next: GraphNode | None = None
    