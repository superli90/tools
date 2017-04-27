#!/usr/bin/env python

"""
@file php_l.py
@author lichao35(com@baidu.com)
@date 2017/04/10 16:43:36
"""   
 
import os
import commands
import sys

global count
count = 0
def hilite(string, status, bold):
    attr = []
    if status:
        # green
        attr.append('32')
    else:
        # red
        attr.append('31')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def walk_recursive_dir(path, dirCallback = None, fileCallback = None):
    stack = []
    ret = []
    stack.append(path);
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if(os.path.isdir(tmp)):
    #        print tmp
            for item in os.listdir(tmp):
                if not item.startswith('.'):
                    stack.append(os.path.join(tmp, item))
        elif(os.path.isfile(tmp)):
            if fileCallback:
                fileCallback(tmp)

def php_l(file):
    if os.path.splitext(file)[1] == '.php':
        code,msg = commands.getstatusoutput('php -l '+file)
        if code != 0:
            print msg
            global count
            count += 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "please input the path you want check"
        print "\tfor example: "+sys.argv[0]+" /home/pay"
        exit(0);
    print hilite('In processing, please wait!', False, True)
    walk_recursive_dir(sys.argv[1], None, php_l)
    if count == 0:
        print hilite('\n\nCongratulations! All passed !', False, True)
    else:
        print hilite('\n\nSome file not pass, has '+str(count)+' failed files totally, please check!', False, True)





