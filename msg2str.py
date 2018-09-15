import can




def msg2str(msg):
    t = msg.timestamp
    ID = msg.arbitration_id
    c = msg.channel
    dlc = msg.dlc
    data = msg.data
    data_str = ''
    for d in data:
        data_str = data_str +'{:x} '.format(d)
    line =  '{} {} {:x} Tx d {} '.format(t,c,ID,dlc) + data_str
    return line


if __name__ == "__main__":
    s = can.Message(arbitration_id = 0x47,channel = 1, extended_id = False, dlc = 3, data=[0x2,0x5a,0x5f])
    line = msg2str(s)
    print(line)
