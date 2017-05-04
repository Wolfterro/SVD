# -*- coding: utf-8 -*-

# Imports gerais
# ==============
from __future__ import print_function
from PyQt4 import QtCore, QtGui

import os
import sys
import ssl
import urllib2
import platform

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from MessageBoxClass import ShowMessageBox

# Classe de atualização dos binários do programa
# ==============================================
class Updater(object):
	# Método de atualização do youtube-dl
	# ===================================
	def Youtube_DL(self):
		os.chdir(unicode(GlobalVars.BinFolder))
		downloadStatus = self.download(GlobalVars.ExecutableName1, 
			GlobalVars.YtDlLatestVersionURL)
		return downloadStatus

	# Método de download do executável atualizado
	# ===========================================
	def download(self, filename, url):
		try:
			request = urllib2.Request(url, headers={'User-agent' : GlobalVars.UserAgent})
			
			# DEBUG APENAS!
			# =============
			# context = ssl._create_unverified_context()
			# response = urllib2.urlopen(request, context=context)
			response = urllib2.urlopen(request)
			fSize = response.headers['content-length']

			downloaded = 0
			with open(filename, 'wb') as f:
				while True:
					fData = response.read(4096)
					downloaded += len(fData)
					if not fData:
						break
					f.write(fData)
					self.showProgress(downloaded, fSize)
			return True
		except Exception as e:
			print(u"[SVD] Erro: %s" % (e))
			return False

	# Método para calcular o progresso do download do executável
	# O método imprime uma barra de processo no terminal
	# ==========================================================
	def showProgress(self, now, total, width=50):
		progress = float(now) / float(total)
		bar = ('#' * int(width * progress)).ljust(width)
		percent = progress * 100.0
		to_print = '[SVD] Baixando: [%s] %.2f%%\r' % (bar, percent)
		print(to_print, end='')
		if round(percent) >= 100:
			print('%s\r' % (' ' * len(to_print)), end='')