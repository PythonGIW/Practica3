#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib

ArbolDOM = xml.dom.minidom.parse("MonumentosZaragoza.xml");
catalogo = ArbolDOM.documentElement;
Features = catalogo.getElementsByTagName("Feature");

for feature in Features:
    datos = feature.getElementsByTagName("PropertyValue");
    print datos[0].childNodes[0].data;

nombre = raw_input("Introduce el nombre del monumento: ");

def cortaDescripcion(texto):
    source = "<h3>Descripción</h3>";
    source = source.decode('utf-8');
    corte1 = texto.split(source);
    print len(corte1);
    #corte2 = corte1[1].split("<h3>Enlaces</h3>");
    #return corte2[0];

for feature in Features:
    datos = feature.getElementsByTagName("PropertyValue");
    if(datos[0].childNodes[0].data == nombre):
        Contenido = urllib.urlopen(datos[1].childNodes[0].data);
        output = Contenido.read();
        print cortaDescripcion(output);
        break;