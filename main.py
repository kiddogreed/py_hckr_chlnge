#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_
# slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
if __name__ == '__main__':


   my_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
   #input list or array
   print("The list is :")
   print(my_list)

   all_elems = set(my_list) #convert the list into dictionary for iteration using .count()
   my_result = 0 #pair counter
   for elements in all_elems: #iterate the object or dictionary using <in> keyword
       my_result += my_list.count(elements) // 2  #increment then check
   print(all_elems)
   print("The total pairs are :")
   print(my_result) # display result


#finding number of pairs in a list or array
