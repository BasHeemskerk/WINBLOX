from src import winblox_debug_system as wds
from src import winblox_error_codes as wes
from src import winblox_ssh_api as wsa
from src import winblox_local_modules as wlm
from src import  winblox_status as ws

head = [
    [wlm.sg.Text("WINBLOX Terminal")]
]

command_line = [
    [wlm.sg.Text("Admin@MikroTik >", key=("-USER-")), wlm.sg.Input("", key=("-COMMAND-")), wlm.sg.Button("Execute")],
]

foot = [
    [wlm.sg.Button("Save line"), wlm.sg.Button("Return")]
]

complete_layout = [
    [wlm.sg.Column(head)],
    [wlm.sg.HSeparator()],
    [wlm.sg.Column(command_line)],
    [wlm.sg.HSeparator()],
    [wlm.sg.Column(foot)]
]

def commandline_window():
    window = wlm.sg.Window("WINBLOX | " + ws.version, complete_layout)

    while True:
        event, values = window.read()
        if event == "Execute":
            wsa.send_package(str(values["-COMMAND-"]))
        if event == "Return" or event == wlm.sg.WIN_CLOSED:
            ws.main_menu = True
            ws.command_page = False
            break

    window.close()
