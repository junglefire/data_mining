#!/usr/bin/env/python
import json
import sys
import similarity
import recommender

# 命令行参数：test_distance.py <json_filename>
if len(sys.argv) <= 1:
    print("[usage] %s <json_filename>" % sys.argv[0])
    sys.exit(-1)

print("load data from: %s" % sys.argv[1])

users = ""
with open(sys.argv[1], 'r') as f:
    users = json.load(f)

"""
print("Manhattan distance of user 'Hailey' and 'Veronica':")
print("  -->", similarity.manhattan_distance(users['Hailey'], users['Veronica']))

print("Euclidean distance of user 'Hailey' and 'Veronica':")
print("  -->", similarity.euclidean_distance(users['Hailey'], users['Veronica']))

print("Minkowski distance of user 'Hailey' and 'Veronica':")
print("  -->", similarity.minkowski_distance(users['Hailey'], users['Veronica'], 5))

print("Pearson correlation of user 'Angelica' and 'Bill':")
print("  -->", similarity.pearson(users['Angelica'], users['Bill']))

print("Cosine similarity of user 'Angelica' and 'Veronica':")
print("  -->", similarity.cosine_similarity(users['Angelica'], users['Veronica']))

k = recommender.kNN(users, debug=False, k = 2)
print("Recommend for `Jordyn`\n    -->", k.recommend('Jordyn'))
print("Recommend for `Hailey`\n    -->", k.recommend('Hailey'))
"""

print("Model base similarity of 'Daft Punk' and 'Lorde':")
print("  -->", similarity.compute_similarity_model('Daft Punk', 'Lorde', users))




