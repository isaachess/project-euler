from decimal import *
import time
getcontext().prec = 1000

max_repeat_size = {
    'num': 0,
    'size': 0
}

def find_min_repeat(result_list, test_list, first_index_start, index_start):
    if len(test_list) is 0:
        return 0

    if index_start+len(test_list) > len(result_list):
        return 0

    compare_list = result_list[index_start:index_start+len(test_list)]
    if compare_list == test_list:
        return index_start - first_index_start
    else:
        return find_min_repeat(result_list, test_list, first_index_start, index_start+1)

def get_max_repeat_size(num):
    arbitrary_index_start = 4
    test_list_length = 4
    result = str(Decimal(1)/Decimal(num))
    result_list = list(result)
    test_list = list(result[arbitrary_index_start:arbitrary_index_start+test_list_length])
    return find_min_repeat(result_list, test_list, arbitrary_index_start, arbitrary_index_start+1)

t1 = time.time()
for num in range(1, 1001):
    repeat_size = get_max_repeat_size(num)
    if repeat_size > max_repeat_size.get('size'):
        max_repeat_size['num'] = num
        max_repeat_size['size'] = repeat_size
t2 = time.time()

print 'Done!', max_repeat_size.get('num'), max_repeat_size.get('size')
print t2-t1
