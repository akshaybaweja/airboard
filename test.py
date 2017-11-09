from sklearn.externals import joblib
import signals

clf = joblib.load('model.pkl')
classes = joblib.load('classes.pkl')

sample_test = signals.Sample.load_from_file("data/sample.txt")

lin = sample_test.get_linearized(reshape=True)

#Predict the number with the machine learning model
number = clf.predict(lin)

#Convert it to a char
char = chr(ord('a')+number[0])

print number
print char
