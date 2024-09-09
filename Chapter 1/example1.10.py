from sklearn import datasets
iris = datasets.load_iris(as_frame=True)
dataset = iris["frame"]
print(dataset.head())