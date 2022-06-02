from math import dist
import PySimpleGUI as sg


PALETTE ={
    "Azul1":"#C7DDEC",
    "Azul2":"#B3D2E7",
    "Azul3":"#98BED9",
    "Azul4":"#485B78",
}
FONT = "Nexa 10 bold"


def build_layout(language_data:dict , available_languages:dict)-> list:
    
    logo_box = [
        sg.Col(
            layout = [[sg.Image("text_logo.png", background_color=PALETTE["Azul1"])]],
            element_justification = "c",
            vertical_alignment = "c",
            expand_x = True,
            background_color = PALETTE["Azul1"]
            )
        ]

    list_box = [
        sg.Listbox(
            values = ["hello"],
            expand_x = True,
            expand_y = True,
            font = FONT, 
            text_color = PALETTE["Azul4"],
            background_color = PALETTE["Azul2"],
            no_scrollbar = True,
            key = "-LISTBOX-"
                
            )
            ]
        
    status_text = [
        sg.Push(PALETTE["Azul1"]),
        sg.Text(
            text = language_data["Status"],
            background_color = PALETTE["Azul1"],
            font = FONT,
            text_color = PALETTE["Azul4"],
            size = (None,2),
            key = "-STATUS-"
        ),
        sg.Push(PALETTE["Azul1"])
        ]

    action_box = [
        sg.Push(PALETTE["Azul1"]),
        sg.Button(
            button_text = language_data["Run"],
            button_color = (PALETTE["Azul4"], PALETTE["Azul3"]),
            border_width = 0,
            font = FONT, 
            size = (25,2),
            key = "-RUN-"    
        ),
        sg.Button(
            button_text = language_data["Find File"],
            button_color = (PALETTE["Azul4"], PALETTE["Azul3"]),
            border_width = 0,
            font = FONT,  
            size = (25,2),
        key = "-FINDFILE-"     
        ),
        sg.Push(PALETTE["Azul1"])
        ]


    menu_def = [
        [language_data["File"],
            [
            language_data["Find File"],
            "---",
            language_data["Exit"],
            ]

        ],

        [language_data["Help"],
            [
            [language_data["Language"],[ key for key in  available_languages.keys()]],
            language_data["Tutorial"],
            language_data["Online Voxelizer"]
            ]
        ],
        [language_data["About"],
            [
            language_data["YouTube Channel"],
            language_data["Repository"],
            language_data["Version"]
            ]
        ]
    ]
    menu = sg.Menu(
        menu_definition = menu_def,
        # background_color = PALETTE["Azul1"],
        # font = FONT,
        # text_color = PALETTE["Azul4"],
        pad=(10,10))

    content_box = sg.Column(
        [list_box, status_text, action_box],
        expand_x = True,
        expand_y = True,
        background_color=PALETTE["Azul1"]
        )

    return [[menu,logo_box,content_box]]