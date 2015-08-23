import random

#
# res = {
#     '0': 0,
#     '10': 0,
#     '20': 0,
#     '30': 0,
#     '40': 0,
#     '50': 0,
#     '60': 0,
#     '70': 0,
#     '80': 0,
#     '90': 0
# }
#
# for i in range(1, 1000000):
#     r = random.randrange(100)
#     for j, k in reversed(sorted(res.items())):
#         if r >= int(j):
#             res[j] += 1
#             break
#
#
# for j, k in reversed(sorted(res.items())):
#     # print("{:>2} {}".format(j, k))
#     print(k)
#

for i in range(100):
    print("{:>3} {:.10}".format(i, random.gauss(0, 1)))