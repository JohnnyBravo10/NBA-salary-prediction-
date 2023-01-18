#importing libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


#def della prediction function
def prediction(data):

    ##loading dataset
    dataframe = pd.read_csv("https://raw.githubusercontent.com/JohnnyBravo10/NBA-salary-prediction-/main/nba_contracts_history.csv")
    dataframe.drop_duplicates(inplace=True)
    
    learningSet= pd.DataFrame(dataframe.iloc[:,3:])
    learningSet['Duration']=dataframe['CONTRACT_END']-dataframe['CONTRACT_START']
    
    #normalizing learningSet (min-max)
    normalizedLearningSet= learningSet.copy()
    
    for feature_name in normalizedLearningSet.iloc[:,1:].columns:
        max_value = learningSet[feature_name].max()
        min_value = learningSet[feature_name].min()
        normalizedLearningSet[feature_name] = (normalizedLearningSet[feature_name] - min_value) / (max_value - min_value)
    
    #tentativo rimuovendo dal learning set le variabili dipendenti da altre (esempio: REB=OREB+DREB)
    
    withoutDependents= normalizedLearningSet.iloc[:,[0,1,3,4,5,7,8,10,11,13,14,16,17,19,20,21,22,23,24,25]].copy() 
    
    #fourth model delevlopment
    x3= withoutDependents.iloc[:,1:].copy()
    y3= withoutDependents.iloc[:,0].copy()
    
    data = pd.DataFrame(np.array(data),columns=x3.columns)

    for column in data.columns:
      max_value = learningSet[column].max()
      min_value = learningSet[column].min()
      data[feature_name] = (data[feature_name] - min_value) / (max_value - min_value)
    
    return KNeighborsRegressor(n_neighbors=4).fit(x3, y3).predict(data)


