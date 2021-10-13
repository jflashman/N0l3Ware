import math

class Hashing:
    def md2_hash(input):
        block_size = 16 # initiate the size of the block

        S = [41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6, 19,
             98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188, 76, 130, 202,
             30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24, 138, 23, 229, 18,
             190, 78, 196, 214, 218, 158, 222, 73, 160, 251, 245, 142, 187, 47, 238, 122,
             169, 104, 121, 145, 21, 178, 7, 63, 148, 194, 16, 137, 11, 34, 95, 33,
             128, 127, 93, 154, 90, 144, 50, 39, 53, 62, 204, 231, 191, 247, 151, 3,
             255, 25, 48, 179, 72, 165, 181, 209, 215, 94, 146, 42, 172, 86, 170, 198,
             79, 184, 56, 210, 150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241,
             69, 157, 112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2,
             27, 96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
             85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197, 234, 38,
             44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65, 129, 77, 82,
             106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123, 8, 12, 189, 177, 74,
             120, 136, 149, 139, 227, 99, 232, 109, 233, 203, 213, 254, 59, 0, 29, 57,
             242, 239, 183, 14, 102, 88, 208, 228, 166, 119, 114, 248, 235, 117, 75, 10,
             49, 68, 80, 180, 143, 237, 31, 26, 219, 153, 141, 51, 159, 17, 131, 20]
             # this is a predetermined set of numbers from pi that is used to generate the hash

        val = input # enter an input that is stored in val

        val = [ord(i) for i in val] # orders the ascii characters 

        padding_diff = block_size - (len(val) % block_size) # create a padding difference that is based on the remaining space of the total block
        padding = padding_diff * [padding_diff] # based on the padding difference the padding is calculated
        val = val + padding # the val is then set to itself with the padding added on

        num = 0 # num variable set to 0
        check_sum = 16 * [0] # the checksum is set to 16 0's
        block = math.ceil(len(val) / block_size) # a block is set to the rounded up answer of the length of the value divided by the block size

        for x in range(block): # now we are double looping through a block and block size number of times
            for y in range(block_size): 
                num = S[(val[x*block_size+y] ^ num)] ^ check_sum[y] # the num is set to the number in the S array that corresponds with the x muliplied by the block size plus y raised to the power of num, and then that number is raised to the power of the value of checksum at index y
                check_sum[y] = num # checksum of index y is now set to that num

        val = val + check_sum # the val is now the val plus the new checksum
        block += 1 # the block is incremented by 1

        val_digest = 48 * [0] # the val digest is now set to 48 0's

        for x in range(block): # another double loop through the block and then the block size
            for y in range(block_size):
                val_digest[block_size+y] = val[x*block_size+y] # the digest of blocksize plus y is set to the value of val at index x multiplied by the block size plus y
                val_digest[2*block_size+y] = (val_digest[block_size+y] ^ val_digest[y]) # then the digest of 2 times that first index is set to the value of the digest at index block size plus y to the power of the value at digest of y
            checktemp = 0 # check temp is then set to 0

            for y in range(18): # double for loop through 18 and then 48
                for z in range(48):
                    checktemp = val_digest[z] ^ S[checktemp] # checktemp is set to the z index of the val digest raised to the power of the value of S at index checktemp
                    val_digest[z] = checktemp # the val digest of z is set to checktemp
                checktemp = (checktemp+y) % 256 # checktemp is then set to checktemp plus y raised to the power of 256

        return("".join(map(lambda x: hex(x).lstrip("0x"), val_digest[0:16]))) # printing out the [numbers]'s to a  single hex representation

    def md4_hash(input):
        block_size = 64 # initiate a block size of 64
    
        padding = [128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                     # initiate the padding

        val = input # the value will be set to the parameter passed in

        val = [ord(i) for i in val] # sets up the input to be in the right format

        val_len = len(val) # length variable set to the length of the value
        index = val_len % 64 # index variable set to the length mod the block size

        if index < 56: # if the index is less than 56
            val = val + padding[0:(56-index)] # the new value is set to itself plus the padding from 0 to 56 minus the index
        else: # otherwise the value is set to itself plus the padding from 0 to 120 minus the index
            val = val + padding[0:(120-index)]
    
        val = val+list((val_len*8).to_bytes(8, 'little')) # the val is then set to itself plus the list version of the length multiplied by 8 and then converted to 8 bytes, with 'little' meaning that the most significant bit is at the end

        word_one = 0x67452301 # word number one that is set to an initial value that will determine the hashing start later in the program
        word_two = 0xefcdab89 # second word
        word_three = 0x98badcfe # third
        word_four = 0x10325476 # fourth

        def logic_func_one(x, y, z): # first logic function that equates to if X then Y, else Z
            return (((x) & (y)) | ((~x) & (z)))

        def logic_func_two(x, y, z): # if two or more of X, Y, Z, then it returns true, else false
            return (((x) & (y)) | ((x) & (z)) | ((y) & (z)))

        def logic_func_three(x, y, z): # this xors X with Y and then that xors with Z
            return ((x) ^ (y) ^ (z))

        def logic_func_four(x, n): # bit shift function
            return (((x) << (n)) | ((x) >> (32-(n))))

        def decode(data): # this decodes the data that is passed in 
            processed_block = [] # initiates an array
            for i in range(0, len(data), 4): # loops through the length of the data at every fourth number
                processed_block.append((data[i]) | ((data[i+1]) << 8) | ((data[i+2]) << 16) | ((data[i+3]) << 24)) # the data in the block is then changed using different logic manipulations
            return(processed_block)

        hex_val_one = 0x100000000
        hex_val_two = 0x5A827999
        hex_val_three = 0x6ED9EBA1

        for i in range(math.ceil(len(val) / block_size)): # loops through and sets block equal to the decoded information
            block = decode(val[i*block_size:(i+1)*block_size])

            var_one = word_one # the first variable is set as a placeholder for the first word
            var_two = word_two # second set as second word
            var_three = word_three # third set to third
            var_four = word_four # fourth fourth

            # first round of the process
            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[0]) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[1]) % hex_val_one , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[2]) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[3]) % hex_val_one , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[4]) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[5]) % hex_val_one , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[6]) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[7]) % hex_val_one , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[8]) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[9]) % hex_val_one , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[10]) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[11]) % hex_val_one , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[12]) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[13]) % hex_val_one , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[14]) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[15]) % hex_val_one , 19)

            # second round
            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[0] + hex_val_two) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[4] + hex_val_two) % hex_val_one , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[8] + hex_val_two) % hex_val_one , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[12] + hex_val_two) % hex_val_one , 13)
    
            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[1] + hex_val_two) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[5] + hex_val_two) % hex_val_one , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[9] + hex_val_two) % hex_val_one , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[13] + hex_val_two) % hex_val_one , 13)
    
            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[2] + hex_val_two) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[6] + hex_val_two) % hex_val_one , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[10] + hex_val_two) % hex_val_one , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[14] + hex_val_two) % hex_val_one , 13)
    
            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[3] + hex_val_two) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[7] + hex_val_two) % hex_val_one , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[11] + hex_val_two) % hex_val_one , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[15] + hex_val_two) % hex_val_one , 13)
    
            # third round
            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[0] + hex_val_three) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[8] + hex_val_three) % hex_val_one , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[4] + hex_val_three) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[12] + hex_val_three) % hex_val_one , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[2] + hex_val_three) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[10] + hex_val_three) % hex_val_one , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[6] + hex_val_three) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[14] + hex_val_three) % hex_val_one , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[1] + hex_val_three) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[9] + hex_val_three) % hex_val_one , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[5] + hex_val_three) % hex_val_one , 11)
           word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[13] + hex_val_three) % hex_val_one , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[3] + hex_val_three) % hex_val_one , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[11] + hex_val_three) % hex_val_one , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[7] + hex_val_three) % hex_val_one , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[15] + hex_val_three) % hex_val_one , 15)

            word_one = (word_one + var_one) % hex_val_one # the words are then changed again to themselves plus their respective variable mod hex_val_one
            word_two = (word_two + var_two) % hex_val_one 
            word_three = (word_three + var_three) % hex_val_one 
            word_four = (word_four + var_four) % hex_val_one 

        val_digest = word_one.to_bytes(8, 'little') # the digest is then set to word one, two, three, and four added to eachother, all in bytes
        val_digest += word_two.to_bytes(8, 'little')
        val_digest += word_three.to_bytes(8, 'little')
        val_digest += word_four.to_bytes(8, 'little')

        return("".join(map(lambda x: hex(x).lstrip("0x"), val_digest))) # returns the hex representation of the digest 

    def md5_hash(input):
        block_size = 64 # block size initialized to 64
        padding = [128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
                    # padding set to 128 followed by 59 0's

        S = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 
             0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501, 
             0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 
             0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821, 
             0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 
             0xd62f105d, 0x2441453,  0xd8a1e681, 0xe7d3fbc8, 
             0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 
             0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a, 
             0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 
             0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 
             0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 
             0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 
             0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 
             0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1, 
             0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 
             0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]
             # S set to a predetermined set of hexidecimal values

        val = input # val set to the input passed in as a parameter
        val = [ord(c) for c in val] # set up the input in a block format

        val_len = len(val) # val length set to the length of the val
        index = val_len % 64 # index set to the the val length mod 64

        if index < 56:
            val = val + padding[0:(56-index)] # if the index is set to less than 56, the val is set to the val plus the padding values from 0 to 56 minus the index
        else:
            val = val + padding[0:(120-index)] # else the val is set to the val plus padding from 0 to 120 minus the index

        val = val + list((val_len*8).to_bytes(8, 'little')) # val is then set to val plus the list of val length multiplied by 8 converted to 8 bytes in the little format

        word_one = 0x67452301 # word one set to a hexadecimal value
        word_two = 0xefcdab89 # word two set to another hex value
        word_three = 0x98badcfe # word three set to another hex value
        word_four = 0x10325476 # word four set to another hex value

        max_hex = 0x100000000

        def logic_func_one(x, y, z):
            return (((x) & (y)) | ((~x) & (z))) # logic function one returns the x and y or not x and z

        def logic_func_two(x, y, z):
            return (((x) & (z)) | ((y) & (~z))) # logic function two returns the x and z or y and not z

        def logic_func_three(x, y, z):
            return ((x) ^ (y) ^ (z)) # logic function three returns the x xor y xor z

        def logic_func_four(x, y, z):
            return ((y) ^ ((x) | (~z))) # logic function four returns y xor the result of x or not z

        def logic_func_five(x, n):
            return (((x) << (n)) | ((x) >> (32-(n)))) # logic function five returns the x left shifter by n or x right shifted by 32 minus n

        def decode(data): # decode function
            processed_block = [] # initialize an empty array called processed_block
            for i in range(0, len(data), 4): # for i in the range of zero to the length of the data, using every fourth instance
                processed_block.append((data[i]) | ((data[i+1]) << 8) | ((data[i+2]) << 16) | ((data[i+3]) << 24)) # the block is then appended with data of i or'd with the data of i plus one right shifted by 8 or'd with the data of i plus 2 shifted right 16 or'd with the data from i plus three bit shifted to the right by 24
            return(processed_block) # return the new processed block

        for i in range(math.ceil(len(val) / block_size)): # for i in the ceiling off the length of the val divided by the block size
            block = decode(val[i*block_size:(i+1)*block_size]) # the block is set to the decoded function value of the val at index i multplied by the the block size to the i plus one multiplied by the block size

            var_one = word_one # var one is initializied to the word one variable
            var_two = word_two # var two is initializied to the word two variable
            var_three = word_three # var three is initializied to the word three variable
            var_four = word_four # var four is initializied to the word four variable

            # first round of the process
            word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[0] + S[0]) % max_hex , 7))
            word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[1] + S[1]) % max_hex , 12))
            word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[2] + S[2]) % max_hex , 17))
            word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[3] + S[3]) % max_hex , 22))
            word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[4] + S[4]) % max_hex , 7))
            word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[5] + S[5]) % max_hex , 12))
            word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[6] + S[6]) % max_hex , 17))
            word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[7] + S[7]) % max_hex , 22))
            word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[8] + S[8]) % max_hex , 7))
            word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[9] + S[9]) % max_hex , 12))
            word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[10] + S[10]) % max_hex , 17))
            word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[11] + S[11]) % max_hex , 22))
            word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[12] + S[12]) % max_hex , 7))
            word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[13] + S[13]) % max_hex , 12))
            word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[14] + S[14]) % max_hex , 17))
            word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[15] + S[15]) % max_hex , 22))

            # second round of the process
            word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[1] + S[16]) % max_hex , 5))
            word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[6] + S[17]) % max_hex , 9))
            word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[11] + S[18]) % max_hex , 14))
            word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[0] + S[19]) % max_hex , 20))
            word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[5] + S[20]) % max_hex , 5))
            word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[10] + S[21]) % max_hex , 9))
            word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[15] + S[22]) % max_hex , 14))
            word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[4] + S[23]) % max_hex , 20))
            word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[9] + S[24]) % max_hex , 5))
            word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[14] + S[25]) % max_hex , 9))
            word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[3] + S[26]) % max_hex , 14))
            word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[8] + S[27]) % max_hex , 20))
            word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[13] + S[28]) % max_hex , 5))
            word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[2] + S[29]) % max_hex , 9))
            word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[7] + S[30]) % max_hex , 14))
            word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[12] + S[31]) % max_hex , 20))

            # third round of the process
            word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[5] + S[32]) % max_hex , 4))
            word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[8] + S[33]) % max_hex , 11))
            word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[11] + S[34]) % max_hex , 16))
            word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[14] + S[35]) % max_hex , 23))
            word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[1] + S[36]) % max_hex , 4))
            word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[4] + S[37]) % max_hex , 11))
            word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[7] + S[38]) % max_hex , 16))
            word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[10] + S[39]) % max_hex , 23))
            word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[13] + S[40]) % max_hex , 4))
            word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[0] + S[41]) % max_hex , 11))
            word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[3] + S[42]) % max_hex , 16))
            word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[6] + S[43]) % max_hex , 23))
            word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[9] + S[44]) % max_hex , 4))
            word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[12] + S[45]) % max_hex , 11))
            word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[15] + S[46]) % max_hex , 16))
            word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[2] + S[47]) % max_hex , 23))

            # fourth round of the process
            word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[0] + S[48]) % max_hex , 6))
            word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[7] + S[49]) % max_hex , 10))
            word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[14] + S[50]) % max_hex , 15))
            word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[5] + S[51]) % max_hex , 21))
            word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[12] + S[52]) % max_hex , 6))
            word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[3] + S[53]) % max_hex , 10))
            word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[10] + S[54]) % max_hex , 15))
            word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[1] + S[55]) % max_hex , 21))
            word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[8] + S[56]) % max_hex , 6))
            word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[15] + S[57]) % max_hex , 10))
            word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[6] + S[58]) % max_hex , 15))
            word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[13] + S[59]) % max_hex , 21))
            word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[4] + S[60]) % max_hex , 6))
            word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[11] + S[61]) % max_hex , 10))
            word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[2] + S[62]) % max_hex , 15))
            word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[9] + S[63]) % max_hex , 21))

            word_one = (word_one + var_one) % max_hex # word one is set to the word one plus the var one mod max_hex
            word_two = (word_two + var_two) % max_hex # word two is set to the word two plus the var two mod max_hex
            word_three = (word_three + var_three) % max_hex # word three is set to the word three plus the var three mod max_hex
            word_four = (word_four + var_four) % max_hex # word four is set to the word four plus the var four mod max_hex

        val_digest = word_one.to_bytes(8, 'little') # the digest is then set to word one, two, three, and four added to eachother, all in bytes
        val_digest += word_two.to_bytes(8, 'little')
        val_digest += word_three.to_bytes(8, 'little')
        val_digest += word_four.to_bytes(8, 'little')

        return("".join(map(lambda x: hex(x).lstrip("0x"), val_digest)))

    def md6_hash(input):
        return(0)

    def sha0_hash(input):
        return(0)

    def sha1_hash(input):
        return(0)

    def sha2_hash(input):
        return(0)

    def sha3_hash(input):
        return(0)
