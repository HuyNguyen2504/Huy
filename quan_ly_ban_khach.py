# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quan_ly_ban_khach.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_quan_ly_ban_khach(object):
    def setupUi(self, quan_ly_ban_khach):
        quan_ly_ban_khach.setObjectName("quan_ly_ban_khach")
        quan_ly_ban_khach.resize(1031, 817)
        self.centralwidget = QtWidgets.QWidget(quan_ly_ban_khach)
        self.centralwidget.setObjectName("centralwidget")
        self.thong_ke_gr = QtWidgets.QGroupBox(self.centralwidget)
        self.thong_ke_gr.setGeometry(QtCore.QRect(0, 0, 1031, 811))
        self.thong_ke_gr.setStyleSheet("background-color: rgb(0, 0, 206);")
        self.thong_ke_gr.setTitle("")
        self.thong_ke_gr.setObjectName("thong_ke_gr")
        self.check = QtWidgets.QPushButton(self.thong_ke_gr)
        self.check.setGeometry(QtCore.QRect(30, 360, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check.setFont(font)
        self.check.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.check.setObjectName("check")
        self.exit = QtWidgets.QPushButton(self.thong_ke_gr)
        self.exit.setGeometry(QtCore.QRect(30, 700, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit.setObjectName("exit")
        self.main = QtWidgets.QPushButton(self.thong_ke_gr)
        self.main.setGeometry(QtCore.QRect(30, 120, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main.setFont(font)
        self.main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main.setObjectName("main")
        self.account = QtWidgets.QPushButton(self.thong_ke_gr)
        self.account.setGeometry(QtCore.QRect(30, 580, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.account.setObjectName("account")
        self.back = QtWidgets.QPushButton(self.thong_ke_gr)
        self.back.setGeometry(QtCore.QRect(900, 747, 93, 41))
        self.back.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.back.setObjectName("back")
        self.quan_ly_san_pham = QtWidgets.QPushButton(self.thong_ke_gr)
        self.quan_ly_san_pham.setGeometry(QtCore.QRect(490, 30, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quan_ly_san_pham.setFont(font)
        self.quan_ly_san_pham.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.quan_ly_san_pham.setObjectName("quan_ly_san_pham")
        self.food = QtWidgets.QPushButton(self.thong_ke_gr)
        self.food.setGeometry(QtCore.QRect(30, 470, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.food.setFont(font)
        self.food.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.food.setObjectName("food")
        self.quan_ly_ban = QtWidgets.QPushButton(self.thong_ke_gr)
        self.quan_ly_ban.setGeometry(QtCore.QRect(220, 30, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quan_ly_ban.setFont(font)
        self.quan_ly_ban.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.quan_ly_ban.setObjectName("quan_ly_ban")
        self.menu = QtWidgets.QPushButton(self.thong_ke_gr)
        self.menu.setGeometry(QtCore.QRect(30, 230, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.menu.setObjectName("menu")
        self.groupBox = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox.setGeometry(QtCore.QRect(220, 120, 771, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ma_sp = QtWidgets.QLineEdit(self.groupBox)
        self.ma_sp.setGeometry(QtCore.QRect(100, 40, 113, 31))
        self.ma_sp.setObjectName("ma_sp")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ten_sp = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp.setGeometry(QtCore.QRect(100, 90, 113, 31))
        self.ten_sp.setObjectName("ten_sp")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.don_gia = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia.setGeometry(QtCore.QRect(100, 150, 113, 31))
        self.don_gia.setObjectName("don_gia")
        self.add_ban = QtWidgets.QPushButton(self.groupBox)
        self.add_ban.setGeometry(QtCore.QRect(460, 40, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_ban.setFont(font)
        self.add_ban.setObjectName("add_ban")
        self.fix_ban = QtWidgets.QPushButton(self.groupBox)
        self.fix_ban.setGeometry(QtCore.QRect(600, 40, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fix_ban.setFont(font)
        self.fix_ban.setObjectName("fix_ban")
        self.xoa_ban = QtWidgets.QPushButton(self.groupBox)
        self.xoa_ban.setGeometry(QtCore.QRect(460, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xoa_ban.setFont(font)
        self.xoa_ban.setObjectName("xoa_ban")
        self.lam_moi_ban = QtWidgets.QPushButton(self.groupBox)
        self.lam_moi_ban.setGeometry(QtCore.QRect(600, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lam_moi_ban.setFont(font)
        self.lam_moi_ban.setObjectName("lam_moi_ban")
        self.tim_kiem_ban = QtWidgets.QLineEdit(self.groupBox)
        self.tim_kiem_ban.setGeometry(QtCore.QRect(460, 290, 181, 31))
        self.tim_kiem_ban.setObjectName("tim_kiem_ban")
        self.searching_ban = QtWidgets.QPushButton(self.groupBox)
        self.searching_ban.setGeometry(QtCore.QRect(640, 290, 31, 31))
        self.searching_ban.setStyleSheet("border-image: url(:/picture/398288296_664763935842542_91204699368765392_n.png);")
        self.searching_ban.setText("")
        self.searching_ban.setObjectName("searching_ban")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(460, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(370, 0, 16, 371))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(390, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 530, 771, 201))
        self.groupBox_2.setMinimumSize(QtCore.QSize(771, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(80, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(340, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(600, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 76, 771, 121))
        self.scrollArea.setMinimumSize(QtCore.QSize(771, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 748, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        quan_ly_ban_khach.setCentralWidget(self.centralwidget)

        self.retranslateUi(quan_ly_ban_khach)
        QtCore.QMetaObject.connectSlotsByName(quan_ly_ban_khach)

    def retranslateUi(self, quan_ly_ban_khach):
        _translate = QtCore.QCoreApplication.translate
        quan_ly_ban_khach.setWindowTitle(_translate("quan_ly_ban_khach", "MainWindow"))
        self.check.setText(_translate("quan_ly_ban_khach", "Hóa Đơn"))
        self.exit.setText(_translate("quan_ly_ban_khach", "Đăng Xuất"))
        self.main.setText(_translate("quan_ly_ban_khach", "Trang chủ"))
        self.account.setText(_translate("quan_ly_ban_khach", "Tài Khoản"))
        self.back.setText(_translate("quan_ly_ban_khach", "Trở về"))
        self.quan_ly_san_pham.setText(_translate("quan_ly_ban_khach", "Quản Lý Sản Phẩm"))
        self.food.setText(_translate("quan_ly_ban_khach", "Gọi Món"))
        self.quan_ly_ban.setText(_translate("quan_ly_ban_khach", "Quản Lý Bàn"))
        self.menu.setText(_translate("quan_ly_ban_khach", "MENU"))
        self.groupBox.setTitle(_translate("quan_ly_ban_khach", "Quản lý bàn"))
        self.label.setText(_translate("quan_ly_ban_khach", "mã bàn"))
        self.label_2.setText(_translate("quan_ly_ban_khach", "  tên bàn"))
        self.label_3.setText(_translate("quan_ly_ban_khach", "Trạng Thái"))
        self.add_ban.setText(_translate("quan_ly_ban_khach", "Thêm"))
        self.fix_ban.setText(_translate("quan_ly_ban_khach", "Sửa"))
        self.xoa_ban.setText(_translate("quan_ly_ban_khach", "Xóa"))
        self.lam_moi_ban.setText(_translate("quan_ly_ban_khach", "Làm Mới"))
        self.label_5.setText(_translate("quan_ly_ban_khach", "TÌm Kiếm"))
        self.label_10.setText(_translate("quan_ly_ban_khach", "Chỉnh Sửa Bàn"))
        self.groupBox_2.setTitle(_translate("quan_ly_ban_khach", "Thông Tin"))
        self.label_6.setText(_translate("quan_ly_ban_khach", "Mã Bàn"))
        self.label_7.setText(_translate("quan_ly_ban_khach", "Tên Bàn"))
        self.label_8.setText(_translate("quan_ly_ban_khach", "Trạng Thái"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quan_ly_ban_khach = QtWidgets.QMainWindow()
    ui = Ui_quan_ly_ban_khach()
    ui.setupUi(quan_ly_ban_khach)
    quan_ly_ban_khach.show()
    sys.exit(app.exec_())
