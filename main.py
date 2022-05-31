
from app import App
from layout import build_layout
def main()-> None:
    title = "MiniWorld-AutoBuilder"
    size = (500,500)
    icon_path ="icon_logo.ico"
    app_layout = build_layout()
    
    app = App(title,app_layout, size, icon_path,)
    app.run()
    app.close()
    

if __name__=="__main__":
    main()