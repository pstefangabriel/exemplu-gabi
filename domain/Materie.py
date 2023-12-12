class Materie:
    
    def __init__(self,__id_materie,__titlu):
        self.__id_materie = __id_materie
        self.__titlu = __titlu

    def get_id_materie(self):
        return self.__id_materie


    def get_titlu(self):
        return self.__titlu


    def set_titlu(self, value):
        self.__titlu = value
