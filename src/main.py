from app import App

__author__ = "Nuno Lima"
__copyright__ = "Copyright 2022 Nuno Lima"
__version__ = "0.0.3"
__maintainer__ = "Nuno Lima"
__email__ = "contato.playcraft@gmail.com"
__status__ = "Production"

def main()-> None:
    
    title = "MiniWorld-AutoBuilder"
    size = (500,500)
    icon_path = "assets\icon_logo.ico"
    language = "pt"

    app = App(title, size, icon_path, language)
    app.run()
    app.close()
    

if __name__=="__main__":
    main()