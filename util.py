from time import time

def __print_time(generator_name, seq_len, loops_num, time ):
    message=""
    message += "===============================================\r\n"
    message += "Generator " + generator_name +"\r\n"
    message += "===============================================\r\n"
    message += ("length of random sequence:  " + str(seq_len)+"\r\n")
    message += ("number of loops:            " + str(loops_num)+"\r\n")
    message += ("total time:                 " + str(round(time,6))+" seconds\r\n")
    message += ("time per loop:              " + str(round(time/loops_num,6))+" seconds\r\n")
    message += "===============================================\r\n"
    print(message)


def test_speed_lcg(function, generator_name, seq_len, loops_num):
    start = time()
    for i in range(0, loops_num):
        function(1, seq_len)
    end = time()
    __print_time(generator_name, seq_len, loops_num, end - start)
