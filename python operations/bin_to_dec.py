# binary to decimal and vice versa 
#Global Variables
user_input = ""
error_msg = ""

################### MAIN FUNCTION ###########################
def main():
    global user_input, error_msg

    error_msg = "Error in Input!\n"

    # 0 = bin->dec, 1=dec->bin
    choice=input("Enter 0 for Binary to Decimal Converter, 1 for Decimal to Binary Converter:") # or X to exit: ").strip().lower()
    if choice == "0":
        bin_to_dec()
    elif choice== "1":
        dec_to_bin()
    else:
        return(error_msg) #print("Invalid Input.\n")
     #   exit(0)
#end of main()

################ BINARY TO DECIMAL ################
def bin_to_dec():
    global user_input
    result = 0  #placeholder for final conversion
    user_input = input("Enter binary: ")

    orig_binary = str(user_input)   #convert to string to access each int

    for bin in orig_binary:         #checks if binary is valid
        if bin == "0" or bin == "1":
            pass
            #continue
        else:
            error_msg= "Error in Input!\n"
            return(error_msg)
            exit(0)


    rev_binary = reversed(str(user_input))  #reverse binary to start converting


    for i, num in enumerate(rev_binary):    #conversion for each binary
        power = 2**i
        if int(num) == 1:
            result += power
        else:
            result += 0

    print(result)

    return(result)
#end of bin2dec


#main call
main()
