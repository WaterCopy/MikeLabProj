############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PACKAGE_DESCRIPTION

####################################### A B O U T #######################################
# In this module:
# I clean the out put directories

####################################### S T A R T #######################################

import _cfg_GLOBAL as CFG
import os
import LOG
import UTILITY as UTL
import datetime


def some_func():
    CFG.start_clock_module = datetime.datetime.now()
    LOG.write_me("\tSTART - CLEAN.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")

    my_root_dir = os.getcwd()
    list_output_dir = list()
    list_of_files = list()

    LOG.write_me("\t\tList of the files deleted from the 'OUTPUT' folders:")
    for root, dirs, files in os.walk(my_root_dir):
        if not str(root).endswith("ABACUS"):
            if "OUTPUT_" in str(root):
                    for file in files:
                        if str(file).endswith(".txt"):
                            rel_path_file = os.path.relpath(root, my_root_dir) + "/" + file
                            LOG.write_me("\t\t- " + rel_path_file )
                            path_file = root + "\\" + file
                            os.remove(path_file)
                            list_of_files.append(rel_path_file)
    if len(list_of_files) == 0:
        LOG.write_me("\t\t\t- No output file to clean")
    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - CLEAN.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")
if __name__ == '__main__':
    some_func()