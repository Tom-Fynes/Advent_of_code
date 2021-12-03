from collections import Counter


counter = 12
control = 0
gamma = []
epsilon = []
results = []

while control < counter:
    with open('input.txt') as f:
        file = f.readlines()
        for line in file:
            if control <= 11:
                line_list= list(line)
                results.append(line_list[control])
        data = Counter(results)
        gamma.append(data.most_common(1)[0][0])
        epsilon.append(data.most_common(2)[1][0])
        results.clear()
        control = control + 1

join_result = ''.join(gamma)
join_result2 = ''.join(epsilon)
print(int(join_result,2) * int(join_result2,2))



