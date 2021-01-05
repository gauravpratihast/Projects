import requests
import math
from tqdm import tqdm
import time
url = 'paste url here'
r = requests.get(url, stream=True)

size = int(r.headers['Content-Length'])
chunk_size = 256
n = math.ceil(size/chunk_size)
with open('file.txt', 'wb') as file:
    for chunk in tqdm(r.iter_content(chunk_size=chunk_size), total=n):
        time.sleep(0.1)
        file.write(chunk)


















# def StringChallenge(str):
#     a = ''
#     for i in str:
#         if i.isalpha():
#             a += i
#         else:
#             a += ' '
#
#     a = a.split()
#     l = ''
#     for i in range(len(a)):
#         if i==0:
#             a[i] = a[i].lower()
#         else:
#             a[i] = a[i].capitalize()
#     l = ''.join(a)
#     return l
#
# # j = input()
# # print(StringChallenge(j))
#
# j = 'a b c d-e-f%g'
# print(StringChallenge(j))
# # stop = ['!','@','$','%','-']
# #
# # j = j.lstrip('-%')
# # print(j)
# -----------------------------------TCS NQT coding questions
# from collections import Counter
# s = input()
# if len(s)>20:
#     print('wrong input')
# else:
#     for i in s:
#         if s.count==1:
#             print(i)
#             break
#     else:
#         print('exception string')
# ---------------------------------------------Finding Magic Square or not
# n = int(input())
# matrix = []
# for i in range(n):
#     nums = input()
#     matrix.append([int(x) for x in nums.split()])
#
# magic = True
# value = sum(matrix[0])
# c_mat = [[] for x in range(n)]
#
# # -------for rows
#
# for i in range(n):
#     if sum(matrix[i]) != value:
#         magic = False
#         print('here')
#
#     for j in range(n):
#         c_mat[j].append(matrix[i][j])
#
# # -------for columns
# for i in range(n):
#     if sum(c_mat[i]) != value:
#         magic = False
#         # print('yha p')
#         # print(value)
#         # print(sum(c_mat[i]))
#
# # -------for diagnoal
# i = 0
# j = 0
# l = [[], []]
# for k in range(n):
#     l[0].append(matrix[i][j])
#     l[1].append(matrix[n-1-i][j])
#     i = i + 1
#     j = j + 1
# if sum(l[0]) != value or sum(l[1]) != value:
#     magic = False
#
# if magic:
#     print('magic square')
# else:
#     print('Not a magic square')


