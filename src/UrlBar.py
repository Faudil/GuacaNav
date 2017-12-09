from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QUrl


class UrlBar(QLineEdit):
    def __init__(self, parent, config):
        super(UrlBar, self).__init__()
        self._parent = parent
        self._url = config["base_url"]
        self._searchUrl = config["search_url"]
        self.setText(self.getUrl())


        # Now we listen when the user press enter
        self.returnPressed.connect(self.listenPressed)
        # And we listen when the webView changes adress
        parent.urlChanged.connect(self._change)

    def getParent(self):
        return self._parent

    def getUrl(self):
        return self._url

    def getSearchUrl(self):
        return self._searchUrl

    def listenPressed(self):
        self._url = self.text()
        if "://" in self.getUrl():
            self.getParent().load(QUrl(self.getUrl()))
        else :
            self.getParent().load(QUrl(self.getSearchUrl() + self.getUrl()))

    def _change(self):
        self._url = self.getParent().url().toString()
        self.setText(self.getUrl())
