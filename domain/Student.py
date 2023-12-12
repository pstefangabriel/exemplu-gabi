class Student:
    def __init__(self,__id_student,__nume):
        self.__id_student = __id_student
        self.__nume = __nume

    def get_id_student(self):
        return self.__id_student


    def get_nume(self):
        return self.__nume


    def set_nume(self, value):
        self.__nume = value
