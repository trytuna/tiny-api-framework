#! /usr/bin/python
# -*- coding: utf-8 -*-

import BaseHTTPServer
import urlparse
import re
import json

class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self, dispatcher, *args, **kwargs):
        self.urldispatcher = dispatcher
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)

class URLDispatcher(object):
    def __init__(self):
        self.route_list = []
        self.query = str()
        
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
                    self.server.urldispatcher.query = request_query
                    return func(arguments)
        return False
            
    def do_GET(self):
        ''' executed if GET is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query

        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'File not found!')
            return
            
        self.send_response(200)
        
        if result.get('format') == 'xml':
            self.send_header('Content-type','application/xml')
            result.pop('format')
            ''' TODO: implement xml output '''
        else:
            self.send_header('Content-type','application/json')
            if result.has_key('format'):
                result.pop('format')
                json.dumps(result)
        
        self.end_headers()
        
        self.wfile.write(result)
        #self.send_response(200)
        
        return
    
    def do_POST(self):
        ''' executed if POST is requested '''
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path
        request_query = parsed_path.query

        result = self.parseRequest(request_path, self.command, request_query)
        if result is False:
            self.send_error(404, 'File not found!')
            return
            
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
    
        self.wfile.write(result)
        return
    
    def do_PUT(self):
            ''' executed if POST is requested '''
            parsed_path = urlparse.urlparse(self.path)
            request_path = parsed_path.path
            request_query = parsed_path.query
    
            result = self.parseRequest(request_path, self.command, request_query)
            if result is False:
                self.send_error(404, 'File not found!')
                return
                
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
        
            self.wfile.write(result)
            return
        
    def do_DELETE(self):
            ''' executed if POST is requested '''
            parsed_path = urlparse.urlparse(self.path)
            request_path = parsed_path.path
            request_query = parsed_path.query
    
            result = self.parseRequest(request_path, self.command, request_query)
            if result is False:
                self.send_error(404, 'File not found!')
                return
                
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
        
            self.wfile.write(result)
            return