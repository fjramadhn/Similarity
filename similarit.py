import numpy as np
import sys
import pandas as pd
import sklearn.cluster
import distance
import time
import datetime
import pickle
import Levenshtein
from sklearn.cluster import AffinityPropagation

path_data = sys.argv[1]
column = sys.argv[2]
path_result = sys.argv[3]
start_time = time.time()
print(datetime.datetime.now())
df = pd.read_csv(path_data)
df[column] = df[column].astype(str)
col = np.asarray(df[column])
lev_similarity = -1*np.array([[Levenshtein.distance(w1,w2) for w1 in col] for w2 in col])
print(lev_similarity)
print(datetime.datetime.now())
affprop = AffinityPropagation(affinity="precomputed", damping=0.7, random_state=0).fit(lev_similarity)
#affprop.fit(lev_similarity)
#filename = "/home/agracham7151/scripts/name_similarity.pkl"
#pickle.dump(ta, open(filename, 'wb'))
df['LABEL'] = pd.DataFrame(affprop.labels_)
print(df.head())
print(datetime.datetime.now())
df[[column, "LABEL"]].to_csv('path_result', index=False)
