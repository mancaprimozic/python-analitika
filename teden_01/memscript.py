def my_func():
    a = [1]*10000
    b = [2]* 9000
    del b
    return a
