import os, shutil
import datetime, time 
from apscheduler.scheduler import Scheduler

file = 'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/Note.txt'
#src = 'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/new/temp'
src = '/home/pi/CAN Logs'
#dest =  'C:/Users/knguyen/Desktop/2.0 Test Bench/2.0 RDM bench/new/curr'
dest = '/mnt/Sdrive'


def move_CAN_log(source,destination):
    if os.path.exists(source) == False:
        print ('path to Source Directory is invalid')
        return
    if os.path.exists(destination) == False:
        print ('path to Destination Directory is invalid')
        return
    
    root, dirs, files = next(os.walk(source))
    file_count = (len(files))

    latest = 0
    paths = {}

    # if there are more than 1 files in this folder s
    if file_count > 1:
        # interate through the directory
        for root, dirs, files in os.walk(source):
            for file in files:
                # make a dictionary of path to file and last modified time
                curr_path = os.path.join(source,file)
                last_modified = os.path.getmtime(curr_path)
                paths[last_modified] = curr_path
                # mark the file created most recently
                if latest < last_modified:
                    latest = last_modified

        # if the file is not the newest, copy the file to network drive
        for time, path in paths.items():
            if time < latest:
                try:
                    shutil.copy2(path,destination)

                except:
                    # Fail to copy file, just exit and print error message
                    print ('Unable to copy file. Exiting...')
                    return
                
        print ('Files moved successfully')

# Execute this at the end of the day        
def directory_cleanup(source, destination):
    
    if os.path.exists(source) == False:
        print ('path to Source Directory is invalid')
        return
    if os.path.exists(destination) == False:
        print ('path to Destination Directory is invalid')
        
    # interate through the source directory
    for root, dirs, files in os.walk(source):
        
       # interate through the files 
        for file in files:

            # create the path to the destination directory
            path = os.path.join(destination,file)

            # if file exists in destination directory
            if os.path.exists(path):
                # delete the file in the source directory
                src_path = os.path.join(source,file)
                os.remove(src_path)
    print ('Clean Up Completed')        
        
def job(string):
    print (string)

if __name__ == "__main__":
    sched = Scheduler()
    sched.start()
    sched.add_interval_job(move_CAN_log, minutes = 5, args = [src,dest,])
    time.sleep(5)
    sched.add_interval_job(directory_cleanup, minutes = 5, args = [src,dest,])

##    for root, dirs, files in os.walk(src):
##        for file in files:
##            # make a dictionary of path to file and last modified time
##            curr_path = os.path.join(src,file)
##            print(curr_path)

    #move_CAN_log(src,dest)
    #directory_cleanup(src,dest)

