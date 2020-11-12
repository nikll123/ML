"""
2 feature
2 samples

"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_roc_curve
import numpy as np
import myPlotter

clf = RandomForestClassifier(random_state=0)
X = [[1,2],[5,7]]  # 2 samples, 2 feature
y = [  1,    2 ]  # classes of each sample
clf.fit(X, y)

print(clf.predict(X))  # predict classes of the training data

for i in range(12):
    prediction_args=[[i,0],[i,1],[i,2],[i,3],[i,4],[i,5],[i,6],[i,7],[i,8],[i,9],[i,10],[i,11],[i,12]]    
    prediction_res=clf.predict(prediction_args)  # predict classes of new data

    
x_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

myPlotter.doPlot(x_values,  prediction_res)
