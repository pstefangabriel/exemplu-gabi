'''
Created on Dec 12, 2023

@author: stefan
'''
from teste.teste import Teste
from validatori.validare import ValidatorStudent,ValidatorMaterie,ValidatorNota
from persistenta.repository import RepoStudenti,RepoMaterie,RepoNote
from business.service import ServiceStudenti,ServiceMaterii,ServiceNote
from prezentare.ui import Console
if __name__ == '__main__':
    teste = Teste()
    teste.run_all_tests()
    
    validator_student = ValidatorStudent()
    validator_materie = ValidatorMaterie()
    validator_nota = ValidatorNota()
    
    repo_studenti = RepoStudenti()
    repo_materii = RepoMaterie()
    repo_note = RepoNote()
    
    service_studenti = ServiceStudenti(validator_student,repo_studenti)
    service_materii = ServiceMaterii(validator_materie,repo_materii)
    service_note = ServiceNote(validator_nota,repo_note,repo_studenti,repo_materii)
    
    ui = Console(service_studenti,service_materii,service_note)
    ui.run()
    