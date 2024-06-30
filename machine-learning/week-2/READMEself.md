# Approach
1. Mounted Drive and used kaggle api to upload datasets
2. Turned all strings to bool using one-hot encoding
3. Removed non-important functions
4. Normalized data
5. Tried out:
    * Random Forest
    * Keras Neural Network \
    classification algorithms
# Challanges
1. First I was confused how to handle dates. There were 1684 dates, 56 mm//yyyy, 5 years.
    * So I initially converted mm//yyyy strings to onehot
    * later I came to know about np.datetime64 to handle dates
2. Sometimes I copied some commands from google to reshape my dataset, but those commands didn't go as expected, so had to do alloperations again.
3. tried out IEEE dataset, but failed in cleaning it.
4. Tried out freeapi to host my model, but failed in initial attempts.
# Results
1. Random Forest gave better accuracy in this data set
2. After cleaning and normalization, better to create a copy of data, in-case data is destroyed while further operations