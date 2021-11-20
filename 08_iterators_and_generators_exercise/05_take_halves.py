def solution():

    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        count = 1
        result = []
        while count <= n:
            for i in seq:
                result.append(i)
                count += 1
                if count >= n:
                    break
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))



# def integers():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# def halves():
#     for i in integers():
#         yield i / 2
#
#
# def take(n, seq):
#     count = 1
#     result = []
#     while count <= n:
#         for i in halves():
#             result.append(i)
#             count += 1
#             if count >= n:
#                 break
#     return result
#
# print(take(5, halves()))