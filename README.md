# Clustering text similarity for Data Management

## Logic

Sometimes we found data that has typo or difference writing of word abbreviation for Name or Address.
This could be handle by find similarity between words and find the closest range and cluster them.
Calculate the distance for every word by Levenshtein then clustering the distance matrix using Affinity Propagation
