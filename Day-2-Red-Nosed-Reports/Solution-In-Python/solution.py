safe, unsafe = 0,0
with open('../data.txt', 'r')  as file:
    data = [[int(i) for i in line.split()] for line in file]
difference = [[i[j] - i[j + 1] for j in range(len(i) - 1)] for i in data]

results =[]
for i in difference:
    res = []
    for j in i:
        if j > 3 or j <- 3 or j == 0:
            res.append("UNSAFEEX")
        else:
            if j > 0:
                res.append('SAFEE')
            else:
                res.append('UNSAFEE')

    results.append(res)
for i in results:
    if len(set(i)) == 1:
        safe += 1
    else:
        unsafe += 1

print(f"SAFE is {safe}\nUNSAFE is {unsafe}")
#!/usr/bin/python

# with open('../data.txt', 'r') as f:
#     content = f.read().strip().split('\n')

# ans = 0
# for report in content:
#     values = list(map(int, report.split()))
#     safepos = set([1, 2, 3])
#     safeneg = set([-1, -2, -3])
#     for i in range(1, len(values)):
#         safepos.add(values[i] - values[i - 1])
#         safeneg.add(values[i] - values[i - 1])

#     if len(safepos) == 3 or len(safeneg) == 3:
#         ans += 1

# print(ans)