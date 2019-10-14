#!/usr/bin/env python
# coding: utf-8

#File By Naman Kaushik


# In[ ]:


#Python Lists Practical 1


# In[2]:


cars = ['Honda', 'Hyundai', 'Maruti Suzuki', 'Mahendra']
print('This is the list of cars \n', cars)


# In[4]:


#Python lists operations


# In[5]:


cars.append('Ferrari') #Appending Elements in the list
print(cars)


# In[6]:


len(cars) #length of the lists


# In[9]:


print(cars[4]) #Printing Specific Element From THe List


# In[10]:


cars.remove('Hyundai') #Removing Element From List
print(cars)


# In[11]:


cars.pop() #Popping the Lists


# In[12]:


print(cars[1:3]) #List Slicing


# In[14]:


# Vowels lists
vowels = ['a', 'e', 'i', 'o', 'i', 'u']


# In[15]:


# Element 'e' is searched
index = vowels.index('e')


# In[16]:


# Index of 'e' is printed
print('The index of e:', index)


# In[17]:


# Element 'i' is searched
index = vowels.index('i')


# In[18]:


# Only the first index of the element is printed
print('The index of i:', index)


# In[20]:


#-------------------------------------------------------------------------------------------------------------------


# In[21]:


#Sets
a={1,3,43,37}
b={67,34,77,90}

#Printing the Sets
print(a,b)


# In[22]:


#Union
a|b


# In[23]:


#Intersection
a&b


# In[24]:


#Difference
a-b


# In[25]:


#Symmetric Difference
a^b


# In[26]:


#Comparison Operators
print(a==b) #Operator ==
print(a!=b) #Operator !=
print(a>b) #Operator >
print(a<b) #Operator <
print(a>=b) #Operator >=
print(a<=b) #Operator <=


# In[27]:


#Logical Operators
print (a and b) #AND Operator
print (a or b) #OR Operator
print (not(a and b)) #NOT Operator


# In[28]:


x=90
y=10
#Arithmetic Operations
print(x+y) #Addtion
print(x-y) #Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x%y) #Modulous
print(x**y) #Exponent


# In[30]:


#Comparison Operators
print(x==y) #Operator ==
print(x!=y) #Operator !=
print(x>y) #Operator >
print(x<y) #Operator <
print(x>=y) #Operator >=
print(x<=y) #Operator <=


# In[32]:


#Assignment Operators
z=x+y
print(z) #Operator =
z+=x
print(z) #Add AND
z-=y
print(z) #Subtract AND
z*=x
print(z) #Multiply AND
z/=y 
print(z) #Divide AND


# In[33]:


#Logical Operators
print (x and y) #AND Operator
print (x or y) #OR Operator
print (not(x and y)) #NOT Operator


# In[34]:


#----------------------------------------------------------------------------------------------------


# In[35]:


#Tuples


# In[36]:


#empty tupple
empty=()
print(empty)


# In[37]:


#non empty set
tup='python','anaconda'
print(tup)


# In[38]:


#concatenation
tup_1=(0,1,2,3)
print(tup+tup_1)


# In[39]:


#nested tupples
tup_2=('btech','HM','law','design')
tup_3=(tup,tup_1,tup_2)
print(tup_3)


# In[40]:


#repetition
tup_4=('python',)*4
print(tup_4)


# In[43]:


#slicing
tup_5=(0,12,43,54,756,'hello','wolrd')
print(tup_5)
print(tup_5[1:])
print(tup_5[0:4])
print(tup_5[:-1])


# In[ ]:





# In[41]:


#indexing
tup_6 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(tup_6.index(7))
print(tup_6.index(6))


# In[44]:


#length
print(len(tup_6))
print(len(tup_5))
print(len(tup_4))
print(len(tup_3))
print(len(tup_2))
print(len(tup))


# In[45]:


#conversion list to tupple
list=[0,12,23,34,54]
print(tuple(list))
list_1=['python','java','toc']
print(tuple(list_1))


# In[46]:


#adding element
tup_7= (1, 2, 3, 4, 5)
tup_7=tup_7+ (76,)
print(tup_7)


# In[48]:


#deleting a tupple
tup_7= (1, 2, 3, 4, 5)
del tup_7


# In[49]:


#maximum and minimum
tup_8=(1,32,43,54,65,76)
print(max(tup_8))
print(min(tup_8))
2 in tup_8
54 in tup_8


# In[50]:


#-------------------------------------------------------------------------------------------------------------------


# In[51]:


#Dictionary
Dict = {1: 'BAS', 2: 'ASD', 3: 'ABG'}
print(Dict)
print(Dict.items())#list of tuple pairs
print(len(Dict))#length


# In[52]:


#key is present or not
print('A' in Dict) 
print(1 in Dict)


# In[53]:


#Nested Dictionary
Dict = {1: 'BAS', 2: 'ASD', 3: {'A' : 'Welcome', 'B' : 'to', 'C' : 'Nested Dict'}}
print(Dict)


# In[54]:


#Adding and updating an element
Dict[0] = 'Nj'
Dict[2] = 'Hey'
Dict[3] = 5
print(Dict)


# In[55]:


#Accessing using key
Dict = {1: 'First', 'name': 'Name here', 3: '!First'}
print(Dict['name']) 
print(Dict[1]) 


# In[56]:


#Accessing using get()
print(Dict.get(3))


# In[57]:


#Deletion in DIctionaries

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Deletion', 
        'A' : {1 : 'One', 2 : 'Two', 3 : 'Three'}, 
        'B' : {1 : 'AOne', 2 : 'BTwo'}} 


# In[58]:


# Deleting a Key value 
del Dict[6] 
print(Dict) 


# In[59]:


# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print(Dict) 


# In[66]:


# Deleting Key-value pair using popitem() 
Dict.popitem() 
print(Dict) 


# In[67]:


# Deleting entire Dictionary 
Dict.clear() 
print(Dict) 


# In[68]:


#update
Dict = {'A': 18,'C':12,'T':22,'R':25}	
Dict.update({"S":9})
print(Dict)

