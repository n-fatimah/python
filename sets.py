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
  print("The elements in either but not common : ", res)

s=set(input("Enter set 1 :"))
print(s)

t=set(input("Enter set 2 :"))
print(t)

u=find_union(s,t)
print("union is : ",u)

i=find_int(s,t)
print("int is : ",i)

non_common_in_both(u,i)


x = set(['n', 'o', 'o', 'r','f'])
x = set(['f', 'a', 't', 'i', 'm', 'a', 'h','r'])