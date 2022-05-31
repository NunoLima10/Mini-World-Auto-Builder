import PySimpleGUI as sg
from langues import langues

PALETTE ={
    "Azul1":"#C7DDEC",
    "Azul2":"#B3D2E7",
    "Azul3":"#98BED9",
    "Azul4":"#485B78",
}
FONT = "Nexa 10 bold"


def build_layout(lang="defaut_lang" )-> list:
    if not lang in langues:
        lang = "defaut_lang"
    
    language = langues[lang]
        

    logo_box = [
        sg.Col(
            layout = [[sg.Image("text_logo.png", background_color=PALETTE["Azul1"])]],
            element_justification = "c",
            vertical_alignment = "c",
            expand_x = True,
            background_color = PALETTE["Azul1"]
            )
        ]

    list_box =[
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
            text = language["Status"],
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
            button_text = language["Run"],
            button_color = (PALETTE["Azul4"], PALETTE["Azul3"]),
            border_width = 0,
            font = FONT, 
            size = (25,2),
            key = "-RUN-"    
        ),
        sg.Button(
            button_text = language["Find File"],
            button_color = (PALETTE["Azul4"], PALETTE["Azul3"]),
            border_width = 0,
            font = FONT,  
            size = (25,2),
        key = "-FINDFILE-"     
        ),
        sg.Push(PALETTE["Azul1"])
        ]


    menu_def = [
        [language["Help"],
            [
            language["Language"],
            language["Tutorial"]
            ]
        ],
        [language["About"],
            [
            language["YouTube Channel"],
            language["Version"],
            language["Repository"]
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