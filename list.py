def matchwords(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and  word == word[::-1]:
      ctr += 1
  return ctr




listt=["122221",'xyzabc','abcdeedcba']
matchwords(listt)
print(matchwords(listt))