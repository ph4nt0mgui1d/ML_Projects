import pandas as pd

df = pd.read_csv('titanic.csv')

df.sample()

sur = df['Survived'].value_counts()[1]
print("People survived : {}".format(sur))

died = df['Survived'].value_counts()[0]
print("People died : {}".format(died))

sur_percentage = df['Survived'].value_counts(normalize = True)[1]
x = round(float(sur_percentage*100), 2)
print("{}% people survived".format(x))

died_percentage = df['Survived'].value_counts(normalize = True)[0]
y = round(float(died_percentage*100), 2)
print("{}% died".format(y))

male_sur = df['Survived'] [df['Sex'] == 'male'].value_counts(normalize = True)[1]
a = round(float(male_sur*100),2)
print("{}% male people survived".format(a))


male_died = df['Survived'] [df['Sex'] == 'male'].value_counts(normalize = True)[0]
b = round(float(male_died*100),2)
print("{}% male people died".format(b))

female_sur = df['Survived'] [df['Sex'] == 'female'].value_counts(normalize = True)
c = round(float(female_sur[1]*100),2)
print("{}% female people survived".format(c))


female_died = df['Survived'] [df['Sex'] == 'female'].value_counts(normalize = True)
d = round(float(female_died[0]*100),2)
print("{}% female people died".format(d))

def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0
    
df['Child'] = df['Age'].apply(filter_data)
e = df['Survived'][df['Child'] == 1].value_counts(normalize = True)
print ("Children Survived : "+str(round(e[1]*100, 2))+"%")
