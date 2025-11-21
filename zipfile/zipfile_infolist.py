#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import datetime
import zipfile

def print_info(archive_name):
    with zipfile.ZipFile(archive_name) as zf:
        for info in zf.infolist():
            print(info.filename)
            print(' Comment :', info.comment)
            mod_date = datetime.datetime(*info.date_time)
            print(' Modified :', mod_date)

            if info.create_system == 0:
                system = 'Windows'
            elif info.create_system == 3:
                system = 'Unix'
            else:
                system = 'UNKNOW'
            print(' System  :', system)
            print(' ZIP Version  :', info.create_version)
            print(' Compressed  :', info.compress_size, 'bytes')
            print(' Uncompressed :', info.file_size, 'bytes')

if __name__ == '__main__':
    print_info('example.zip')
            
