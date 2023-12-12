class SefPromotieDTO:
    
    def __init__(self,id_student,nume_student,medie):
        self.__id_student = id_student
        self.__nume_student = nume_student
        self.__medie = medie

    def get_nume_student(self):
        return self.__nume_student


    def get_medie(self):
        return self.__medie

    def __str__(self):
        return f"[{self.__id_student}] {self.__nume_student} cu medie {self.__medie}. "
