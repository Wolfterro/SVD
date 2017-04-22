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
import subprocess

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from MessageBoxClass import ShowMessageBox

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Classe de downloads do programa
# ===============================
class Downloader(object):
	# Inicializando objetos da classe
	# ===============================
	def __init__(self, videoURL, saveOption, keepOriginal):
		# Propriedades da classe
		# ----------------------
		self.videoURL = videoURL
		self.saveOption = saveOption
		self.keepOriginal = keepOriginal

		self.messageBox = ShowMessageBox()

		self.saveFormat = ""
		self.isConversion = None
		self.downloadCommand = ""

		# Declarações da classe
		# ---------------------
		self.getSaveFormat()
		self.assembleDownloadCommand()

	# Resgatando o formato desejado pelo usuário
	# ==========================================
	def getSaveFormat(self):
		if "(Conversão)" in self.saveOption:
			self.isConversion = True
		else:
			self.isConversion = False
		self.saveFormat = str(self.saveOption).replace(" (Conversão)", "").lower()

	# Montando o comando para o download do vídeo
	# ===========================================
	def assembleDownloadCommand(self):
		base = "\"%s\" --ignore-errors" % (GlobalVars.Youtube_dl)

		if self.keepOriginal:
			extra1 = "-k"
		else:
			extra1 = ""
		
		if self.saveFormat in GlobalVars.AudioFormats:
			extra2 = "--extract-audio --audio-quality 0 --audio-format %s %s" % (self.saveFormat, self.videoURL)
		elif self.isConversion:
			extra2 = "--recode-video %s %s" % (self.saveFormat, self.videoURL)
		else:
			extra2 = "--format %s %s" % (self.saveFormat, self.videoURL)

		self.downloadCommand = ("%s %s %s" % (base, extra2, extra1)).encode(sys.getfilesystemencoding())

	# Realizando download do vídeo selecionado
	# ========================================
	def download(self):
		print(u"\n[SVD] Baixando Vídeo no formato \".%s\" ..." % (self.saveFormat))
		print(u"-------------------------------------------")

		downloadStatus = subprocess.call(self.downloadCommand)

		print(u"\n=================================")
		print(u"[SVD] Download Finalizado!")

	# Imprimindo comando na tela (DEBUG)
	# ==================================
	def printCommand(self):
		print(self.downloadCommand)
