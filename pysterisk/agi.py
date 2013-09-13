#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

class Log(object):

    def __init__(self, log_file):
        self.log_path = log_file

    def log(self, text):
        open(self.log_path, 'ab+', 512).write(
                "%s: %s\n" % (datetime.datetime.now(), text)
        )


class Agi(Log):

    def __init__(self, socket=None, debug=False, log_file='/tmp/pysterisk_agi.log'):
        super(Agi, self).__init__(log_file)
        self.is_socket = socket
        self.debug = debug
        self.env = {}

    def connect(self):
        lines = sys.stdin.readlines()
        for line in lines:
            if not line.strip():
                break

            key, data = line.split(':')
            self.env[key.strip()] =  data.strip()

        if self.debug:
            self.log(self.env)

    def get(self):
        res = sys.stdin.readline()
        sys.stdout.write(">>> %s\n" % res)
        return res

    def send(self, text):
        sys.stdout.write('%s\n' % text)
        sys.stdout.flush()


    def cmd(self):
        pass

