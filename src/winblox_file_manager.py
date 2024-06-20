import winblox_local_modules as wlm
import winblox_debug_system as wds
import winblox_error_codes as wec


#file management script

#a system to simply open files via other scripts/modules
def open_file(location, filename, extension, mode):

    final_path = location + filename + extension

    if (wlm.os.path.exists(final_path)):
        file = open(final_path, mode)
        wds.debug("The file " + final_path + " has been opened!")
    else:
        wds.error("The file " + final_path + " does not exist or could not be found, " + wec.codes[0])
        wds.debug("Because the file could not be found it has been created in the designated location.")
        create_file(location, filename, extension)

    return file
    close(file)

#a system to simply create files via other scripts/modules
def create_file(target_location, filename, extension):

    final_path = target_location + filename + extension

    if (wlm.os.path.exist(final_path) == False):
        file = open(final_path, "x")
    else:
        wds.error("The file could not be created because it already exists, " + wec.codes[1])
        wds.debug("The file exists in the following location: " + final_path)

    return file
    close(file)




#folder management
def open_folder(location, mode):

    final_path = location

def create_folder(target_location, mode):

    final_path = target_location


def file_saver_window(filename_input, folder_location_input):
    print(folder_location_input)
    print(filename_input)
    