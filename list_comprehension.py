check = [{'keyy' : 'noor', 'is' : 2, 'besstt' : 3},
              {'keyy' : 'lameee'}, {'best' : 3, 'keyy' : 'hat'}]

print("The original list is : " + str(check))

res = [ sub['keyy'] for sub in check ]

# print(res)
print("The values corresponding to key : " + str(res))