__author__ = 'rami'


def convert_int_to_str(num):
    n = num
    ret_str = ''
    while n>0:
        r_digit = int((float(n)/10 - n/10)*10+0.1) # add 0.1 due to a float inexactitud issue
        n /= 10
        ret_str = str(r_digit) + ret_str

    return ret_str

def convert_str_to_int(str):
    ret_int = 0
    for i in str:
        ret_int *= 10
        ret_int += int(i)

    return ret_int
