def two_sum(nums,target):
  numsmap={}
  for i,n in enumerate(nums):
    tofind=target - n
    if tofind in numsmap:
      return [numsmap[tofind],i]
  
  return []



nums=[2,7,11,15]
target=9
res=two_sum(nums,target)