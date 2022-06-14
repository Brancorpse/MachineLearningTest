#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
# importando módulo de decisão em árvore 

from sklearn.tree import DecisionTreeClassifier

# importando classe para exportar decision tree gráfico

from sklearn import tree

# importando classe para dividir dados em treino e teste

from sklearn.model_selection import train_test_split

# Importando classe para calcular precisão

from sklearn.metrics import accuracy_score

# importando classe para trabalhar com modelos persistentes

# from sklearn.externals import joblib

# lendo o arquivo csv

music_data = pd.read_csv('music.csv')

# Comando para visualizar o arquivo csv

music_data


# In[84]:


# Conceitos para tratar dados usando Machine Learning:
# Importar dados;
# Limpar dados;
# Dividir dados entre treino e teste
# Criar um modelo
# Treinar o modelo
# Fazer previsões


# In[85]:


# limpar dados usando o método 'drop'

X = music_data.drop(columns=['genre'])

# Visualizar coluna específica

y = music_data['genre']

# alocando dados para treino e teste

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X)
print(y)


# In[87]:


# Criando instância de classe para o módulo de decisão

model = DecisionTreeClassifier()

# Agora, precisamos treinar o model para aprender os padrões dos dados

model.fit(X_train, y_train)

# Por fim, precisamos pedir para o modelo fazer uma previsão

predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
score

tree.export_graphviz(model, out_file='music_recommender.dot',
                    feature_names=['age', 'gender'],
                    class_names=sorted(y.unique()),
                    label='all',
                    rounded=True,
                    filled=True)


# In[ ]:


# Calculando a precisão da previsão
# O padrão é separar 70/80% dos dados para treino, 30, 20% para teste


# In[ ]:


# Modelos persistentes:

# model = joblib.dump(model, 'music-recommender.joblib')
# predictions = model.predict([[21, 1]])
# predictions

# Assim, você pode salvar e carregar modelos prontos


# In[ ]:


# Exportando nosso modelo usando o Decision Tree

