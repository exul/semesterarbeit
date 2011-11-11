import matplotlib.pyplot as plot

xs = [2, 3, 5, 7, 11]
ys = [4, 9, 5, 9, 1]
plot.plot(xs, ys)
plot.savefig("squaremod10.png")

f = open('result.txt', 'r')
list_x = list()
list_y = list()

for line in f:
    x, y = line.split()

    list_x.append(x)
    list_y.append(y)

plot.plot(list_x, list_y)
plot.savefig("tsp.png")
