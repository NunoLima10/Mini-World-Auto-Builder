
class Language:
    def __init__(self,language_id:str) -> None:
        defaut_language = "en" 
        self.language_id = language_id

        self.langues_data = {
        "en":self.en,
        "pt":self.pt
        }
        
        self.language_data = self.langues_data[defaut_language]
        if self.language_id in self.language_data:
            self.language_data = self.langues_data[self.language_id] 
    
    
    def get_languages_labels(self)-> list:
        return [self.langues_data[language]["Label"] for language in self.langues_data]

    def get_language_data(self)-> list:
        return self.language_data

    def change_language(self,language_Label:str)-> list:
        language_id = self.find_language_by_label(language_Label)

        if self.language_id == language_id: return self.language_data

        self.language_id = language_id  
        self.language_data = self.langues_data[language_id] 
        return self.language_data
        



    def find_language_by_label(self,language_Label:str)-> str:
        for language in self.langues_data:
            if self.langues_data[language]["Label"] == language_Label:
                return self.langues_data[language]["Id"]


            
    pt = {
        "Label":"Português",
        "Id":"pt",
        "Status":"Estado",
        "Run":"Executar",
        "Find File":"Localizar Arquivo",
        "File":"Ficheiro",
        "Exit":"Sair",
        "Help":"Ajuda",
        "Language":"Idioma",
        "Tutorial":"Tutorial",
        "Online Voxelizer":"Voxelizer Online",
        "About":"Sobre",
        "YouTube Channel":"Canal no YouTube",
        "Version":"Versão",
        "Repository":"Repositorio"
    }
    en = {
        "Label":"English",
        "Id":"en",
        "Status":"Status",
        "Run":"Run",
        "Find File":"Find File",
        "File":"File",
        "Exit":"Exit",
        "Help":"Help",
        "Language": "Language",
        "Tutorial":"Tutorial",
        "Online Voxelizer":"Online Voxelizer",
        "About":"About",
        "YouTube Channel":"YouTube Channel",
        "Version":"Version",
        "Repository":"Repository"
    }


    