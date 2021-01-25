# # # Sol 1
# # a = int(input())
# # b = int(input())
# # print(a * (b % 10))
# # print(a * ((b % 100) // 10))
# # print(a * (b // 10))
# # print(a * b)
#
# # Sol 2
# a = int(input())
# b = input()
# for _ in b[::-1]:
#     print(a*int(_))
# print(a*int(b))

# Sol 3
a, b = int(input()), input()
print(*[a*int(_) for _ in b][::-1], a*int(b))
