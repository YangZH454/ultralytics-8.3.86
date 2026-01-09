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
        self.stackedWidget.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5f7fa, stop:1 #c3cfe2);\n"
"border-radius: 8px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.orig_img_label = QLabel(self.page)
        self.orig_img_label.setObjectName(u"orig_img_label")
        self.orig_img_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout.addWidget(self.orig_img_label)

        self.det_img_label = QLabel(self.page)
        self.det_img_label.setObjectName(u"det_img_label")
        self.det_img_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout.addWidget(self.det_img_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5568d9, stop:1 #6a3a92);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5f7fa, stop:1 #c3cfe2);\n"
"border-radius: 8px;")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.orig_cap_label = QLabel(self.page_2)
        self.orig_cap_label.setObjectName(u"orig_cap_label")
        self.orig_cap_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout_2.addWidget(self.orig_cap_label)

        self.det_cap_label = QLabel(self.page_2)
        self.det_cap_label.setObjectName(u"det_cap_label")
        self.det_cap_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"color: rgb(255, 0, 0);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout_2.addWidget(self.det_cap_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.pushButton_cap = QPushButton(self.page_2)
        self.pushButton_cap.setObjectName(u"pushButton_cap")
        self.pushButton_cap.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5568d9, stop:1 #6a3a92);\n"
"}")

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
        self.orig_video_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout_3.addWidget(self.orig_video_label)

        self.det_video_label = QLabel(self.page_3)
        self.det_video_label.setObjectName(u"det_video_label")
        self.det_video_label.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e0e0e0, stop:1 #bdbdbd);\n"
"border: 2px solid #757575;\n"
"border-radius: 6px;\n"
"padding: 2px;")

        self.horizontalLayout_3.addWidget(self.det_video_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_video = QPushButton(self.page_3)
        self.pushButton_video.setObjectName(u"pushButton_video")
        self.pushButton_video.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5568d9, stop:1 #6a3a92);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_video)

        self.pushButton_video_pause = QPushButton(self.page_3)
        self.pushButton_video_pause.setObjectName(u"pushButton_video_pause")
        self.pushButton_video_pause.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5568d9, stop:1 #6a3a92);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_video_pause)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalSlider_video = QSlider(self.page_3)
        self.horizontalSlider_video.setObjectName(u"horizontalSlider_video")
        self.horizontalSlider_video.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #bdbdbd;\n"
"    height: 8px;\n"
"    background: #e0e0e0;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border: 2px solid white;\n"
"    width: 18px;\n"
"    margin: -5px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}")
        self.horizontalSlider_video.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_video)

        self.label_video_progress = QLabel(self.page_3)
        self.label_video_progress.setObjectName(u"label_video_progress")
        self.label_video_progress.setStyleSheet(u"color: #424242;\n"
"font-size: 13px;\n"
"font-weight: 500;\n"
"padding: 4px;")

        self.verticalLayout_2.addWidget(self.label_video_progress)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.comboBox_page = QComboBox(self.centralwidget)
        self.comboBox_page.setObjectName(u"comboBox_page")
        self.comboBox_page.setStyleSheet(u"QComboBox {\n"
"    background: white;\n"
"    border: 2px solid #bdbdbd;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"}\n"
"QComboBox:hover {\n"
"    border-color: #667eea;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #667eea;\n"
"    margin-right: 5px;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_page)

        self.comboBox_model = QComboBox(self.centralwidget)
        self.comboBox_model.setObjectName(u"comboBox_model")
        self.comboBox_model.setStyleSheet(u"QComboBox {\n"
"    background: white;\n"
"    border: 2px solid #bdbdbd;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"}\n"
"QComboBox:hover {\n"
"    border-color: #667eea;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #667eea;\n"
"    margin-right: 5px;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_model)

        self.horizontalSlider_model = QSlider(self.centralwidget)
        self.horizontalSlider_model.setObjectName(u"horizontalSlider_model")
        self.horizontalSlider_model.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #bdbdbd;\n"
"    height: 8px;\n"
"    background: #e0e0e0;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border: 2px solid white;\n"
"    width: 18px;\n"
"    margin: -5px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c8ff0, stop:1 #8a5fb8);\n"
"}")
        self.horizontalSlider_model.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_model)

        self.label_conf = QLabel(self.centralwidget)
        self.label_conf.setObjectName(u"label_conf")
        self.label_conf.setStyleSheet(u"color: #424242;\n"
"font-size: 13px;\n"
"font-weight: 500;\n"
"padding: 4px;")

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YOLO\u76ee\u6807\u68c0\u6d4b\u7cfb\u7edf", None))
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

