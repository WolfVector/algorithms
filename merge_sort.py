def merge_sort(array):
    if(len(array) == 1): 
        return array

    half = int(len(array) / 2)
    first_half = merge_sort(array[:half])
    second_half = merge_sort(array[half:])

    return merge(first_half, second_half)

def merge(first_half, second_half):
    len1 = len(first_half)
    len2 = len(second_half)
    size = len1 + len2
    array = []
    i = 0
    j = 0

    print(first_half, second_half)

    for k in range(size):
        if(j >= len2 or (i < len1 and first_half[i] < second_half[j])): 
            array.append(first_half[i])
            i += 1
        elif(j < len2):
            array.append(second_half[j])
            j += 1

    return array     


print("\n" + str(merge_sort([42, 12, 1, 4, 65, 9, 1])))
