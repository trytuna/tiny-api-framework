#! /usr/bin/python

from taf import URLDispatcher, MyHTTPServer, MyHandler
import urlparse
import urllib

c = URLDispatcher()
get = c.get
post = c.post
delete = c.delete
put = c.put
request = c.request
print request

@get('/path/(?P<a>[0-9]+)\.(?P<format>(json|xml))')
def func(vars):
    parsed_path = urlparse.urlparse(c.request.path)
    request_path = parsed_path.path
    request_query = parsed_path.query
    content_type = 'application/xml' if 'xml' in vars.get('format') else 'application/json'
    ip, port = c.request.server.server_address
    port = '' if port is '80' else ':'+str(port)
    hostname = urllib.quote_plus('http://'+ip+port)
    
    #print dir(c.request.headers)
    print c.request.headers.items()
    #print c.request.headers.getaddr()
        
    c.request.send_response(200)
    c.request.send_header('Authentication', 'OAuth')
    c.request.send_header('Content-Type', content_type)
    c.request.end_headers()
    
    header_string = 'OAuth oauth_consumer_key="xvz1evFS4wEEPTGEFPHBog",oauth_nonce="kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg",oauth_signature="tnnArxj06cWHq44gCs1OSKk%2FjLY%3D",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1318622958",oauth_token="370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb",oauth_version="1.0"'
    
    header_string = header_string.split(' ')
    header_string = header_string[1].split(',')
    header_string.sort()
    header_string = ''.join(str(i) for i in header_string)
    header_string = header_string.replace('"','')
    header_string = urllib.quote_plus(header_string)
    
    parameter_string = str()
    
    base_string = str()
    # Contert the HTTP Method to uppercase and add the '$' character
    base_string += c.request.command.upper() + '&'
    base_string += hostname + request_path + '&'
    base_string += header_string
    
    print 'Base String ' + base_string
    
    #print dir(c.request)
    #print request_path
    #print request_query
    #print c.request.command
    #print ip
    #print port
    #print 'Request' + c.request.request_version
    #print 'Response' + c.request.protocol_version

    return vars

@get('/path/(?P<a>[a-z]+)')
def func(vars):
    print 'buchstabe:'
    return vars

@post('/set/(?P<a>[0-9]+)\.(?P<format>(json|xml))')
def func(vars):
    
    return vars

@delete('/delete')
def func(vars):
    return vars

@put('/put')
def func(vars):
    return vars
      
server = MyHTTPServer(c, ('localhost', 8080), MyHandler)
print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()