
import PySimpleGUI as sg

class Layout:
    def __init__(self,language_data: dict, languages_labels: dict) -> None:
        
        self.language_data = language_data
        self.languages_labels = languages_labels
        self.font = "Nexa 10 bold"
    
        self.palette =   {
        "Color1":"#C7DDEC",
        "Color2":"#B3D2E7",
        "Color3":"#98BED9",
        "Color4":"#485B78",
        }

    def build_layout(self) -> list:
        logo_box = [
            sg.Col(
                layout = [[sg.Image('assets\\text_logo.png', background_color=self.palette["Color1"])]],
                element_justification = "c",
                vertical_alignment = "c",
                expand_x = True,
                background_color = self.palette["Color1"]
            ) 
        ]

        list_box = [
            sg.Listbox(
                values = [],
                expand_x = True,
                expand_y = True,
                font = "Nexa 15 bold", 
                text_color = self.palette["Color4"],
                background_color = self.palette["Color2"],
                no_scrollbar = True,
                enable_events  = True,
                key = "-LISTBOX-"    
            )
        ]  

        status_text = [
            sg.Push(self.palette["Color1"]),
            sg.Text(
                text = self.language_data["Status"],
                background_color = self.palette["Color1"],
                font = self.font,
                text_color = self.palette["Color4"],
                size = (None,1),
                key = "-STATUS-"
            ),
            sg.Push(self.palette["Color1"])
        ]

        action_box = [
            sg.Push(self.palette["Color1"]),
            sg.Button(
                button_text = self.language_data["Convert"],
                button_color = (self.palette["Color4"], 
                self.palette["Color3"]),
                border_width = 0,
                font = self.font, 
                size = (25,2),
                key = "-CONVERT-"    
            ),
            sg.Button(
                button_text = self.language_data["Find File"],
                button_color = (self.palette["Color4"], self.palette["Color3"]),
                border_width = 0,
                font = self.font,  
                size = (25,2),
                key = "-SELECT_FILE-"     
            ),
            sg.Push(self.palette["Color1"])
        ]
              
        pallete_layout = [
            [
                sg.Button(
                    button_text="",
                    image_source ='assets\\pallete_icon.png',
                    key="-PALLETE_ICON-", 
                    button_color = (self.palette["Color1"],
                    self.palette["Color1"]),
                    border_width=0
                ),
                sg.Image( 
                    background_color=self.palette["Color1"],
                    key="-PALLETE_IMG-",
                    data=None
                )
            ]
        ]

        pallete = [
            sg.Frame(
                self.language_data["Palette"],
                layout=pallete_layout,
                expand_x=True,
                background_color=self.palette["Color1"],
                font = self.font,
                title_color=self.palette["Color4"],
                relief=sg.RELIEF_FLAT
            )
        ]


        menu_def = [
                [
                self.language_data["File"],
                [   self.language_data["Find File"],
                    self.language_data["Output Folder"],
                    "---",
                    self.language_data["Exit"],
                ]
                ],
                [
                self.language_data["Help"],
                [
                    [self.language_data["Language"],self.languages_labels],
                    self.language_data["Tutorial"],
                    self.language_data["Online Voxelizer"]
                ]
                ],
                [
                self.language_data["About"],
                [
                    self.language_data["YouTube Channel"],
                    self.language_data["Repository"]
                ]
                ]
            ]
        menu = sg.Menu(
            menu_definition = menu_def,
            pad=(10,10)
        )
        
        content_box = sg.Column(
            [list_box, pallete, status_text , action_box],
            expand_x = True,
            expand_y = True,
            background_color=self.palette["Color1"]
        )
        return [[menu, logo_box, content_box]]