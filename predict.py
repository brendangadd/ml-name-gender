import pickle
import os
import sys
import numpy as np

def sample(string, max_len):
    features = [char for char in string.encode()]
    features.extend([0 for _ in range(0, max_len - len(features))])
    npa = np.array(features)
    return npa.reshape(1, -1)[0]

fp = os.path.join(os.path.dirname(__file__), "reference", "model.p")
with open(fp, "rb") as f:
    clf,max_len = pickle.load(f)

print(clf.predict([sample(sys.argv[1], max_len)])[0])
