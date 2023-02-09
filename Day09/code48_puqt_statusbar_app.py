import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
       
    def initUI(self):
        # 메뉴바
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q') # 단축키 지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')
        
        actEdit = QAction(QIcon('./Day09/edit.png'),'Edit', self)
        actEdit.setShortcut('')
        actEdit.setStatusTip('수정')

        actPrint = QAction(QIcon('./Day09/print.png'),'Print', self)
        actPrint.setShortcut('Ctrl+P')
        actPrint.setStatusTip('출력')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar') # 툴바 타이틀은 없어도 됨
        toolbar.addAction(actExit)
        toolbar.addAction(actSave)
        toolbar.addAction(actPrint)
        toolbar.addAction(actEdit)

        # 상태바
        now = QDate.currentDate() # 현재일자
        time = QTime.currentTime() # 현재시각
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString())
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면설정
        self.setWindowTitle('Bar Window')
        self.move(50,50)
        self.resize(400,200)
        self.setCenter() # move로 셋팅해도 정중앙에
        self.show() # 핵심!
   
    # 화면 중심으로 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())