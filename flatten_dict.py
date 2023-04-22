# question
dict_netsed = {
  "one" : { 
    "one.one" : 1 , 
  },
  "two" : 2,
  
}

# the function takes in a dictionary
def flatten_dict(dict):
# create a new list to store keys
  key_list = []
# create a new list to store values
  value_list = []
# create an empty dict
  new_dict ={}
# loop through the given dict using key and value
  for key,value in dict.items(): 
# check if the item is an int or dict
# if the item is an int, add the key to the key list and value to the value list
    if type(value) is int:
      key_list.append(key)
      value_list.append(value)
# if the item is a dict, add the key to the key list by adding the parent key to it
    else:
      for key_1,value_1 in value.items():
        key_list.append(key +'.'+ key_1)
        value_list.append(value_1)
  # for k in new_list:
  #     for v in value_list:
  #       new_dict[k] = v
  #       value_list.remove(v)
  new_dict = {key_list[item]:value_list[item] for item in range(len(value_list))}
  # new_dict = zip(new_list,value_list)
  print(new_dict)


flat_dict = flatten_dict(dict_netsed)


# expected output
{
  "one.one.one" : 1,
  "two":2,
}