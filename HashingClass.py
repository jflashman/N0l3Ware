import math

class Hashing:
    def md2_hash(input):
        block_size = 16 # initiate the size of the block

        S = [
        41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6, 19,
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
        padding = [
        128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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

        for i in range(math.ceil(len(val) / block_size)): # loops through and sets block equal to the decoded information
            block = decode(val[i*block_size:(i+1)*block_size])

            var_one = word_one # the first variable is set as a placeholder for the first word
            var_two = word_two # second set as second word
            var_three = word_three # third set to third
            var_four = word_four # fourth fourth

            # first round of the process
            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[0]) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[1]) % 0x100000000 , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[2]) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[3]) % 0x100000000 , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[4]) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[5]) % 0x100000000 , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[6]) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[7]) % 0x100000000 , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[8]) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[9]) % 0x100000000 , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[10]) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[11]) % 0x100000000 , 19)

            word_one = logic_func_four((word_one + logic_func_one(word_two, word_three, word_four) + block[12]) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_one(word_one, word_two, word_three) + block[13]) % 0x100000000 , 7)
            word_three = logic_func_four((word_three + logic_func_one(word_four, word_one, word_two) + block[14]) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_one(word_three, word_four, word_one) + block[15]) % 0x100000000 , 19)

            # second round
            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[0] + 0x5A827999) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[4] + 0x5A827999) % 0x100000000 , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[8] + 0x5A827999) % 0x100000000 , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[12] + 0x5A827999) % 0x100000000 , 13)

            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[1] + 0x5A827999) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[5] + 0x5A827999) % 0x100000000 , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[9] + 0x5A827999) % 0x100000000 , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[13] + 0x5A827999) % 0x100000000 , 13)

            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[2] + 0x5A827999) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[6] + 0x5A827999) % 0x100000000 , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[10] + 0x5A827999) % 0x100000000 , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[14] + 0x5A827999) % 0x100000000 , 13)

            word_one = logic_func_four((word_one + logic_func_two(word_two, word_three, word_four) + block[3] + 0x5A827999) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_two(word_one, word_two, word_three) + block[7] + 0x5A827999) % 0x100000000 , 5)
            word_three = logic_func_four((word_three + logic_func_two(word_four, word_one, word_two) + block[11] + 0x5A827999) % 0x100000000 , 9)
            word_two = logic_func_four((word_two + logic_func_two(word_three, word_four, word_one) + block[15] + 0x5A827999) % 0x100000000 , 13)

            # third round
            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[0] + 0x6ED9EBA1) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[8] + 0x6ED9EBA1) % 0x100000000 , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[4] + 0x6ED9EBA1) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[12] + 0x6ED9EBA1) % 0x100000000 , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[2] + 0x6ED9EBA1) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[10] + 0x6ED9EBA1) % 0x100000000 , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[6] + 0x6ED9EBA1) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[14] + 0x6ED9EBA1) % 0x100000000 , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[1] + 0x6ED9EBA1) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[9] + 0x6ED9EBA1) % 0x100000000 , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[5] + 0x6ED9EBA1) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[13] + 0x6ED9EBA1) % 0x100000000 , 15)

            word_one = logic_func_four((word_one + logic_func_three(word_two, word_three, word_four) + block[3] + 0x6ED9EBA1) % 0x100000000 , 3)
            word_four = logic_func_four((word_four + logic_func_three(word_one, word_two, word_three) + block[11] + 0x6ED9EBA1) % 0x100000000 , 9)
            word_three = logic_func_four((word_three + logic_func_three(word_four, word_one, word_two) + block[7] + 0x6ED9EBA1) % 0x100000000 , 11)
            word_two = logic_func_four((word_two + logic_func_three(word_three, word_four, word_one) + block[15] + 0x6ED9EBA1) % 0x100000000 , 15)

            word_one = (word_one + var_one) % 0x100000000 # the words are then changed again to themselves plus their respective variable mod 0x100000000
            word_two = (word_two + var_two) % 0x100000000 
            word_three = (word_three + var_three) % 0x100000000 
            word_four = (word_four + var_four) % 0x100000000 

        val_digest = word_one.to_bytes(8, 'little') # the digest is then set to word one, two, three, and four added to eachother, all in bytes
        val_digest += word_two.to_bytes(8, 'little')
        val_digest += word_three.to_bytes(8, 'little')
        val_digest += word_four.to_bytes(8, 'little')

        return("".join(map(lambda x: hex(x).lstrip("0x"), val_digest))) # returns the hex representation of the digest 
    
