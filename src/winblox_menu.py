from src import winblox_backup as wb

from src import winblox_command_interface as wci
from src import winblox_script_interface as wsi

from src import winblox_ssh_api as wsa

from src import winblox_status as ws

from src import winblox_web_requests as wwr
from src import winblox_local_modules as wlm

head = [
    [wlm.sg.Text("WINBLOX Menu")],
    [wlm.sg.Text("Logged in as: " + ws.username)]
]

menu = [
    [wlm.sg.Text("Tools")],
    [wlm.sg.Button("Terminal"), wlm.sg.Button("IDE"), wlm.sg.Button("Editor")],
    [wlm.sg.HSeparator()],
    [wlm.sg.Text("Scripts")],
    [wlm.sg.Button("Building blocks"), wlm.sg.Button("Examples")],
    [wlm.sg.HSeparator()],
    [wlm.sg.Text("Dcoumentation")],
    [wlm.sg.Button("Mikrotik"), wlm.sg.Button("Boards"), wlm.sg.Button("Winblox github")],
]

foot = [
    [wlm.sg.Button("Return to login screen")],
    [wlm.sg.Button("Exit")]
]

complete_layout = [
    [wlm.sg.Column(head), wlm.sg.VSeparator(), wlm.sg.Column(menu), wlm.sg.VSeparator(), wlm.sg.Column(foot)],
]

def main_menu_window():
    window = wlm.sg.Window("WINBLOX | " + ws.version, complete_layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == wlm.sg.WIN_CLOSED:
            ws.main_menu = True
            ws.command_page = False
            break

    window.close()