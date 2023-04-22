# the function takes in an argument n
def fizzBuzz(number):
# create a list by using n as the end number [0-n]
  new_list = range(1,number)
# create an empty list
  result_array =[]
# loop through the list 
  for number in new_list:
# if num is divisible by 3 - fizz
    if(number % 3 == 0):
     result_array.append("Fizz")
# if num is divisible by 5 - buzz
    elif(number % 5 ==0):
      result_array.append("Buzz")
# if not divisible by either return the num as string
    else:
      result_array.append(str(number))
# return the new list
  return result_array
  
print(fizzBuzz(11))