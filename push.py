import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color('#fff')
layout = [
    [sg.Push(),sg.Text("UNISKA MAAB", font=('helvatica', 25)),sg.Push()],
    [sg.Push(),sg.Text("UNISKA MAAB", font=('courier', 18)),sg.Push()],
]

window = sg.Window(title='Element Text',
                    layout=layout,
                      size=(600, 300),
                        font=('Georgia', 20)
                        )
window()
window.close()
