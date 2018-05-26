import time, inspect
from os.path import basename

start_time = time.time()

def Answer(answer):
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    print("------------------------------------------------")
    print("   " + basename(filename))
    print("   The Answer is: %s" %answer)
    print("   Time Elasped: %ssec" %(time.time() - start_time))
    print("------------------------------------------------")
