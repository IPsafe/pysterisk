#!/usr/bin/python
# encode: utf8

import os
import sys
import datetime

class Log(object):

    def __init__(self):
        open

    def log(self, text):
        buff = '[LOG] %s' % text
        print(buff)

class Agi(Log):

    def __init__(self, socket=None):
        self.is_socket = socket
        self.env = {}

    def connect(self):
        while(True):
            line = sys.stdin.readline().strip()
            if not line:
                break

            key, data = line.split(':')
            self.env[key.strip()] = data.strip()
            log(self.env)

    def get(self):
        res = sys.stdin.readline()
        sys.stdout.write(">>> %s\n" % res)
        return res

    def send(self, text):
        sys.stdout.write('%s\n' % text)
        sys.stdout.flush()


    def cmd(self):
        pass

