#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


def AddToYAML(url, file):
    newLine = "  - DOMAIN-SUFFIX," + url
    if (not ContentExists(file, newLine)):
        AddOnelineAndSortWithoutFirstLine(
            file, newLine, "payload:")

    return


def AddToList(url, file):
    newLine = "DOMAIN-SUFFIX," + url + ",PROXY"
    if (not ContentExists(file, newLine)):
        AddOnelineAndSortWithoutFirstLine(
            file, newLine, "# > Additional")

    return


def ContentExists(file, content):
    with open(file, mode='r') as f:
        for line in f:
            if (line.startswith(content)):
                return True


def AddOnelineAndSortWithoutFirstLine(file, line, firstLine):
    lastLineWithEnter = False
    with open(file, mode='r') as f:
        lines = f.readlines()
        lastLine = lines[-1]
        lastLineWithEnter = "\n" in lastLine

    with open(file, mode='a') as f:
        if (not lastLineWithEnter):
            f.writelines('\n')
        f.writelines(line)
        f.writelines('\n')
    list = []
    with open(file, mode='r') as f:
        for line in f:
            if (line.startswith(firstLine)):
                continue  # 跳开第一行, 不排序
            list.append(line)

    with open(file, mode='w') as f:
        f.writelines(firstLine)
        f.writelines('\n')
        for item in sorted(list):
            f.writelines(item)

    return


def main(url):
    AddToYAML(url, './c/additional.yaml')
    AddToList(url, './q/additional.list')
    return


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except Exception as e:
        print(sys.argv)
        print(e)
