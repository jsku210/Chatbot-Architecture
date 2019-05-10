# Author : Hyunwoong
# When : 5/10/2019
# Homepage : github.com/gusdnd852
import os

import pandas as pd

result = pd.DataFrame(columns=['question', 'intent'])
root = './'
data_path = ['동사', '명사', '목적', 'etc']
for path in data_path:
    specific_paths = os.listdir(root + '/' + path)
    for specific_path in specific_paths:
        file_names = os.listdir(root + '/' + path + '/' + specific_path)
        for filename in file_names:
            try:
                file = pd.read_csv(root + '/' + path + '/' + specific_path + '/' + filename,
                                   names=['question', 'intent'])
                result = pd.concat([result, file], sort=True)
            except:
                pass
result = pd.DataFrame(result, columns=['question', 'intent'])
result.to_csv('train_intent.csv', index=None)
data = result
intent_mapping = {}

idx = -1
for q, i in data.values:
    if i not in intent_mapping:
        idx += 1
    intent_mapping[i] = idx

for i in result.values:
    print(i[1])

for i, x in enumerate(intent_mapping):
    print(i, ' : ', x)
