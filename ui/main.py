# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(265, 160)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_select_video = QPushButton(Form)
        self.bt_select_video.setObjectName(u"bt_select_video")

        self.verticalLayout.addWidget(self.bt_select_video)

        self.lb_video_path = QLabel(Form)
        self.lb_video_path.setObjectName(u"lb_video_path")
        self.lb_video_path.setLayoutDirection(Qt.LeftToRight)
        self.lb_video_path.setWordWrap(False)
        self.lb_video_path.setMargin(0)
        self.lb_video_path.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.lb_video_path)

        self.ly_start = QHBoxLayout()
        self.ly_start.setObjectName(u"ly_start")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))

        self.ly_start.addWidget(self.label)

        self.sp_start_h = QSpinBox(Form)
        self.sp_start_h.setObjectName(u"sp_start_h")
        self.sp_start_h.setMaximum(999)

        self.ly_start.addWidget(self.sp_start_h)

        self.sp_start_m = QSpinBox(Form)
        self.sp_start_m.setObjectName(u"sp_start_m")
        self.sp_start_m.setMaximum(60)

        self.ly_start.addWidget(self.sp_start_m)

        self.sp_start_s = QSpinBox(Form)
        self.sp_start_s.setObjectName(u"sp_start_s")
        self.sp_start_s.setMaximum(60)

        self.ly_start.addWidget(self.sp_start_s)


        self.verticalLayout.addLayout(self.ly_start)

        self.ly_end = QHBoxLayout()
        self.ly_end.setObjectName(u"ly_end")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(30, 30))

        self.ly_end.addWidget(self.label_2)

        self.sp_end_h = QSpinBox(Form)
        self.sp_end_h.setObjectName(u"sp_end_h")
        self.sp_end_h.setMaximum(999)

        self.ly_end.addWidget(self.sp_end_h)

        self.sp_end_m = QSpinBox(Form)
        self.sp_end_m.setObjectName(u"sp_end_m")
        self.sp_end_m.setMaximum(60)

        self.ly_end.addWidget(self.sp_end_m)

        self.sp_end_s = QSpinBox(Form)
        self.sp_end_s.setObjectName(u"sp_end_s")
        self.sp_end_s.setMaximum(60)

        self.ly_end.addWidget(self.sp_end_s)


        self.verticalLayout.addLayout(self.ly_end)

        self.bt_cut_video = QPushButton(Form)
        self.bt_cut_video.setObjectName(u"bt_cut_video")

        self.verticalLayout.addWidget(self.bt_cut_video)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_select_video.setText(QCoreApplication.translate("Form", u"Select Video", None))
        self.lb_video_path.setText(QCoreApplication.translate("Form", u"VIDEO PATH", None))
        self.label.setText(QCoreApplication.translate("Form", u"Start", None))
        self.sp_start_h.setSpecialValueText("")
        self.sp_start_h.setSuffix(QCoreApplication.translate("Form", u"H", None))
        self.sp_start_m.setSuffix(QCoreApplication.translate("Form", u"M", None))
        self.sp_start_s.setSuffix(QCoreApplication.translate("Form", u"S", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"End", None))
        self.sp_end_h.setSpecialValueText("")
        self.sp_end_h.setSuffix(QCoreApplication.translate("Form", u"H", None))
        self.sp_end_m.setSuffix(QCoreApplication.translate("Form", u"M", None))
        self.sp_end_s.setSuffix(QCoreApplication.translate("Form", u"S", None))
        self.bt_cut_video.setText(QCoreApplication.translate("Form", u"Cut Video", None))
    # retranslateUi

