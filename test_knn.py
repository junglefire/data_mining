#!/usr/bin/env/python
import json
import sys
import distance
import formatter
import recommender

# 命令行参数：test_knn.py <ratings_filename>
if len(sys.argv) <= 1:
    print("[usage] %s <ratings_filename>" % sys.argv[0])
    sys.exit(-1)

print("load data from: %s" % sys.argv[1])

ratings = formatter.csv2json(sys.argv[1])

k = recommender.kNN(ratings, debug=True, k = 1)
print("Recommend for `Heather`\n    -->", k.recommend('Heather'))





