import HashingClass

if __name__ == "__main__":
    wordList = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "111", "2222", "33333", "444444", "5555555", "66666666", "777777777", "8888888888", "99999999999", "0123456789", "9876543210", "Trampoline543", "34computer83", "5p4tul4", "f1zz6uzz", "5h4rp3ned", "flash77drive77", "test123", "456admin", "5upr3m3", "The quick brown fox jumped over the lazy dog.", "A man. A plan. A canal. Panama.", "Three Blind Mice"]

    with open('blake2bKey.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).blake2b():
                print("Issue with " + wordList[index] + " in Blake2b Hash")
                issues += 1
            index += 1
        print("Number of Issues with Blake2b Hash: " + str(issues))

    with open('blake2sKey.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).blake2s():
                print("Issue with " + wordList[index] + " in Blake2s Hash")
                issues += 1
            index += 1
        print("Number of Issues with Blake2s Hash: " + str(issues))

    with open('md2Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).md2():
                print("Issue with " + wordList[index] + " in MD2 Hash")
                issues += 1
            index += 1
        print("Number of Issues with MD2 Hash: " + str(issues))

    with open('md4Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).md4():
                print("Issue with " + wordList[index] + " in MD4 Hash")
                issues += 1
            index += 1
        print("Number of Issues with MD4 Hash: " + str(issues))

    with open('md5Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).md5():
                print("Issue with " + wordList[index] + " in MD5 Hash")
                issues += 1
            index += 1
        print("Number of Issues with MD5 Hash: " + str(issues))

    with open('sha1Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha1():
                print("Issue with " + wordList[index] + " in SHA1 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA1 Hash: " + str(issues))

    with open('sha224Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha224():
                print("Issue with " + wordList[index] + " in SHA224 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA224 Hash: " + str(issues))

    with open('sha256Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha256():
                print("Issue with " + wordList[index] + " in SHA256 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA256 Hash: " + str(issues))

    with open('sha384Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha384():
                print("Issue with " + wordList[index] + " in SHA384 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA384 Hash: " + str(issues))

    with open('sha3_224Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha3_224():
                print("Issue with " + wordList[index] + " in SHA3_224 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA3_224 Hash: " + str(issues))

    with open('sha3_256Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha3_256():
                print("Issue with " + wordList[index] + " in SHA3_256 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA3_256 Hash: " + str(issues))

    with open('sha3_384Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha3_384():
                print("Issue with " + wordList[index] + " in SHA3_384 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA3_384 Hash: " + str(issues))

    with open('sha3_512Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha3_512():
                print("Issue with " + wordList[index] + " in SHA3_512 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA3_512 Hash: " + str(issues))

    with open('sha512Key.txt') as file:
        index = 0
        issues = 0
        for line in file:
            if line.strip() != HashingClass.HashingClass(wordList[index]).sha512():
                print("Issue with " + wordList[index] + " in SHA512 Hash")
                issues += 1
            index += 1
        print("Number of Issues with SHA512 Hash: " + str(issues))
