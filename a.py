# print(chr(105))
# print(ord('i'))


# for u in range(65,90):
#     print(chr(u),end = ',')

# for u in range(97,122):
#     print(chr(u),end = ',')

# print('z')

# n = input()

# for u in n:
#     print(ord(u),end = ',')


# with open (f'a.txt','r',encoding='utf-8') as file:
#     e1 = file.read()
#     otv = ''
#     res = ''
#     # print(e1)
#     for u in str(e1):
#         if u == '\n':
#             res += chr(int(otv))
#             otv = ''
#         else:
#             otv += u
#     print(res)
      

n = input()
n2 = ''
n3 = ''
for t in n:

    if ord(t)+13 > 90  and ord(t)+13 < 104 :
        n2 = ord(t)+13- 26
        n3 += (chr(int(n2)))
       
    elif ord(t)+13 < 90 and ord(t)+13 < 104 :
        n2 = str((ord(t))+ 13) 
        n3 += (chr(int(n2)))

    elif  ord(t)+13 > 122 :
        n2 = ord(t)+13- 26
        n3 += (chr(int(n2)))
       
    elif  ord(t)+13 < 122 and ord(t)+13 > 97 :
        n2 = str((ord(t))+ 13) 
        n3 += (chr(int(n2)))

print(n3)






        
