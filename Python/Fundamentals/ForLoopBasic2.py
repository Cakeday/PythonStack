# def biggie(list):
#     for i in range (0,len(list),1):
#         if list[i] > 0:
#             list[i] = 'big'
#     return list
# print(biggie([-5,-4,-3,-2,-1,0,1,2,3,4,5]))

# def count(list):
#     counter=0
#     for i in range (0,len(list),1):
#         if list[i] > 0:
#             counter += 1
#     list[len(list)-1] = counter
#     return list
# print(count([-5,-4,-3,-2,-1,0,1,1,1,2,3,4,5]))

# def sum(list):
#     sum = 0
#     for i in range (0,len(list),1):
#         sum+=list[i]
#     return sum
# print(sum([-5,-4,-3,-2,-1,0,1,1,1,2,3,4,5]))

# def avg(list):
#     sum = 0
#     for i in range (len(list)):
#         sum+=list[i]
#         print(sum)
#     return (sum/len(list))
# print(avg([4,1]))

# def length(list):
#     return len(list)
# print(length([4,1,5,3,567,3]))

# def min(list):
#     min = list[0]
#     if list == []:
#         return False
#     for i in range (1,len(list)-1):
#         if list[i]<min:
#             min = list[i]
#     return min
# print(min([4,1,5,3,567,3]))

# def max(list):
#     if list == []:
#         return False
#     max = list[0]
#     for i in range (1,len(list)-1):
#         if list[i]>max:
#             max = list[i]
#     return max
# print(max([4,1,5,3,567,3]))

# def ultimate(list):
#     dict = {}
#     max = list[0]
#     min = list[0]
#     sum = 0
#     for val in range (len(list)):
#         if list[val] < min:
#             min = list[val]
#         elif list[val] > max:
#             max = list[val]
#         sum += list[val]
#     dict["sum"]=sum
#     dict["max"]=max
#     dict["min"]=min
#     dict["avg"]=sum/len(list)
#     dict["length"]=len(list)
#     return dict
# print(ultimate([4,1,5,3,567,3]))

# def reverse(list):
#     for i in range (len(list)/2):
#         temp = list[len(list)-i-1]
#         list[len(list)-i-1] = list[i]
#         list[i] = temp
#     return list
# print(reverse([4,1,5,3,567,3]))