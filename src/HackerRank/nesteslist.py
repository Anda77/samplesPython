nested_list = [['cherry', 7], ['apple', 100], ['anaconda', 1360]]

print(nested_list)


def my_max_by_weight(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored
        # in their second element.
        if item[1] > maximum[1]:
            maximum = item

    return maximum


print(my_max_by_weight(nested_list))
