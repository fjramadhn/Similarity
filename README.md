# Clustering text similarity for Data Management

## Logic

Sometimes we found data that has typo or difference writing of word abbreviation for Name or Identity cards ID.
This could be handle by find similarity between words and find the closest range and cluster them.
Calculate the distance for every word by *levenshtein* then clustering the distance matrix using *Affinity Propagation*
