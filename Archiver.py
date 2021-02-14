##Archives anything in downloads that was modified over a month ago. Then deletes any archive modified over 2 months ago.
import shutil
import os
from time import time, ctime

src = "/Users/Ittim/Downloads"
dst = "/Users/Ittim/Desktop/Archive/"
month = 2.628e+6
month_two = 5.256e+6

now = time()
presently = ctime(now)
modTime = now - month
delTime = now - month_two

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) < modTime:
        dst_fname = os.path.join(dst, fname)
        Alog = open("ArchivedFiles.txt", "a")
        Alog.write(fname + ' ' + "Archived on:" + ' ' + presently + "\n")
        shutil.move(src_fname, dst_fname)

for fname in os.listdir(dst):
    dst_fname = os.path.join(dst, fname)
    if last_mod_time(dst_fname) < delTime:
        Dlog = open("DeletedFiles.txt", "a")
        Dlog.write(fname + ' ' + "Deleted on:" + ' ' + presently + "\n")
        try:
            os.remove(dst_fname)
        except:
            Dlog.write(fname + ' ' + "Could not be deleted on:" + ' ' + presently + "\n")