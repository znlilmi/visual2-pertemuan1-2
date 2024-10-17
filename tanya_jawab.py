import PySimpleGUI as sg

sg.theme("DarkGrey")
sg.theme_text_color('#fff')
layout = [
    [sg.Text("Contoh Button", font=('helvatica', 25))],
    [sg.Button('Simpan')],
    [sg.Button('Keluar')],
]

window = sg.Window(title='Contoh Button',
                    layout=layout,
                      size=(600, 300),
                        font=('Georgia', 20),
                        element_justification='center'
                        )
kejadian, nilai = window.read()
print(kejadian,"=>", nilai)
window.close()