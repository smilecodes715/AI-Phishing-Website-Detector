import re

def extract_features(url):

    features = {}

    features['url_length'] = len(url)

    features['has_https'] = 1 if "https" in url else 0

    features['has_at'] = 1 if "@" in url else 0

    features['has_dash'] = 1 if "-" in url else 0

    features['dot_count'] = url.count('.')

    features['slash_count'] = url.count('/')

    return list(features.values())
