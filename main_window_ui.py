# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(253, 255, 217);\n"
"background-color: rgb(213, 255, 206);\n"
"background-color: rgb(255, 255, 120);\n"
"background-color: rgb(250, 255, 192);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.orig_img_label = QLabel(self.page)
        self.orig_img_label.setObjectName(u"orig_img_label")
        self.orig_img_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout.addWidget(self.orig_img_label)

        self.det_img_label = QLabel(self.page)
        self.det_img_label.setObjectName(u"det_img_label")
        self.det_img_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout.addWidget(self.det_img_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(202, 203, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.orig_cap_label = QLabel(self.page_2)
        self.orig_cap_label.setObjectName(u"orig_cap_label")
        self.orig_cap_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout_2.addWidget(self.orig_cap_label)

        self.det_cap_label = QLabel(self.page_2)
        self.det_cap_label.setObjectName(u"det_cap_label")
        self.det_cap_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout_2.addWidget(self.det_cap_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.pushButton_cap = QPushButton(self.page_2)
        self.pushButton_cap.setObjectName(u"pushButton_cap")
        self.pushButton_cap.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.pushButton_cap)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.orig_video_label = QLabel(self.page_3)
        self.orig_video_label.setObjectName(u"orig_video_label")
        self.orig_video_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout_3.addWidget(self.orig_video_label)

        self.det_video_label = QLabel(self.page_3)
        self.det_video_label.setObjectName(u"det_video_label")
        self.det_video_label.setStyleSheet(u"background-color: rgb(171, 244, 255);")

        self.horizontalLayout_3.addWidget(self.det_video_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_video = QPushButton(self.page_3)
        self.pushButton_video.setObjectName(u"pushButton_video")
        self.pushButton_video.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_video)

        self.pushButton_video_pause = QPushButton(self.page_3)
        self.pushButton_video_pause.setObjectName(u"pushButton_video_pause")
        self.pushButton_video_pause.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_video_pause)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalSlider_video = QSlider(self.page_3)
        self.horizontalSlider_video.setObjectName(u"horizontalSlider_video")
        self.horizontalSlider_video.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_video)

        self.label_video_progress = QLabel(self.page_3)
        self.label_video_progress.setObjectName(u"label_video_progress")

        self.verticalLayout_2.addWidget(self.label_video_progress)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.comboBox_page = QComboBox(self.centralwidget)
        self.comboBox_page.setObjectName(u"comboBox_page")

        self.verticalLayout.addWidget(self.comboBox_page)

        self.comboBox_model = QComboBox(self.centralwidget)
        self.comboBox_model.setObjectName(u"comboBox_model")

        self.verticalLayout.addWidget(self.comboBox_model)

        self.horizontalSlider_model = QSlider(self.centralwidget)
        self.horizontalSlider_model.setObjectName(u"horizontalSlider_model")
        self.horizontalSlider_model.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_model)

        self.label_conf = QLabel(self.centralwidget)
        self.label_conf.setObjectName(u"label_conf")

        self.verticalLayout.addWidget(self.label_conf)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 916, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.orig_img_label.setText("")
        self.det_img_label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u68c0\u6d4b", None))
        self.orig_cap_label.setText("")
        self.det_cap_label.setText("")
        self.pushButton_cap.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u6444\u50cf\u5934", None))
        self.orig_video_label.setText("")
        self.det_video_label.setText("")
        self.pushButton_video.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.pushButton_video_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u64ad\u653e", None))
        self.label_video_progress.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8fdb\u5ea6\uff1a0 / 0", None))
        self.label_conf.setText("")
    # retranslateUi

