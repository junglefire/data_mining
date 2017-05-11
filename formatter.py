#!/usr/bin/env/python
import sys
from pprint import *

def csv2json(filename):
    f = open(filename, 'r')
    fetch_header = False
    fetch_title = False
    movie_title = ""        # 存储电影名
    users_name = []         # 用户名数组
    ratings = {}            # 存储用户对电影的评分
    for line in f:
        line = line.strip('\n')
        # 提取第一行的用户名
        if fetch_header == False:
            for item in line.split(","):
                if item:
                    ratings[item] = {}
                    users_name.append(item)
            fetch_header = True
            continue
        # 提取用户对电影的评分
        fetch_title = False
        i = 0
        for item in line.split(","):
            if fetch_title == False:
                movie_title = item
                fetch_title = True
            else:
                if item:
                    item = int(item)
                    ratings[users_name[i]][movie_title] = item
                i+=1
    f.close()
    return ratings

def movielens2json(movies, ratings):
    # 加载电影ID和名称的对应字典
    f = open(movies, 'r')
    i = 0
    movies_dict = {}
    for line in f:
        line = line.strip('\n')
        if i == 0:
            i += 1
            continue
        items = line.split(",")
        movies_dict[items[0]] = items[1]
        i += 1
    f.close()
    # 读取用户评分
    f = open(ratings, 'r')
    i = 0
    for line in f:
        line = line.strip('\n')
        if i == 0:
            i += 1
            continue
        items = line.split(",")
        print("user_%s:%s:%f" % (items[0], movies_dict[items[1]], float(items[2])))
    f.close()

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("[usage] %s <format> <filename>" % sys.argv[0])
        sys.exit(-1)

    if sys.argv[1] == "csv2json":
        pprint(csv2json(sys.argv[2]))

    if sys.argv[1] == "movielens2json":
        movielens2json(sys.argv[2], sys.argv[3])

