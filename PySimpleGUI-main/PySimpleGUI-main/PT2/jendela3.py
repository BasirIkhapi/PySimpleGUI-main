import PySimpleGUI as sg
sg.theme("DarkGreen4")  
sg.theme_text_color ("#FFFF00")
window = sg.Window(title ="Profile", 
                    layout =   [[sg.Text("NPM       : 2210010209")],
                                [sg.Text("NAMA      : Gusti Amanda Sielviana")],
                                [sg.Text("Kelas     : 5M Reguler Banjarmasin")]
                                ],
                    size=(400,200),
                    font=("Times", 18))
window()
window.close()