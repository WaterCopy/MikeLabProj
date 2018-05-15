############################################-############################################
################################ F I L E  A U T H O R S  ################################
# see _doc_PROJECT_DESCRIPTION

####################################### A B O U T #######################################
# -  variabale that I need to share across the diverse modules (just import GLOBAL)

####################################### S T A R T #######################################

# GLOBAL VARIABLES
global input_file

# global input_file_clean
# global dat_input


############################################-############################################
################################### A T T E N T I O N ###################################
#                  Parameters for controlling the prg logic/processes
################################### A T T E N T I O N ###################################
############################################-############################################

# CONSTANT - rem what you want to skip (or put in last position what you want to do)
file_log = "LOG\_log.txt"

input_path_abc = "/INPUT_SPLIT/ABC(100)/REAL_DATA"
input_path_abc = "/INPUT_SPLIT/ABC(100)/TEST"
output_path_abc = "/OUTPUT_SPLIT/ABC(100)"

input_path_ascii = "/INPUT_ASCII/REAL_DATA"
input_path_ascii = "/INPUT_ASCII/TEST"
output_path_ascii = "/OUTPUT_ASCII"

input_path_binary = "/INPUT_BINARY/REAL_DATA"
input_path_binary = "/INPUT_BINARY/TEST"
output_path_binary = "/OUTPUT_BINARY"

input_path_ngram = "/INPUT_NGRAM/REAL_DATA"
input_path_ngram = "/INPUT_NGRAM/TEST"
output_path_ngram = "/OUTPUT_NGRAM"


############################################-############################################
# JOBS TO DO -
# rem what you want to skip (or put in last position what you want to do)
############################################-############################################

############################################
# PARAMETERS ABOUT SPLITTING
############################################
# on what source of data do you want to work?
source_of_data = "Twitter"
source_of_data = "ABC"

############################################
#  how do you wish splitting the file?
split_file = "split_by_line"
split_file = "split_by_size"
split_file = "split_by_fraction"
split_file = "none"

############################################
# if you have chosen to split the file by size please tell me the output file size
wanted_file_size = 20000  # this variable is used only if you choose to split the file by size

############################################
# if you have chosen to split the file by fraction please tell me how many output file you want
number_of_split = 4  # this variable is used only if you choose to split the file by fraction


############################################
# PARAMETERS ABOUT CHECK TEXT IS ASCII ONLY
############################################
# if non-ASCII chars are found in a file, what you what to do?
ascii_check = "skip_that_file"
#ascii_check = "replace_with_dummy"
#ascii_check = "none"

dummy = "1"
dummy = "0"


############################################
# PARAMETERS ABOUT MAKE_IT_BINARY
############################################
# on what source of data do you want to work?
binary_version = "none"
#binary_version = "8bit_version"
#binary_version = "7bit_version"



############################################
# PARAMETERS ABOUT N-GRAM CREATION
############################################
# on what source of data do you want to work? (any N+ is ok)
number_of_n_gram = "none"
number_of_n_gram = 1
number_of_n_gram = 2
#number_of_n_gram = 3
#number_of_n_gram = 4














######################################### E N D #########################################

