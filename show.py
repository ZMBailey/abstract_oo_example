from abc import ABC, abstractmethod

class Show(ABC):

        def __init__(self):
            self.cast = []
            self.add_performers()

        def add_performers(self):
            for _ in range(4):
                self.cast.append(self.get_performer())

        @abstractmethod
        def get_performer(self):
            pass


class Play(Show):
        
        def get_performer(self):
            return Actor()


class Concert(Show):
        def get_performer(self):
            return Musician()



class Performer(ABC):
    
    def perform(self):
           pass


class Actor(Performer):
     
    def perform(self):
        print("The play's the thing!")


class Musician(Performer):

    def perform(self):
        print("Music!")

