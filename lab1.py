
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   if int_list == None:
       raise ValueError("Value Error")
   elif len(int_list) == 0:
       return None
   greatest = int_list[0]
   for num in int_list:     #iterates through list, replacing greatest with num if num is greater 
       if num > greatest:
           greatest = num
   return greatest

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   
   if int_list == None:
       raise ValueError("Value Error")
   if len(int_list) <= 1:   #base case where the length of the list is less than or equal to 1
       return (int_list)
   return reverse_rec(int_list[1:]) + int_list[0:1]
   #An additional solution: return int_list[-1:] + reverse_rec(int_list[:-1]) 



def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   if int_list == None:
       raise ValueError("Value Error")
   mid = ((low + high) // 2)  #determines the middle index
   if high - low >= 0:    #base case where middle is target
       if int_list[mid] == target:
           return mid
       elif target < int_list[mid]:   #recurs for the lower half of the list
           return bin_search(target, low, mid - 1, int_list)
       else:    #recurs for the upper half of the list
           return bin_search(target, mid + 1, high, int_list)
   else:
       return None
