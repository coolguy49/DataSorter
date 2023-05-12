def find_mean(arr):
    num = 0
    for x in arr:
        num += x
    return(num / len(arr))

# def find_range(arr):
#     print(len(arr))
#     print(type(len(arr)))
#     return(arr[len(arr)] - arr[1])

print(find_mean([1234, 546, 2352, 2453, 5756871, 1, 1, 1, 1, 1]))
# print(find_range([1, 2, 3]))
    
