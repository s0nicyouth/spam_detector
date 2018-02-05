#/usr/bin/python3

def get3lastchars(str):
    return str[-3:]

class SpamClassifier:


    def fit(data):
        for k, v in data.items():
