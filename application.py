#! /usr/bin/python

from taf import URLDispatcher, MyHTTPServer, MyHandler

c = URLDispatcher()

@c.get('/path/(?P<a>[0-9]+)\.(?P<format>(json|xml))')
def func(vars):
    print 'zahl:'
    print c.query
    return vars

@c.get('/path/(?P<a>[a-z]+)')
def func(vars):
    print 'buchstabe:'
    return vars

@c.post('/set/(?P<a>[0-9]+)')
def func(vars):
    return vars

@c.delete('/delete')
def func(vars):
    return vars

@c.put('/put')
def func(vars):
    return vars
      
server = MyHTTPServer(c, ('localhost', 8080), MyHandler)
print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()