'''
BINARY SEARCH
'''
def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:

        # mid = (low + high) // 2  # not correct - could cause integer overflow
        mid = low + (high - low) / 2 # proper way
        mid_value = list[mid]

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return mid # value found!
        
    return -1 # value not found


list = [4, 7, 8, 12, 45, 99, 102]

print(binary_search(list, 8))

