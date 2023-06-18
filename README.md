# analitica_escalable
Trabajo final de analitica escalable

# Comando Docker:
docker pull lucas3697/pec2_analitica_escalable

# Guia del algoritmo: 
Escogí el dataset del titanic porque es el que más veces hice a lo largo de mi carrera y también porque fue el que me introdujo al mundo del machine learning. 
Luego de importar las primeras librerías necesarias, pandas y numpy cargo la data en un dataframe. El cual inspeccionó brevemente con un head y un describe. 
Procedo a dividir el dataset en train y test, para esto me ayudo de la librería StratifiedShuffleSplit, un test size de 0.2 y un random state de 42. 

Data Prep
Me importo el BaseEstimator y TransformerMixin, que me permite darle a mis clases funciones de fit y transform. Junto con el SimpleImputer, OneHotEncoder y StandardScaler. 
Procedo a crear las clases que preparan mi data.  
AgeImputer, para solucionar los nan de esa variable con el valor más frecuente. 
FeatureEncoder, con esta función y la ayuda de OneHotEncoder soluciono el problema de las variables categóricas. 
FeatureDropper, con esta clase me ocupo de quitar las variables que ya no voy a usar. 
Scaler, última clase ocupada de escalar el data frame X. Que el mismo contendrá todas las variables menos la target. 
Luego importo la Pipeline y el modelo que voy a utilizar junto con el GridSearchCV para que me ayude a elegir el valor mas favorable de los parámetros entre un conjunto que yo le pase.
Luego conformó la pipeline con las clases que cree para el data prep y el algoritmo de clasificacion de RandomForestClassifier con los parametros, max_depth = 5, min_sample_split=1, n_estimators=250. 
Le aplico un fit a mi pipeline y ya puedo ver las probabilidades de mis predicciones y el accuracy del modelo el cual arroja un 80,15%
