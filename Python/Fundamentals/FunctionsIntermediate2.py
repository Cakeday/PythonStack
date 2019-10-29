# x=[[5,2,3],[10,8,9]]

# students=[
#     {'first_name':'Michael', 'last_name':'Jordan'},
#     {'first_name':'John', 'last_name':'Rosales'}
# ]

# sports_directory={
#     'basketball':['Kobe','Jordan','James','Curry'],
#     'soccer':['Messi','Ronaldo','Rooney']
# }

# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)
# students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])
# sports_directory['soccer'][0]='Andres'
# print(sports_directory['soccer'])
# z[0]['y']=30
# print(z)


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary():
#     for i in students:
#         print(f"first_name - {i['first_name']}")
# iterateDictionary()


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(key, list):
#     for i in students:
#         print(i[key])
# iterateDictionary2('first_name', students)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dict):
#     for key in dict:
#         print(dojo[key])
#         for el in dict[key]:
#             print(el)
# printInfo(dojo)



# myobj = {
#     'fruits':['apple','orange'],
#     'categories':{
#         'bottles':['hydroflask', 'thermal', 'coca cola bottle']
#     }
# }
# print(myobj['categories']['bottles'][0])
# for thing in myobj:
#     if thing == 'categories':
#         for element in myobj[thing]:
#             if element == 'bottles':
#                 print(myobj[thing][element])
#                 print(element)
