############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PROJECT_DESCRIPTION

####################################### A B O U T #######################################
# In this module:


####################################### S T A R T #######################################
import os
import _cfg_GLOBAL as CFG
import LOG
import UTILITY as UTL
import datetime
#import shutil

#I create a different bug


def some_func():
    CFG.start_clock_module = datetime.datetime.now()
    LOG.write_me("\tSTART - ASCII.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")

    directory_in_path = os.getcwd() + CFG.input_path_ascii
    directory_in = os.fsencode(directory_in_path)
    list_not_only_ascii = list()
    list_only_ascii = list()

    LOG.write_me("\t\tWorking on the files in this path : " + os.path.relpath(directory_in.decode(), os.path.dirname(os.path.abspath(__file__))))
    LOG.write_me("\t\tdummy : '" + CFG.dummy + "'")
    empty_folder = True
    for n_file, file, c_files in UTL.list_of_files(directory_in):
        empty_folder = False
        path_e_file = directory_in.decode() + "\\" + file.decode()
        read_write(path_e_file, file, list_only_ascii, list_not_only_ascii)
    if empty_folder:
        UTL.empty_input_folder(directory_in_path)
    LOG.write_me("\t\tTotal Number of files : " + str(c_files))
    LOG.write_me(" ")

    LOG.write_me("\t\tList of file with only ASCII chars :")
    for item in list_only_ascii:
        LOG.write_me("\t\t" + str(item).rjust(35, ' '))
    LOG.write_me(" ")
    LOG.write_me("\t\tList of file with also NON-ASCII chars ():")
    for item in list_not_only_ascii:
        LOG.write_me("\t\t" + str(item).rjust(35, ' '))
    LOG.write_me(" ")
    LOG.write_me("\t\tFile created at the following location: " + CFG.output_path_ascii)
    LOG.write_me(" ")

    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - ASCII_ONLY.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")


def read_write(path_e_file, file, list_only_ascii, list_not_only_ascii):
    c_file = 1
    directory_out_path = os.getcwd() + CFG.output_path_ascii
    path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] + "_ascii_only" + ".txt"
    file_out = open(path_name_file_out, 'w')
    flag_only_ascii = True
    with open(path_e_file) as f:
        lines = f.readlines()
        last_line = len(lines)
        c_line = 0
        #for c_line in range(c_line, last_line):
        while c_line < last_line:
            # I skip the empty line
            line = lines[c_line]
            line_leaned = line.replace(" ", "")
            line_leaned = line_leaned.replace("\n", "")
            if line_leaned != "":
                if not all(ord(char) < 128 for char in line):
                    flag_only_ascii = False
                    if CFG.ascii_check == "\t\treplace_with_dummy":
                        line = "".join([x if ord(x) < 128 else CFG.dummy for x in line])
                    elif CFG.ascii_check == "skip_that_file":
                        file_out.write("this file will be removed")
                        file_out.close()
                        os.remove(path_name_file_out)
                        c_line = last_line  # a trick for: exiting the loop
                if all(ord(char) < 128 for char in line):
                    file_out.write(line)
            c_line = c_line + 1
            if c_line >= last_line and os.path.isfile(path_name_file_out):
                file_out.close()
    if flag_only_ascii == False:
        list_not_only_ascii.append(file)
    else:
        list_only_ascii.append(file)
    return list_only_ascii, list_not_only_ascii

if __name__ == '__main__':
    some_func()