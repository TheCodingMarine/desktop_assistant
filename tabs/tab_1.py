from PySide6.QtWidgets import QWidget, QVBoxLayout
# from PySide6.QtWebEngineWidgets import QWebEngineView
# import folium
# import io

class Tab1(QWidget):
    def __init__(self, parent=None):
        super(Tab1, self).__init__(parent)
        self.parent = parent
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        # coordinates = (37.8199286, -122.4782551)
        # m = folium.Map(tiles='Stamen Terrain', 
        #                location=coordinates, 
        #                zoom_start=13)
        
        
        # data = io.BytesIO()
        # m.save(data, close_file=False)
        
        # self.webview = QWebEngineView()
        # self.webview.setHtml(data.getvalue().decode())
        # self.layout.addWidget(self.webview)