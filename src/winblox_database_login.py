from src import winblox_debug_system as wds
from src import winblox_status as ws

from src import winblox_local_modules as wlm

wlm.sg.theme("DarkBlue")

settings = [
    [wlm.sg.Button("Check for updates"), wlm.sg.Text("", key=("-SEARCH_UPDATES-"))],
    [wlm.sg.HSeparator()],
    [wlm.sg.Button("Source Code"), wlm.sg.Button("Documentation")],
]

login_form = [
    [wlm.sg.Text("Welcome to winblox, the most advanced IDE for mikrotik programming")],
    [wlm.sg.HSeparator()],
    [wlm.sg.Text("Username:")],
    [wlm.sg.Input("", key=("-USERNAME-"))],
    [wlm.sg.Text("Password:")],
    [wlm.sg.Input("", key=("-PASSWORD-"))],
    [wlm.sg.Button("Database login"), wlm.sg.Button("Request account")],
    [wlm.sg.Button("Guestmode")],
    [wlm.sg.HSeparator()],
    [wlm.sg.Button("Close")],
]

logo = [
    [wlm.sg.Text("Developed by Bas Heemskerk, version " + ws.version), wlm.sg.Image("./gfx/bumbo.png"), wlm.sg.Button("My Github")]
]

complete_layout = [
    [wlm.sg.Column(settings)],
    [wlm.sg.VSeperator()],
    [wlm.sg.Column(login_form)],
    [wlm.sg.VSeperator()],
    [wlm.sg.Column(logo)],
]

def login_window():

    window = wlm.sg.Window("WINBLOX | " + ws.version, complete_layout)

    while True:
        event, values = window.read()
        if event == "Database login":
            if (str(values["-USERNAME-"]) != "", str(values["-PASSWORD-"]) != ""):
                login_database(str(values["-USERNAME-"]), str(values["-PASSWORD-"]), "mfa_not_set_up", ws.database_link)
            else:
                wds.error("Username or password is incorrect, " + 3)
        if (event == "My Github"):
            wlm.webbrowser.open(ws.github_dev)
        if (event == "Source Code"):
            wlm.webbrowser.open(ws.source)
        if (event == "Check for updates"):
            check_updates(ws.version)
            window["-SEARCH_UPDATES-"].update("Checking for updates...")
            new_ver = check_updates(ws.version)
        if event == "Close" or event == wlm.sg.WIN_CLOSED:
            break
    
    window.close()

def login_database(username, password, mfa_code, link):
    wds.debug(username)
    wds.debug(password)
    if (mfa_code != "mfa_not_set_up"):
        wds.debug(mfa_code)
    else:
        wds.debug("MFA is not enabled")
    wds.debug(link)

def check_updates(current_version):
    response = wlm.requests.get(ws.github_api_link)
    wds.debug("Requesting information from " + ws.github_api_link)
    wds.debug(str(response.json()))
    wds.debug(str(response.json()["name"]))
    wds.debug("checking for updates, current version = " + current_version)

    if (ws.version == str(response.json()["name"])):
        return False
    else:
        return True