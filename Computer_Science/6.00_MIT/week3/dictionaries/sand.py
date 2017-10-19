'''
    Sandbox space to experiment with Python
'''


def how_many(my_dict):
    '''
        my_dict: dictionary, all values are list

        returns: int, how many values are in the dictionary.
    '''
    total = 0
    for i in my_dict.values():
        total += len(i)
    return total

def biggest(my_dict):
    '''
        my_dict: dictionary, all values are list

        returns: key, Key with largest number of values associated with it
    '''
    keys = my_dict.keys()#[0]
    size = 0
    for i in keys:
        if len(my_dict[i]) > size:
            key = i
            size = len(my_dict[key])
    return key

MY_DICT = {'u': [10, 15, 5, 2, 6], 'B': [15]}
print(how_many(MY_DICT))
print(biggest(MY_DICT))
