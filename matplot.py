import matplotlib.pyplot as plot
# plot mst
f_mst = open('mst_nodes.txt', 'r')
list_x = list()
list_y = list()

# plot every seond node (one edge)
i = 0
for line in f_mst:
    if i % 2 == 0:
        list_mst_x = list()
        list_mst_y = list()

        x, y = line.split()

        list_mst_x.append(x)
        list_mst_y.append(y)
    else:
        x, y = line.split()

        list_mst_x.append(x)
        list_mst_y.append(y)

        plot.plot(list_mst_x, list_mst_y, marker='o',color='#ff0000')
    i += 1

plot.savefig("mst.png")


# plot matching 
# =============
f_match= open('matching_nodes.txt', 'r')
list_x = list()
list_y = list()

#plot every seond node (one edge)
i = 0
for line in f_match:
   if i % 2 == 0:
       list_mst_x = list()
       list_mst_y = list()

       x, y = line.split()

       list_mst_x.append(x)
       list_mst_y.append(y)
   else:
       x, y = line.split()

       list_mst_x.append(x)
       list_mst_y.append(y)

       plot.plot(list_mst_x, list_mst_y, marker='o',color='#0000ff')
   i += 1

plot.savefig("matching.png")

# plot tsp
# ========
f = open('result.txt', 'r')
for line in f:
    x, y = line.split()

    list_x.append(x)
    list_y.append(y)


plot.plot(list_x, list_y, marker='o',color='#000000')
plot.savefig("tsp.png")
