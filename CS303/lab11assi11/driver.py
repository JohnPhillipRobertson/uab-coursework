from uGraph import *
from time import perf_counter as p


def operate(fileName):
    tupni = open(fileName, "r")
    line = tupni.readline()
    i = -1
    dictio = {}
    while line != '':
        i += 1
        if i in [0, 1]:
            line = tupni.readline()
            continue
        else:
            x = [j.strip() for j in line.split(" ")]
            a = int(x[0])
            b = int(x[1])
            latter = [b]
            if a in dictio:
                dictio[a] = dictio[a] + latter
            else:
                dictio[a] = latter
            line = tupni.readline()
    tupni.close()

    nodes = []
    nodeDict = {}
    nodeNames = []
    #https://www.tutorialspoint.com/How-to-iterate-through-a-dictionary-in-Python
    #https://stackoverflow.com/questions/16475384/rename-a-dictionary-key
    for i in dictio.keys():
        n = Node(i)
        nodes.append(n)
        nodeDict[i] = n
        nodeNames.append(i)

    for i in nodes:
        dictio[i] = dictio.pop(i.name)


    for i, j in dictio.items():
        for k in j:
            if k not in nodeNames:
                n = Node(k)
                nodes.append(n)
                nodeNames.append(k)
                nodeDict[k] = n


    for i, j in dictio.items():
        for k in j:
            i.add([nodeDict[k]])

    del nodeDict
    start = nodes[0]
    graph = Ugraph(nodes)
    t = p()
    graph.bfs(start)
    print("The breadth-first search took {} seconds.\nHere's the path.".format(p() - t))
    for i in nodes:
        graph.print_path(start, i)

    #Below is optional debug code.
    #graph.printGraph()

#The first one is optional
#operate("tinyG.txt")
operate("mediumG.txt")
operate("largeG.txt")
