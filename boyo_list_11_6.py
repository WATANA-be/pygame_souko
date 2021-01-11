class Commander:
    __counter = 0
    def __init__(self, name: str) -> None:

        self.__name = name
        Commander.__counter += 1
        self.__id = Commander.__counter
    def id(self) -> int:
        return self.__id

    def max_id(cls) -> int:
        return cls.__counter
    def print(self) ->  None:
        print("{}:{}番".format(self.__name, self.__id))

    