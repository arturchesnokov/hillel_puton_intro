import shutil
from datetime import datetime, date, time
import os


def time_stamp():
    d = datetime.now()
    return f'{d.hour}_{d.minute}_{d.second}_{d.microsecond}'


print(time_stamp() + ".txt")
os.system(f'copy copy2.txt {time_stamp()}.txt')
