import UserString

__author__ = 'rami'


def bubble_sort( my_list ):
    ret_list = list(my_list)
    swapped = True
    while swapped:
        swapped = False
        for i in xrange(1,len(my_list)):
            if ret_list[i-1]>ret_list[i]:
                tmp = ret_list[i-1]
                ret_list[i-1]=ret_list[i]
                ret_list[i]=tmp
                swapped = True

    return ret_list


def binary_search( array, lower, upper, target ):
    pos = (upper - lower) /2
    i=lower+pos
    if pos == 0:
        if array[i] == target:
            return i
        else:
            return -1

    if target < array[i]:
        return binary_search(array, lower, i-1, target)
    else:
        return binary_search(array, i+1, upper, target)


def str_del_char(str, index):
     s=UserString.MutableString(str)
     del s[index]
     return s.data


########################
def _append_char_to_list(char, str_list):
    ret_list = []
    for str in str_list:
        ret_list.append(char+str)
    return ret_list


def get_str_permutations(str):
    ret_permutations = []
    if len(str) == 1:
        return [str,]

    for i in xrange(0, len(str)):
        str_left_chars=str_del_char(str, i)
        str_left_chars_permutations = get_str_permutations(str_left_chars)
        ret_permutations.extend(_append_char_to_list(str[i],str_left_chars_permutations))
    return ret_permutations



