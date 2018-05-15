############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PACKAGE_DESCRIPTION

####################################### A B O U T #######################################
# In this module:


####################################### S T A R T #######################################
import os
import _cfg_GLOBAL as CFG
import LOG
import UTILITY as UTL
import datetime
import nltk
import pandas as pd

def some_func():
    CFG.start_clock_module = datetime.datetime.now()
    LOG.write_me("\tSTART - NGRAM.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")

    directory_in_path = os.getcwd() + CFG.input_path_ngram
    directory_in = os.fsencode(directory_in_path)
    LOG.write_me("\t\tWorking on the files in this path : " + os.path.relpath(directory_in.decode(), os.path.dirname(os.path.abspath(__file__))))
    empty_folder = True
    for n_file, file, c_files in UTL.list_of_files(directory_in):
        empty_folder = False
        path_e_file = directory_in.decode() + "\\" + file.decode()
        read_write(path_e_file, file)
    if empty_folder:
        UTL.empty_input_folder(directory_in_path)
    LOG.write_me("\t\tTotal Number of files : " + str(c_files))
    LOG.write_me("\t\tFile created at the following location: " + CFG.output_path_ngram)

    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - NGRAM.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")

def read_write(path_e_file, file): #, list_only_ascii, list_not_only_ascii):
    c_file = 1
    directory_out_path = os.getcwd() + CFG.output_path_ngram

    path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] + "_ngram_" + str(CFG.number_of_n_gram) + "grams.txt"
    file_out = open(path_name_file_out, 'w')
    with open(path_e_file) as f:
        lines = f.readlines()
        last_line = len(lines)
        c_line = 0
        while c_line < last_line:
            line = lines[c_line]
            print("line : ", line)
            #### I have decided that the "cleaning" of the rows:
            #### - has to be done in a specific module
            #### - has to be done parametric in order to decide qhat we want to keep
            # line_no_trailing = (line.rstrip()).lstrip()
            # print("line_no_trailing : ", line_no_trailing)
            # print("line_no_trailing : ", line_no_trailing)
            # print(line_no_trailing.split())
            # print(line_no_trailing.split())
            line_split = line.split()
            grams = nltk.ngrams(line_split, CFG.number_of_n_gram)
            for i in range(CFG.number_of_n_gram):
                my_index = ("n_gram" + "_" + str(i))

            lines_as_ngram_df = pd.DataFrame()
            for i_gram in grams:
                print(i_gram)
                print(i_gram[0])
                my_index =

                tmp = pd.Series(i_gram, index=my_index)
                #tmp = i_gram.grouper.result_index.values
                lines_as_ngram_df = lines_as_ngram_df.append(tmp)

            file_out.write(line_as_ngram + "\n")
            c_line = c_line + 1
    file_out.close()
    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - NGRAM.py (" + tmp_input_file + " | " + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")