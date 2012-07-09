#!/usr/bin/env python

import pyjd
from pyjamas.JSONService import JSONProxy
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas import Window

class IndexHtml(object):
    def onModuleLoad(self):
        self.remote = DataService()
        
        self.button = Button("echo", self.echo)
        RootPanel().add(self.button)
        
    def echo(self):
        self.remote.sendRequest('echo', {'message': 'hello'}, self)
    
    def onRemoteResponse(self, response, request_info):
        Window.alert("got a response:" + response)
        
    def onRemoteError(self, code, errobj, request_info):
        Window.alert("got an error")

     
class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, 'service/')
    
if __name__ == '__main__':
    pyjd.setup("index.html")
    app = IndexHtml()
    app.onModuleLoad()
    pyjd.run()