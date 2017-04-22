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
import ctypes
import platform
import subprocess

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from DownloaderClass import Downloader
from MessageBoxClass import ShowMessageBox

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Determinando a pasta 'home' do usuário.
# =======================================
if platform.system() == "Windows":
	buf = ctypes.create_unicode_buffer(1024)
	ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
	home_dir = buf.value
else:
	home_dir = expanduser("~")

# Classe do gerenciador da janela principal
# =========================================
class WindowHandler(object):
	# Inicializando objetos da classe
	# ===============================
	def __init__(self, ui, MainWindow):
		self.ui = ui
		self.MainWindow = MainWindow
		self.messageBox = ShowMessageBox()

		# Propriedades da classe
		# ----------------------
		if platform.system() == "Windows":
			self.div = "\\"
		else:
			self.div = "/"
		self.isFFmpegPresent = False

		self.videoURL = ""
		self.selectedDir = ""
		self.saveOption = ""
		self.keepOriginal = None
		self.openChosenDirAfterDownload = None

		# Declarações da classe
		# ---------------------
		self.checkBinaries()

	# Verificando se os binários do youtube-dl e ffmpeg estão na pasta /bin
	# =====================================================================
	def checkBinaries(self):
		programLocation = os.getcwdu()
		GlobalVars.BinFolder = "%s%s%s" % (programLocation, self.div, "bin")

		GlobalVars.Youtube_dl = "%s%s%s" % (GlobalVars.BinFolder, self.div, "youtube-dl.exe")
		ffmpegBin = "%s%s%s" % (GlobalVars.BinFolder, self.div, "ffmpeg.exe")

		if not os.path.isfile(GlobalVars.Youtube_dl):
			self.messageBox.show(u"Erro!", 
				QtGui.QMessageBox.Critical, 
				u"Binário 'youtube-dl.exe' não está presente na pasta /bin!", 
				u"É necessário que o binário 'youtube-dl.exe' esteja presente na pasta /bin para" +
				" realizar o download dos vídeos!",
				QtGui.QMessageBox.Ok, 
				1)

		if not os.path.isfile(ffmpegBin):
			self.messageBox.show(u"Aviso!", 
				QtGui.QMessageBox.Warning, 
				u"Binário 'ffmpeg.exe' não está presente na pasta /bin!", 
				u"O programa não poderá fazer conversões de formatos sem o ffmpeg!",
				QtGui.QMessageBox.Ok, 
				0)
			self.isFFmpegPresent = False
		else:
			self.isFFmpegPresent = True

	# Mostrando informações do programa no terminal auxiliar
	# ======================================================
	def displayInfo(self):
		print(u"====================================")
		print(u"SVD - Simple Video Downloader - v%s" % (GlobalVars.Version))
		print(u"====================================\n")
		
		print(u"Este prompt de comando serve de apoio para o programa.")
		print(u"Mantenha este prompt aberto enquanto o programa estiver sendo executado!")

	# Mostrando informações do programa em uma MessageBox
	# ===================================================
	def displayAbout(self):
		self.messageBox.show(u"Simple Video Downloader", 
			QtGui.QMessageBox.Information, 
			u"SVD - Simple Video Downloader - Versão %s" % (GlobalVars.Version), 
			u"Criado por: Wolfgang Almeida - © 2017\n\n*** Este programa é licenciado sob a licença MIT ***" +
			u"\nVisite o repositório no GitHub: https://github.com/Wolfterro/SVD",
			QtGui.QMessageBox.Ok, 
			0)

	# Inserindo a pasta de destino padrão
	# ===================================
	def setDefaultDir(self):
		self.ui.lineEdit_2.setText("%s%s%s" % (home_dir, self.div, "SVD"))

	# Saindo do programa
	# ==================
	def exitProgram(self):
		sys.exit(0)

	# Verificando a pasta de destino
	# ==============================
	def checkSelectedDir(self):
		if os.path.exists(unicode(self.selectedDir)):
			os.chdir(unicode(self.selectedDir))
		else:
			os.makedirs(unicode(self.selectedDir))
			os.chdir(unicode(self.selectedDir))

	# Método para selecionar pasta de destino.
	# ========================================
	def selectOutputDir(self):
		self.selectedDir = QtGui.QFileDialog.getExistingDirectory(self.MainWindow, 
			'Selecione a pasta de destino:', home_dir, QtGui.QFileDialog.ShowDirsOnly)
		
		if self.selectedDir != "":
			if platform.system() == "Windows":
				self.ui.lineEdit_2.setText(self.selectedDir.replace("/", "\\"))
			else:
				self.ui.lineEdit_2.setText(self.selectedDir)

	# Congelando os botões da janela principal
	# ========================================
	def freezeProgramFields(self, freeze):
		if freeze:
			self.ui.pushButton.setEnabled(False)
			self.ui.toolButton.setEnabled(False)
			QtGui.QApplication.processEvents()
		else:
			self.ui.pushButton.setEnabled(True)
			self.ui.toolButton.setEnabled(True)
			QtGui.QApplication.processEvents()

	# Resgatando informações do usuário
	# =================================
	def gatherUserInformation(self):
		self.videoURL = str(self.ui.lineEdit.text())
		self.selectedDir = str(self.ui.lineEdit_2.text())
		self.checkSelectedDir()

		self.saveOption = str(self.ui.comboBox.currentText())
		self.keepOriginal = self.ui.checkBox_2.isChecked()
		self.openChosenDirAfterDownload = self.ui.checkBox.isChecked()
		
		if self.videoURL != "":
			self.beginDownloadProcess()
		else:
			self.messageBox.show(u"Erro!", 
				QtGui.QMessageBox.Critical, 
				u"URL do Vídeo ou Playlist vazia!", 
				u"Insira a URL do Vídeo ou Playlist desejada e tente novamente!",
				QtGui.QMessageBox.Ok, 
				0)

	# Iniciando o processo de download
	# ================================
	def beginDownloadProcess(self):
		self.freezeProgramFields(True)
		# ------------------------------------------------------------------------
		downloader = Downloader(self.videoURL, self.saveOption, self.keepOriginal)
		downloader.download()
		# ------------------------------------------------------------------------
		self.freezeProgramFields(False)

		if self.openChosenDirAfterDownload:
			if platform.system() == "Windows":
				os.startfile(unicode(self.selectedDir))
			else:
				try:
					subprocess.Popen(["xdg-open", "%s" % unicode(self.selectedDir)])
				except Exception as e:
					pass

	# Atualizando o binário do youtube-dl
	# ===================================
	def updateYoutube_dl(self):
		try:
			print(u"\n[SVD] Atualizando youtube-dl...")
			print(u"-------------------------------")

			self.freezeProgramFields(True)
			# -----------------------------------------------
			self.updateCommand = ("%s %s" % (GlobalVars.Youtube_dl, "-U")).encode(sys.getfilesystemencoding())
			updateStatus = subprocess.call(self.updateCommand)
			# -----------------------------------------------
			self.freezeProgramFields(False)

			print(u"\n[SVD] Atualização do youtube-dl concluída!")
		except Exception as e:
			print(u"\n[SVD] Erro ao tentar atualizar o youtube-dl!")
			print(u"[SVD] Erro: %s" % (e))