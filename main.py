"""
Test Task Synchronization
Dobri Popov

I can also write code that would only sync the folders if it detects source file's 
have been modified. But I wasn't sure if this is necessary!
"""

import datetime
import os
import shutil
import time

source_fp = os.path.join(os.getcwd(), "source")
source_replica_fp = os.path.join(os.getcwd(), "replica")

while True:
    # sleeps for 20 seconds causing the loop to run every 20 seconds or whatever time necessary
    time.sleep(20)

    # loop though files in source copy & paste and over it into replica overwriting it
    for file in os.listdir(source_fp):

        file_in_source_path = os.path.join(source_fp, file)
        file_in_replica_path = os.path.join(source_replica_fp, file)

        # creates log text file if it doesn't exist, logs every event
        # from synchronization, original destination, final destination and date & time
        log_file = os.path.join(source_fp, "log")
        with open(log_file, mode="a+") as log:
            log.write(f"\n {file_in_source_path} has been copied & overwritten to {file_in_replica_path} at {datetime.datetime.now()}")

        # copy and paste file, from source file path to replica path
        shutil.copyfile(file_in_source_path, file_in_replica_path)
