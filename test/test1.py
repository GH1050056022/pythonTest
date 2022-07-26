def hello(environ, start_response):

 start_response('200 OK', [('Content-Type', 'text/html')])

 return [b'<h1>hello python from lucio!</h1>']

from wsgiref.simple_server import make_server

a=900

httpd = make_server('', a, hello)

httpd.serve_forever()