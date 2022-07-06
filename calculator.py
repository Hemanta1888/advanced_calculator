import time
class Calculator:
    def addition(self) -> int:
        '''
        It is going to take multiple user inputs and
        it is going to perform addition operations.

        ==> Eg: 34,23,56
        ==> Ans: 113
        '''
        while True:
            try:
                ask_user = input(
                    "you want to perform Addition operation [Yes/No/STOP]?  "
                    )
                if ask_user.lower() == "yes":
                    uinput = input(
                        "Please enter more than one comma separated \
number to perform this operation: "
                    )
                    nums = list(map(int, uinput.split(",")))
                    result = 0
                    for num in nums:
                        result += num
                    return "The addition of the entered number is: " + str(result)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.normal_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type YES if you want to proceed else NO"
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                print("You entered wrong format. Please try again")
                time.sleep(2)

    def substraction(self) -> int:
        '''
        It is going to take multiple user inputs and
        it is going to perform substraction operations.

        ==> Eg: 12,4,10
        ==> Ans: -2
        '''
        while True:
            try:
                ask_user = input(
                    "you want to perform Substraction operations [Yes/No/STOP]? "
                )
                if ask_user.lower() == "yes":
                    u_input = input(
                        "Please enter more than one comma separated \
number to perform this operation: "
                    )
                    nums = list(map(int, u_input.split(",")))
                    sub_value = nums[0]
                    for n in range(len(nums)-1):
                        sub_value = sub_value - nums[n+1]
                    return "The substraction of the entered number is: " + str(sub_value)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.normal_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'"
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                print("You entered wrong format. Please try again")
                time.sleep(2)

    def multiplication(self) -> int:
        '''
        It is going to take multiple user inputs and
        it is going to perform multiplication operations.

        ==> Eg: 12,5,1,2
        ==> Ans: 120
        '''
        while True:
            try:
                ask_user = input(
                    "you want to perform Multiplication operations [Yes/No/STOP]? "
                )
                if ask_user.lower() == "yes":
                    u_input = input(
                        "Please enter more than one comma separated \
number to perform this operation: "
                    )
                    nums = list(map(int, u_input.split(",")))
                    mul = 1
                    for num in nums:
                        mul *= num
                    return "The multiplication of the entered number is: " + str(mul)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.normal_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'"
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                print("You entered wrong format. Please try again")
                time.sleep(2)

    def division(self) -> int:
        '''
        It is going to take two user inputs and
        it is going to perform division  operations.

        ==> Eg: First No. = 13
        ==>     Second No. = 5
        ==> Ans: Quotient = 2 and Remainder = 3
        '''
        while True:
            try:
                ask_user = input(
                    "you want to perform Division operations [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    input1 = int(input("Please enter your first number: "))
                    input2 = int(input("Please enter your second number: "))
                    quo = input1 // input2
                    remain = input1 % input2
                    print(
                        "The quotient value after dividing the first number \
with second number is: " + str(quo))
                    return (
                        "The remainder value after dividing the "
                        "first number with second number is: " + str(remain))
                elif ask_user.lower() == 'no':
                    print(
                        "Please choose again which operations you want to perform"
                        )
                    time.sleep(3)
                    return str(self.normal_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'"
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                print("You entered wrong number or wrong format.")
                time.sleep(2)

    def power(self) -> int:
        '''
        It is going to take two user inputs and
        find the power.

        ==> Eg: First No. = 2
        ==>     Second No. = 3
        ==> Result: 8 (2 to the power of 3 is 8)
        '''
        while True:
            try:
                ask_user = input(
                    "you want to perform Power operations [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    input1 = int(input("Please enter your first number: "))
                    input2 = int(
                        input(
                            "Please enter your second number: "
                            )
                        )
                    power = input1 ** input2
                    return "The power of " + str(input1) + " and " + str(input2) + " is: " + str(power)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                print("You entered wrong number or wrong format.")
                time.sleep(2)

    def triangle_area(self) -> int:
        '''
        It is going to take base and height as user inputs and
        find the area of the triangle

        ==> Eg: Base = 4
        ==>     Height = 5
        ==> Ans: Area = (Base * Height) / 2
        '''
        while True:
            try:
                ask_user = input(
                    "you want to find Triangle Area [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    base = int(input("Please enter the Base value: "))
                    height = int(input("Please enter the Height value: "))
                    area = (base * height) / 2
                    return "The Area of the Triangle is: " + str(area)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def triangle_perimeter(self) -> int:
        '''
        It is going to take 3 sides value as user inputs and
        find the perimeter of the triangle.

        ==> Eg: First side = 4
        ==>     Second side = 5
        ==>     Third side = 6
        ==> Ans: Perimeter = 4 + 5 + 6 = 15
        '''
        while True:
            try:
                ask_user = input(
                    "you want to find Triangle Perimeter [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    input1 = int(input("Please enter the first side value: "))
                    input2 = int(input("Please enter the second side value: "))
                    input3 = int(input("Please enter the third side value: "))
                    perimeter = input1 + input2 + input3
                    return "The Perimeter of the Triangle is: " + str(perimeter)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def rectangle_perimeter(self) -> int:
        '''
        It is going to take length & width value as user inputs and
        find the perimeter of the Rectangle.

        ==> Eg: Length = 4
        ==>     Width = 5
        ==> Ans: Perimeter = 2*(Length + Width) = 18
        '''
        while True:
            try:
                ask_user = input(
                    "you want to find Rectangle Perimeter [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    len = int(input("Please enter the Length value: "))
                    wid = int(input("Please enter the Width value: "))
                    perimeter = 2 * (len + wid)
                    return "The Perimeter of the Rectangle is: " + str(perimeter)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def rectangle_area(self) -> int:
        '''
        It is going to take length & width value as user inputs and
        find the Area of the Rectangle.

        ==> Eg: Length = 4
        ==>     Width = 5
        ==> Ans: Perimeter = Length * Width = 20
        '''
        while True:
            try:
                ask_user = input(
                    "you want to find Rectangle Area [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    len = int(input("Please enter the Length value: "))
                    wid = int(input("Please enter the Width value: "))
                    area = len * wid
                    return "The Area of the Rectangle is: " + str(area)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def square_perimeter(self) -> int:
        '''
        It is going to take sides value as user inputs and
        find the perimeter of the square.

        ==> Eg: side = 4
        ==> Ans: Perimeter = 4 * side = 16
        '''
        while True:
            try:
                ask_user = input("you want to find Rectangle Area [Yes/No/STOP]? ")
                if ask_user.lower() == "yes":
                    len = int(input("Please enter one side  value: "))
                    perimeter = 4 * len
                    return "The Perimeter of the Rectangle is: " + str(perimeter)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def square_area(self) -> int:
        '''
        It is going to take length & width value as user inputs and
        find the Area of the Rectangle.

        ==> Eg: side = 4
        ==> Ans: area = side * side = 16
        '''
        while True:
            try:
                ask_user = input(
                    "you want to find Rectangle Area [Yes/No/STOP]? "
                    )
                if ask_user.lower() == "yes":
                    side = int(input("Please enter the one side value: "))
                    area = side * side
                    return "The Perimeter of the Rectangle is: " + str(area)
                elif ask_user.lower() == 'no':
                    print("Please choose again which operations you want to perform")
                    time.sleep(3)
                    return str(self.advanced_operations())
                elif ask_user.lower() == 'stop':
                    self.exit_code()
                else:
                    print(
                        "I didn't understand. Please type 'YES' if you want to proceed else 'NO'."
                        )
                    time.sleep(2)
            except Exception as error:
                print("The error is: ", error)
                time.sleep(2)

    def normal_operations(self) -> str:
        '''It is going to handle different normal calculator functions'''
        print("You choosed to perform normal operations.")
        time.sleep(2)
        print("Please enter the operation number you want to perform")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        while True:
            ask = int(input("Please enter a number from above option: "))
            if ask == 1:
                return str(self.addition())
            elif ask == 2:
                return str(self.substraction())
            elif ask == 3:
                return str(self.multiplication())
            elif ask == 4:
                return str(self.division())
            else:
                print("Please enter a correct number from above options.")

    def advanced_operations(self) -> str:
        '''It is going to handle different advanced calculator functions'''
        print("You choosed to perform advanced operations.")
        time.sleep(2)
        print("Please enter the operation number you want to perform")
        print("1. Power")
        print("2. Triangle Area")
        print("3. Triangle Perimeter")
        print("4. Rectangle Area")
        print("5. Rectangle Perimeter")
        print("6. Square Area")
        print("7. Square Perimeter")
        while True:
            ask = int(input("Please enter a number from above option: "))
            if ask == 1:
                return str(self.power())
            elif ask == 2:
                return str(self.triangle_area())
            elif ask == 3:
                return str(self.triangle_perimeter())
            elif ask == 4:
                return str(self.rectangle_area())
            elif ask == 5:
                return str(self.rectangle_perimeter())
            elif ask == 6:
                return str(self.square_area())
            elif ask == 7:
                return str(self.square_perimeter())
            else:
                print("Please enter a correct number from above options.")

    def exit_code(self):
        print("Thank you for using Hemanta's calculator.")
        exit()

    def __str__(self) -> str:
        print(
            "Hello dear! Please choose below option \
according to your requiremnt."
        )
        print("1. Normal Calculation(ADD, SUB, MUL, DIV)")
        print("2. Calculate Area & Perimter (Triangle, Square, Rectangle)")
        count = 0
        while True:
            count += 1
            if count <= 5:
                ask = int(input("Please enter a number from above option: "))
                if ask == 1:
                    return str(Calculator.normal_operations(self))
                elif ask == 2:
                    return str(Calculator.advanced_operations(self))
                else:
                    print("Please enter a right option.")
            else:
                return "You exceeded minimum number of try for now. Please try again later."


calculate = Calculator()
print(calculate)
