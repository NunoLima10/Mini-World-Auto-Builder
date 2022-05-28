
import PySimpleGUI as sg

class App:
    def __init__(self,title: str ,size: tuple, icon:str = None) -> None:
        self.title = title
        self.size = size 
        self.icon = icon
        self.font = "Nexa 12 bold"

        self.layout = self.build_layout()
        self.create_window()
        

    def build_layout(self)-> list:
        layout = [[sg.Push(),sg.Text("Hello",font = self.font ),sg.Push()]]

        return layout

    def create_window(self)->None:
        self.window = sg.Window(self.title, self.layout, size = self.size, icon = self.icon)


    def run(self)-> None:
        while True:
            event,values = self.window.read()

            if event == sg.WIN_CLOSED:
                break


    def close(self)-> None:
        self.window.close()


