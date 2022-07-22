import PySimpleGUI as sg


class Popup:
    def __init__(self, icon:str, size) -> None:

        self.icon = icon
        self.size = size
        self.font = "Nexa 10 bold"
        self.palette =   {
        "Color1":"#C7DDEC",
        "Color2":"#B3D2E7",
        "Color3":"#98BED9",
        "Color4":"#485B78",
        }

       

    def build_layout(self, description:str, button_text: str) -> list:
        description = [
            sg.Push(self.palette["Color1"]),
            sg.Text(
                text = description,
                background_color = self.palette["Color1"],
                font = self.font,
                text_color = self.palette["Color4"],
                size = (None,3),
              
            ),
            sg.Push(self.palette["Color1"])
            ]
        ok_button = [
            sg.Push(self.palette["Color1"]),
            sg.Button(
                button_text = button_text,
                button_color = (self.palette["Color4"], self.palette["Color3"]),
                border_width = 0,
                font = self.font, 
                size = (15,2)   
            ),
            sg.Push(self.palette["Color1"])
            ]
        return [[sg.Column(
                [description, ok_button ],
                expand_x = True,
                expand_y = True,
                background_color=self.palette["Color1"]
                )]]


    def show(self,title: str, description: str, button_text: str) -> None:

        layout = self.build_layout(description, button_text)

        window = sg.Window(title, layout,icon=self.icon, modal=True, 
                            background_color=self.palette["Color1"],size=self.size)

        while True:
            app_event, values = window.read()

            if app_event == sg.WIN_CLOSED or app_event == button_text:
                break
        window.close()
        
        
      

        
   
    




        