from typing import Generic, TypeVar
Type = TypeVar("Type")



class Queue(Generic[Type]):
    """
    Array based queue. Allows only Memory efficient, but O(n) for worst case insertion and deletion.
    """
    
    def __init__(self, data_type, size):
        """Circular Buffer based Queue implementation. Size cannot be changed dynamically"""
        self.__queue: list[Type] = []
        self.size = size
        self.data_type = data_type
        self.front = 0
        self.rear = 0
        
    def __bool__(self) -> bool:
        return bool(self.__queue)
    
    
    def __str__(self) -> str:
        return str(self.__queue)
    
    def __iter__(self):
        return iter(self.__queue)
    
    def add(self, data: Type) -> None:
        if not isinstance(data, self.data_type):
            raise TypeError(f"Data type must be {self.data_type}")
        if (self.rear + 1) % self.size == self.front:
            raise Exception("Can't add. Size exceeds the defiend Queue size.")
        
        self.__queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size        
        
    def remove(self):
        if self.front == self.rear:
            raise Exception("Queue is empty")
        
        data = self.__queue[self.front]
        self.front = (self.front + 1) % self.size
        return data    
        
    def empty(self) -> bool:
        """
        Checks if queue is empty or not.
        """
        return not bool(self.__queue)
    
    def search(self, data: Type) -> int:
        """
        Returns 1 based index of the element. If element is not found, returns -1
        """
        try:
            return self.__queue.index(data) + 1
        except ValueError:
            return -1
