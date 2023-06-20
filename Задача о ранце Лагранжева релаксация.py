from solver import ListSolver
# def ListSolver(n, C, weight, cost):

#     l = [[-1, -1, 0, 0]]
#     res_l = []

#     tmp = []
#     tmp.append([0, 1, l[0][2], l[0][3]])
#     tmp.append([1, 1, l[0][2] + weight[1], l[0][3] + cost[1]])

#     l = tmp.copy()
#     # del(tmp)
#     # print(l)
#     res_l.append(l)
#     # print(res_l)

#     for i in range(2, n+1):
#         tmp = []
#         for j in range(0, len(l)):
#             sample = l[j].copy()
#             if (sample[2] + weight[i] <= C):
#                 tmp.append([1, j+1, sample[2] + weight[i], sample[3] + cost[i]])
#         # print('tmp: ', tmp)

#         # merge
#         idx_tmp = 0
#         idx_l = 0
#         new_l = []


#         while ((idx_l < len(l)) and (idx_tmp < len(tmp))):
#             #dom
#             if (l[idx_l][2] <= tmp[idx_tmp][2]) and (l[idx_l][3] >= tmp[idx_tmp][3]):
#                 # del(tmp[idx_tmp])
#                 idx_tmp += 1

#             elif (tmp[idx_tmp][2] <= l[idx_l][2]) and (tmp[idx_tmp][3] >= l[idx_l][3]):
#                 idx_l += 1

#             elif l[idx_l][2] <= tmp[idx_tmp][2]:
#                 new_l.append([0, idx_l + 1, l[idx_l][2], l[idx_l][3]])
#                 # del(l[idx_l])
#                 idx_l += 1

#             else:
#                 new_l.append(tmp[idx_tmp])
#                 # del(tmp[idx_tmp])
#                 idx_tmp += 1


#         for i in range(idx_l, len(l)):
#             new_l.append([0, i + 1, l[i][2], l[i][3]])

#         for i in range(idx_tmp, len(tmp)):
#             new_l.append(tmp[i])

#         # del(l)
#         # print(new_l)
#         l = new_l.copy()
#         # del(new_l)
#         # print(l)
#         # print()
#         res_l.append(l)
#         # print(res_l)

#     used = [0]*n

#     idx = len(res_l[n-1]) - 1
#     max_ = res_l[n-1][-1][3]
#     # print(idx, max_)

#     for i in range(n-1, -1, -1):
#         # print(i, idx)
#         if res_l[i][idx][0]:
#             used[i] = 1
#         idx = res_l[i][idx][1] - 1
#     # print(used)
    
#     used_list = []
#     # print(max_, sum(used))
#     for i in range(n-1, -1, -1):
#         if used[i]:
#             # print(i)
#             used_list.append(i)
#     return max_, used_list



n, m = map(int, input().split())

C = [0]
inp = input().split()
for elem in inp:
    C.append(int(elem))

price = [0]
inp = input().split()
for elem in inp:
    price.append(int(elem))   
    
weight = [[0]]
for i in range(0, m):
    weight.append([0])
# print(weight)

for i in range(0, n):
    # weight.append([0])
    inp = input().split()
    for j in range(0, m):
        weight[j+1].append(int(inp[j]))

    
# print(n, m, C, price, weight)


# g_j - задача об одномерном рюкзаке
# g_j = C_j - w_ij*x_i
# def ListSolver(n, C, weight, cost):

w = weight[-1].copy()
# print(w)
l = []
for i in range(0, m-1):
    l.append(1)
# print(l)

old_D = 0
# начало обучения
for cnt in range(0, 20000):
    New_C = 0
    New_cost = [0]
    for i in range(0, n):
        New_cost.append(price[i+1])

    for i in range(0, m-1):
        # print(i)
        New_C += l[i]*C[i+1]
        for j in range(0, n):
            # print(j)
            # print('w', weight[i+1][j+1])
            New_cost[j+1] -= l[i]*weight[i+1][j+1]

    # print('C, Cost', New_C, New_cost)
    res, used = ListSolver(n, C[-1], w, New_cost)
    
    # print(res, used)
    if res < 0:
        res = 0
        used = []
    D = res + New_C
    # print(D)
        
    dot = []
    # print()
    for i in range(0, len(l)):
        dot_tmp = 0
        # for j in range(0, n):
        for j in used:
            dot_tmp += weight[i+1][j+1] #*used[j]
        dot.append(C[i+1] - dot_tmp)
    # grad = C[-1] - dot
    # print('1', dot)

    norm = 0
    sq_sum = 0
    for i in range(0, len(dot)):
        sq_sum += dot[i]**2
    norm = (sq_sum)**(1/2)
    norm += 1e-6
    
    # if norm <= 1e-6:
    #     break
    # print('2', dot)
    a = 1 / (cnt+1)
    for i in range(0, len(l)):
        l[i] -= a * dot[i] / norm
        if l[i] < 0:
            l[i] = 0

    
    # if cnt % 100 == 0:
    #     print(l, used, dot, cnt)

    
New_C = 0
New_cost = [0]
for i in range(0, n):
    New_cost.append(price[i+1])

for i in range(0, m-1):
    # print(i)
    New_C += l[i]*C[i+1]
    for j in range(0, n):
        # print(j)
        # print('w', weight[i+1][j+1])
        New_cost[j+1] -= l[i]*weight[i+1][j+1]

# print('C, Cost', New_C, New_cost)
res, used = ListSolver(n, C[-1], w, New_cost)
# print(res, used)
if res < 0:
    res = 0
    used = []
D = res + New_C

print(D)
for elem in l:
    print(elem)
