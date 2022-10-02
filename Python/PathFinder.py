from abc import ABC, abstractmethod 

class PathFinder(ABC):
    @abstractmethod 
    def get_path(self, path_query):
        pass
