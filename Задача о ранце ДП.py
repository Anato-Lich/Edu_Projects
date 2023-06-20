n, C = map(int, input().split())

weight = [0]
cost = [0]

for i in range(0, n):
    w, c = map(int, input().split())
    weight.append(w)
    cost.append(c)
    

#----------------------------------------------------

din_Table = [[0]*(C+1)]
for i in range(0, n+1):
    din_Table.append([])
# print(din_Table)

#заполнение первого ряда таблицы
w = weight[1]
# print(w)
c = cost[1]
# print(c)
for i in range(0, C+1):
    if w > i:
        din_Table[1].append(0)
    else:
        din_Table[1].append(c)


# заполнение остальных динамически
for m in range(2, n+1):
    din_Table[m].append(0)
    for i in range(1, C+1):
        g1 = din_Table[m-1][i]
        
        
        idx = i - weight[m]
        if idx >= 0:
            g2 = din_Table[m-1][idx] + cost[m]
        else:
            g2 = 0
        # print(g1, g2)
        din_Table[m].append(max(g1, g2))

    
g = din_Table[n][C]

#-----------------------------------------------------------------
#получение использованых предметов
#-------------------------------------------------------------

used = [0]*n


check_m = n
check_c = C
for m in range(n, 0, -1):
    
    # print(din_Table[check_m][check_c])
    if din_Table[check_m][check_c] == din_Table[check_m-1][check_c - weight[check_m]] + cost[check_m]:
        used[m-1] += 1
        # print(m-1)
        check_c = check_c - weight[check_m]
    check_m -= 1
        
# print(used)

del(weight)
del(cost)
s = sum(used)

#---------------------------------------------------------
#вывод
#--------------------------------------------------------
print(g, s)
for i in range(n-1, -1, -1):
    if used[i] == 1:
        print(i)