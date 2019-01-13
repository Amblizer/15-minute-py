from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

class MainWindow(QMainWindow):
    """ Main Window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Config
        isTab       = True
        isNaviBar   = True
        isUrlBar    = True
        isStatusBar = True
        hideWindowsTitleBar = True

        homepage = 'https://mzhao.page'
        self.setWindowTitle('Pyggy')
        self.setWindowIcon(QIcon('src\\pyggy.png'))

    # System title bar
        if hideWindowsTitleBar:
            self.setWindowFlags(Qt.FramelessWindowHint)

    # Tab
        self.browser = self.browser_set(homepage)

        if isTab:
            self.tab = QTabWidget()
            self.tab.addTab(self.browser, 'Home')

            self.setCentralWidget(self.tab)
            
        else:
            self.setCentralWidget(self.browser)

    # Navi-bar
        if isNaviBar:
            NaviBar = QToolBar('Navigation')
            NaviBar.setIconSize(QSize(64, 64))
            self.addToolBar(NaviBar)

            NaviBar.addAction(self.NaviBotton(self.browser, 'back'))  # add botton to navibar
            NaviBar.addAction(self.NaviBotton(self.browser, 'next'))
            NaviBar.addAction(self.NaviBotton(self.browser, 'stop'))
            NaviBar.addAction(self.NaviBotton(self.browser, 'reload'))

    # UrlBar
        if isUrlBar:
            self.UrlBar = QLineEdit()
            self.UrlBar.returnPressed.connect(self.NaviUrl)

            NaviBar.addSeparator()              # add seperator
            NaviBar.addWidget(self.UrlBar)      # add url bar

            self.browser.urlChanged.connect(self.UrlBarRenew)   # show current url in urlbar

    # status bar
        if isStatusBar:
            self.status = QStatusBar()
            self.setStatusBar(self.status)

        self.show()
    
    def NaviBotton(self, slot, name):
        """ navigation bottons
        
        Arguments:
            slot -- NaviBar object
            name -- name of the botton
        """
        if name == 'back':
            btn_back = QAction(QIcon('src\\' + name + '.png'), 'Back', self)
            btn_back.setStatusTip("Back to previous page")
            btn_back.triggered.connect(slot.back)

        if name == 'next':
            btn_back = QAction(QIcon('src\\' + name + '.png'), 'Next', self)
            btn_back.setStatusTip("Forward to next page")
            btn_back.triggered.connect(slot.forward)

        if name == 'stop':
            btn_back = QAction(QIcon('src\\' + name + '.png'), 'Stop', self)
            btn_back.setStatusTip("Stop loading")
            btn_back.triggered.connect(slot.stop)

        if name == 'reload':
            btn_back = QAction(QIcon('src\\' + name + '.png'), 'Reload', self)
            btn_back.setStatusTip("Reload page")
            btn_back.triggered.connect(slot.reload)
        
        return btn_back

    def UrlBarRenew(self, slot):
        """ refresh url according to page
        
        Arguments:
            slot -- self.browser object
        """
        self.UrlBar.setText(slot.toString())
        self.UrlBar.setCursorPosition(0)

    def NaviUrl(self):
        """
        Navigate to url in the url bar
        """
        q = QUrl(self.UrlBar.text())

        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def browser_set(self, url):
        """ create new tab
        
        Arguments:
            url     -- 
            label   -- 
        """
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))

        return browser


app = QApplication(sys.argv)    # app
window = MainWindow()           # main window
app.exec_()                     # run and monitor