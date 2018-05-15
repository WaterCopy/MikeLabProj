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
    LOG.write_me("\tSTART - BINARY.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + ")")

    directory_in_path = os.getcwd() + CFG.input_path_binary
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
    LOG.write_me("\t\tFile created at the following location: " + CFG.output_path_binary)

    elapsed_formatted = UTL.format_elapsed(CFG.start_clock_module)
    LOG.write_me("\tEND - BINARY.py (" + datetime.datetime.now().strftime("%y-%m-%d | %H:%M") + " | hh.mm.ss.ms " + elapsed_formatted + ")")
    LOG.write_me("")
    LOG.write_me("")


def read_write(path_e_file, file):
    c_file = 1
    directory_out_path = os.getcwd() + CFG.output_path_binary
    path_name_file_out = directory_out_path + "\\" + os.path.splitext(file.decode())[0] + "_bin" + CFG.binary_version[:4] + ".txt"
    file_out = open(path_name_file_out, 'w')
    with open(path_e_file) as f:
        lines = f.readlines()
        last_line = len(lines)
        c_line = 0
        while c_line < last_line:
            line = lines[c_line]
            line_no_trailing = line.rstrip()
            if CFG.binary_version is "7bit_version":
                n = 7
                bin_version = "07b"
            if CFG.binary_version is "8bit_version":
                n = 8
                bin_version = "08b"
            assembled_line_in_binary_0nb = ""
            for char in line_no_trailing:
                char_in_bytes = char.encode()
                char_in_integers = int.from_bytes(char_in_bytes, byteorder='big')
                char_0nb_version = format(char_in_integers, bin_version).ljust(n, "0")
                assembled_line_in_binary_0nb = assembled_line_in_binary_0nb + char_0nb_version
            file_out.write(assembled_line_in_binary_0nb+"\n")
            c_line = c_line + 1
        file_out.close()



        ### lascio queste righe giusto per promemoria dei diversi approcci che potrei usare
                #line_no_trailing_in_bytes = line_no_trailing.encode()
                #line_no_trailing_in_integers = int.from_bytes(line_no_trailing_in_bytes, byteorder='big')
                #line_no_trailing_in_binary_bin = bin(line_no_trailing_in_integers)
                # line_no_trailing_in_binary_08b = format(line_no_trailing_in_integers, '08b')
                # line_no_trailing_in_binary_c08b = format(line_no_trailing_in_integers, '#08b')
                # assembled_line_in_binary_08b = line_no_trailing_in_binary_bin[2:]
                # print("line_no_trailing_in_binary_bin : ", str(line_no_trailing_in_binary_bin))
                # print("line_no_trailing_in_binary_08b : ", str(line_no_trailing_in_binary_08b))
                # print("line_no_trailing_in_binary_c08b : ", str(line_no_trailing_in_binary_c08b))
                # print("assembled_line_in_binary_08b : ", str(assembled_line_in_binary_08b))
                # print("______")
                # print("str(int(assembled_line_in_binary_08b, base=2)) : ", str(int(assembled_line_in_binary_08b, base=2)))
                # print("str(int(assembled_line_in_binary_08b, base=2))", str(int(assembled_line_in_binary_08b, base=2)))
                # print("str(int(assembled_line_in_binary_08b, base=2)) : ", str(int(assembled_line_in_binary_08b, base=2)))
                # print("str(line_no_trailing_in_integers)) : ", str(line_no_trailing_in_integers))
            #file_out.write(line_no_trailing_in_binary)
