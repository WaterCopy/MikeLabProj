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


def some_func():
    CFG.start_clock_module = datetime.datetime.now()
    LOG.write_me("\tSTART - SPLIT.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")

    if CFG.source_of_data == "ABC":
        LOG.write_me("\t\tParameters set for CFG.source_of_data : " + CFG.source_of_data)
        abc_file_list()
    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - INPUT_SPLIT.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")


def abc_file_list():
    directory_in_path = os.getcwd() + CFG.input_path_abc
    directory_in = os.fsencode(directory_in_path)
    dict_too_small = dict()
    dict_big_enough = dict()

    LOG.write_me("\t\tWorking on the files in this path : " + os.path.relpath(directory_in.decode(), os.path.dirname(os.path.abspath(__file__))))
    empty_folder = True
    for n_file, file, c_files in UTL.list_of_files(directory_in):
        empty_folder = False
        path_e_file = directory_in.decode() + "\\" + file.decode()
        if CFG.split_file == "split_by_line":
            read_write_single_line(n_file,path_e_file, file,  dict_too_small, dict_big_enough)
        if CFG.split_file == "split_by_size":
            read_write_by("split_by_size", n_file, path_e_file, file, dict_too_small, dict_big_enough)
        if CFG.split_file == "split_by_fraction":
            read_write_by("split_by_fraction", n_file, path_e_file, file, dict_too_small, dict_big_enough)
    if empty_folder:
        UTL.empty_input_folder(directory_in_path)
    LOG.write_me("\t\tTotal Number of files : " + str(c_files))
    LOG.write_me("")
    LOG.write_me("\t\tProcessed files - dict_big_enough[file]:")
    LOG.write_me("\t\tname".rjust(35, ' ') + "\t|\t size:")
    for key, value in dict_big_enough.items():
        LOG.write_me("\t\t" + str(key).rjust(35, ' ') + "\t|\t" + str(value))
    LOG.write_me("\t\tFile created at the following location: " + CFG.output_path_abc)
    LOG.write_me(" ")
    LOG.write_me("\t\tNot processed files - dict_too_small[file]:")
    LOG.write_me("\t\tname".rjust(35, ' ') + "\t|\t size:")
    for key, value in dict_too_small.items():
        LOG.write_me("\t\t" + str(key).rjust(35, ' ') + "\t|\t" + str(value))
    LOG.write_me(" ")

    # codice che temgo x memoria su copia file
    #directory_out_path = os.getcwd() + CFG.output_path_abc + "/" + CFG.split_file
    #directory_in_path + " are copied in " + directory_in.decode() + " : ")
    # for file in os.listdir(directory_in):
    #     file_from = os.getcwd() + CFG.input_path_ascii + "//" + file.decode()
    #     file_to = os.getcwd() + CFG.output_path_ascii + "//" + file.decode()
    #     shutil.copy(file_from, file_to)
    #     LOG.write_me("\t\t\t- " + file.decode())


def read_write_single_line(n_file, path_e_file, file, dict_too_small, dict_big_enough):
    at_least_one_good_line = False
    c = 0
    with open(path_e_file) as f:
        for line in f:
            # if there is any non ASCII I convert it into ""
            lineleaned = (''.join)([x for x in line if ord(x) < 128])
            # if there is any " " it into ""
            lineleaned = lineleaned.replace(" ", "")
            # if there is any return character "\n" I convert it into ""
            lineleaned = lineleaned.replace("\n", "")
            # as result I skip the empty line but I keep line with miked char (ASCII e non ASCII)
            if lineleaned != "":
                at_least_one_good_line = True
                c = c + 1
                directory_out_path = os.getcwd() + CFG.output_path_abc + "/" + CFG.split_file
                path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] + "_" + str(c) + ".txt"
                file_out = open(path_name_file_out, 'w')
                file_out.write(line)
                file_out.close()
    if at_least_one_good_line:
        dict_big_enough[file] = os.path.getsize(path_e_file)
    else:
        dict_too_small[file] = os.path.getsize(path_e_file)




def read_write_by(n_file, job_type, path_e_file, file, dict_too_small, dict_big_enough):
    file_size = os.path.getsize(path_e_file)
    if job_type == "split_by_fraction":
        CFG.wanted_file_size = file_size/CFG.number_of_split
        LOG.write_me("CFG.wanted_file_size : " + CFG.wanted_file_size)

    if file_size < CFG.wanted_file_size:
        dict_too_small[file] = file_size
    else:
        dict_big_enough[file] = file_size
        c_file = 1
        directory_out_path = os.getcwd() + CFG.output_path_abc + "/" + CFG.split_file
        path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] + "_" + str(c_file) + ".txt"
        file_out = open(path_name_file_out, 'w')
        with open(path_e_file) as f:
            lines = f.readlines()
            last_line = len(lines)
            c_line = 0
            for c_line in range (c_line,  last_line):
                # I skip the empty line
                line = lines[c_line]
                lineleaned = (''.join)([x for x in line if ord(x) < 128])
                lineleaned = lineleaned.replace(" ", "")
                lineleaned = lineleaned.replace("\n", "")
                if lineleaned != "":
                    file_out.write(line)
                    file_out_size = file_out.tell()
                    if file_out_size >= CFG.wanted_file_size:
                        file_out.close()
                        c_file = c_file + 1
                        path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] \
                                             + "_" + str(c_file) + ".txt"
                        file_out = open(path_name_file_out, 'w')
                c_line = c_line + 1
                if c_line == last_line:
                    file_out.close()
    return(dict_too_small, dict_big_enough)



if __name__ == '__main__':
    some_func()