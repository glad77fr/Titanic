import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

Titanic_path = os.path.join("Datasets", "train.csv")
prepared_data = os.path.join("Datasets", "prepared.csv")
prepared_data_xlsx = os.path.join("Datasets", "prepared.xlsx")

data_train = pd.read_csv(Titanic_path)
data_label = data_train["Survived"]
data_train = data_train.drop('Survived', axis=1)

num_attributs = ["Age", "Parch"]
cat_attributs = data_train.columns
cat_attributs = cat_attributs.drop(num_attributs)

data_num = data_train[num_attributs]
data_cat = data_train[cat_attributs]

# Remplace

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ("attribs_adder",)
])
imputer = SimpleImputer(strategy="median")
imputer.fit(data_num)

#print(data_train.info())
