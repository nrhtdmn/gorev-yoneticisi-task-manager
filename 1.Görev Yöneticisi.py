import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog, QAction
)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class GorevYoneticisi(QWidget):
    def __init__(self):
        super().__init__()
        
        self.arayuzAyarla()
    
    def arayuzAyarla(self):
        self.setWindowTitle('Görev Yöneticisi')
        
        # Düzenler
        dikey_düzen = QVBoxLayout()
        yatay_düzen = QHBoxLayout()
        
        # Bileşenler
        self.gorev_girisi = QLineEdit(self)
        self.gorev_girisi.setPlaceholderText('Görev girin...')
        
        self.ekle_butonu = QPushButton('Ekle', self)
        self.ekle_butonu.clicked.connect(self.gorev_ekle)
        
        self.sil_butonu = QPushButton('Sil', self)
        self.sil_butonu.clicked.connect(self.gorev_sil)
        
        self.duzenle_butonu = QPushButton('Düzenle', self)
        self.duzenle_butonu.clicked.connect(self.gorev_duzenle)
        
        self.tamamla_butonu = QPushButton('Tamamla', self)
        self.tamamla_butonu.clicked.connect(self.gorev_tamamla)
        
        self.gorev_listesi = QListWidget(self)
        
        # Bileşenleri düzenlere ekle
        yatay_düzen.addWidget(self.gorev_girisi)
        yatay_düzen.addWidget(self.ekle_butonu)
        yatay_düzen.addWidget(self.sil_butonu)
        yatay_düzen.addWidget(self.duzenle_butonu)
        yatay_düzen.addWidget(self.tamamla_butonu)
        
        dikey_düzen.addLayout(yatay_düzen)
        dikey_düzen.addWidget(self.gorev_listesi)
        
        # Ana düzeni ayarla
        self.setLayout(dikey_düzen)
        
        # Klavye kısayollarını ekle
        self.kisayollari_ekle()
        
        # QSS stili uygula
        self.setStyleSheet(self.qss_stili())
        
        self.show()
    
    def kisayollari_ekle(self):
        ekle_kisayolu = QAction(self)
        ekle_kisayolu.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_N))
        ekle_kisayolu.triggered.connect(self.gorev_ekle)
        self.addAction(ekle_kisayolu)
        
        sil_kisayolu = QAction(self)
        sil_kisayolu.setShortcut(QKeySequence(Qt.Key_Delete))
        sil_kisayolu.triggered.connect(self.gorev_sil)
        self.addAction(sil_kisayolu)
        
        duzenle_kisayolu = QAction(self)
        duzenle_kisayolu.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_E))
        duzenle_kisayolu.triggered.connect(self.gorev_duzenle)
        self.addAction(duzenle_kisayolu)
        
        tamamla_kisayolu = QAction(self)
        tamamla_kisayolu.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_D))
        tamamla_kisayolu.triggered.connect(self.gorev_tamamla)
        self.addAction(tamamla_kisayolu)
    
    def gorev_ekle(self):
        gorev = self.gorev_girisi.text()
        if gorev:
            self.gorev_listesi.addItem(gorev)
            self.gorev_girisi.clear()
        else:
            QMessageBox.warning(self, 'Uyarı', 'Görev boş olamaz')
    
    def gorev_sil(self):
        secili_gorev = self.gorev_listesi.currentRow()
        if secili_gorev >= 0:
            self.gorev_listesi.takeItem(secili_gorev)
        else:
            QMessageBox.warning(self, 'Uyarı', 'Silmek için bir görev seçin')
    
    def gorev_duzenle(self):
        secili_gorev = self.gorev_listesi.currentItem()
        if secili_gorev:
            yeni_gorev, ok = QInputDialog.getText(self, 'Görev Düzenle', 'Görevi düzenleyin:', QLineEdit.Normal, secili_gorev.text())
            if ok and yeni_gorev:
                secili_gorev.setText(yeni_gorev)
        else:
            QMessageBox.warning(self, 'Uyarı', 'Düzenlemek için bir görev seçin')
    
    def gorev_tamamla(self):
        secili_gorev = self.gorev_listesi.currentItem()
        if secili_gorev:
            secili_gorev.setText(f'{secili_gorev.text()} - Tamamlandı')
            secili_gorev.setForeground(Qt.gray)
        else:
            QMessageBox.warning(self, 'Uyarı', 'Tamamlamak için bir görev seçin')
    
    def qss_stili(self):
        return """
        QWidget {
            font-family: Arial;
            font-size: 14px;
        }
        QLineEdit {
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        QPushButton {
            padding: 5px 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #0056b3;
        }
        QPushButton:pressed {
            background-color: #004080;
        }
        QListWidget {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        }
        QListWidget::item {
            padding: 5px;
        }
        QListWidget::item:selected {
            background-color: #007BFF;
            color: white;
        }
        """
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gorev_yoneticisi = GorevYoneticisi()
    sys.exit(app.exec_())


"""
Görev ekleme: Ctrl+N
Görev silme: Delete
Görev düzenleme: Ctrl+E
Görev tamamlama: Ctrl+D"""
