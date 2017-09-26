import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def to_features(string):
  return [char for char in string.encode()]

print('Loading...')
frame = pd.read_csv('names.csv')
X0 = frame['name'].values
y = frame['target'].values

print('Extracting features...')
X1 = [to_features(name) for name in X0]
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

def sample(string):
  features = to_features(string)
  features.extend([0 for _ in range(0, max_len - len(features))])
  npa = np.array(features)
  return npa.reshape(1, -1)

def predict(strings):
  for string in strings:
    prediction = int(clf.predict(sample(string))[0])
    print('%s: %d' % (string, prediction))

scores = cross_val_score(clf, X1, y, n_jobs = -1)
print('Cross validation: %s' % scores)
predict(['brendan', 'dude', 'anna', 'antenilina', 'abigaletta'])
