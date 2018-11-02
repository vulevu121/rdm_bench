import os, shutil
import datetime, time 
import sched

file = 'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/Note.txt'
src = 'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/new/temp'
dest =  'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/new/curr'



#t = os.path.getmtime(file)
#date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
#print(date)

def move_CAN_log(source,destination):
    root, dirs, files = next(os.walk(source))
    file_count = (len(files))

    latest = 0
    paths = {}

    # if there are more than 1 files in this folder
    if file_count > 1:
        # interate through the directory
        for root, dirs, files in os.walk(source):
            for file in files:
                # make a dictionary of path to file and last modified time
                curr_path = os.path.join(source,file)
                last_modified = os.path.getmtime(curr_path)
                paths[last_modified] = curr_path
                if latest < last_modified:
                    latest = last_modified

        # check if S drive path is valid
        if os.path.exists(destination):

            # if the file is not the newest, copy the file to network drive
            for time, path in paths.items():
                if time < latest:
                    try:
                        shutil.copy(path,destination)
                    except:
                        # Fail to copy file, just exit and print error message
                        print ('Unable to copy to S drive. Exiting...')
                        break
            
            # remove the newest pair from the list.             
            del paths[latest]
            
            # Then deleted the files that were copied
            for time, path in paths.items():
                if os.path.exists(path):
                    os.remove(path)
        else:
            print('Destination is not valid. Exiting...')

if __name__ == "__main__":
    move_CAN_log(src,dest)
