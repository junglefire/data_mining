#!/usr/bin/env/python
import sys
import classifier

# 命令行参数：test_classifier.py <training_filename> <test_filename>
if len(sys.argv) <= 2:
    print("[usage] %s <training_filename> <test_filename>" % sys.argv[0])
    sys.exit(-1)

"""
c = classifier.Classifier(sys.argv[1])

print("Median and deviation data:")
print("  -> ", c.medianAndDeviation)

print("Normalized data:")
print("  -> ", c.data)

print(c.classify([70, 170]))
"""

# python test_classifier.py data/chap04/athletesTrainingSet.txt data/chap04/athletesTestSet.txt
classifier.test(sys.argv[1], sys.argv[2])

