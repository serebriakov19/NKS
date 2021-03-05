# Лабораторна робота №1
# Виконав студент групи ІО-71 Серебряков Роман
# Варіант №22

times = [315, 245, 11, 290, 47, 49, 595, 618, 559,
         530, 369, 1035, 546, 673, 11, 314, 1156, 33,
         1201, 1055, 241, 91, 6, 1596, 680, 1100, 97,
         307, 771, 2063, 46, 25, 42, 112, 124, 245,
         19, 214, 719, 38, 278, 285, 719, 274, 110,
         543, 72, 176, 650, 2105, 546, 1088, 187, 36,
         213, 148, 813, 933, 857, 1512, 669, 307, 41,
         190, 99, 215, 260, 363, 388, 532, 1486,
         1445, 516, 351, 497, 67, 1200, 142, 50, 629,
         252, 410, 772, 973, 13, 410, 1401, 1656,
         721, 75, 243, 1318, 535, 629, 266, 487, 349,
         38, 95, 1533]

gamma = 0.98
time1 = 1098
time2 = 2055

interval_len = 0
list_of_intervals = []
stat_densities = []
P_list = []

times.sort()
Tcp = sum(times) / len(times)


def get_T(gamma):
    global interval_len, stat_densities, list_of_intervals, P_list
    interval_len = (times[-1] - times[0]) / 10

    for i in range(0, 10):
        list_of_intervals.append([a for a in times if (i * interval_len <= a <= (i + 1) * interval_len)])

    stat_densities = [len(interval) / (len(times) * interval_len) for interval in list_of_intervals]
    area_sum = 1
    for i in range(10):
        P_list.append(area_sum)
        area_sum -= stat_densities[i] * interval_len

    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])

    index_less = P_list.index(p_less)

    d = (p_less - gamma) / (p_less - p_more)
    T = (interval_len * index_less) - interval_len * d
    return T


def P(time):

    Sum = 1
    whole_intervals = int(time // interval_len)
    for i in range(whole_intervals):
        Sum -= stat_densities[i] * interval_len
    Sum -= stat_densities[whole_intervals] * (time % interval_len)
    return Sum


def lamb(time):
    f = stat_densities[int(time // interval_len)]
    p = P(time)
    return f / p


print("Середній наробіток до відмови Tср = {} \n".format(Tcp))

print("γ-відсотковий наробіток на відмову Tγ при (γ = {}) = {} \n".format(gamma, get_T(gamma)))

print("Ймовірність безвідмовної роботи на час {} годин = {} \n".format(time1, P(time1)))

print("Інтенсивність відмов на час {} годин = {} ".format(time2, lamb(time2)))
