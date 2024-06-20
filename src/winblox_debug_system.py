import datetime as dt
import os.path

log_file_path = "./log/log.txt"

def note_date_and_time():
    string = str("-----Session started at " + str(dt.datetime.now()) + "-----\n")
    print(string)
    log_to_file(string)

def debug(str_input):
    string = str_input
    print(string)
    log_to_file(string + "\n")


def error(str_input, code):
    string = str_input + code
    log_to_file(string + "\n")

def log_to_file(str_input):
    file = open(log_file_path, "a")
    file.write(str_input)