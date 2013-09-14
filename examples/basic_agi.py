#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysterisk.agi import AGI

ast = AGI(debug=True)
ast.command('ANSWER')
ast.command('SAY NUMBER 123')