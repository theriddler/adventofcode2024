# define our arrs to read data into
col1 = []
col2 = []

# helper function to correctly insert data
def insert_sorted(arr, num_to_insert):

  # if empty arr, insert at first index
  if(len(arr) == 0): 
    arr.insert(0, num_to_insert)
    return
  
  # check arr
  for i, num in enumerate(arr):

    # if num to insert is less than current num
    if(num_to_insert <= num):
      arr.insert(i, num_to_insert)
      return
    
  arr.append(num_to_insert)
  
# read data
with open('input.txt') as file:
  for line in file:
    num1, num2 = line.split()
    insert_sorted(col1, num1)
    insert_sorted(col2, num2)

# add up all distances
sum = 0
for i, num1 in enumerate(col1):
  num2 = col2[i]
  sum += abs(int(num1)-int(num2))

print(sum)