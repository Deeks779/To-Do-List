from time import sleep

print("MY TO DO LIST")
print("_________")
print("1. ENTER A FOR ADDING IN TO DO LIST")
print("2. ENTER B FOR DELETING IN TO DO LIST")
print("3. ENTER D FOR DISPLAYING THE LIST")
print("4. ENTER C FOR MARKING THE COMPLETED TASK")
print("5. ENTER E FOR EXITING THE PROGRAM")
print("6. HERE * MEANS THAT THE TASK IS COMPLETED")
print("\n" * 2)

my_task = []


def my_list():
    print('-------------------------------')
    print("MY TO DO LIST\n")
    for i in my_task:
        print(i,my_task.index(i))
    print("------------------------------")
    sleep(1)


while True:
    i = input("What is your choice? [A,B,C,D,E]").lower()

    if i == 'a':
        task = input("Enter the task your want to add:")
        my_task.append(task)

    elif i == 'b':
        my_list()
        my_del = input("\tENTER THE TASK YOU WANT TO DELETE FROM THE LIST:")
        check = input("\t\tARE YOU SURE YOU WANT TO DELETE THE TASK [y/n]:")
        if check == 'y':
            flag = True
            for i in my_task:
                if my_del == i:
                    my_task.remove(i)
                    my_list()
                    flag = True
                    break
                else:
                    flag = False
            if not flag:
                print("NO SUCH TASK IS THERE IN THE LIST")
                my_list()
        elif check == 'n':
            my_list()

    elif i == 'd':
        my_list()

    elif i == 'c':
        my_com = input("\tENTER THE TASK YOU HAVE COMPLETED ")
        flag = True
        for i in my_task:
            if my_com == i:
                index = my_task.index(i)
                my_task[index] = " * " + i
                my_list()
                flag = True
                break
            else:
                flag = False
        if not flag:
            print("NO SUCH TASK WAS FOUND")

    elif i == 'e':
        break
