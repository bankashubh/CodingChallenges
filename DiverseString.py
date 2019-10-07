def function(a, B, C):
  #A = 3
  #B = 0
  #C = 1

  l = A+B+C
  #print(l)
  s = ['x'] * l
  if A >= B and A >=C:
    for i in range(l):
      if i > 1:
        if s[i-1] == s[i-2] and s[i-1] == 'a':
          if B > 0:
            s[i] = 'b'
            B -= 1
            continue
          elif C > 0:
            s[i] = 'c'
            C -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'b':
          if C > 0:
            s[i] = 'c'
            C -= 1
            continue
          elif A > 0:
            s[i] = 'a'
            A -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'c':
          if A > 0:
            s[i] = 'a'
            A -= 1
            continue
          elif B > 0:
            s[i] = 'b'
            B -= 1
            continue
            #print(i)
      if A > 0:
        s[i] = 'a'
        A -=1
      elif B > 0:
        s[i] = 'b'
        B -=1
      elif C > 0:
        s[i] = 'c'
        C -=1

  if B >= C and B >=A:
    for i in range(l):
      if i > 1:
        if s[i-1] == s[i-2] and s[i-1] == 'b':
          if C > 0:
            s[i] = 'c'
            C -= 1
            continue
          elif A > 0:
            s[i] = 'a'
            A -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'c':
          if A > 0:
            s[i] = 'a'
            A -= 1
            continue
          elif B > 0:
            s[i] = 'b'
            B -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'a':
          if B > 0:
            s[i] = 'b'
            B -= 1
            continue
          elif C > 0:
            s[i] = 'c'
            C -= 1
            continue
            #print(i)

      if B > 0:
        s[i] = 'b'
        B -=1
      elif C > 0:
        s[i] = 'c'
        C -=1
      elif A > 0:
        s[i] = 'a'
        A -=1
    #print(i)

  if C >= A and C >=B:
    for i in range(l):
      if i > 1:
        if s[i-1] == s[i-2] and s[i-1] == 'c':
          if A > 0:
            s[i] = 'a'
            A -= 1
            continue
          elif B > 0:
            s[i] = 'b'
            B -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'a':
          if B > 0:
            s[i] = 'b'
            B -= 1
            continue
          elif C > 0:
            s[i] = 'c'
            C -= 1
            continue
        elif s[i-1] == s[i-2] and s[i-1] == 'b':
          if C > 0:
            s[i] = 'c'
            C -= 1
            continue
          elif A > 0:
            s[i] = 'a'
            A -= 1
            continue
            #print(i)

      if C > 0:
        s[i] = 'c'
        C -=1
      elif A > 0:
        s[i] = 'a'
        A -=1
      elif B > 0:
        s[i] = 'b'
        B -=1

  #n = ''.join(s) 


  for i in range(len(s)-2):
    if s[i] is s[i+1]:
      if s[i] is s[i+2]:
        s[i] = '0'

  #n = ''.join(m)    
  s[:] = (value for value in s if value != '0')
  n = ''.join(s)  
  #print(n)
  return n
