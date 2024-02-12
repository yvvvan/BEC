# scoreChanges: [[10, 5, -10], [0, 0, 10]],
# scoreChanges: [[-10, -5, 5], [-5, -10, 5]],
# scoreChanges: [[10, -5, 5], [-10, 5, 5]]
# scoreChanges: [[10, -10, -10], [5, 5, 10]]
# scoreChanges: [[-5, 10, 10], [10, -5, -10]]

scoreChanges = [[[10, 0, -5], [-5, -5, 5]] , 
                [[5, -10, -5], [5, 10, 10]] , 
                [[10, 5, -10], [-5, 0, 10]], 
                [[-10, -5, 5], [-5, -10, 5]], 
                [[10, -5, 5], [-15, 5, 5]],
                [[5, -10, -10], [-5, 5, 10]],
                [[-5, 10, 10], [10, -5, -10]]]

initial = [50,50,50]

end = [initial]
end_temp = []


for i in range(7):
    for stat in end:
        stat1 = list(map(lambda x :x[0]+x[1]*2 ,zip(stat,scoreChanges[i][0]))) 
        stat2 = list(map(lambda x :x[0]+x[1]*2 ,zip(stat,scoreChanges[i][1]))) 
        if stat1 not in end_temp:
            end_temp.append(stat1)
        if stat2 not in end_temp:
            end_temp.append(stat2)
    end = []
    for stat in end_temp:
        end.append(stat)
    end_temp = []
print(end)
print(len(end))


sorted_list = sorted(end, key=lambda x: (x[0], x[1], x[2]))
for state in sorted_list:
    for i in state:
        if i <= 0:
            print(state)
            break

