import PySimpleGUI as sg


def aluno():


    # All the stuff inside your window.
    layout = [  [sg.Text("Digite o nome do aluno"),sg.InputText()],
                [sg.Text("Digite a primeira nota"),sg.InputText()],
                [sg.Text("Digite a segunda nota"), sg.InputText()], 
                [sg.Button('SIM'),sg.Button('NÃO')]]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'NÃO':
            break
        if event== 'SIM':
           window.close() 
           resultado()
    window.close()



def resultado():
    import PySimpleGUI as sg

    # All the stuff inside your window.
    layout = [  [sg.Text("Digite o nome do aluno")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()



aluno()