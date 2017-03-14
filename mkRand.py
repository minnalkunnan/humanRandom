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
   val = 0
   blocks = len(bitArr)
   blockSize = 32 / blocks
   
   for i in range(blocks):
      val = val | (bitArr[i] << (i * blockSize))
   return val   

#bitArr = [1] * 32
#print(str(getInt(bitArr)))
