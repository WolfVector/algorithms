def merge_sort(array):
    if(len(array) == 1): 
        return array, 0

    half = int(len(array) / 2)
    first_half, left_inv = merge_sort(array[:half])
    second_half, right_inv = merge_sort(array[half:])

    sorted_array, split_inv = merge(first_half, second_half)
    return (sorted_array, left_inv + right_inv + split_inv)

def merge(first_half, second_half):
    len1 = len(first_half)
    len2 = len(second_half)
    size = len1 + len2
    array = []
    i = 0
    j = 0
    inv = 0;

    print(first_half, second_half)

    for k in range(size):
        if(j >= len2 or (i < len1 and first_half[i] < second_half[j])): 
            array.append(first_half[i])
            i += 1
        elif(j < len2):
            array.append(second_half[j])
            j += 1
            inv += len1 - i

    return array, inv     

#[42, 12, 1, 4, 65, 9, 13]
print("\n" + str(merge_sort([42, 12, 1, 4, 65, 9, 13])))
