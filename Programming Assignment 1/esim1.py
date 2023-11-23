#! /usr/bin/env python
from graafi import Graph
from CountShortest_dum import CountShortest


def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S = set([])
    for i in x:
        S.add(int(i))
    return S


if __name__ == "__main__":

    G = Graph('testgraph_1')
    B = ReadSet('testset_1')
    x = CountShortest(G, B, 1, 10)
    print("1. Should be 3. The result is", x, end="")
    if x != 3:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_2')
    B = ReadSet('testset_2')
    x = CountShortest(G, B, 1, 20)
    print("2. Should be 2. The result is", x, end="")
    if x != 2:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_3')
    B = ReadSet('testset_3')
    x = CountShortest(G, B, 1, 30)
    print("3. Should be 2. The result is", x, end="")
    if x != 2:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_4')
    B = ReadSet('testset_4')
    x = CountShortest(G, B, 1, 40)
    print("4. Should be 2. The result is", x, end="")
    if x != 2:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_5')
    B = ReadSet('testset_5')
    x = CountShortest(G, B, 1, 50)
    print("5. Should be 3. The result is", x, end="")
    if x != 3:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_6')
    B = ReadSet('testset_6')
    x = CountShortest(G, B, 1, 60)
    print("6. Should be 4. The result is", x, end="")
    if x != 4:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_7')
    B = ReadSet('testset_7')
    x = CountShortest(G, B, 1, 70)
    print("7. Should be 4. The result is", x, end="")
    if x != 4:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_8')
    B = ReadSet('testset_8')
    x = CountShortest(G, B, 1, 80)
    print("8. Should be 4. The result is", x, end="")
    if x != 8:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_9')
    B = ReadSet('testset_9')
    x = CountShortest(G, B, 1, 90)
    print("9. Should be 3. The result is", x, end="")
    if x != 3:
        print( " which is wrong.")
    else:
        print()

    G = Graph('testgraph_10')
    B = ReadSet('testset_10')
    x = CountShortest(G, B, 1, 100)
    print("10. Should be 3. The result is", x, end="")
    if x != 3:
        print( " which is wrong.")
    else:
        print()
