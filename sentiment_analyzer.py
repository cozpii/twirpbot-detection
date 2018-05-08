# twirpbot-detection - GPL - Copyright 2018 - aswinmguptha

feature_list = ['god', 'kill', 'muslim', 'country']

def extract_features(tweet):
    flag = 0
    tweet_words = set(tweet.split())
    print tweet_words
    for word in feature_list:
        if word in tweet_words:
            flag += 1
    return flag

print extract_features('god is great')
