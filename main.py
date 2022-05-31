
from app import App


def main()-> None:
    
    title = "MiniWorld-AutoBuilder"
    size = (500,500)
    icon_path = "icon_logo.ico"

    app = App(title, size, icon_path)
    app.run()
    app.close()
    

if __name__=="__main__":
    main()