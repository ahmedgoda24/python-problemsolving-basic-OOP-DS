def bubblesort(list):

   for number in range(len(list)-1,0,-1):
      for index in range(number):
         if list[index ]>list[index+1]:
            temp = list[index]
            list[index] = list[index+1]
            list[index+1] = temp
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)