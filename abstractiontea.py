from abc import ABC ,abstractmethod

class tea(ABC):

    @abstractmethod
    def ingri(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def serve(Self):
        pass

    def maketea(self):

        self.ingri()
        self.brew()
        self.serve()


class greentea(tea):

    def ingri(self):

        print("\n\t GREEN LEAVES AND WATER IS READY!")

    def brew(self):

        print("\n\t GREEN TEA IS BREWED!")

    def serve (self):

        print("\n\t GREEN TEA IS READY TO SERVE!")


class masalatea(tea):

    def ingri(self):

        print("\n\t MASALA AND WATER IS READY !")


    def brew(self):

        print("\n\t MASALA TEA IS BREWED!")

    def serve(self):
        print("\n\t MASALA TEA READY TO SERVE!")


def  main():

    Greentea=greentea()

    Greentea.maketea()

    Masalatea=masalatea()

    Masalatea.maketea()


if __name__== "__main__":
    main()
        



        
        
