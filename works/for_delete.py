import sklearn
import pandas as pd

print(f"Версія Scikit-learn: {sklearn.__version__}")
print(f"Версія Pandas: {pd.__version__}")

from sklearn.datasets import load_boston
data = load_boston()
print("Успіх! load_boston працює!")