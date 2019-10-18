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


print()
print(data[data['Density'] > 100])
print()



index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]

print(index)


populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
print(populations)
print()
pop = pd.Series(populations, index)
print(pop)
print()


index2 = pd.MultiIndex.from_tuples(index)
print(index2)
print()

pop2 = pop.reindex(index2)
print(pop2)
print()
print(pop2['California'])
print()
print(pop2[:])
print()


pop2_df = pop2.unstack()
print(pop2_df)
print()

pop2_stacked = pop2_df.stack()
print(pop2_stacked)
print()

pop2_df = pd.DataFrame({'total': pop2, 'under18':[9267089, 9284094, 4687374, 4318033, 5906301, 6879014]})

print(pop2_df)
print()


f_u18 = pop2_df['under18'] / pop2_df['total']
print(f_u18)
print()

print(f_u18.unstack())
print()


index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
print(index)
print()

columns = pd.MultiIndex.from_product([['Bob', 'Jim', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
print(columns)
print()


# Daten simulieren
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# DataFrame erzeugen
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)
print()

print(health_data['Jim'])
print()

print(health_data['Bob']['HR'])
print()

print(health_data['Bob']['HR'][2013])



