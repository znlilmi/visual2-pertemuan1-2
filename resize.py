import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB",font=("helvetica",24))],
         [sg.Text("BANJARMASIN",font=("Courier",18))]]
window = sg.Window(title="New Icon",
                   layout=susunan,
                   element_justification= "centre",
                   icon= "favicon.ico",
                   resizable=True,
                   size=(430,200))

window.read()
window.close()