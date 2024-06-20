from src import winblox_local_modules as wlm
from src import winblox_status as ws

from src import winblox_debug_system as wds

from src import winblox_database_login as wdl
from src import winblox_command_interface as wci
from src import winblox_menu as wm

def __main__():
    if (ws.login_page):
        wds.note_date_and_time()
        wds.debug("on login page!")
        wdl.login_window()
    if (ws.main_menu):
        wds.debug("on main menu page!")
        wm.main_menu_window()
    if (ws.command_page):
        wds.debug("on command page!")
        wci.commandline_window()

        wlm.time.sleep(1)
        __main__()


__main__()