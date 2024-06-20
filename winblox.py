from src import winblox_local_modules as wlm
from src import winblox_status as ws

from src import winblox_debug_system as wds

from src import winblox_database_login as wdl

def __main__():
    if (ws.login_page):
        wds.note_date_and_time()
        wds.debug("on login page!")
        wdl.login_window()


__main__()