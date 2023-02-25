from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QStatusBar, QGraphicsScene, \
    QGraphicsRectItem, QGraphicsTextItem, QGraphicsPixmapItem, QGraphicsView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the menu bar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        # Create the file menu
        file_menu = QMenu('File', self)
        menubar.addMenu(file_menu)

        # Create the help menu
        help_menu = QMenu('Help', self)
        menubar.addMenu(help_menu)

        # Create the status bar
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)

        # Create the graphics view
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setFixedSize(400, 600)
        self.setCentralWidget(self.graphics_view)

        # Create the graphics scene
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_scene.setSceneRect(0, 0, 400, 600)
        self.graphics_view.setScene(self.graphics_scene)

        # Add background image
        background_image = QGraphicsPixmapItem()
        background_image.setPixmap(QPixmap('background.png'))
        self.graphics_scene.addItem(background_image)

        # Add title text
        title_text = QGraphicsTextItem('Orbwalker Menu')
        title_text.setDefaultTextColor(QColor('#FFFFFF'))
        title_text.setFont(QFont('Arial', 20, QFont.Bold))
        title_text.setPos(30, 30)
        self.graphics_scene.addItem(title_text)

        # Add option 1
        option1_text = QGraphicsTextItem('Option 1')
        option1_text.setDefaultTextColor(QColor('#FFFFFF'))
        option1_text.setFont(QFont('Arial', 16))
        option1_text.setPos(30, 100)
        self.graphics_scene.addItem(option1_text)

        # Add option 2
        option2_text = QGraphicsTextItem('Option 2')
        option2_text.setDefaultTextColor(QColor('#FFFFFF'))
        option2_text.setFont(QFont('Arial', 16))
        option2_text.setPos(30, 150)
        self.graphics_scene.addItem(option2_text)

        # Connect the left shift key to show/hide the menu
        self.left_shift_pressed = False
        self.show_menu = False
        self.showNormal()
        self.raise_()
        self.activateWindow()
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Shift and not self.show_menu:
                self.show_menu = True
                self.showNormal()
                self.raise_()
                self.activateWindow()
                return True
            elif event.key() == Qt.Key_Shift and self.show_menu:
                self.show_menu = False
                self.hide()
                return True
        return super(MainWindow, self).eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
