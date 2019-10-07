def funstion(S):
  l = len(S) - 2
  m = list(S)

  #print(m)

  for i in range(l):
    if m[i] is m[i+1]:
      if m[i] is m[i+2]:
        m[i] = '0'

  #n = ''.join(m)    
  m[:] = (value for value in m if value != '0')
  n = ''.join(m)  
  #print(n)
  return n
