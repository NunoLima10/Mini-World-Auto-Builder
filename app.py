
import PySimpleGUI as sg

from layout import build_layout,PALETTE,FONT


class App:
    def __init__(self,title: str, size: tuple, icon:str = None,lang:str = "pt") -> None:
        self.title = title
        self.size = size 
        self.icon = icon
        self.font = FONT

        self.layout = build_layout(lang)
        self.create_window()
        
    def create_window(self)->None:
        self.window = sg.Window(self.title, self.layout, size = self.size, icon = self.icon)
        self.window.BackgroundColor = PALETTE["Azul1"]


    def run(self)-> None:
        while True:
            event,values = self.window.read()

            if event == sg.WIN_CLOSED:
                break


    def close(self)-> None:
        self.window.close()


