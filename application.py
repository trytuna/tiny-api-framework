#! /usr/bin/python
from taf import URLDispatcher, MyHTTPServer, MyHandler

c = URLDispatcher()

@c.get('/path/(?P<a>[0-9]+)\.(?P<format>(json))')
def func(query, vars):
    print 'zahl:'
    vars['query'] = query
    return vars

@c.get('/path/(?P<a>[a-z]+)')
def func(query, vars):
    print 'buchstabe:'
    return vars

@c.post('/set/(?P<a>[0-9]+)')
def func(query, vars):
    return vars

@c.delete('/delete')
def func(query, vars):
    return vars

@c.put('/put')
def func(query, vars):
    return vars
      
server = MyHTTPServer(c, ('localhost', 8080), MyHandler)
print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()