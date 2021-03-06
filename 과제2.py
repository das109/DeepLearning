# -*- coding: utf-8 -*-
"""과제2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xP1ABxeIQBArTqWOJQrxZU9UP4NJr9gt
"""

def hanoi_print(A, B, C): #출력
  global cnt
  print(str(cnt)+"번째입니다.") #숫자세기
  print(A)
  print(B)
  print(C)
  print(" ")
  return

def hanoi(n, h_from, h_to, h_tmp):
  global cnt
  if n == 1: #작대기에 가장 큰 디스크만 남음
    for i in range(0, 3): #출발이 되는 작대기에서 디스크 꺼냄
      if h_from[2-i] != 0:
        tmp = h_from[2-i]
        h_from[2-i] = 0
        break
  
    for i in range(0, 3): #도착이 되는 작대기에 디스크 넣음
      if h_to[i] == 0:
        h_to[i] = tmp
        break
    cnt = cnt+1
    hanoi_print(A, C, B) 
    return
    

  hanoi(n-1, h_from, h_tmp, h_to) #가장 큰 디스크 빼고 나머지 디스크를 보조작대기로 옮겨야함
  
  for i in range(0, 3): #출발이 되는 작대기에서 디스크 꺼냄
    if h_from[2-i] != 0:
      tmp = h_from[2-i]
      h_from[2-i] = 0
      break
  
  for i in range(0, 3): #도착이 되는 작대기에 디스크 넣음
    if h_to[i] == 0:
      h_to[i] = tmp
      break
  cnt = cnt+1
  hanoi_print(A, C, B)


  hanoi(n-1, h_tmp, h_to, h_from) #보조작대기에 있는 디스크를 도착작대기로 옮겨야함

A = [3, 2, 1]
  B = [0, 0, 0]
  C = [0, 0, 0]
  cnt = 0
  hanoi_print(A, B, C)
  hanoi(3, A, B, C)

"""  [3, 2, 1]
  [0, 0, 0]
  [0, 0, 0]

  [3, 2, 0]
  [0, 0, 0]
  [1, 0, 0]

  [3, 0, 0]
  [2, 0, 0]
  [1, 0, 0]

  [3, 0, 0]
  [2, 1, 0]
  [0, 0, 0]

  [0, 0, 0]
  [2, 1, 0]
  [3, 0, 0]

  [1, 0, 0]
  [2, 0, 0]
  [3, 0, 0]
  
  [1, 0, 0]
  [0, 0, 0]
  [3, 2, 0]

  [0, 0, 0]
  [0, 0, 0]
  [3, 2, 1]
"""