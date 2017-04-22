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
from WindowHandlerClass import WindowHandler

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Codificação dos elementos da janela principal
# =============================================
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

# Classe da janela principal do programa
# ======================================
class Ui_MainWindow(object):
	def setupUi(self, MainWindow, Handler):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(648, 253)
		MainWindow.setMaximumSize(QtCore.QSize(648, 253))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(GlobalVars.IconName)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout = QtGui.QGridLayout(self.groupBox)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.label = QtGui.QLabel(self.groupBox)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.lineEdit = QtGui.QLineEdit(self.groupBox)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
		self.lineEdit_2.setReadOnly(True)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
		self.toolButton = QtGui.QToolButton(self.groupBox_2)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.gridLayout_2.addWidget(self.toolButton, 0, 1, 1, 1)
		self.checkBox = QtGui.QCheckBox(self.groupBox_2)
		self.checkBox.setChecked(True)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
		self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
		self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.comboBox = QtGui.QComboBox(self.groupBox_3)
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
		self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 1, 1)
		self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
		self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
		self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		self.pushButton = QtGui.QPushButton(self.groupBox_4)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 20))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuAtualizar = QtGui.QMenu(self.menubar)
		self.menuAtualizar.setObjectName(_fromUtf8("menuAtualizar"))
		self.menuSobre = QtGui.QMenu(self.menubar)
		self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionYoutube_dl = QtGui.QAction(MainWindow)
		self.actionYoutube_dl.setObjectName(_fromUtf8("actionYoutube_dl"))
		self.actionSair = QtGui.QAction(MainWindow)
		self.actionSair.setObjectName(_fromUtf8("actionSair"))
		self.actionSimple_Video_Downloader = QtGui.QAction(MainWindow)
		self.actionSimple_Video_Downloader.setObjectName(_fromUtf8("actionSimple_Video_Downloader"))
		self.menuAtualizar.addAction(self.actionYoutube_dl)
		self.menuAtualizar.addSeparator()
		self.menuAtualizar.addAction(self.actionSair)
		self.menuSobre.addAction(self.actionSimple_Video_Downloader)
		self.menubar.addAction(self.menuAtualizar.menuAction())
		self.menubar.addAction(self.menuSobre.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		app.aboutToQuit.connect(Handler.exitProgram)

		# Conectando os botões da janela principal do programa
		# ====================================================
		self.pushButton.clicked.connect(Handler.gatherUserInformation)
		self.toolButton.clicked.connect(Handler.selectOutputDir)

		# Conectando os menus da janela principal do programa
		# ===================================================
		self.actionYoutube_dl.triggered.connect(Handler.updateYoutube_dl)
		self.actionSair.triggered.connect(Handler.exitProgram)
		self.actionSimple_Video_Downloader.triggered.connect(Handler.displayAbout)

		# Declarações da classe
		# =====================
		Handler.setDefaultDir()
		self.populateSaveOptions()
		Handler.displayInfo()

	# Populando a lista de salvamento
	# ===============================
	def populateSaveOptions(self):
		if Handler.isFFmpegPresent:
			counter = 0
			for option in GlobalVars.PossibleSaveOptions:
				self.comboBox.addItem(_fromUtf8(""))
				self.comboBox.setItemText(counter, _translate("MainWindow", option, None))
				counter += 1
			self.checkBox_2.setEnabled(True)
		else:
			counter = 0
			for option in GlobalVars.PossibleSaveOptions:
				if "(Conversão)" in option:
					continue
				else:
					self.comboBox.addItem(_fromUtf8(""))
					self.comboBox.setItemText(counter, _translate("MainWindow", option, None))
					counter += 1
			self.checkBox_2.setEnabled(False)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "SVD - Simple Video Downloader - v%s" % (GlobalVars.Version), None))
		self.groupBox.setTitle(_translate("MainWindow", "Endereço", None))
		self.label.setText(_translate("MainWindow", "URL do Vídeo ou Playlist:", None))
		self.groupBox_2.setTitle(_translate("MainWindow", "Pasta de destino", None))
		self.toolButton.setText(_translate("MainWindow", "...", None))
		self.checkBox.setText(_translate("MainWindow", "Abrir pasta de destino quando o download for concluído", None))
		self.groupBox_3.setTitle(_translate("MainWindow", "Opções de Salvamento", None))
		self.checkBox_2.setText(_translate("MainWindow", "Manter arquivo original (em conversões)", None))
		self.groupBox_4.setTitle(_translate("MainWindow", "Iniciar download", None))
		self.pushButton.setText(_translate("MainWindow", "Download", None))
		self.menuAtualizar.setTitle(_translate("MainWindow", "Atualizar", None))
		self.menuSobre.setTitle(_translate("MainWindow", "Sobre", None))
		self.actionYoutube_dl.setText(_translate("MainWindow", "youtube-dl", None))
		self.actionSair.setText(_translate("MainWindow", "Sair", None))
		self.actionSimple_Video_Downloader.setText(_translate("MainWindow", "Simple Video Downloader", None))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()

	# Os métodos do programa serão definidos pelo Handler
	# ---------------------------------------------------
	Handler = WindowHandler(ui, MainWindow)
	GlobalVars.Ui = ui
	GlobalVars.MainWindow = MainWindow
	GlobalVars.IconPath = os.path.abspath(GlobalVars.IconName)

	ui.setupUi(MainWindow, Handler)
	MainWindow.show()
	sys.exit(app.exec_())