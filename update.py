import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import Vulkan
from view import View
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Update(webapp2.RequestHandler):
    def get(self,id):
        self.response.headers['Content-Type']='text/html'
        my=id
        user=users.get_current_user()
        myuser_key=ndb.Key('Vulkan',my)
        myuser=myuser_key.get()
        template_values={'myuser':myuser,'my':my}
        template=JINJA_ENVIRONMENT.get_template('update.html')
        self.response.write(template.render(template_values))
    def post(self,id):
        self.response.headers['Content-Type']='text/html'
        my=id
        if self.request.get('button')=='Update':
            user=users.get_current_user()
            myuser_key=ndb.Key('Vulkan',my)
            myuser=myuser_key.get()
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
            self.redirect('/view/%s'%(my))
        elif self.request.get('button')=='Cancel':
            self.redirect('/')
