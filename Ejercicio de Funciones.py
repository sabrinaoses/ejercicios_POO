#!/usr/bin/env python
# coding: utf-8

# In[12]:


#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

#pares, impares = separar([6,5,2,1,7])
#print(pares)   # valdría [2, 6]
#print(impares)  # valdría [1, 5, 7]
#Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

numeros = [6,5,2,1,7]

# Completa el ejercicio aquí
def separar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for n in lista:
        if numeros%2==0:
         pares.append(n)
        else:
         impares.append(n)
        
    return pares,impares

pares,impares= separar(numeros)
print(pares)
print(impares)


# In[ ]:





# In[ ]:




