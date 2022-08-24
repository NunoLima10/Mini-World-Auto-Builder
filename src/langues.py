
class Language:
    def __init__(self, language_id: str) -> None:
        defaut_language = "en" 
        self.language_id = language_id

        self.langues_data = {
        "en":self.en,
        "pt":self.pt,
        "es":self.es,
        "fr":self.fr,
        "tl":self.tl,
        "vn":self.vn,
        "cn":self.cn
        }
        
        self.language_data = self.langues_data[defaut_language]
        if self.language_id in self.langues_data:
            self.language_data = self.langues_data[self.language_id] 
    
    def get_languages_labels(self) -> list[str]:
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
        "Convert":"Converter",
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
        "Convert":"Convert",
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
    es = { 
         "Label":"Español", 
         "Id":"es", 
         "Status":"Estado", 
         "Convert":"Ejecutar", 
         "Find File":"Encontrar Archivo", 
         "Output Folder":"Carpeta de Salida", 
         "File":"Archivo", 
         "Exit":"Salir", 
         "Palette":"Paleta", 
         "Select Palette":"Selecionar Paleta", 
         "Show Palette":"Mostrar Paleta", 
         "Help":"Ayuda", 
         "Language": "Lenguaje ", 
         "Tutorial":"Tutorial", 
         "Online Voxelizer":"Voxelizador Online", 
         "About":"Acerca de", 
         "YouTube Channel":"Canal de Youtube", 
         "Repository":"Repositorio", 
         "Converted":"Convertido", 
         "Unconverted":"Sin convertir", 
         "Not supported":"No es compatible", 
         "Converting":"Convirtiendo", 
         "ok":"Aceptar", 
         "Warning":"Alerta", 
         "VoxPaserException":"Error en conversion de archivo, \ntipo de archivo no compatible", 
         "FileNotFoundException":"El Archivo no fue encontrado", 
         "PalletSizeException":"El tamaño de la paleta no es el correcto  \nel tamaño correcto es (256,1)", 
         "VoxHasNoPalleteException":"La paleta de color seleccionada no fue encontrada", 
         "CannotChangeLanguage":" No puedes cambiar el lenguaje durante la conversion" 
     }
    fr = {
        "Label":"Français",
        "Id":"fr",
        "Status":"Statut",
        "Convert":"Convertir",
        "Find File":"Trouver un fichier",
        "Output Folder":"Dossier de sortie",
        "File":"Dossier",
        "Exit":"Sortir",
        "Palette":"Palette",
        "Select Palette":"Sélectionner Palette",
        "Show Palette":"Afficher la palette",
        "Help":"Aider",
        "Language": "Langue",
        "Tutorial":"Didacticiel",
        "Online Voxelizer":"Voxeliseur en ligne",
        "About":"À propos de",
        "YouTube Channel":"Chaîne Youtube",
        "Repository":"Dépôt",
        "Converted":"Converti",
        "Unconverted":"Non converti",
        "Not supported":"Non supporté",
        "Converting":"Conversion",
        "ok":"d'accord",
        "Warning":"Avertissement",
        "VoxPaserException":"Une erreur s'est produite lors de la conversion du fichier, \nle type de fichier n'est pas pris en charge",
        "FileNotFoundException":"Le fichier n'a pas été trouvé",
        "PalletSizeException":"La taille de la palette ne correspond pas\nà la taille standard (256,1)",
        "VoxHasNoPalleteException":"La palette de couleurs sélectionnée n'a pas été trouvée",
        "CannotChangeLanguage":" Impossible de changer de langue pendant la conversion"
    }
    tl = {
        "Label":"แบบไทย",
        "Id":"tl",
        "Status":"สถานะ",
        "Convert":"แปลง",
        "Find File":"ค้นหาไฟล์",
        "Output Folder":"โฟลเดอร์เอาต์พุต",
        "File":"ไฟล์",
        "Exit":"ทางออก",
        "Palette":"จานสี",
        "Select Palette":"เลือกจานสี",
        "Show Palette":"แสดงจานสี",
        "Help":"ช่วย",
        "Language": "ภาษา",
        "Tutorial":"กวดวิชา",
        "Online Voxelizer":"Voxelizer ออนไลน์",
        "About":"เกี่ยวกับ",
        "YouTube Channel":"ช่อง YouTube",
        "Repository":"ที่เก็บ",
        "Converted":"แปลงแล้ว",
        "Unconverted":"ยังไม่กลับใจใหม่",
        "Not supported":"ไม่รองรับ",
        "Converting":"กำลังแปลง",
        "ok":"ตกลง",
        "Warning":"คำเตือน",
        "VoxPaserException":"เกิดข้อผิดพลาดในการแปลงไฟล์ \nไม่รองรับประเภทไฟล์",
        "FileNotFoundException":"ไม่พบไฟล์",
        "PalletSizeException":"ขนาดของจานสีไม่ตรงกัน \nขนาดมาตรฐาน (256,1)",
        "VoxHasNoPalleteException":"ไม่พบจานสีที่เลือก",
        "CannotChangeLanguage":" ไม่สามารถเปลี่ยนภาษาระหว่างการแปลง"
    }
    vn = {
        "Label":"Tiếng Việt",
        "Id":"vn",
        "Status":"Trạng thái",
        "Convert":"Chuyển thành",
        "Find File":"Tìm tập tin",
        "Output Folder":"Thư mục đầu ra",
        "File":"Tập tin",
        "Exit":"Lối ra",
        "Palette":"Bảng màu",
        "Select Palette":"Chọn bảng màu",
        "Show Palette":"Hiển thị bảng màu",
        "Help":"Cứu giúp",
        "Language": "Ngôn ngữ",
        "Tutorial":"Hướng dẫn",
        "Online Voxelizer":"Voxelizer trực tuyến",
        "About":"Về",
        "YouTube Channel":"Kênh Youtube",
        "Repository":"Kho",
        "Converted":"Chuyển đổi",
        "Unconverted":"Không được chuyển đổi",
        "Not supported":"Không được hỗ trợ",
        "Converting":"Chuyển đổi",
        "ok":"Vâng",
        "Warning":"Cảnh báo",
        "VoxPaserException":"Đã xảy ra lỗi khi chuyển đổi tệp, \ n loại tệp không được hỗ trợ",
        "FileNotFoundException":"Tệp không được tìm thấy",
        "PalletSizeException":"Kích thước của bảng màu không phù hợp với \ kích thước tiêu chuẩn (256,1)",
        "VoxHasNoPalleteException":"Bảng màu đã chọn không được tìm thấy",
        "CannotChangeLanguage":" Không thể thay đổi ngôn ngữ trong quá trình chuyển đổi"
    }
    cn = {
        "Label":"中国人",
        "Id":"cn",
        "Status":"地位",
        "Convert":"兑换",
        "Find File":"查找文件",
        "Output Folder":"导出目录",
        "File":"文件",
        "Exit":"出口",
        "Palette":"调色板",
        "Select Palette":"选择调色板",
        "Show Palette":"显示调色板",
        "Help":"帮助",
        "Language": "语",
        "Tutorial":"教程",
        "Online Voxelizer":"在线体素器",
        "About":"关于",
        "YouTube Channel":"YouTube 频道",
        "Repository":"存储库",
        "Converted":"已转换",
        "Unconverted":"未转换",
        "Not supported":"不支持",
        "Converting":"转换",
        "ok":"好的",
        "Warning":"警告",
        "VoxPaserException":"文件转换出错，\n不支持文件类型",
        "FileNotFoundException":"找不到文件",
        "PalletSizeException":"调色板的大小与\n标准大小不匹配 (256,1)",
        "VoxHasNoPalleteException":"未找到选定的调色板",
        "CannotChangeLanguage":" 转换期间无法更改语言"
    }

    