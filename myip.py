import cherrypy
import json

class MyIp(object):
    @cherrypy.expose
    def index(self):
        myip = {}
        myip['ip_addr'] = cherrypy.request.headers['Remote-Addr']
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(myip)

cherrypy.quickstart(MyIp())
