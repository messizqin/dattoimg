#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python3

import os
 
def convert(inpath, outpath):
    # get all files in the directory
    fileitems = os.listdir(inpath)
 
    cc = 0
    # loop over each file in the directory
    for fileitem in fileitems:
        # get file name
        filename = fileitem[0:fileitem.find('.')]
 
        # read binary file
        f1 = open(os.path.join(inpath, fileitem), 'rb')
        fileitembytes = f1.read()
        newfile = []
 
        if (fileitembytes[0] ^ 0xFF) == (fileitembytes[1] ^ 0xD8):
            y1 = fileitembytes[0] ^ 0xFF
            print('%d: %s,JPG,encode pattern 0x%X' % (cc + 1, fileitem, y1))
 
            # perform byte conversion
            for i in fileitembytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
 
            # write new file
            f2 = open(os.path.join(outpath, filename + '.jpg'), 'wb')
            f2.write(newfile2)
            cc += 1
 
        elif (fileitembytes[0] ^ 0x89) == (fileitembytes[1] ^ 0x50):
            y1 = fileitembytes[0] ^ 0x89
            print('%d: %s,PNG,encode pattern 0x%X' % (cc + 1, fileitem, y1))
            for i in fileitembytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            f2 = open(os.path.join(outpath, filename+'.png'), 'wb')
            f2.write(newfile2)
            cc += 1
 
        elif (fileitembytes[0] ^ 0x47) == (fileitembytes[1] ^ 0x49):
            y1 = fileitembytes[0] ^ 0x47
            print('%d: %s,GIF,encode pattern 0x%X' % (cc + 1, fileitem, y1))
            for i in fileitembytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            f2 = open(os.path.join(outpath, filename+'.gif'), 'wb')
            f2.write(newfile2)
            cc += 1
        else:
            print('%s not recognized!' % fileitem)
    print('converted %d images in total!' % cc):

 

if __name__ == '__main__':
    convert(
        r'/Applications/WeChat/FileStorage/Image/2020-11',
        r'/Downloads/Image/'
    )



