# debug global method
def debug(msg, prefix=""):
    print("\033[45m DEBUG: \033[00m", end="")
    if prefix:
        print("\033[41m", prefix, "\033[00m", end="")
        
    print("\033[91m", msg, "\033[00m")
