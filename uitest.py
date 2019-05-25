import time
import sys
import datetime
import pygame
import inspect
import ctypes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from threading import Thread

# self.label.setStyleSheet("QLabel{background:white;}"
#                          "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
#                          "QLabel:hover{color:rgb(100,100,100,120);}")

class option :
    name = 'xiang'
    yinliang =  0.50
    result_hour = -1
    result_minute = -1
    naozhong_flag = 0
class Qnaozhong_hour(QLineEdit):
    """
    新建QLineEdit类
    """
    def __init__(self, *args):
        super(QLineEdit, self).__init__(*args)
        self.setStyleSheet("QLineEdit{background-color:rgba(0, 0, 0, 0)}") # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self.setFixedWidth(40)
        self.setAlignment(Qt.AlignJustify)


def bofang(hour, name ,yinliang): #报时播放
    hours = str(hour)
    if hour < 10:
        path = name + "/0" + hours + ".mp3"
    elif hour == 24:
        path = name + "/0" + '0' + ".mp3"

    else:
        path = name + "/" + hours + ".mp3"

    print(path)
    pygame.mixer.init()

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(yinliang)

def clock(name, yinliang): #闹钟播放
    pygame.mixer.init()
    path = name + '/clock.mp3'
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(yinliang)



class naozhong(Thread): #闹钟线程
    def __init__(self):
        super().__init__()
    def run(self):
        while 1:
            while option.naozhong_flag:
                if ((option.result_hour) >= 0) & ((option.result_hour) <= 23) & ((option.result_minute) >= 0) & ((option.result_minute) <= 59) :
                    passtime_naozhong = time.localtime(time.time())
                    # print(passtime_naozhong)
                    # # 开始时间
                    # print(passtime_naozhong.tm_hour, passtime_naozhong.tm_min, passtime_naozhong.tm_sec)
                    # # 时 分 秒
                    # print(type(passtime_naozhong))
                    # print(type(result_hour))
                    hour_chaa = option.result_hour - passtime_naozhong.tm_hour -1
                    minute_chaa = option.result_minute - passtime_naozhong.tm_min + 60 -1
                    sec_chaa = 60 - passtime_naozhong.tm_sec
                    print(hour_chaa,minute_chaa,sec_chaa)
                    total_sec = hour_chaa*60*60 + minute_chaa*59 + sec_chaa
                    print(total_sec)
                    if total_sec >= 0:
                        chaa = total_sec

                    else:
                        chaa = 24 * 60 * 60 + total_sec + 60




                    print(chaa)
                    for i in range(0,chaa):
                        time.sleep(1)
                        if(option.naozhong_flag==0):
                            break
                    if(option.naozhong_flag==1):
                        clock(name, yinliang)
                        option.naozhong_flag = 0


class baoshi(Thread):  #报时线程
    def __init__(self):
        super().__init__()
    def run(self):
        flag = 1
        while flag:
            passtime = time.localtime(time.time())
            # print(passtime)
            # 开始时间
            # print(passtime.tm_hour, passtime.tm_min, passtime.tm_sec)
            # 时 分 秒
            cha = (59 - passtime.tm_min) * 60 + 60 - passtime.tm_sec
            print(cha)
            time.sleep(cha)
            bofang(passtime.tm_hour + 1, name, yinliang)

