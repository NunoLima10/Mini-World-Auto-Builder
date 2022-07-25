
class Language:
    def __init__(self,language_id:str) -> None:
        defaut_language = "en" 
        self.language_id = language_id

        self.langues_data = {
        "en":self.en,
        "pt":self.pt
        }
        
        self.language_data = self.langues_data[defaut_language]
        if self.language_id in self.langues_data:
            self.language_data = self.langues_data[self.language_id] 
    
    
    def get_languages_labels(self) -> list:
        return [self.langues_data[language]["Label"] for language in self.langues_data]

    def change_language(self, language_Label: str) -> None:
        language_id = self.find_language_by_label(language_Label)

        self.language_id = language_id  
        self.language_data = self.langues_data[self.language_id] 
        
    def find_language_by_label(self, language_Label: str) -> str:
        for language in self.langues_data:
            if self.langues_data[language]["Label"] == language_Label:
                return self.langues_data[language]["Id"]


            
    pt = {
        "Label":"Português",
        "Id":"pt",
        "Status":"Estado",
        "Run":"Executar",
        "Find File":"Localizar Arquivo",
        "Output Folder":"Salvar na pasta",
        "File":"Ficheiro",
        "Exit":"Sair",
        "Palette":"Paleta",
        "Select Palette":"Selecionar Paleta",
        "Show Palette":"Ver Paleta",
        "Help":"Ajuda",
        "Language":"Idioma",
        "Tutorial":"Tutorial",
        "Online Voxelizer":"Voxelizer Online",
        "About":"Sobre",
        "YouTube Channel":"Canal no YouTube",
        "Version":"Versão",
        "Repository":"Repositorio",
        "Converted":"Convertido",
        "Unconverted":"Não Convertido",
        "Not supported":"Não suportado",
        "Converting":"Convertendo",
        "ok":"ok",
        "Warning":"Aviso",
        "VoxPaserException":"Ocorreu um erro na converção do ficheiro, \n tipo de ficheiro não é suportado",
        "FileNotFoundException":"O ficheiro não foi encontrado",
        "PalletSizeException":"O tamanho da paleta não corresponde \nao tamanho padrão (256,1)",
        "VoxHasNoPalleteException":"Paleta de cores selecionado não foi encontrado",
        "CannotChangeLanguage":"Não pode mudar o idioma durante a conversão"
    }
    en = {
        "Label":"English",
        "Id":"en",
        "Status":"Status",
        "Run":"Run",
        "Find File":"Find File",
        "Output Folder":"Output Folder",
        "File":"File",
        "Exit":"Exit",
        "Palette":"Palette",
        "Select Palette":"Select Palette",
        "Show Palette":"Show Palette",
        "Help":"Help",
        "Language": "Language",
        "Tutorial":"Tutorial",
        "Online Voxelizer":"Online Voxelizer",
        "About":"About",
        "YouTube Channel":"YouTube Channel",
        "Version":"Version",
        "Repository":"Repository",
        "Converted":"Converted",
        "Unconverted":"Unconverted",
        "Not supported":"Not supported",
        "Converting":"Converting",
        "ok":"ok",
        "Warning":"Warning",
        "VoxPaserException":"An error has occurred in the conversion of the file, \nfile type is not supported",
        "FileNotFoundException":"The file was not found",
        "PalletSizeException":"The size of the palette does not match  \nthe standard size (256,1)",
        "VoxHasNoPalleteException":"Selected color pallete was not found",
        "CannotChangeLanguage":" Cannot change language during conversion"
    }


    