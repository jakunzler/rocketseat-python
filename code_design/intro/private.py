class MyClass:
    
    def methodo_1(self) -> None:
        print("methodo_1")
        self.__methodo_2()
        
    def __methodo_2(self) -> None:
        print("methodo_2")
        

obj = MyClass()
obj.methodo_1()
# obj.__methodo_2