#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysterisk.agi import Agi

ast = Agi(debug=True, log_file='./basic.log')
ast.connect()
ast.send('SAY NUMBER 123')