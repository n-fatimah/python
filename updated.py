***
try to use sum() function to increment if the
condition satisfy. and return the sum



for the next task try to have if and if else 
statement in list comprehension

***

def matchwords(words):
    return sum(1 for word in words if len(word) > 1 and word == word[::-1])

listt = ["122221", 'xyzabc', 'abcdeedcba']
print(matchwords(listt))



***
use f String
***

check = [{'keyy': 'noor', 'is': 2, 'besstt': 3},
         {'keyy': 'lameee'},
         {'best': 3, 'keyy': 'hat'}]

print(f"The original list is: {check}")


***


instead of using str() use ",".join(res)

***
check = [{'keyy': 'noor', 'is': 2, 'besstt': 3},
         {'keyy': 'lameee'},
         {'best': 3, 'keyy': 'hat'}]

res = [str(item) for item in check]
joined_res = ", ".join(res)
print(f"The original list is: {joined_res}")


***
use f string
***
def find_union(s,t):
  u=s.union(t)
#   print("union is ",u)
  return u

def find_int(s,t):
  i=s.intersection(t)
#   print("int is ",i)

  return i

def non_common_in_both(u,i):
  res=u.difference(i)
  print(f"The elements in either but not common : {res}")

s=set(input(f"Enter set 1 :"))
print(s)

t=set(input(f"Enter set 2 :"))
print(t)

u=find_union(s,t)
print(f"union is : {u}")

i=find_int(s,t)
print(f"int is : {i}")

non_common_in_both(u,i)


