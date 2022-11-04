def sum_pairs(lst, num):
    lenght = len(lst)
    print(lenght)
    pair = []
    for i in range(lenght-2):
        if (lst[i] + lst[i+1]) == num:
            pair.append(lst[i])
            pair.append(lst[i+1])
            return pair
    return pair

print(sum_pairs([1,3,5,8], 4))