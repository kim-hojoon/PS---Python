# word = str(input())
# num = len(word)
# for i in range(len(word)):
#     if(word[i] in "="):
#         if(word[i-1:i+1] == "c="):
#             num -= 1
#         elif(word[i-2:i+1] == "dz="):
#             num -= 2
#         elif(word[i-1:i+1] == "s="):
#             num -= 1
#         elif(word[i-1:i+1] == "z="):
#             num -= 1
#     elif(word[i] in "-"):
#         if(word[i-1:i+1] == "c-"):
#             num -= 1
#         elif(word[i-1:i+1] == "d-"):
#             num -= 1
#     elif(word[i] in "j"):
#         if(word[i-1:i+1] == "lj"):
#             num -= 1
#         elif(word[i-1:i+1] == "nj"):
#             num -= 1
# print(num)

word = str(input())
cro_al = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in cro_al:
    word = word.replace(a,"0")

print(len(word))