"""
1 feature
2 samples

"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_roc_curve
import numpy as np
import myPlotter


clf = RandomForestClassifier(random_state=0)
X = [[1],[5]]  # 2 samples, 1 feature
y = [ 1,  2 ]  # classes of each sample
clf.fit(X, y)

print(clf.predict(X))  # predict classes of the training data

prediction_args=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]]
prediction_res=clf.predict(prediction_args)  # predict classes of new data

x_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

myPlotter.doPlot(x_values,  prediction_res)
