
import os
import glob
import argparse
import textwrap
import shutil
import time
from datetime import datetime

def _parse_args():
    
    description = """BM Downloader"""
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(description),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--datetime',
                        type=str,
                        help='Image date and time in format %Y/%m/%d %H:%M',
                        required=True)
    return parser.parse_args()

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def main():
    args = _parse_args();

    date_object = datetime.strptime(args.datetime, '%Y/%m/%d %H:%M')
    timestamp = str(time.mktime(date_object.timetuple()))[0:7]

    path = os.path.join("\\home\\User\\data\\BeltMetrics\logs\\processedFragmentation", str(date_object.year), str(date_object.month), str(date_object.day), "*" + str(timestamp) + "*.png").replace("\\","/")
    print(path)
    tmp_path = os.mkdir('tmp/logs') 
    for log in glob.glob(path, recursive=True):
        shutil.copy(log, tmp_path)

if __name__ == '__main__':
    main()