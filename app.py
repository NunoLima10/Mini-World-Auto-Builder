
import PySimpleGUI as sg

from layout import PALETA,FONT


class App:
    def __init__(self,title: str, layout: list, size: tuple, icon:str = None) -> None:
        self.title = title
        self.size = size 
        self.icon = icon
        self.font = FONT

        self.layout = layout
        self.create_window()
        

    

    def create_window(self)->None:
        self.window = sg.Window(self.title, self.layout, size = self.size, icon = self.icon)
        self.window.BackgroundColor = PALETA["Azul1"]


    def run(self)-> None:
        while True:
            event,values = self.window.read()

            if event == sg.WIN_CLOSED:
                break


    def close(self)-> None:
        self.window.close()


