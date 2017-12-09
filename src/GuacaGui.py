#!/usr/bin/python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from UrlBar import UrlBar

class Gui():
    def __init__(self, config):
        app = QApplication(sys.argv)

        grid = QGridLayout()
        webView = QWebEngineView()
        bar = UrlBar(webView, config)
        u = QUrl()

        grid.addWidget(bar, 1, 0)
        grid.addWidget(webView, 2, 0)
        webView.load(QUrl(config["base_url"]))

        frame = QWidget()
        frame.setLayout(grid)
        frame.show()
        sys.exit(app.exec_())
