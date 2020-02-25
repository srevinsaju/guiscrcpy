'''
Copyright 2014 Lloyd Konneker
Release under the GPLv3
'''

from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import QObject, QByteArray, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


class DownLoader(QObject):
    '''
    Asynchronous download from network, which is expected to be unreliable and possibly slow.

    A thin wrapper around QNetworkAccessManager()

    Qt docs: 'One QNetworkAccessManager should be enough for the whole Qt application.'
    Similarly, one DownLoader might be enought for the whole app.
    It is untested what happens when you create more than one.

    Usage:

      foo = Downloader(url)
      foo.downloaded.connect(clientLoader)

      foo.doDownload(QUrl('http:/...'))
      # execution continues, clientLoader slot will receive signal

      def clientLoader():
        bar = foo.downloadedData()
        # bar is only a reference, consume it before calling doDownload() again

    '''

    downloaded = Signal()

    def __init__(self):  # parent not used
        super(DownLoader, self).__init__()  # !!! init QObject
        # private
        self._webController = QNetworkAccessManager()
        self._downloadedData = None

        # connect asynchronous result, when a request finishes
        self._webController.finished.connect(self._fileDownloaded)

    # private slot, no need to declare as slot
    def _fileDownloaded(self, reply):
        '''
        Handle signal 'finished'.  A network request has finished.
        '''
        self._downloadedData = reply.readAll()
        # prior _downloadedData is now garbage collectable
        assert isinstance(self._downloadedData, QByteArray)
        reply.deleteLater()  # schedule for delete from main event loop
        # print("emitted")
        self.downloaded.emit()

    '''
    Public API
    '''

    def doDownload(self, url):
        assert isinstance(url, QUrl)

        request = QNetworkRequest(url)
        self._webController.get(request)
        # asynchronous, does not wait, execution continues

    def downloadedData(self):
        '''
        QByteArray that was downloaded.

        Call this only after receiving signal 'downloaded'.
        Copy result before calling doDownload() again.
        '''
        return self._downloadedData
