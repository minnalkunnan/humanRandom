def get1bitlen(msg):
   newBits = len(msg) % 2;
   return newBits
   
def get2bitlen(msg):
   newBits = len(msg) % 4;
   return newBits
   
def get4bitlen(msg):
   newBits = len(msg) % 16;
   return newBits
   
def get8bitlen(msg):
   newBit = len(msg) % 256;
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
