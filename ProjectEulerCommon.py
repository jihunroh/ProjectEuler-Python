import time, inspect

def Answer(answer):
    start_time = time.time()
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    print("------------------------------------------------")
    print("   " + filename)
    print("   The Answer is: %s" %answer)
    print("   Time Elasped: %ssec" %(time.time() - start_time))
    print("------------------------------------------------")
