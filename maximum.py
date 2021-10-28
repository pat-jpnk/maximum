#!/usr/bin/python3

arr = [2,1,8,6,5,11,3,4,9]

def brute_force(arr):
  for i in arr:
    found = True
    for j in arr:
      if(i >= j):
        continue
      else:
        found = False
    if(found):
      return i

  return None;


def divide_and_conquer(arr):
  length = len(arr)
  if(length == 1):
    return arr[0]

  i_1 = length // 2
  a_1 = arr[0:i_1]
  m_1 = max(a_1)

  a_2 = arr[i_1:length]
  m_2 = max(a_2)

  return max(m_1,m_2)



def dynamic_programming(arr):
  length = len(arr)
  b = arr[0::]
  b[0] = arr[0]
  
  for i in range(2,length):
   if(b[i-1] > arr[i]):
      b[i] = b[i-1]
   else:
      b[i] = arr[i]

  return b[length-1]


def greedy_method(arr):
  maximum = arr[0]
  for i in range(1,len(arr)):
    if(arr[i] > maximum):
      maximum = arr[i]
  return maximum


def transform_and_conquer(arr):
  arr.sort();
  return arr[-1]


def decrease_and_conquer(arr):
  if(len(arr) == 1):
    return arr[0]
  
  m_1 = max(arr[1:len(arr)])
  return max(arr[0],m_1)


print(decrease_and_conquer(arr));

print(transform_and_conquer(arr));

print(greedy_method(arr));

print(dynamic_programming(arr));

print(divide_and_conquer(arr));

print(brute_force(arr));