class UI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("界面背景图片设置")
        # 设置对象名称
        self.setObjectName("MainWindow")
        # #todo 1 设置窗口背景图片
        self.setStyleSheet("#MainWindow{border-image:url(photo.png);}")
        # backphotoLabel = QLabel(self)
        #
        # pixmap = QPixmap("photo.png")
        # backphotoLabel.setPixmap(pixmap)
        # backphotoLabel.setScaledContents(True)
        # backphotoLabel.adjustSize()
        self.setWindowFlags(Qt.FramelessWindowHint) #取消边框
        self.setFixedSize(900, 600)#自适应大小
        self.label = QLabel(self)
        self.label.setFixedWidth(370)
        self.label.move(67, 145)
        self.label.setStyleSheet(
            "QLabel{color:rgb(100,100,100,200);}"
            "QLabel:hover{color:rgb(100,100,100,100);}")

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()#自动刷新
        self.initUI()
        self.center()

    def showtime(self): #时间显示
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label.setText(text)
        self.label.setFont(QFont("Roman times", 16, QFont.Bold))




    def initUI(self):
        # self._MaximumButton = QTitleButton(b'\xef\x80\xb1'.decode("utf-8"), self)
        # self._MaximumButton.setStyleSheet('background-color:rgba(0, 0, 0, 0)')
        # self._MaximumButton.clicked.connect(self.MaximumButton)

        self._MinimumButton = QPushButton(b'\xef\x80\xb0'.decode("utf-8"), self)
        self._MinimumButton.setStyleSheet("QPushButton{background-color:rgba(0, 0, 0, 0)}"
                                          "QPushButton:hover{background-color:rgb(0,0,0,20);}")
        self._MinimumButton.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self._MinimumButton.setFixedWidth(40)
        self._MinimumButton.clicked.connect(self.MinimumButton)

        self._CloseButton = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self)
        self._CloseButton.setStyleSheet("QPushButton{background-color:rgba(0, 0, 0, 0)}"
                                        "QPushButton:hover{background-color:rgb(0,0,0,20);}")
        self._CloseButton.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮

        self._CloseButton.clicked.connect(self.CloseButton)
        self._CloseButton.setFixedWidth(40)


        self._CloseButton.move(self.width() - self._CloseButton.width(), 0)
        self._MinimumButton.move(self.width() - (self._CloseButton.width() + 1) * 2 + 1, 0)
        # self._MaximumButton.move(self.width() - (self._CloseButton.width() + 1) * 3 + 1, 0)

        self.hours = QLineEdit(self)
        self.hours.setStyleSheet("QLineEdit{background-color:rgba(0, 0, 0, 0)}")
        self.hours.move(67, 190)
        self.hours.setPlaceholderText("时")
        self.hours.setFixedWidth(40)
        self.hours.setAlignment(Qt.AlignJustify)
        self.hours.setFont(QFont("Roman times", 12, QFont.Bold))
        self.hours.setMaxLength(2)
        hours_set = QIntValidator(self)
        hours_set.setRange(0, 23)
        reg = QRegExp('[0-9]+$')
        hours_sets = QRegExpValidator(self)
        hours_sets.setRegExp(reg)
        self.hours.setValidator(hours_set)



        label_maohao = QLabel(self)
        label_maohao.setText(":")
        label_maohao.move(110, 190)
        label_maohao.setFixedWidth(10)
        label_maohao.setAlignment(Qt.AlignJustify)
        label_maohao.setFont(QFont("Roman times", 16, QFont.Bold))

        self.minutes = QLineEdit(self)
        self.minutes.setStyleSheet("QLineEdit{background-color:rgba(0, 0, 0, 0)}")

        self.minutes.move(130, 190)
        self.minutes.setPlaceholderText("分")
        self.minutes.setFixedWidth(40)
        self.minutes.setAlignment(Qt.AlignJustify)
        self.minutes.setFont(QFont("Roman times", 12, QFont.Bold))
        self.minutes.setMaxLength(2)
        minutes_set = QIntValidator(self)
        minutes_set.setRange(0, 59)
        reg = QRegExp('[0-9]+$')
        minutes_set = QRegExpValidator(self)
        minutes_set.setRegExp(reg)
        self.minutes.setValidator(minutes_set)

        dui = QPushButton(b'\xef\x80\xb4'.decode("utf-8"), self)
        dui.setStyleSheet("QPushButton{background-color:rgba(0, 0, 0, 20)}"
                                        "QPushButton:hover{background-color:rgb(0,0,0,40);}")
        dui.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        dui.move(185,190)
        dui.setFixedWidth(40)
        dui.clicked.connect(self.dui_do)
        # dui.clicked.connect(lambda:self.dui_do(minutes))

        cuo = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self)
        cuo.setStyleSheet("QPushButton{background-color:rgba(0, 0, 0, 20)}"
                          "QPushButton:hover{background-color:rgb(0,0,0,40);}")
        cuo.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        cuo.move(240, 190)
        cuo.setFixedWidth(40)
        cuo.clicked.connect(self.cuo_do)


        self.show()
    def dui_do(self,btn):
        if (self.hours.text() == '')|(self.minutes.text() == ''):
            QMessageBox.warning(self, "输错啦", "请输入0-23和0-59", QMessageBox.Yes,
                                QMessageBox.Yes)
            return
        option.result_hour = int(self.hours.text())
        option.result_minute = int(self.minutes.text())
        if ((option.result_hour) >= 0) & ((option.result_hour) <= 23) & ((option.result_minute) >= 0) & ((option.result_minute) <= 59):
            option.naozhong_flag = 1
            self.hours.setReadOnly(True)
            self.minutes.setReadOnly(True)

        else:
            QMessageBox.warning(self, "输错啦", "请输入0-23和0-59", QMessageBox.Yes,
                                QMessageBox.Yes)


    def cuo_do(self,btn):
        option.naozhong_flag = 0
        self.hours.setText('')
        self.minutes.setText('')
        self.hours.setReadOnly(False)
        self.minutes.setReadOnly(False)

    def center(self): #窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def CloseButton(self):
        """
        关闭窗口
        """
        self.close()

    @pyqtSlot()
    def MinimumButton(self):
        """
        最小化窗口
        """
        self.showMinimized()
    @pyqtSlot()
    def MaximumButton(self):
        """
        最小化窗口
        """
        self.showMaximized()

if __name__ == '__main__':
    yinliang = option.yinliang
    name = option.name
    now_time = datetime.datetime.now()
    print(now_time)

    app = QApplication(sys.argv)
    ex = UI()
    ex.show()

    a = baoshi()
    b = naozhong()
    a.setDaemon(True)
    b.setDaemon(True)
    a.start()
    b.start()

    sys.exit(app.exec_())