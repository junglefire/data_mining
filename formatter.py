#!/usr/bin/env/python

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

if __name__ == "__main__":
    print(csv2json("data/Movie_Ratings.csv"))