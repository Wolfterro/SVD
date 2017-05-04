# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports gerais
# ==============
from __future__ import print_function
from PyQt4 import QtCore, QtGui

import os
import sys

# Imports do programa
# ===================
from GlobalVars import GlobalVars

# Classe da caixa de mensagens
# ============================
class ShowMessageBox(object):
	def show(self, title, iconType, text, infoText, closeType, closeVal):
		msg = QtGui.QMessageBox()
		msg.setIcon(iconType)
		msg.setWindowIcon(QtGui.QIcon(GlobalVars.IconPath))

		msg.setText(text)
		msg.setInformativeText(infoText)
		msg.setWindowTitle(title)
		msg.setStandardButtons(closeType)
		msg.exec_()
		
		if closeVal != 0:
			sys.exit(closeVal)