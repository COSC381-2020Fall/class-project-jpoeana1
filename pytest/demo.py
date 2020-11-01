import sys

def find_min(arr):
    if arr is None:
        print('fatal error: input array should not be none', file=sys.stderr)
        return

    if not arr:
        return None

    min_number = arr[0]
    for num in arr:
        if num < min_number:
            min_number = num
        
    return min_number

def helper():
    print("find_min(arr): it's a  function to find out the minimal number in an array")
