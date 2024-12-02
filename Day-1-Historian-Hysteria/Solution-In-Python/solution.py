with open("../data.txt", "r") as file:

    left_list = []
    right_list = []
    total = 0

    for x in file:
        data = x.split(" ")
        left_list.append(data[0])
        right_list.append(data[3])
    
    left_list = sorted([int(i) for i in left_list])
    right_list = sorted([int(i) for i in right_list])

    for i in range(len(left_list)):
        if left_list[i] >= right_list[i]:
            total += left_list[i] - right_list[i]
        else:
            total += right_list[i] - left_list[i]

    print(total)

# Part Two
total_two = 0
for i in left_list:
    total_two += i * right_list.count(i)    
        
print(total_two)
