#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib

'''
cortamos los datos recibidos por la url, primero por el tag <h3>Descripción</h3>
y luego por el tag <h3>Enlaces</h3>
esto nos dejará solo la descripcion
'''
def cortaDescripcion(texto):
    source = "<h3>Descripción</h3>";
    source = source.decode('utf-8');
    corte1 = texto.split(source);
    print len(corte1);
    #corte2 = corte1[1].split("<h3>Enlaces</h3>");
    #return corte2[0];

ArbolDOM = xml.dom.minidom.parse("MonumentosZaragoza.xml");
catalogo = ArbolDOM.documentElement;
#Cogemos todos los elementos Features, para tenerlos agrupados por monumento
Features = catalogo.getElementsByTagName("Feature");

'''Recorremos todos los elementos y sacamos sus elementos PropertyValue
    cada uno de los datos del array datos es un elemento distinto
        - datos[0] => nombre
        - datos[1] => url
        - ...
    mostramos todos los nombres.
'''
for feature in Features:
    datos = feature.getElementsByTagName("PropertyValue");
    print datos[0].childNodes[0].data;

nombre = raw_input("Introduce el nombre del monumento: ");

for feature in Features:
    datos = feature.getElementsByTagName("PropertyValue");
    if(datos[0].childNodes[0].data == nombre):
        Contenido = urllib.urlopen(datos[1].childNodes[0].data); #descargamos los datos de la URL.
        output = Contenido.read();
        print cortaDescripcion(output);
        break;