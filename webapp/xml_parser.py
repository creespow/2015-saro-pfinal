#!/usr/bin/python

#Parser for Madrid Activities XML
#A partir de Jokes Parser
#Daniel Crespo Beltran

# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from webapp.models import event

import urllib
import string
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def parse_it():

    def normalize_whitespace(text):
        "Remove redundant whitespace from a string"
        return string.join(string.split(text), ' ')

    class CounterHandler(ContentHandler):

        def __init__ (self):
            self.inContent = 0
            self.theContent = ""

            self.titulo = ""
            self.price = ""
            self.long_duration = ""
            self.date = ""
            self.time = ""
            self.url = ""
            self.place = ""
            self.event_type = ""
            

        def startElement (self, name, attrs):
            if name == 'atributo':
                self.title = normalize_whitespace(attrs.get('nombre'))
                self.inContent = 1
                if self.title == "TITULO":
                    self.inContent = 1
                elif self.title == "GRATUITO":
                    self.inContent = 1
                elif self.title == "EVENTO-LARGA-DURACION":               
                    self.inContent = 1
                elif self.title == "FECHA-EVENTO":                
                    self.inContent = 1                
                elif self.title == "HORA-EVENTO":                
                    self.inContent = 1
                elif self.title == "CONTENT-URL":                
                    self.inContent = 1                
                elif self.title == "LOCALIDAD":
                    self.inContent = 1             
                elif self.title == "TIPO":
                    self.inContent = 1    
            
        def endElement (self, name):            
            
            if self.inContent:
                self.theContent = normalize_whitespace(self.theContent)
            if name == 'atributo':
                if self.title == "TITULO":
                    self.titulo = self.theContent                                                        
                elif self.title == "PRECIO":
                    self.price = self.theContent                    
                elif self.title == "EVENTO-LARGA-DURACION":
                    self.long_duration = self.theContent                    
                elif self.title == "FECHA-EVENTO":
                    self.date = self.theContent
                    self.date = str(self.date).split(" ")[0]                    
                elif self.title == "HORA-EVENTO":
                    self.time = self.theContent
                elif self.title == "CONTENT-URL":
                    self.url = self.theContent
                elif self.title == "LOCALIDAD":
                    self.place = self.theContent
                elif self.title == "TIPO":
                    self.event_type = self.theContent

                    c = event(title=self.titulo, price=self.price, long_duration=self.long_duration,
                    date=self.date, time=self.time, url=self.url, place=self.place, event_type=self.event_type)                
                    c.save()            

            if self.inContent:
                self.inContent = 0
                self.theContent = ""            
            
                       
            
        def characters (self, chars):
            if self.inContent:
                self.theContent = self.theContent + chars

                
    # --- Main prog
        
    # Load parser and driver

    MyParser = make_parser()
    MyHandler = CounterHandler()
    MyParser.setContentHandler(MyHandler)

    # Ready, set, go!
    url = "http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.xml"
    xmlFile = urllib.urlopen(url)
    MyParser.parse(xmlFile)
    out = "OK"

    return out





