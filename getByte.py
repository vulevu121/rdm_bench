def getByte(sourceByte, sourceIdxRange, destByte, destIdxRange):
    if len(sourceIdxRange) != len(destIdxRange):
        def getBit(val, bit):
            return (int((val & (1 << bit)) != 0))

        def setBit(byte, bit, bitval):
            if bitval == 1:
                return (byte | (1 << bit))
            else:
                return (byte & ~(1 << bit))

        
        for s, d in zip(sourceIdxRange, destIdxRange):
            destByte = setBit(destByte, d, getBit(sourceByte, s))

        return destByte
    else:
        print('Length of source and destination bits are not same.')
