import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Chargement des données
Titanic_path = os.path.join("Datasets", "train.csv")
prepared_data = os.path.join("Datasets", "prepared.csv")
prepared_data_xlsx = os.path.join("Datasets", "prepared.xlsx")
saved_data = os.path.join("Datasets", "save")
train_data = pd.read_csv(Titanic_path)

# Analyse du jeu de donnees
"""
print(train_data.info())
print(train_data.shape[0])
print(train_data.columns)
print(train_data.describe(include=['O']))
print(list(zip(train_data.columns, [train_data[col].isna().sum() for col in train_data.columns])))
train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)
"""
# Ajout de données

def add_title(dataset):
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
        'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

add_title(train_data)

def isalone(dataset):
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1
    dataset.drop(columns=['FamilySize'])

isalone(train_data)
def delete_data(dataset):
    dataset.drop(columns=["PassengerId",'Ticket','Cabin'])

# 

"""
# Gestion des variables continues, creation de bins
train_data["Age Type"] = pd.cut(train_data["Age"], bins=[0., 15.0, np.inf],
                               labels=["<15","+15"])
train_data["Cat_fare"] = pd.cut(train_data["Fare"], bins=[0., 20.0, 40.0, 50.00, 80.0, 100.0, 200.0, 300.0, np.inf], labels=False)
train_data["Age Type"] = train_data["Age Type"].cat.add_categories(["Empty_age"])
train_data["Age Type"].fillna("Empty_age", inplace=True)

# Transformation de variable qualitative en variable quantitative via la fonction get_dummies
delete_attributs = ["PassengerId", "Name", "Ticket", "Cabin"]
num_attributs = ["Age", "Parch", "Fare"]
filter_cat = delete_attributs + num_attributs
cat_attributs = [x for x in train_data.columns if x not in filter_cat]
train_data = pd.get_dummies(data=train_data, columns=cat_attributs,prefix=cat_attributs)

#train_data.to_pickle(saved_data)
print(train_data.columns)

#corr_matrix = data_train.corr()

#print(corr_matrix["Survived"])
#data_train.to_csv(prepared_data)
#data_train.to_excel(prepared_data_xlsx, engine="xlsxwriter")

"""
