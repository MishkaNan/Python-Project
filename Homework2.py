"""
1

#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car = 'audi'? I predict False.")
print(car == 'audi')
print("\n")
#2
Name = 'Joe'
print("Is Name = 'Joe'? I predict True.")
print(Name == 'Joe')
print("Is Name = 'Sally'? I predict False.")
print(Name == 'Sally')
print("\n")
#3
Population='4 Million'
print("Is Population ='4 Million'? I think it's True.")
print(Population=='4 Million')
print("Is Population ='10 Million'? I think it's False.")
print(Population=='10 Million')
print("\n")
"""
"""
#5.2
#1 Tests using the lower() method
txt='HELLO WORLD'
x= txt.lower()
print(x)

#2 Tests for equality and inequality with strings / greater than and less than
x=5
y=2
m=6
if x > y:  
    print(f'{x}',f'is bigger than',f'{y}')
if x < m:
    print(f'{x}',f'is lower than',f'{m}')
if x == m:
    print(f'{x}',f'is equal',f'{m}')    
if x != m:
    print(f'{x}',f'is not equal',f'{m}')      

#3 equality and inequality
x=3
y=3
if x==y:
    print(True)
if x !=y:
    print(False)    

#4 Tests using the and keyword and the or keyword
went_market=False
went_mall=True
print(f'{went_market and went_mall} ')

went_market=False
went_mall=True
print(f'{went_market or went_mall} ')

#5 Test whether an item is in a list / Test whether an item is not in a list
lists=[1,2,3,4,5,6]
i=2
if i in lists:
    print('True')
else:
    print('False')   

"""

"""
#2 
#5.3
#1
Alien_Color=['green','yellow','red']
if 'green' in Alien_Color:
    print('the player just earned 5 points.')
#2
if 'black' in Alien_Color:
    print()
#5.4
i='green'
if i == 'green':
    print('the player just earned 5 points for shooting the alien.')
else:
    print('the player just earned 10 points.')    

#5.5
x='yellow'
if 'green' in x:
    print('the player earned 5 points.')
elif 'yellow' in x:
    print('the player earned 10 points.')     
elif 'red' in x:
    print('the player earned 15 points.')      

#5.6

Age=15
if Age <= 2:
    print('the person is a baby.')
elif 2 < Age < 4:
    print('the person is a toddler.')  
elif 4 < Age < 13:
    print('the person is a kid.')        
elif 13 < Age < 20:
    print('the person is a teenager.')
elif 20 < Age < 65:
    print('the person is an adult')
else :
    print('the person is an elder')

#5.7
favorite_fruits=['apple','banana','orange']
fruit='banana'
if fruit in favorite_fruits:
    print('You really like bananas!')
"""


"""
#4
products = ['BMW', 12000,'Mercedes', 15000,'Audi', 20000,'Porche', 25000,'Ferrari', 50000]
for x in products :
    print(x)

"""



