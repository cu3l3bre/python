import pandas as pd
import numpy as np


print("Some stuff with pandas")


#
#data1 = pd.Series([0.25, 0.5, 0.75, 1.0])
#print(type(data1))
#
#
#data2 = data1.values
#print(data2)
#typeData2 = type(data2)
#
#data3 = data1.index
#print(data3)
#typeData3 = type(data3)


data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)

print(data.values[0])
print(data.index[0])

print(data['a'])



data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
print()
print(data)


population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}



population = pd.Series(population_dict)
print()
print(population)
print()
print(population['California':'New York'])


print()

data = pd.Series([0.25, 0.5, 0.75, {1.0,2.0}], index=[2, 5, 3, 7])
data = pd.Series([{0.25, 0.5, 0.75, 1.0,2.0}])#, index=[2, 5, 3, 7])
print()
print(data)



print()

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict)

print()
print(population)


area_dict = {'California': 423967, 'Texas': 695662,
             'New York': 141297, 'Florida': 170312,
             'Illinois': 149995}

area = pd.Series(area_dict)


print()
print(area)



states = pd.DataFrame({'population': population,
                       'area': area})

print()
print(states)




data = pd.DataFrame(np.random.rand(3, 2),
                    columns=['foo', 'bar'],
                    index=['a', 'b', 'c'])

print()
print(data)



A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
print()
print(A)



data = pd.DataFrame(A)
print()
print(data)




ind = pd.Index([2, 3, 5, 7, 11])
print()
print("Index Values:", ind.values)
print("Index an Stelle 1: ",ind[1])
print("Indies mit Schrittweite 2: ", ind[::2])

indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

print("IndexA: ", indA)
print("IndexB: ", indB)
print()
print("Schnittmenge: ", indA & indB) # Indies die in beiden beihalted sind
print("Vereiningsm.: ", indA | indB) # Indies die insgesamt vorkommen
print("Symet. Diff.: ", indA ^ indB) # Indies die jeweils nicht im anderen vorkommen




data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print()
print(data)

print("a in data?: ",'a' in data)
print("e in data?: ",'e' in data)

print(data.keys())
print(data.values, type(data.values))
print(data.items())



area = pd.Series({'California': 423967,
                    'Texas': 695662,
                    'New York': 141297,
                    'Florida': 170312,
                    'Illinois': 149995})

# pop steht für population = Einwohner
population = pd.Series({'California': 38332521,
                'Texas': 26448193,
                'New York': 19651127,
                'Florida': 19552860,
                'Illinois': 12882135})


data = pd.DataFrame({'Area': area, "Population":population})
print()
print(data)

# geht so
#print(data['Area'])
#print(data['Population'])

# geht aber auch als Attribut, fancy shit, also der Indes mit Großbuchstaben
#print(data.Area)
#print(data.Population)


data['Density'] = data['Population'] / data['Area']
print()
print(data)


