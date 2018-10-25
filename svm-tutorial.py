# Import modules
from sklearn import datasets
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import train_test_split

# Load cancer dataset
cancer = datasets.load_breast_cancer()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3)

# Create an SVM Classifier with a linear kernel
clf = svm.SVC(kernel='linear', C=1.0)

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Print model accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))