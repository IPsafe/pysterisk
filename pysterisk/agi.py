#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime

class Log(object):


    def __init__(self, log_file):
        self.log_path = log_file

    def log(self, text):
        open(self.log_path, 'ab+', 512).write(
                "%s: %s\n" % (datetime.datetime.now(), text)
        )


class AGI(Log):


    def __init__(self, socket=None, debug=False,
                    log_file='/tmp/pysterisk_agi.log'):
        super(AGI, self).__init__(log_file)
        self.is_socket = socket
        self.debug = debug
        self.env = {}
        self._connect()

    def _connect(self):
        lines = sys.stdin.readlines()
        for line in lines:
            if not line.strip():
                break

            key, data = line.split(':')
            self.env[key.strip()] =  data.strip()

        if self.debug:
            self.log(self.env)

    def _get(self):
        res = sys.stdin.readline()
        self.log(">>> %s\n" % res)
        return res

    def _send(self, text):
        sys.stdout.write('%s\n' % text)
        sys.stdout.flush()


    def command(self, cmd, *args):
        self._send('%s %s' % (cmd, ' '.join(map(str,args))))
        return self._get()


