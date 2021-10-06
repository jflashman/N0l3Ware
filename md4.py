import math

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
