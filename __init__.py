############################################-############################################
################################ F I L E  A U T H O R S  ################################
# MIKE - see contacts in _doc_PACKAGE_DESCRIPTION

####################################### A B O U T #######################################
# This is the "main" from which the various module are called

####################################### S T A R T #######################################
if __name__ == '__main__':
    print("PRG START: __init________")

    import datetime
    import _cfg_GLOBAL as CFG
    import LOG
    import CLEAN
    import SPLIT
    import ASCII
    import BINARY
    import NGRAM


    CFG.start_clock_prg = datetime.datetime.now()
# 05 - LOG
    LOG.open_my_log()

# 08 - DELETE ALL OUTPUT FILES
    CLEAN.some_func()

# 10 - SPLIT (set available options in _cfg_GLOBAL.py )
    LOG.write_me("\tCFG.split_file : " + CFG.split_file)
    if CFG.split_file is not "none":
        SPLIT.some_func()
    else:
        LOG.write_me("\t\tParameters set for CFG.split_file : " + CFG.split_file)
        LOG.write_me("\t\tYou have chosen to make '" + CFG.split_file + "' split and therefore nothing there will be in the " + CFG.output_path_abc + " folders")

# 20 - ASCII (set available options in _cfg_GLOBAL.py )
    LOG.write_me("\tascii_check : " + CFG.ascii_check)
    if CFG.ascii_check is not "none":
        ASCII.some_func()
    else:
        LOG.write_me("\t\tYou have chosen to make '" + CFG.ascii_check + "' ASCII-check and therefore nothing there will be in the " + CFG.output_path_ascii + " folders")

# 30 - BYNARY (set available options in _cfg_GLOBAL.py )
    LOG.write_me("\tbinary_version : " + CFG.binary_version)
    if CFG.binary_version is not "none":
        BINARY.some_func()
    else:
        LOG.write_me("\t\tYou have chosen to make '" + CFG.binary_version + "' binary transformation and therefore nothing there will be in the " + CFG.output_path_binary + " folders")

# 40 - N=GRAM CREATION (set available options in _cfg_GLOBAL.py)
    LOG.write_me("\tnumber_of_n_gram : " + str(CFG.number_of_n_gram))
    if CFG.number_of_n_gram is not "none":
        NGRAM.some_func()
    else:
        LOG.write_me(
            "\t\tYou have chosen to make '" + CFG.number_of_n_gram + "' n-gram generation and therefore nothing there will be in the " + CFG.output_path_ngram + " folders")

    LOG.close_my_log()

    print("PRG END: __init________")
    print("######################################### E N D #########################################")
######################################### E N D #########################################