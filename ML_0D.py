""" 
Scalar example
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_roc_curve
import matplotlib.pyplot as plt


rfc = RandomForestClassifier(random_state=42)

print("1 feature x 1 sample")
X = [[ 1]] 
y = [1]
rfc.fit(X, y)
print(rfc.predict(X))  # predict classes of the training data
print(rfc.predict([[4], [15],[11],[-2]]))  # predict classes of new data

rfc_disp = plot_roc_curve(rfc, X, y)
rfc_disp.figure_.suptitle("Degenerate example")

#plt.show()


if 1==0:
    print("1 feature x 2 samples")
    X = [[ 1], [2]]  # 2 sample
    y = [1, 1]
    clf.fit(X, y)
    print(clf.predict(X))  # predict classes of the training data
    print(clf.predict([[7], [100],[-454],[22]]))  # predict classes of new data


    print("1 feature x 6 samples")
    X = [[1], [5]] 
    y = [2, 10]
    clf.fit(X, y)
    print(clf.predict(X))  # predict classes of the training data
    print(clf.predict([[1], [100],[-10],[22]]))  # predict classes of new data
