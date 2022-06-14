#!/usr/bin/env python
# coding: utf-8

# In[11]:


print('hello world')


# In[12]:


import pandas as pd
# lendo o arquivo csv

df = pd.read_csv('vgsales.csv')

# Comando para verificar tamanho  do arquivo csv

df.shape


# In[13]:


# Comando que detalha informações detalhadas de cada coluna
df.describe()


# In[14]:


# Comando que mostra valores de cada coluna numa matriz
df.values


# In[ ]:


# Em Jypiter, o código é dividido em celas e pode ser rodado totalemte ou parcialmente


# In[ ]:


# para deletar, precione d duas vezes na cela selecionada


# In[ ]:




