#!/usr/bin/env/python
import json
import sys
import distance
import recommender

# 命令行参数：test_distance.py <json_filename>
if len(sys.argv) <= 1:
    print("[usage] %s <json_filename>" % sys.argv[0])
    sys.exit(-1)

print("load data from: %s" % sys.argv[1])

users = ""
with open(sys.argv[1], 'r') as f:
    users = json.load(f)

print("Manhattan distance of user 'Hailey' and 'Veronica':")
print("  -->", distance.manhattan_distance(users['Hailey'], users['Veronica']))

print("Euclidean distance of user 'Hailey' and 'Veronica':")
print("  -->", distance.euclidean_distance(users['Hailey'], users['Veronica']))

print("Minkowski distance of user 'Hailey' and 'Veronica':")
print("  -->", distance.minkowski_distance(users['Hailey'], users['Veronica'], 5))

print("Pearson correlation of user 'Angelica' and 'Bill':")
print("  -->", distance.pearson(users['Angelica'], users['Bill']))

print("Cosine similarity of user 'Angelica' and 'Veronica':")
print("  -->", distance.cosine_similarity(users['Angelica'], users['Veronica']))

k = recommender.kNN(users, debug=False, k = 2)
print("Recommend for `Jordyn`\n    -->", k.recommend('Jordyn'))
print("Recommend for `Hailey`\n    -->", k.recommend('Hailey'))




