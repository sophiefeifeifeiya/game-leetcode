def shortest_way(source, target):
    subsequences_count = 0
    i = 0 

    while i < len(target):
        subsequence_1_length = 0 
        j = 0 
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                subsequence_1_length += 1
                i += 1
            j += 1
        if subsequence_1_length == 0:
            return -1
        subsequences_count += 1
    return subsequences_count



print(shortest_way("abc", "abcbc")) # 2
print(shortest_way("abc", "acdbc")) # -1
print(shortest_way("xyz", "xzyxz")) # 3


