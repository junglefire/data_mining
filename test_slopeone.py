#!/usr/bin/env/python
import json
import sys
import similarity
import formatter
import recommender

# 命令行参数：test_slopeone.py <ratings_filename>
if len(sys.argv) <= 1:
    print("[usage] %s <ratings_filename>" % sys.argv[0])
    sys.exit(-1)

print("load data from: %s" % sys.argv[1])

users = ""
with open(sys.argv[1], 'r') as f:
    users = json.load(f)

r = recommender.SlopeOne(users, debug=True)
r.computeDeviations()
print("deviations: ", r.deviations)

print("Recommender for 'Ben':")
print("  -->", r.slopeOneRecommendations(users['Ben']))





