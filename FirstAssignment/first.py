import math
def isPrime(num):
    limit = int(math.sqrt(num))
    if num > 1:
        for i in range(2, limit+1):
            if(num % i ==0):
                return False
        return True
    else:
        return False

def primesInFile(file, lenNumber):
     count=0
     f = open(file, "rb")
     f.seek(0,2) #Jumps to the end
     endloc = f.tell()    #Give you the end location (characters from start)
     f.seek(0)   #Jump to the beginning of the file again
     while(f.tell() != endloc-lenNumber-1):
        currnum  = int(f.read(lenNumber))
        if(isPrime(currnum)):
            count+=1
            print(currnum, " is prime!")
            #return
        f.seek(-lenNumber+1, 1)

     if(count > 0):
         print("There are ", count, " prime numbers in the file!")
     else:
         print("There are no prime numbers in the file!")
     f.close()

def main():
    lenNumber = input("Enter how much digits do you want for a number: ")
    lenNumber = int(lenNumber)
    primesInFile("eulerDigits.txt", lenNumber)

if __name__ == "__main__":
    main()