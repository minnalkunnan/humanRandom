def get1bitlen(msgLen):
   newBits = msgLen % 2;
   return newBits
   
def get2bitlen(msgLen):
   newBits = msgLen % 4;
   return newBits
   
def get4bitlen(msgLen):
   newBits = msgLen % 16;
   return newBits
   
def get8bitlen(msgLen):
   newBit = msgLen % 256;
   return newBit
   
def getInt(bitArr):
   char = 0
   val = ""
   blocks = len(bitArr)
   blockSize = 32 / blocks
   j = 0
   for i in range(blocks):
      char = char | (bitArr[i] << (j * blockSize))
      j += 1
      if j * blockSize == 8:
         val = val + chr(char)
         char = 0
         j = 0
         
   return val   

#bitArr = [1] * 32
#print(str(getInt(bitArr)))
