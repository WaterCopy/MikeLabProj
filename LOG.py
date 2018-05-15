############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PACKAGE_DESCRIPTION

####################################### A B O U T #######################################
# In this module:
# I log the program activities

####################################### S T A R T #######################################

import os
import _cfg_GLOBAL as CFG
import datetime
import UTILITY as UTL

def open_my_log():
    CFG.path_name_file_log = os.getcwd() + "\\" + CFG.file_log
    CFG.file_log = open(CFG.path_name_file_log, 'w')
              ####################################### S T A R T #######################################
    write_me("###################################### A B A C U S ######################################")
    write_me("                    Advanced Basic Accessory Computing Useless Stuff                     ")
    write_me("############################################-############################################")
    write_me("")
    write_me("\tOPEN - LOG.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")
    write_me("")
    write_me("")


def write_me(log_string):
    CFG.file_log.write(log_string + "\n")
    print(log_string)


def close_my_log():
    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_prg)
    write_me("\tCLOSE - LOG.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    print("")
    CFG.file_log.close()


