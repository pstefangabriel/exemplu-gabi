from domain.SefPromotieDTO import SefPromotieDTO
class ServiceMaterii:
    
    
    def __init__(self, validator_materie, repo_materii):
        self.__validator_materie = validator_materie
        self.__repo_materii = repo_materii
    
    



class ServiceNote:
    
    
    def __init__(self, validator_nota, repo_note, repo_studenti, repo_materii):
        self.__validator_nota = validator_nota
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_materii = repo_materii
    

    def __calculeaza_medii(self, note):
        medii = {}
        for nota in note:
            id_student = nota.get_student().get_id_student()
            if id_student not in medii:
                medii[id_student] = [0,0]
            medii[id_student][0] += nota.get_valoare()
            medii[id_student][1] += 1
        return medii
    
    def sefi_promotie(self,k):
        note = self.__repo_note.get_all()
        medii = self.__calculeaza_medii(note)
        result = []
        for id_student in medii:
            nume_student = self.__repo_studenti.cauta_dupa_id(id_student)
            medie = medii[id_student][0]/medii[id_student][1]
            sef_promotie_dto = SefPromotieDTO(id_student,nume_student,medie)
            result.append(sef_promotie_dto)
        result.sort(key = lambda x : x.get_medie(),reverse = True)
        return result[:k]
            



class ServiceStudenti:
    
    
    def __init__(self, validator_student, repo_studenti):
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti
    
    



