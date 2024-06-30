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
1. I was not that fluent in python. So faced issues in basic commands like selecting a range or rows, reshaping (since Keras requires a 2-D matrix), and so on...
2. Sometimes I copied some commands from google to reshape my dataset, but those commands didn't go as expected, so had to do alloperations again.
3. tried out IEEE dataset, but failed in cleaning it.
4. Tried out freeapi to host my model, but failed in initial attempts.
# Results
1. Random Forest gave better accuracy in this data set
2. After cleaning and normalization, better to create a copy of data, in-case data is destroyed while further operations