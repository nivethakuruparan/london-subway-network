from abc import ABC, abstractmethod 

class PathFinder(ABC):
    @abstractmethod 
    def get_path(self, graph, starting_station:str, ending_station:str):
        pass
