from uGraph import *
from time import perf_counter as p


def operate(fileName, dg=False):
    tupni = open(fileName, "r")
    line = tupni.readline()
    dictio = {}
    while line != '':
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

    del nodeNames

    for i, j in dictio.items():
        for k in j:
            i.add([nodeDict[k]], dg)

    del dictio
    del nodeDict


    graph = Ugraph(nodes)
    t = p()
    output = graph.topological_sort()
    print("The topological sort took {} seconds.".format(p() - t))
    for i in output:
        print(str(i), end=" ")
    print()
    for n in nodes:
        for o in nodes:
            graph.bfs(n)
            graph.print_path(n, o)
        print()
    print("\nDone with {}".format(fileName))


#operate("tinyG.txt")
#operate("mediumG.txt")
#operate("tinyDG.txt", dg=True)
"""
The above three will not work properly because they were originally written such that the first two lines would be skipped. The change was done to accomodate the two new .txt files.
"""
operate("top_DG1.txt", dg=True)
operate("top_DG2.txt", dg=True)
