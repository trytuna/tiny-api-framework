# -*- coding: utf-8 -*-

import BaseHTTPServer
import re
import json
import urlparse

class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self, dispatcher, *args, **kwargs):
        self.urldispatcher = dispatcher
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)

class URLDispatcher(object):
    def __init__(self):
        self.route_list = []
        self.query = str()
        self.request = {}
        
    def get(self, path, method='GET'):
        return self.route(path, method)
    
    def post(self, path, method='POST'):
        return self.route(path, method)
    
    def put(self, path, method='PUT'):
        return self.route(path, method)
        
    def delete(self, path, method='DELETE'):
        return self.route(path, method)
    
    def route(self, path, method='GET'):
        def decorator(function):
            self.route_list.append((path, function, method))
            return function
        return decorator

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = "TinyAPI"
    ''' Implementing content length '''
    #protocol_version = 'HTTP/1.1'
    
    def parseRequest(self, request_path='/', request_method='GET', request_query=''):
        route_list = self.server.urldispatcher.route_list
        available_routes = [(path, func, method) for path, func, method in route_list if method == request_method]
                
        for route, func, method in available_routes:
            m = None
            m = re.match(route, request_path)
            if m is not None:
                arguments = m.groupdict()
                print arguments
                if callable(func):
                    self.server.urldispatcher.request = self
                    return func(arguments)
        return False
            
    def do_GET(self):
        ''' executed if GET is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query
        
        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'Request not found!')
            return
        
        if 'json' in result.get('format'):
            result.pop('format')
            result = json.dumps(result)
            
        self.wfile.write(result)
        
        return
    
    def do_POST(self):
        ''' executed if POST is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query
        
        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'Request not found!')
            return
        
        if 'json' in result.get('format'):
            result = json.dumps(result)
        
        self.wfile.write(result)
        
        return
    def do_PUT(self):
        ''' executed if POST is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query
        
        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'Request not found!')
            return
        
        if 'json' in result.get('format'):
            result = json.dumps(result)
        
        self.wfile.write(result) 
               
        return
        
    def do_DELETE(self):
        ''' executed if POST is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query
        
        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'Request not found!')
            return
        
        if 'json' in result.get('format'):
            result = json.dumps(result)
        
        self.wfile.write(result)
        
        return

