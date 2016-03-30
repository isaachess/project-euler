from decimal import *
import time
getcontext().prec = 1000

max_repeat_size = {
    'num': 0,
    'size': 0
}

arbitrary_index_start = 4
test_length = 7
num_max = 1000

def iterative():
    max_repeat_size = {
        'num': 0,
        'size': 0
    }

    def find_min_repeat(result, test):
        # import ipdb; ipdb.set_trace()
        if len(test) is 0:
            return 0

        index = arbitrary_index_start+1
        while index < num_max+1:
            if index+len(test) > len(result):
                return 0
            compare = int(result[index:index+len(test)])
            if compare == int(test):
                return index - arbitrary_index_start
            index += 1
        return 0

    def get_max_repeat_size(num):
        result = str(Decimal(1)/Decimal(num))
        test = result[arbitrary_index_start:arbitrary_index_start+test_length]
        return find_min_repeat(result, test)

    t1 = time.time()
    for num in range(1, num_max+1):
        repeat_size = get_max_repeat_size(num)
        if repeat_size > max_repeat_size.get('size'):
            max_repeat_size['num'] = num
            max_repeat_size['size'] = repeat_size
    t2 = time.time()

    print 'Done!', max_repeat_size.get('num'), max_repeat_size.get('size')
    print t2-t1

def recursive():
    max_repeat_size = {
        'num': 0,
        'size': 0
    }

    def find_min_repeat(result, test, index_start):
        if len(test) is 0:
            return 0

        if index_start+len(test) > len(result):
            return 0

        compare_list = result[index_start:index_start+len(test)]
        if compare_list == test:
            return index_start - arbitrary_index_start
        else:
            return find_min_repeat(result, test, index_start+1)

    def get_max_repeat_size(num):
        result = str(Decimal(1)/Decimal(num))
        test = result[arbitrary_index_start:arbitrary_index_start+test_length]
        return find_min_repeat(result, test, arbitrary_index_start+1)

    t1 = time.time()
    for num in range(1, num_max+1):
        repeat_size = get_max_repeat_size(num)
        if repeat_size > max_repeat_size.get('size'):
            max_repeat_size['num'] = num
            max_repeat_size['size'] = repeat_size
    t2 = time.time()

    print 'Done!', max_repeat_size.get('num'), max_repeat_size.get('size')
    print t2-t1

recursive()
iterative()
