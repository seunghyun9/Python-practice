from bye.example import Example

if __name__ == '__main__':
    ex = Example()
    while 1:
        menu = input("0.bugs 1.melon 2.practice1 3.practice2 ")

        if menu == '00':
            ex.bugs()
        elif menu == '1':
            ex.melon()
        elif menu == '2':
            ex.practice1()
        elif menu == '3':
            ex.practice1()
