############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PACKAGE_DESCRIPTION

####################################### A B O U T #######################################
# In this module:
# small convininet code

####################################### S T A R T #######################################

import os
import _cfg_GLOBAL as CFG
import datetime
import LOG
import sys

# for n_file, file in enumerate(os.listdir(directory_in)):
def list_of_files(path):
    c_files = 0
    for n_item, file in enumerate(os.listdir(path)):
        if os.path.isfile(os.path.join(path, file)):
            c_files = c_files + 1
            yield n_item, file, c_files

def format_elapsed(clock_start):
    elapsed = datetime.datetime.now() - clock_start
    hours, decimals = divmod(elapsed.seconds, 3600)
    minutes, seconds = divmod(decimals, 60)
    microseconds = elapsed.microseconds
    elapsed_formatted = str(hours) + "." + str(minutes).rjust(2, "0") + "." + str(seconds).rjust(2, '0') + "." + str(microseconds).rjust(6, "0")
    return elapsed_formatted

def empty_input_folder(directory_in_path):
    LOG.write_me("\t\t The input folder is empty, please check | The program execution is interrupted")
    sys.exit("\t\tEmpty Input Folder '" + directory_in_path)