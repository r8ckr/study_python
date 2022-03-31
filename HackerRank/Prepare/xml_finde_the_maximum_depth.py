# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=true

import xml.etree.ElementTree as etree

maxdepth = -1


def depth(elem, level):
    global maxdepth
    # your code goes here
    if level == maxdepth:
        maxdepth += 1

    for i in elem:
        depth(i, level + 1)


if __name__ == "__main__":
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
