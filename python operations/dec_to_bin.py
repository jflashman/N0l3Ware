# binary to decimal and vice versa 
#Global Variables
user_input = ""
error_msg = ""

################### MAIN FUNCTION ###########################
def main():
    global user_input, error_msg

    error_msg = "Error in Input!\n"

    # 0 = bin->dec, 1=dec->bin
    choice=1
    #input("Enter 0 for Binary to Decimal Converter, 1 for Decimal to Binary Converter:") # or X to exit: ").strip().lower()
    if choice == "0":
        bin_to_dec()
    elif choice== "1":
        dec_to_bin()
    else:
        return(error_msg) #print("Invalid Input.\n")
     #   exit(0)
#end of main()


################# DECIMAL TO BINARY ######################
def dec_to_bin():
    global user_input, error_msg
    user_input = input("Enter decimal: ")

    orig_decimal = str(user_input)  #temp to check if decimal is valid

    if orig_decimal.isdigit():      #checks if devimal is valid
        pass
    else:
        return(error_msg)
      #  print("Error in Input!\n")
        exit(0)#break

    # conversion from decimal to binary
    num = int(user_input)
    final_binary = ""
    while (num > 0):
        temp = int(float(num % 2))
        final_binary = str(temp) + final_binary
        num = (num - temp) / 2

    #end of conversion

    print(final_binary)

    return(final_binary)
#end of dec2bin function


#Fxnn Calls
main()

