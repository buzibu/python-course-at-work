

# while True:
#     user_name = str(input("Enter username at least 3 symbols"))
#     if len(user_name) >= 5:
#         break
# print("Welcome {}". format(user_name))


# i = 1
# sum = 0
# while i <= 100:
#     if i%2 ==0:
#         sum += i
#     i += 1
# print(sum)

# str = 'one two three'
# for c in str:
#     if c =='o' or c =='e':
#         continue
#     print(c)


# import random
#
# max_tries = 5
#
# machine_num = random.randint(1,10)
# print('machine number: {}'.format(machine_num))
# tries = 0
# while tries <= max_tries:
#     user_number = int(input("Guess the number between 1 and 10 > "))
#     tries += 1
#     if user_number < machine_num:
#         print("your number is less than mine")
#     elif user_number > machine_num:
#         print("your number is more than mine")
#     else:
#         print("Congratulations!")
#         break


# # сумата на четните числа от 50 до 100
# suma = 0
# for i in range(50, 101, 2):
#     suma += i
# print(suma)
#
# # the same
# print(sum( range(50, 101, 2)))
#
# # range to list
# print([x for x in range(10)])



#print([x for x in user_name[::-1]])

#
# user_name = 'abcd'
#
# for i in range(len(user_name)-1,-1,-1):
#     print(user_name[i])







# 2018-03-30 -------------------------------------------------------------------------------------

# numbers = {
#     "Vladi": "0878517880",
#     "police": "166",
#     "customer care": "123",
#     "emergency": "111",
#     "Pesho": "0888 88 88 88",
#     "Bill Gates": "*******"
# }
#
# for i in numbers:
#     print("{} - {}".format(i, numbers[i]))


# student_scores = {
#     'Ivan': 5.0,
#     'Alex': 3.5,
#     'Maria': 5.5,
#     'Georgy': 5.0
# }
#
# best_student_scores = {}
#
# for student in student_scores:
#     if student_scores[student] > 4.0:
#         best_student_scores[student] = student_scores[student]
#
# for st in best_student_scores:
#     print(st)
#
# def my_f(a, b):
#     """
#
#     :param a:
#     :param b:
#     :return:
#     """
#     return a+b
#

# 2018-04-02 -------------------------------------------------------------------------------------

