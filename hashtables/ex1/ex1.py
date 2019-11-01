#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # make tuples out of the weights with enumerate and insert into hash table where
    # weight is the key and its index is the value
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    # for those tuples, check the table for limit - weight as the difference
    # if difference exists in table, then those weights sum up to limit
    for index, weight in enumerate(weights):
        difference = limit - weight
        key = hash_table_retrieve(ht, difference)
        if key is not None:
            if key >= index:
                return (key, index)
            else:
                return (index, key)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
