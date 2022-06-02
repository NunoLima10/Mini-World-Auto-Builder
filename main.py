from app import App


def main()-> None:
    
    title = "MiniWorld-AutoBuilder"
    size = (500,500)
    icon_path = "icon_logo.ico"
    language = "pt"

    app = App(title, size, icon_path, language)
    app.run()
    app.close()
    

if __name__=="__main__":
    main()