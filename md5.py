import math

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
