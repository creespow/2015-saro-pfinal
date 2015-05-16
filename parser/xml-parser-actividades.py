#!/usr/bin/python

#Parser for Madrid Activities XML
#Daniel Crespo Beltran

# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the jokes in a JokesXML file

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib
import string

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return string.join(string.split(text), ' ')

class CounterHandler(ContentHandler):

    def __init__ (self):
        self.inContent = 0
        self.theContent = ""

    def startElement (self, name, attrs):
        if name == 'atributo':
            self.title = normalize_whitespace(attrs.get('nombre'))
            self.inContent = 1
            print self.title + ' '
        
    def endElement (self, name):
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)

        if name == 'atributo':       
            print self.theContent 
            print ""            
                
        if self.inContent:
            self.inContent = 0
            self.theContent = ""
        
    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars          

            
# --- Main prog
    
# Load parser and driver

JokeParser = make_parser()
JokeHandler = CounterHandler()
JokeParser.setContentHandler(JokeHandler)

# Ready, set, go!
url = "http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.xml"

xmlFile = urllib.urlopen(url)
JokeParser.parse(xmlFile)


