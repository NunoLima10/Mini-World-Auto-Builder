import PySimpleGUI as sg

PALETA ={
    "Azul1":"#C7DDEC",
    "Azul2":"#B3D2E7",
    "Azul3":"#98BED9",
    "Azul4":"#485B78",
}

FONT = "Nexa 10 bold"


def build_layout()-> list:
    logo_box = [
        sg.Col(
            layout = [[sg.Image("text_logo.png", background_color=PALETA["Azul1"])]],
            element_justification = "c",
            vertical_alignment = "c",
            expand_x = True,
            background_color = PALETA["Azul1"]
            )
        ]

    list_box =[
        sg.Listbox(
            values = ["hello"],
            expand_x = True,
            expand_y = True,
            font = FONT, 
            text_color = PALETA["Azul4"],
            background_color = PALETA["Azul2"],
            no_scrollbar = True,
            key = "-LISTBOX-"
                
            )
            ]
        
    status_text = [
        sg.Push(PALETA["Azul1"]),
        sg.Text(
            text = "Status",
            background_color = PALETA["Azul1"],
            font = FONT,
            text_color = PALETA["Azul4"],
            size = (None,2),
            key = "-STATUS-"
        ),
        sg.Push(PALETA["Azul1"])
        ]

    action_box = [
        sg.Push(PALETA["Azul1"]),
        sg.Button(
            button_text = "Executar",
            button_color = (PALETA["Azul4"], PALETA["Azul3"]),
            border_width = 0,
            font = FONT, 
            size = (25,2),
            key = "-RUN-"    
        ),
        sg.Button(
            button_text = "Localizar Arquivo",
            button_color = (PALETA["Azul4"], PALETA["Azul3"]),
            border_width = 0,
            font = FONT,  
            size = (25,2),
        key = "-FINDFILE-"     
        ),
        sg.Push(PALETA["Azul1"])
        ]
      
    content_box = sg.Column(
        [list_box, status_text, action_box],
        expand_x = True,
        expand_y = True,
        background_color=PALETA["Azul1"]
        )

    return [[logo_box,content_box]]