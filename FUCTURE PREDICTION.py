###################### FUCTURE PREDICTION #################################

dataset1 = pd.read_excel(r"D:\NIT\JANUARY\4 jan(knn classification)\4th\future prediction _ 2.xlsx")


d2 = dataset1.copy()

dataset1 = dataset1.iloc[:, [2, 3]].values





from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

y_pred1 = pd.DataFrame()

d2 ['y_pred1'] = classifier.predict(M)

d2.to_csv('final_pred_knn_1.csv')

import os
os.getcwd()

