from erori.exceptii import ValidError,RepoError,UiError
class Console:
    
    
    def __ui_sefi_promotie(self,params):
        if len(params)!=1:
            raise UiError("nr params invalid!")
        try:
            k = int(params[0])
            sefi_promotie = self.__service_note.sefi_promotie()
            if len(sefi_promotie)==0:
                print("nu exista studenti!")
                return
            for sef_promotie in sefi_promotie:
                print(sef_promotie)
        except ValueError:
            raise UiError("valoare numerica invalida!")
        
    
    def __init__(self, service_studenti, service_materii, service_note):
        self.__service_studenti = service_studenti
        self.__service_materii = service_materii
        self.__service_note = service_note
        self.__comenzi = {
            "sefi_promotie":self.__ui_sefi_promotie
            }

    
    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return 
            parts = comanda.split()
            nume_comanda = parts[0]
            params = parts[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](params)
                except ValidError as ve:
                    print(f"valid error:{ve}")
                except RepoError as re:
                    print(f"repo error:{re}")
                except UiError as ue:
                    print(f"ui error: {ue}")
            else:
                print("comanda invalida!")
            
    
    
    
    



