# -*- coding=utf-8 -*-
#!/usr/bin/env/python
from math import sqrt

# 实现minkowski距离函数, 其中rating1、rating2表示用户对某个物品的打分，
# 格式为{'Macbook':5, 'XPS12':3}
# r为阶数，当r=1时，又称为曼哈顿距离；r=2时，称为欧式距离
def minkowski_distance(rating1, rating2, r):
    distance = 0
    ratings = False
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key]-rating2[key]), r)
            ratings = True
    if ratings:
        return pow(distance, 1/r)
    else:
        return 0

# 曼哈顿距离
def manhattan_distance(rating1, rating2):
    return minkowski_distance(rating1, rating2, 1)

# 欧氏距离
def euclidean_distance(rating1, rating2):
    return minkowski_distance(rating1, rating2, 2)

# 实现皮尔逊系数
def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # now compute denominator
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator

# 实现余弦相似度
def cosine_similarity(rating1, rating2):
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for key in rating1:
        if key in rating2:
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
    for key in rating1:
        sum_x2 += pow(rating1[key], 2)
    for key in rating2:
        sum_y2 += pow(rating2[key], 2)
    return sum_xy / (sqrt(sum_x2) * sqrt(sum_y2))

# 调整后的余弦相似度，用于计算物品的相似模型
def compute_similarity_model(m1, m2, user_ratings):
    averages = {}
    for (key, ratings) in user_ratings.items():
        averages[key] = (float(sum(ratings.values())) / len(ratings.values()))
    num = 0
    dem1 = 0
    dem2 = 0
    for (user, ratings) in user_ratings.items():
        if m1 in ratings and m2 in ratings:
            avg = averages[user]
            num += (ratings[m1] - avg) * (ratings[m2] - avg)
            dem1 += (ratings[m1] - avg)**2
            dem2 += (ratings[m2] - avg)**2
    return num / (sqrt(dem1) * sqrt(dem2))



