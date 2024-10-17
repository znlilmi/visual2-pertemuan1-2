import PySimpleGUI as sg

sg.theme("DarkGrey")
sg.theme_text_color('#fff')
layout = [
    [sg.VPush(),sg.Text("UNISKA MAAB", font=('helvatica', 25)),sg.Push()],
    [sg.Push(),sg.Text("UNISKA MAAB", font=('courier', 18)),sg.VPush()],
]

window = sg.Window(title='Element Text',
                    layout=layout,
                      size=(600, 300),
                        font=('Georgia', 20)
                        )
window()
window.close()
