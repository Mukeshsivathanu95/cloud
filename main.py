import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import Vulkan
from view import View
from update import Update
from query import Query
from compare import Compare
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        myuser=None
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'LOGOUT'
            myuser_key = ndb.Key('Vulkan',user.user_id())
            myuser = myuser_key.get()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'Login here'
        result=Vulkan.query().fetch()
        template_values = {'url' : url,'url_string' : url_string,'user' : user,'welcome':welcome,'myuser':myuser,'result':result}
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type']='text/html'
        if self.request.get('button')=='Create':
            user=users.get_current_user()
            name=self.request.get('users_name')
            myuser_key=ndb.Key('Vulkan',name)
            myuser=myuser_key.get()
            if myuser==None:
                myuser=Vulkan(id=name)
                myuser.put()
                myuser_key=ndb.Key('Vulkan',name)
                myuser=myuser_key.get()
                myuser.name=self.request.get('users_name')
                myuser.manufacturer=self.request.get('users_manufacturer')
                myuser.date=datetime.strptime(self.request.get('users_date'),'%Y-%m-%d')
                if self.request.get('users_geometryShader'):
                    myuser.geometryShader=True
                else:
                    myuser.geometryShader=False
                if self.request.get('users_tesselationShader'):
                    myuser.tesselationShader=True
                else:
                    myuser.tesselationShader=False
                if self.request.get('users_shaderInt16'):
                    myuser.shaderInt16=True
                else:
                    myuser.shaderInt16=False
                if self.request.get('users_sparseBinding'):
                    myuser.sparseBinding=True
                else:
                    myuser.sparseBinding=False
                if self.request.get('users_textureCompressionETC2'):
                    myuser.textureCompressionETC2=True
                else:
                    myuser.textureCompressionETC2=False
                if self.request.get('users_vertexPipelineStoresAndAtomics'):
                    myuser.vertexPipelineStoresAndAtomics=True
                else:
                    myuser.vertexPipelineStoresAndAtomics=False
                myuser.put()
                self.redirect('/')
            else:
                self.redirect('/un')
        if self.request.get('button')=='Query':
            self.redirect('/query')
        if self.request.get('button')=='Result':
            self.redirect('/query')
        if self.request.get('button')=='Compare':
            self.redirect('/compare')

class Username(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.write("Duplication of username is restricted<br/>")
        self.response.out.write('<br />')
        self.response.write('<a href="/"> Back </a><br/>')
        self.response.out.write('</html></body>')


app = webapp2.WSGIApplication([('/', MainPage),('/view/(.*)',View),('/update/(.*)',Update),('/un',Username),('/query',Query),('/compare',Compare)], debug=True)
