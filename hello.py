def wsgi_app(environ, start_response):
    body = environ['QUERY_STRING']
    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    start_response (status,headers)
    return ['\r\n'.join(body.split('&'))]
