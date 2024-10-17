import PySimpleGUI as sg
sg.theme("#007FFF")
sg.theme_text_color('yellow')
window = sg.Window(title="Profile",
    layout=[[sg.Text("Latihan",
                    font=("Arial", 20, "italic", "bold", "underline"))],
            [sg.Text("NPM          : 2210010415 ")],
            [sg.Text("Nama         : Muhammad Zainal Ilmi ")],
            [sg.Text("Kelas         : 5O Regular Banjarmasin ")]],
    size=(510, 200),
    font=("comic", 18))
window()
window.close()