
pt = {
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
    "Status":"Status",
    "Run":"Run",
    "Find File":"Find File",
    "File":"Ficheiro",
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

langues_data = {
    "defaut_lang":en,
    "en":en,
    "pt":pt
    }

available_languages = {
    "Português":"pt",
    "English":"en",
}


def get_language_data(lang:str="defaut_lang" )->dict:
    return langues_data[lang] if lang in langues_data else langues_data["defaut_lang"]



    
    
