import PySimpleGUI as sg

sg.theme("DarkAmber")

def first_window():
    first_layout = [
        [sg.Text("First Name:", font=("Calibri", 12)), sg.InputText(enable_events=True, key="first_name", font=("Calibri", 12))],
        [sg.Text("Last Name:", font=("Calibri", 12)), sg.InputText(enable_events=True, key="last_name", font=("Calibri", 12))],
        [sg.Text("Year of Birth:", font=("Calibri", 12)), sg.InputText(enable_events=True, key="year", font=("Calibri", 12))],
        [sg.Text("", key="message", font=("Calibri", 12))],
        [sg.Button("Verify", key="verify", font=("Calibri", 12)), sg.Button("Next", key="next", disabled=True, font=("Calibri", 12))]
    ]

    first_window = sg.Window("Age Verification", first_layout, element_justification="center", size=(400, 170))

    while True:
        event, values = first_window.read()
        year = values["year"]
        first_name = values["first_name"]
        last_name = values["last_name"]
        if event == "verify":
            if not first_name or not last_name or not year:
                first_window["message"].update("Please fill in all fields.", text_color="red")
                first_window["next"].update(disabled=True)
            elif 2023 - int(year) >= 18:
                first_window["message"].update(first_name + " " + last_name + ", you can proceed.", text_color="green")
                first_window["next"].update(disabled=False)
            else:
                first_window["message"].update("Sorry, " + first_name + " " + last_name + ", you cannot access this page.", text_color="red")
                first_window["next"].update(disabled=True)
        if event == "next":
            first_window.close()
            second_window()

def second_window():
    second_layout = [
        [sg.Text("")],
        [sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="11", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="12", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="13", font=("Calibri", 12))],
        [sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="21", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="22", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="23", font=("Calibri", 12))],
        [sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="31", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="32", font=("Calibri", 12)),
         sg.Button("", size=(2, 1), button_color=("white", "white"), disabled=True, key="33", font=("Calibri", 12))],
        [sg.Text("")],
        [sg.Button("I", key="I", size=(2, 1), font=("Calibri", 12)), sg.Button("II", key="II", size=(2, 1), font=("Calibri", 12)),
         sg.Button("III", key="III", size=(2, 1), font=("Calibri", 12)), sg.Button("IV", key="IV", size=(2, 1), font=("Calibri", 12)),
         sg.Button("V", key="V", size=(2, 1), font=("Calibri", 12)), sg.Button("VI", key="VI", size=(2, 1), font=("Calibri", 12))]
    ]

    second_window = sg.Window("Dice Game", second_layout, element_justification="center", size=(310, 250))

    def clear():
        buttons = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        for button in buttons:
            second_window[button].update(button_color=("white", "white"))

    while True:
        event, values = second_window.read()
        if event == "I":
            clear()
            second_window["22"].update(button_color=("white", "red"))
        if event == "II":
            clear()
            second_window["13"].update(button_color=("white", "red"))
            second_window["31"].update(button_color=("white", "red"))
        if event == "III":
            clear()
            second_window["22"].update(button_color=("white", "red"))
            second_window["13"].update(button_color=("white", "red"))
            second_window["31"].update(button_color=("white", "red"))
        if event == "IV":
            clear()
            second_window["11"].update(button_color=("white", "red"))
            second_window["13"].update(button_color=("white", "red"))
            second_window["31"].update(button_color=("white", "red"))
            second_window["33"].update(button_color=("white", "red"))
        if event == "V":
            clear()
            second_window["22"].update(button_color=("white", "red"))
            second_window["11"].update(button_color=("white", "red"))
            second_window["13"].update(button_color=("white", "red"))
            second_window["31"].update(button_color=("white", "red"))
            second_window["33"].update(button_color=("white", "red"))
        if event == "VI":
            clear()
            second_window["11"].update(button_color=("white", "red"))
            second_window["21"].update(button_color=("white", "red"))
            second_window["31"].update(button_color=("white", "red"))
            second_window["13"].update(button_color=("white", "red"))
            second_window["23"].update(button_color=("white", "red"))
            second_window["33"].update(button_color=("white", "red"))

if __name__ == "__main__":
    first_window()
