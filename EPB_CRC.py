import numpy as np
##def crc8(RAW_DATA, size):
##    remainder = np.uint32(0xff)
##    CRCResult = 0 
##    for byte_index in range (0,size):
##        if size == 1:
##            remainder = remainder ^ RAW_DATA
##        else:
##            remainder = remainder ^ RAW_DATA[byte_index]
##
##        for bit_index in range (8,0,-1):
##            if remainder & 0x80:
##                remainder =(remainder << 1) ^ 0x1d
##            else:
##                remainder = (remainder << 1)
##
##        remainder = np.uint32(remainder)
##    CRCResult = ~remainder & 0x00FF
##    return CRCResult


# Case 2: for PTECT_BRAKE_STATUS_TRAVEL in BRAKE_STATUS_1 (0x1B3) Group 1 in EPBsendmessage.py
def crc8_PTECT_BRAKE_STATUS_TRAVEL(msg):
    ID       = msg.arbitration_id
    RAW_DATA = msg.data
    CRCResult = 0 

    if ID == 0x1B3:
        BRAKE_STATUS_TRAVEL = np.uint16(0xff)
        BRAKE_STATUS_TRAVEL = (RAW_DATA[0] & 0x00FF) << 2
        BRAKE_STATUS_TRAVEL = BRAKE_STATUS_TRAVEL + (RAW_DATA[1] & 0x00C0) >> 6
        CNT_BRAKE_STATUS_1  = (RAW_DATA[1] & 0x000C) >> 2
        CRCResult = BRAKE_STATUS_TRAVEL + CNT_BRAKE_STATUS_1
        CRCResult = ((CRCResult ^ -1) + 1) & 0x03FF
        
    return CRCResult


# Case 3: PTECT_DRIV_INTEND_BRAKE_TORQ in EBCM_BRAKE_TORQUE (0xF5) Group 3 in EPBsendmessage.py
def crc8_PTECT_DRIV_INTEND_BRAKE_TORQ (msg):
    ID       = msg.arbitration_id
    RAW_DATA = msg.data
    CRCResult = 0 

    if ID == 0xF5:
        CNT_EBCM_BRAKE_TORQUE = np.uint8(0xf)
        CNT_EBCM_BRAKE_TORQUE = RAW_DATA[0] & 0x03
        
        CMD_TOT_BRAKE_FRICTION_TORQ1 = np.uint16(0xff)
        CMD_TOT_BRAKE_FRICTION_TORQ1 = (RAW_DATA[1] & 0x00FF) << 8

        CMD_TOT_BRAKE_FRICTION_TORQ2 = np.uint8(0xf)
        CMD_TOT_BRAKE_FRICTION_TORQ2 = RAW_DATA[2] & 0x00FF

        CMD_TOT_BRAKE_FRICTION_TORQ = np.uint16(0xff)
        CMD_TOT_BRAKE_FRICTION_TORQ = CMD_TOT_BRAKE_FRICTION_TORQ1 + CMD_TOT_BRAKE_FRICTION_TORQ2

        DRIV_INTEND_BRAKE_TORQUE3   = np.uint16(0xff)
        DRIV_INTEND_BRAKE_TORQUE3   = (RAW_DATA[3] & 0x00FF) << 8

        DRIV_INTEND_BRAKE_TORQUE4   = np.uint8(0xf)
        DRIV_INTEND_BRAKE_TORQUE4   = RAW_DATA[4] & 0x00FF

        DRIV_INTEND_BRAKE_TORQUE    = np.uint16(0xff)
        DRIV_INTEND_BRAKE_TORQUE    = DRIV_INTEND_BRAKE_TORQUE3 + DRIV_INTEND_BRAKE_TORQUE4

        CRCResult = ((DRIV_INTEND_BRAKE_TORQUE ^ CMD_TOT_BRAKE_FRICTION_TORQ) + CNT_EBCM_BRAKE_TORQUE)
        CRCResult = ((((~CRCResult))+1)&0xFFFF)
        
    return CRCResult        


def crc8(msg, crc_byte_position = None):
    ID       = msg.arbitration_id
    RAW_DATA = msg.data
    CRCResult = 0 
    remainder = np.uint32(0xff)
    size      = len(RAW_DATA)

    # Case 1: for most messages    
    if crc_byte_position != None:
        
        for byte_index in range (size):
            if byte_index != crc_byte_position:
                if size == 1:
                    remainder = remainder ^ RAW_DATA
                else:
                    remainder = remainder ^ RAW_DATA[byte_index]

                for bit_index in range (8,0,-1):
                    if remainder & 0x80:
                        remainder =(remainder << 1) ^ 0x1d
                    else:
                        remainder = (remainder << 1)

                remainder = np.uint32(remainder)
        CRCResult = ~remainder & 0x00FF
        
    # Return CRC
    return CRCResult
