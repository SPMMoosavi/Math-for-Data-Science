import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()

# The dataset
dataset = iris["data"]

# To center the dataset
m = np.mean(dataset,axis=0)
vectors = dataset - m

# To make a data frame
centered_df = pd.DataFrame(data=vectors)
