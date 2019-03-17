import webapp2
import cgi, cgitb
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import Vulkan
from view import View
from update import Update

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        result=Vulkan.query().fetch()
        s=None
        form = cgi.FieldStorage()
        self.response.write('<form method="get" action="/compare">')
        self.response.write('<select name = "dropdown">')
        for i in result:
            self.response.write('<option value = "%s" selected>%s</option>'%(i.name,i.name))
        self.response.write('</select>')
        self.response.write('<select name = "dropdown1">')
        for i in result:
            self.response.write('<option value = "%s" selected>%s</option>'%(i.name,i.name))
        self.response.write('</select>')
        if form.getvalue('dropdown'):
            s=form.getvalue('dropdown')
            t=form.getvalue('dropdown1')
        else:
            s="hello"
        self.response.out.write('<input type="submit" value="Compare" name="button"/>')
        self.response.out.write('</form>')
        self.response.out.write('</form>')
        if self.request.get('button')=='Compare':
            q=Vulkan.query(Vulkan.name==s).fetch()
            w=Vulkan.query(Vulkan.name==t).fetch()
            for i,j in zip(q,w):
                if i==j:
                    self.response.out.write('</html></body>')
                    self.response.out.write('<b>Please choose two diffrent name to compare</b>')
                else:
                    #self.response.write('<table align="left"')
                    #self.response.write('<tr>')
                    self.response.write('<b>GPU1 Name:</b>%s<b>                            GPU2 Name:</b>%s<br/>'%(i.name,j.name))
                    self.response.write('<b>GPU1 Manufacture:</b>%s<b>                     GPU2 Manufacture:</b>%s<br/>'%(i.manufacturer,j.manufacturer))
                    self.response.write('<b>GPU1 Date:</b>%s<b>                            GPU2 Date:</b>%s<br/>'%(i.date,j.date))
                    self.response.write('<b>GPU1 geometryShader:</b>%s<b>                  GPU2 geometryShader:</b>%s<br/>'%(i.geometryShader,j.geometryShader))
                    self.response.write('<b>GPU1 shaderInt16:</b>%s<b>                     GPU2 shaderInt16:</b>%s<br/>'%(i.shaderInt16,j.shaderInt16))
                    self.response.write('<b>GPU1 tesselationShader:</b>%s<b>               GPU2 tesselationShader:</b>%s<br/>'%(i.tesselationShader,j.tesselationShader))
                    self.response.write('<b>GPU1 sparseBinding:</b>%s<b>                   GPU2 sparseBinding:</b>%s<br/>'%(i.sparseBinding,j.sparseBinding))
                    self.response.write('<b>GPU1 vertexPipelineStoresAndAtomics:</b>%s<b>  GPU2 vertexPipelineStoresAndAtomics:</b>%s<br/>'%(i.vertexPipelineStoresAndAtomics,j.vertexPipelineStoresAndAtomics))
                    self.response.write('<b>GPU1 textureCompressionETC2:</b>%s<b>          GPU2 textureCompressionETC2:</b>%s<br/>'%(i.textureCompressionETC2,j.textureCompressionETC2))
                    #self.response.write('</tr>')
        self.response.out.write('</html></body>')
        self.response.out.write('<br />')
        self.response.out.write('<br />')
        self.response.write("<a href='/'> Back </a><br/>")
