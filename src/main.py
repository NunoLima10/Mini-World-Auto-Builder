
from app import App

__author__ = "Nuno Lima"
__copyright__ = "Copyright 2022 Nuno Lima"
__version__ = "0.1.0"
__maintainer__ = "Nuno Lima"
__email__ = "contato.playcraft@gmail.com"
__status__ = "Production"

def main() -> None:  
    app = App()
    app.run()
    app.close()
    

if __name__=="__main__":
    main()