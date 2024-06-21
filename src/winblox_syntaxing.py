from src import winblox_local_modules as wlm
from src import winblox_debug_system as wds
from src import winblox_file_manager as wfm

json_path = "./json/"
extension = ".json"

prefix_list = wfm.open_file(json_path, "prefix_list", extension)
data_types_list = wfm.open_file(json_path, "data_types_list", extension)
operators_list = wfm.open_file(json_path, "operators_list", extension)
esc_seq_list = wfm.open_file(json_path, "esc_sequence_list", extension)
delimiters_list = wfm.open_file(json_path, "delimiters_list", extension)
comment_list = wfm.open_file(json_path, "comment_list", extension)

def set_highligts(scr_input: str):
    print(scr_input)
    #x = wlm.re.search(r"" + keyword_list, scr_input)
    #x = wlm.re.search("interfaceputlocalglobal()[]{}:;$/numboolstripip-prefixip6ip6-prefixidtimenil'\\\\n\r\t\\$\\?\\_\x07\x08\x0c\x0b'+*-/%=<><=>=!=!&&and||orin~|^&>><<.,[]()$~->#", keyword_list)
    #for kl in range(len(keyword_list)):
        #x = wlm.re.search(keyword_list[kl], scr_input)
    #print(keyword_list)
    #print (x)

#def split_string(scr_input):
    #words_to_check = scr_input.split()

    #for wtc in words_to_check:
        #print (wtc)
        #set_highligts(wtc)

