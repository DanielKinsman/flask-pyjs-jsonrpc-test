flask-pyjs-jsonrpc-test
=======================

Tests json rpc calls to a simple flask server from a pyjamas client

To test, run:
pyjsbuild index.py
./web.py

Then open http://localhost:5000 in a browser and hit the 'echo' button.
If it works you'll see a popup dialog saying 'hello', if not you'll
see nothing.

I have found that it works with pyjsbuild 0.7~+pre2
but not with 0.8~+alpha1 or 0.8.1~+alpha1 (pyjsbuild --version).
It's working again In the latest source build of pyjamas
(https://github.com/pyjs/pyjs).

You'll need flask of course (http://flask.pocoo.org/).
