start_k = "Почтовое отделение"

R = {"Почтовое отделение" : [0, 2],
     "Ул. Грибоедова, 104/25" : [2, 5],
     "Ул. Бейкер стрит, 221б" : [5, 2],
     "Ул. Большая Садовая, 302-бис" : [6, 6],
     "Вечнозелёная Аллея, 742" : [8, 3]}

res = {}

for name, val in R.items():
    res[name] = {}
    for i, j in R.items():
        if name == i:
            continue
        else:
            res[name][i] = ((j[0] - R[name][0]) ** 2 + (j[1] - R[name][1]) ** 2) ** 0.5

def nearest_neighbor(cities, start):
    path = [start]
    current_city = start
    total_distance = 0
    ans = [start]
    all_dist = 0
    while len(cities) > (len(path)):
        dist = max(cities[current_city].values())
        for value in cities[current_city]:
            if ((value not in path) & (dist >= cities[current_city][value])):
                dist = cities[current_city][value]
                min_dist_key = value
        all_dist += dist
        total_distance += cities[current_city][min_dist_key]
        current_city = min_dist_key
        path.append(current_city)
        ans.append('->')
        ans.append(current_city)
        if len(ans) > 2:
            ans.append([all_dist])
    ans.append('->')
    ans.append(start)
    over_distance = cities[current_city][start]
    path.append(start)
    total_distance += over_distance
    ans.append([total_distance])

    return ans

def trans(street):
    for i in range(len(street)):
        try:
            if street[i] in R.keys():
                #street.pop([i])
                street[i] = tuple(R.get(street[i]))
        except TypeError:
            pass
    street.append('=')
    street.append(street[-2][0])
    ans = ''
    for i in street:
        if type(i) == list:
            ans = ans[0: -1]
            ans += str(i) + ' '
        else:
            ans += str(i) + ' '
    print(ans)


n = nearest_neighbor(res, start_k)
trans(n)
