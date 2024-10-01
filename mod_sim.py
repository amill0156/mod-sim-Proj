import simpy
import random
import golf_course
import course_operator

def main():
    print("Hello and welcome to Miller's Landing Golf and Country Club!")
    print("We're glad you're here!")



def cart_recieve():
    num_of_carts = 52
    num_of_tee_times = 26

    carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    taken_carts = []
    tee_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    for group_num in tee_times:
        print("\nPlease type '+' to receive group " + str(group_num) + "'s carts:")
        user_input = input()
        if user_input == '+':

            taken_carts = random.choices(carts, k=2)
            carts.remove(taken_carts[0])
            carts.remove(taken_carts[1])

            print("Carts taken:")
            print(str(taken_carts))
            print("Carts available:")
            print(carts)
        else:
            print("Please return to pro shop for assistance.")
            break


def cart_return():
    carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    taken_carts = []
    tee_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    for group_num in tee_times:
            carts.add(taken_carts[0])
            carts.add(taken_carts[1])
            print("Carts taken:")
            print(str(taken_carts))
            print("Carts available:")
            print(carts)




if __name__ == "__main__":
    main()
    cart_recieve()