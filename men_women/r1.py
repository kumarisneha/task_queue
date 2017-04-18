import time

def test():
    time.sleep(10)

def check(s):
    if(s== 'm'):
        result1 = "Male ticket done"
        test()
    else:
        result1 = "Female ticket done"
        test()
    return result1


