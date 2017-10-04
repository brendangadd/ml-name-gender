import numpy as np
import os
import json
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def sample(string, max_len):
    features = [char for char in string.encode()]
    features.extend([0 for _ in range(0, max_len - len(features))])
    npa = np.array(features)
    return npa.reshape(1, -1)[0]

def main(test):
    print('Loading...')
    fp = os.path.join(os.path.dirname(__file__), "reference", "data.json")
    with open(fp) as f:
        data = json.load(f)

    X0 = data['name']
    y = data['target']

    print('Extracting features...')
    X1 = [[char for char in name.encode()] for name in X0]
    max_len = max([len(entry) for entry in X1])
    for entry in X1:
        entry.extend([0 for _ in range(0, max_len - len(entry))])

    print('Fitting...')
    clf = RandomForestClassifier(
        n_estimators = 10,
        max_depth = None,
        min_samples_split = 2,
        random_state = 0
    )
    clf.fit(X1, y)

    print('Predicting...')

    # scores = cross_val_score(clf, X1, y)
    # print('Cross validation: %s' % scores)

    predictions = clf.predict([sample(string, max_len) for string in test])
    for i,j in zip(test, predictions):
        print(i,":",j)

    print('Saving model...')
    fp = os.path.join(os.path.dirname(__file__), "reference", "model.p")
    with open(fp, "wb") as f:
        pickle.dump([clf, max_len], f)

if __name__ == "__main__":
    test = ['brendan', 'dude', 'anna', 'antenilina', 'abigaletta']
    main(test)
