
import can
import os.path
from os import path  # path.exists only check for file in the current directory

vehicle_in_test_num = 10


def create_file_name(vehicle_number = 10):
    if isinstance(vehicle_number,int):
        file_name = 'PV{:02d}.asc'.format(vehicle_number)
        print('int')
    else:
        file_name = 'PV{:02.1f}.asc'.format(vehicle_number)
        print('float')
    return file_name

def log_file_name():
    global vehicle_in_test_num
    file_name = create_file_name(vehicle_in_test_num)
    while path.exists(file_name) :
        print (file_name)
        # file already exists, add 0.1 to vehicle test number
        vehicle_in_test_num = vehicle_in_test_num + 0.1
        file_name = create_file_name(vehicle_in_test_num) 
    return file_name


def msg2str(msg):
    #t = msg.timestamp (timestamp is already handled by the log_event function)
    ID = msg.arbitration_id
    c = 1
    dlc = msg.dlc
    data = msg.data
    data_str = ''
    for d in data:
        data_str = data_str +'{:02x} '.format(d)
    line =  '{}  {:03x}             Tx   d {} '.format(c,ID,dlc) + data_str
    return line


if __name__ == "__main__":
    s = can.Message(arbitration_id = 0x47,channel = 1, extended_id = False, dlc = 3, data=[0x2,0x5a,0x5f])
    line = msg2str(s)
    #print(line)
    log_file_name()
    #print(create_file_name(10.02))
