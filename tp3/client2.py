from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")  # titre d'interface
        self.setFixedSize(400, 300)  # change la taille de la fenetre
        self.label1 = QLabel("IP a geolocalisé:", self)
        # ca fait changer le champ de texte de place (x-horizontale,y-vertical)
        self.text = QLineEdit(self)
        self.text.move(10, 30)

        self.label3 = QLabel("Votre ip:", self)
        self.label3.move(0, 55)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 80)

        self.label4 = QLabel("Api key:", self)
        self.label4.move(0, 110)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 135)

        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 170)  # ca fait changer le text anwser
        self.button = QPushButton("Send", self)  # .button donne le type
        self.button.move(10, 200)  # ca fait changer le bouton de place

        # on dit que si on clic sur button ca appel la fonction on_click
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def create_url(res, self):
        openstreet_url = "https://www.openstreetmap.org/?mlat=%s&mlon=%smap=12" % (
            res["lat"], res["long"])
        return openstreet_url

    def on_click(self):
        hostname = self.text2.text()  # 2001:978:2:2c::172:b
        ip = self.text.text()  # 127.0.0.1:8000
        api = self.text3.text()  # Rkj5oXutwUuRlVBNSiLjdczdjVglGhlC

        if hostname == "" or ip == "" or api == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname, ip, api)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()
                Urls = main.create_url(res)
                QDesktopServices.openUrl(QUrl(Urls))

    def __query(self, hostname, ip, api):
        url = "http://%s/ip/%s/api=%s" % (hostname, ip, api)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
