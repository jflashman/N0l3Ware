#Global Variables
user_input = ""

#Functions
def main():
    global user_input

#test for if dec2bin or bni2dec
	user_input = input("Enter 0 for Binary to Decimal Converter, 1 for Decimal to Binary Converter or X to exit: ").strip().lower()
    if user_input == "0":
        bin2dec()
    elif user_input == "1":
        dec2bin()
    elif user_input == "x":
        exit(0)
    else:
        print("Invalid Input.\n")
        exit(0)

def bin2dec():
    global user_input
    contFlag = False
    	user_input = input("Enter binary: ")
        Data = list(user_input)
        sum = 0
        i = 1
	#if ()
        for bin in Data:
            if bin == "0" or bin == "1":
                sum += int(bin) * pow(2, len(binData) - i)
                i += 1
            else:
                print("Error in Input!")
                contFlag = True
                break

        if contFlag == True:
            contFlag = False
            continue

        print("Binary Value: " + user_input + "\nDecimal Value: " + str(sum))

    #else:
     exit(0)


def dec2bin():
    global user_input
    	user_input = input("Enter decimal: ").strip()
        if user_input == "x":
            exit(0)
        num = int(user_input)
        binary = ""
        while (num > 0):
            temp = int(float(num % 2))
            binary = str(temp) + binary
            num = (num - temp) / 2
        print("Decimal Value: " + user_input + "\nBinary Value: " + binary)
    #else:
     #   exit(0)

#Fxnn Calls
main()
