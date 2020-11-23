n = int(input())
x = [float(x) for x in input().split()]
y = [float(y) for y in input().split()]
mean_x = sum(x) / n
arr_x = [(x - mean_x) for x in x]
arr_x2 = [(x - mean_x) ** 2 for x in x]
sd_x = (sum(arr_x2) / n) ** 0.5
mean_y = sum(y) / n
arr_y = [(y - mean_y) for y in y]
arr_y2 = [(y - mean_y) ** 2 for y in y]
sd_y = (sum(arr_y2) / n) ** 0.5
arr_xy = [(x * y) for x, y in zip(arr_x, arr_y)]
p = sum(arr_xy) / (n * sd_x * sd_y)
print(round(p, 3))
