from uGraph import *
from time import perf_counter as p

def operate(fileName):
    tupni = open(fileName, "r")
    line = tupni.readline()
    dictio = {}
    weightList = []
    guard = 0
    while line != '':
        if guard in [0, 1]:
            guard += 1
            line = tupni.readline()
        else:
            x = [j.strip() for j in line.split(" ")]
            if '' in x:
                while '' in x:
                    x.remove('')
            a = int(x[0])
            b = int(x[1])
            c = float(x[2])
            weightList.append((a, b, c))
            latter = [b]
            if a in dictio:
                dictio[a] = dictio[a] + latter
            else:
                dictio[a] = latter
            line = tupni.readline()
    tupni.close()
    del guard, x, a, b, c, line, tupni

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

    del nodeNames, n, i, j, k

    for i, j in dictio.items():
        for k in j:
            for s in weightList:
                if s[0] == i.name and k == s[1]:
                    i.add(nodeDict[k], s[2])

    del dictio, nodeDict, weightList, i, j, k, s

    graph = Ugraph(nodes)

    graph.printGraph()
    graph.mst_prim(nodes[0])
    graph.spanTree()


operate("tinyDG.txt")
operate("mediumDG.txt")
operate("largeDG.txt")
operate("XtraLargeDG.txt")
