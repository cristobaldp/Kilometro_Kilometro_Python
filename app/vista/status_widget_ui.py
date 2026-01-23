# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_StatusWidget(object):
    def setupUi(self, StatusWidget):
        if not StatusWidget.objectName():
            StatusWidget.setObjectName(u"StatusWidget")
        StatusWidget.resize(360, 220)
        StatusWidget.setMinimumSize(QSize(360, 220))
        self.verticalLayout = QVBoxLayout(StatusWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cardFrame = QFrame(StatusWidget)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardLayout = QVBoxLayout(self.cardFrame)
        self.cardLayout.setSpacing(12)
        self.cardLayout.setObjectName(u"cardLayout")
        self.iconLabel = QLabel(self.cardFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.iconLabel)

        self.titleLabel = QLabel(self.cardFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.titleLabel)

        self.messageLabel = QLabel(self.cardFrame)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageLabel.setWordWrap(True)

        self.cardLayout.addWidget(self.messageLabel)

        self.actionButton = QPushButton(self.cardFrame)
        self.actionButton.setObjectName(u"actionButton")

        self.cardLayout.addWidget(self.actionButton)


        self.verticalLayout.addWidget(self.cardFrame)


        self.retranslateUi(StatusWidget)

        QMetaObject.connectSlotsByName(StatusWidget)
    # setupUi

    def retranslateUi(self, StatusWidget):
        self.cardFrame.setStyleSheet(QCoreApplication.translate("StatusWidget", u"\n"
"QFrame#cardFrame {\n"
" background-color: #E8F5E9;\n"
" border-radius: 14px;\n"
"}\n"
"      ", None))
        self.iconLabel.setStyleSheet(QCoreApplication.translate("StatusWidget", u"\n"
"font-size: 36px;\n"
"color: #2E7D32;\n"
"         ", None))
        self.iconLabel.setText(QCoreApplication.translate("StatusWidget", u"\u2714", None))
        self.titleLabel.setStyleSheet(QCoreApplication.translate("StatusWidget", u"\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #1B5E20;\n"
"         ", None))
        self.titleLabel.setText(QCoreApplication.translate("StatusWidget", u"Operaci\u00f3n completada", None))
        self.messageLabel.setStyleSheet(QCoreApplication.translate("StatusWidget", u"\n"
"color: #2E7D32;\n"
"         ", None))
        self.messageLabel.setText(QCoreApplication.translate("StatusWidget", u"Los datos se han guardado correctamente.", None))
        self.actionButton.setStyleSheet(QCoreApplication.translate("StatusWidget", u"\n"
"QPushButton {\n"
" background-color: #2E7D32;\n"
" color: white;\n"
" border-radius: 8px;\n"
" padding: 6px 18px;\n"
"}\n"
"QPushButton:hover {\n"
" background-color: #1B5E20;\n"
"}\n"
"         ", None))
        self.actionButton.setText(QCoreApplication.translate("StatusWidget", u"Aceptar", None))
        pass
    # retranslateUi

