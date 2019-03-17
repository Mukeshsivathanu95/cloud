import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import Vulkan
from view import View
from update import Update

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Query(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.out.write('<form method="get" action="/query">')
        self.response.out.write('geometryShader:<input type="checkbox" name="users_geometryShader" value="True" />')
        self.response.out.write('<br />')
        self.response.out.write('tesselationShader:<input type="checkbox" name="users_tesselationShader"  value="True"/>')
        self.response.out.write('<br />')
        self.response.out.write('shaderInt16:<input type="checkbox" name="users_shaderInt16"  value="True"/>')
        self.response.out.write('<br />')
        self.response.out.write('sparseBinding:<input type="checkbox" name="users_sparseBinding"  value="True"/>')
        self.response.out.write('<br />')
        self.response.out.write('textureCompressionETC2:<input type="checkbox" name="users_textureCompressionETC2"  value="True"/>')
        self.response.out.write('<br />')
        self.response.out.write('vertexPipelineStoresAndAtomics:<input type="checkbox" name="users_vertexPipelineStoresAndAtomics"  value="True"/><br/>')
        self.response.out.write('<br />')
        self.response.out.write('<br />')
        self.response.out.write('<input type="submit" value="Query" name="button"/>')
        self.response.out.write('</form>')
        q=[]
        if self.request.get('button')=='Query':
            myuser=Vulkan.query()
            for i in myuser:
                l=[]
                l1=[]
                if (self.request.get('users_geometryShader') == "True") and i.geometryShader==True:
                    l.append('True')
                if (self.request.get('users_tesselationShader') == "True") and i.tesselationShader==True:
                    l.append('True')
                if (self.request.get('users_sparseBinding') == "True") and i.sparseBinding==True:
                    l.append('True')
                if self.request.get('users_shaderInt16') == "True" and i.shaderInt16==True:
                    l.append('True')
                if (self.request.get('users_textureCompressionETC2') == "True") and i.textureCompressionETC2==True:
                    l.append('True')
                if self.request.get('users_vertexPipelineStoresAndAtomics') == "True" and i.vertexPipelineStoresAndAtomics==True:
                    l.append('True')
                if (self.request.get('users_geometryShader') == "True"):
                    l1.append('True')
                if (self.request.get('users_tesselationShader') == "True"):
                    l1.append('True')
                if (self.request.get('users_sparseBinding') == "True"):
                    l1.append('True')
                if self.request.get('users_shaderInt16') == "True":
                    l1.append('True')
                if (self.request.get('users_textureCompressionETC2') == "True"):
                    l1.append('True')
                if self.request.get('users_vertexPipelineStoresAndAtomics') == "True":
                    l1.append('True')
                if len(l)==len(l1):
                    q.append(i.name)
            for i in q:
                self.response.write('%s<br/>'%(i))
                self.response.out.write('<br />')
            self.response.write("<a href='/'> Back </a><br/>")
            self.response.out.write('</html></body>')
