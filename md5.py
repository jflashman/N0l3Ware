import math

def md5_hash(input):
    block_size = 64 # block size initialized to 64
    padding = [
        128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ] # padding set to 128 followed by 59 0's
    S = [   0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 
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
        word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[0] + 0xd76aa478) % 0x100000000 , 7))
        word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[1] + 0xe8c7b756) % 0x100000000 , 12))
        word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[2] + 0x242070db) % 0x100000000 , 17))
        word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[3] + 0xc1bdceee) % 0x100000000 , 22))
        word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[4] + 0xf57c0faf) % 0x100000000 , 7))
        word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[5] + 0x4787c62a) % 0x100000000 , 12))
        word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[6] + 0xa8304613) % 0x100000000 , 17))
        word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[7] + 0xfd469501) % 0x100000000 , 22))
        word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[8] + 0x698098d8) % 0x100000000 , 7))
        word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[9] + 0x8b44f7af) % 0x100000000 , 12))
        word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[10] + 0xffff5bb1) % 0x100000000 , 17))
        word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[11] + 0x895cd7be) % 0x100000000 , 22))
        word_one = (word_two + logic_func_five((word_one + logic_func_one(word_two, word_three, word_four) + block[12] + 0x6b901122) % 0x100000000 , 7))
        word_four = (word_one + logic_func_five((word_four + logic_func_one(word_one, word_two, word_three) + block[13] + 0xfd987193) % 0x100000000 , 12))
        word_three = (word_four + logic_func_five((word_three + logic_func_one(word_four, word_one, word_two) + block[14] + 0xa679438e) % 0x100000000 , 17))
        word_two = (word_three + logic_func_five((word_two + logic_func_one(word_three, word_four, word_one) + block[15] + 0x49b40821) % 0x100000000 , 22))

        # second round of the process
        word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[1] + 0xf61e2562) % 0x100000000 , 5))
        word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[6] + 0xc040b340) % 0x100000000 , 9))
        word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[11] + 0x265e5a51) % 0x100000000 , 14))
        word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[0] + 0xe9b6c7aa) % 0x100000000 , 20))
        word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[5] + 0xd62f105d) % 0x100000000 , 5))
        word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[10] + 0x2441453) % 0x100000000 , 9))
        word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[15] + 0xd8a1e681) % 0x100000000 , 14))
        word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[4] + 0xe7d3fbc8) % 0x100000000 , 20))
        word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[9] + 0x21e1cde6) % 0x100000000 , 5))
        word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[14] + 0xc33707d6) % 0x100000000 , 9))
        word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[3] + 0xf4d50d87) % 0x100000000 , 14))
        word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[8] + 0x455a14ed) % 0x100000000 , 20))
        word_one = (word_two + logic_func_five((word_one + logic_func_two(word_two, word_three, word_four) + block[13] + 0xa9e3e905) % 0x100000000 , 5))
        word_four = (word_one + logic_func_five((word_four + logic_func_two(word_one, word_two, word_three) + block[2] + 0xfcefa3f8) % 0x100000000 , 9))
        word_three = (word_four + logic_func_five((word_three + logic_func_two(word_four, word_one, word_two) + block[7] + 0x676f02d9) % 0x100000000 , 14))
        word_two = (word_three + logic_func_five((word_two + logic_func_two(word_three, word_four, word_one) + block[12] + 0x8d2a4c8a) % 0x100000000 , 20))

        # third round of the process
        word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[5] + 0xfffa3942) % 0x100000000 , 4))
        word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[8] + 0x8771f681) % 0x100000000 , 11))
        word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[11] + 0x6d9d6122) % 0x100000000 , 16))
        word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[14] + 0xfde5380c) % 0x100000000 , 23))
        word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[1] + 0xa4beea44) % 0x100000000 , 4))
        word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[4] + 0x4bdecfa9) % 0x100000000 , 11))
        word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[7] + 0xf6bb4b60) % 0x100000000 , 16))
        word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[10] + 0xbebfbc70) % 0x100000000 , 23))
        word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[13] + 0x289b7ec6) % 0x100000000 , 4))
        word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[0] + 0xeaa127fa) % 0x100000000 , 11))
        word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[3] + 0xd4ef3085) % 0x100000000 , 16))
        word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[6] + 0x4881d05) % 0x100000000 , 23))
        word_one = (word_two + logic_func_five((word_one + logic_func_three(word_two, word_three, word_four) + block[9] + 0xd9d4d039) % 0x100000000 , 4))
        word_four = (word_one + logic_func_five((word_four + logic_func_three(word_one, word_two, word_three) + block[12] + 0xe6db99e5) % 0x100000000 , 11))
        word_three = (word_four + logic_func_five((word_three + logic_func_three(word_four, word_one, word_two) + block[15] + 0x1fa27cf8) % 0x100000000 , 16))
        word_two = (word_three + logic_func_five((word_two + logic_func_three(word_three, word_four, word_one) + block[2] + 0xc4ac5665) % 0x100000000 , 23))

        # fourth round of the process
        word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[0] + 0xf4292244) % 0x100000000 , 6))
        word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[7] + 0x432aff97) % 0x100000000 , 10))
        word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[14] + 0xab9423a7) % 0x100000000 , 15))
        word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[5] + 0xfc93a039) % 0x100000000 , 21))
        word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[12] + 0x655b59c3) % 0x100000000 , 6))
        word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[3] + 0x8f0ccc92) % 0x100000000 , 10))
        word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[10] + 0xffeff47d) % 0x100000000 , 15))
        word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[1] + 0x85845dd1) % 0x100000000 , 21))
        word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[8] + 0x6fa87e4f) % 0x100000000 , 6))
        word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[15] + 0xfe2ce6e0) % 0x100000000 , 10))
        word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[6] + 0xa3014314) % 0x100000000 , 15))
        word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[13] + 0x4e0811a1) % 0x100000000 , 21))
        word_one = (word_two + logic_func_five((word_one + logic_func_four(word_two,word_three, word_four) + block[4] + 0xf7537e82) % 0x100000000 , 6))
        word_four = (word_one + logic_func_five((word_four + logic_func_four(word_one, word_two, word_three) + block[11] + 0xbd3af235) % 0x100000000 , 10))
        word_three = (word_four + logic_func_five((word_three + logic_func_four(word_four, word_one, word_two) + block[2] + 0x2ad7d2bb) % 0x100000000 , 15))
        word_two = (word_three + logic_func_five((word_two + logic_func_four(word_three, word_four, word_one) + block[9] + 0xeb86d391) % 0x100000000 , 21))

        word_one = (word_one + var_one) % 0x100000000 # word one is set to the word one plus the var one mod 0x100000000
        word_two = (word_two + var_two) % 0x100000000 # word two is set to the word two plus the var two mod 0x100000000
        word_three = (word_three + var_three) % 0x100000000 # word three is set to the word three plus the var three mod 0x100000000
        word_four = (word_four + var_four) % 0x100000000 # word four is set to the word four plus the var four mod 0x100000000

    val_digest = word_one.to_bytes(8, 'little') # the digest is then set to word one, two, three, and four added to eachother, all in bytes
    val_digest += word_two.to_bytes(8, 'little')
    val_digest += word_three.to_bytes(8, 'little')
    val_digest += word_four.to_bytes(8, 'little')

    return("".join(map(lambda x: hex(x).lstrip("0x"), val_digest)))
