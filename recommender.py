import codecs
import similarity
from math import sqrt

# 实现kNN算法
class kNN:
    def __init__(self, data, k=1, metric='pearson', n=5, debug=False):
        """ initialize recommender
        currently, if data is dictionary the recommender is initialized
        to it.
        For all other data types of data, no initialization occurs
        k is the k value for k nearest neighbor
        metric is which distance formula to use
        n is the maximum number of recommendations to make"""
        self.debug = debug
        self.k = k
        self.n = n
        # for some reason I want to save the name of the metric
        self.metric = metric
        if self.metric == 'pearson':
            self.fn = similarity.pearson
        # if data is dictionary set recommender data to it
        if type(data).__name__ == 'dict':
            self.data = data

    def convertProductID2name(self, id):
        """Given product id number return product name"""
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id
        
    def computeNearestNeighbor(self, username):
        """creates a sorted list of users based on their distance to
        username"""
        distances = []
        for instance in self.data:
            if instance != username:
                distance = self.fn(self.data[username], self.data[instance])
                distances.append((instance, distance))
        # sort based on distance -- closest first
        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        if self.debug:
            print("Nearest neighbor: ", distances)
        return distances

    def recommend(self, user):
        """Give list of recommendations"""
        recommendations = {}
        # first get list of users  ordered by nearness
        nearest = self.computeNearestNeighbor(user)
        # now get the ratings for the user
        userRatings = self.data[user]
        if self.debug:
            print("User", user, "'s ratings: ", userRatings)
        # determine the total distance
        totalDistance = 0.0
        for i in range(self.k):
            totalDistance += nearest[i][1]
        if self.debug:
            print("Total distance: ", totalDistance)
        # now iterate through the k nearest neighbors
        # accumulating their ratings
        for i in range(self.k):
            # compute slice of pie 
            weight = nearest[i][1] / totalDistance
            # get the name of the person
            name = nearest[i][0]
            # get the ratings for this person
            neighborRatings = self.data[name]
            print("nr:", neighborRatings)
            # get the name of the person
            # now find bands neighbor rated that user didn't
            for artist in neighborRatings:
                if not artist in userRatings:
                    if artist not in recommendations:
                        recommendations[artist] = (neighborRatings[artist]*weight)
                    else:
                        recommendations[artist] = (recommendations[artist] + neighborRatings[artist] * weight)
        # now make list from dictionary
        recommendations = list(recommendations.items())
        recommendations = [(self.convertProductID2name(k), v)
                          for (k, v) in recommendations]
        # finally sort and return
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
        # Return the first n items
        return recommendations[:self.n]

# 基于加权SlopeOne的推荐
class SlopeOne:
    def __init__(self, data, k=1, metric='pearson', n=5, debug=False):
        """ initialize recommender
        currently, if data is dictionary the recommender is initialized
        to it.
        For all other data types of data, no initialization occurs
        k is the k value for k nearest neighbor
        metric is which distance formula to use
        n is the maximum number of recommendations to make"""
        self.k = k
        self.n = n
        # The following two variables are used for Slope One
        self.frequencies = {}
        self.deviations = {}
        # for some reason I want to save the name of the metric
        self.metric = metric
        self.debug = debug
        if self.metric == 'pearson':
            self.fn = similarity.pearson
        # if data is dictionary set recommender data to it
        if type(data).__name__ == 'dict':
            self.data = data

    # 计算偏差
    def computeDeviations(self):
        if self.debug:
            print("user ratings:", self.data.values())
        # for each person in the data, get their ratings
        for ratings in self.data.values():
            # for each item & rating in that set of ratings:
            for (item, rating) in ratings.items():
                self.frequencies.setdefault(item, {})
                self.deviations.setdefault(item, {})
                # for each item2 & rating2 in that set of ratings:
                for (item2, rating2) in ratings.items():
                    if item != item2:
                        # add the difference between the ratings to our
                        # computation
                        self.frequencies[item].setdefault(item2, 0)
                        self.deviations[item].setdefault(item2, 0.0)
                        self.frequencies[item][item2] += 1
                        self.deviations[item][item2] += rating - rating2
                        if self.debug:
                            print("deviations of '%s:%d' -> '%s:%d'" % (item, rating,item2, rating2))
        for (item, ratings) in self.deviations.items():
            for item2 in ratings:
                ratings[item2] /= self.frequencies[item][item2]

    # 基于SlopeOne的推荐
    def slopeOneRecommendations(self, userRatings):
        recommendations = {}
        frequencies = {}
        # for every item and rating in the user's recommendations
        for (userItem, userRating) in userRatings.items():
            # for every item in our dataset that the user didn't rate
            for (diffItem, diffRatings) in self.deviations.items():
                if diffItem not in userRatings and userItem in self.deviations[diffItem]:
                    freq = self.frequencies[diffItem][userItem]
                    recommendations.setdefault(diffItem, 0.0)
                    frequencies.setdefault(diffItem, 0)
                    # add to the running sum representing the numerator
                    # of the formula
                    recommendations[diffItem] += (diffRatings[userItem]+userRating)*freq
                    # keep a running sum of the frequency of diffitem
                    frequencies[diffItem] += freq
        recommendations = [(k, v / frequencies[k]) for (k, v) in recommendations.items()]
        # finally sort and return
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        # I am only going to return the first 50 recommendations
        return recommendations[:50]




