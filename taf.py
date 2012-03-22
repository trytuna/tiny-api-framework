#! /usr/bin/python
# -*- coding: utf-8 -*-

import BaseHTTPServer
import urlparse
import re

class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self, dispatcher, *args, **kwargs):
        self.urldispatcher = dispatcher
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)

class URLDispatcher(object):
    def __init__(self):
        self.route_list = []
        
    def get(self, path, method='GET'):
        return self.route(path, method)
    
    def post(self, path, method='POST'):
        return self.route(path, method)
    
    def put(self, path, method='PUT'):
        return self.route(path, method)
        
    def delete(self, path, method='DELETE'):
        return self.route(path, method)
    
    def head(self, path, method='HEAD'):
        return self.route(path, method)
    
    def route(self, path, method='GET'):
        def decorator(function):
            self.route_list.append((path, function, method))
            return function
        return decorator

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def parseRequest(self, request_path='/', request_method='GET', request_query=''):
        # DEBUG
        print 'Requested path: \t'+request_path
        print 'Request method: \t'+request_method
        print 'Route list: \t\t'+str(self.server.urldispatcher.route_list)
        # BEBUG END
        route_list = self.server.urldispatcher.route_list
        available_routes = [(a,b,c) for a,b,c in route_list if c == request_method]
        
        print 'Filtered routes: \t'+str(available_routes)
        
        for route, func, method in available_routes:
            m = None
            m = re.match(route, request_path)
            if m is not None:
                arguments = m.groupdict()
                if callable(func):
                    return func(request_query, arguments)
        return False
            
    def do_GET(self):
        ''' executed if GET is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query

        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'HAU AB!')
            return
            
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
    
        self.wfile.write(result)
        return
    
    def do_POST(self):
        ''' executed if POST is requested '''
        self.send_response(200)
        return