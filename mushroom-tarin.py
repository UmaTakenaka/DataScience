#%%
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection, metrics

#%%
mr = pd.read_csv("mushroom.csv", header=None)
mr

#%%
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v)) # ix[]メソッドの使い方？？
    data.append(row_data)

data_train, data_test, labe_train, label_test= model_selection.train_test_split(data, label)

clf = RandomForestClassifier()
clf.fit(data_train, labe_train)

predict = clf.predict(data_test)

ac_scrore = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_scrore)
print("レポート=\n", cl_report)

#%%
