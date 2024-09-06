import PySimpleGUI as sg


def aluno():


    # All the stuff inside your window.
    layout = [  [sg.Text("Digite o nome do aluno"),sg.InputText(key="aluno")],
                [sg.Text("Digite a primeira nota"),sg.InputText(key="primeira nota")],
                [sg.Text("Digite a segunda nota"), sg.InputText(key="segunda nota")], 
                [sg.Text('', key='erro')],
                [sg.Button('SIM'),sg.Button('NÃO'), sg.Button('ADICIONAR')]]

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


        if event == 'ADICIONAR':
            nome_alunos = values["aluno"]
            nota1 = values["primeira nota"]
            nota2= values["segunda nota"]
            
            if len(nome_alunos) < 3:
                window['erro'].update('O nome está errado')

                if len(nota1) <= 10:
                    window['erro'].update('A nota não é válida')

                    if len(nota2) <= 10:
                        window['erro'].update('A nota não é válida')

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