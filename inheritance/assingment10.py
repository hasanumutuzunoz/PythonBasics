from abc import ABC, abstractmethod

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

# click() method is not implemented, this is an abstract class, we cannot initialize
class HP(TouchScreenLaptop):

    def scroll(self):
        print("HP Scroll On")

# click() method is not implemented, this is an abstract class
class DELL(TouchScreenLaptop):

    def scroll(self):
        print("DELL Scroll On")

class HPNotebook(HP):

    def click(self):
        print("HP Notebook Click")

class DELLNotebook(DELL):

    def click(self):
        print("DELL Notebook Click")


HPNotebook = HPNotebook()
HPNotebook.click()
HPNotebook.scroll()

DELLNotebook = DELLNotebook()
DELLNotebook.click()
DELLNotebook.scroll()