#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: https://balau82.wordpress.com/about-me/
# Articulo original: https://balau82.wordpress.com/2010/06/28/simplest-rpg-game-in-python/

# Traduccion y Analisis del codigo
# https://www.pythondiario.com/2016/10/simple-juego-rpg-en-python.html
# Diego Caraballo
 
from random import randint
 
class Personaje:
  def __init__(self):
    self.nombre = ""
    self.salud = 1
    self.salud_max = 1
    
  def hacer_danio(self, Enemigo):
    danio = min(max(randint(0, self.salud) - randint(0, Enemigo.salud), 0), Enemigo.salud)
    Enemigo.salud = Enemigo.salud - danio
    if danio == 0: print "%s evade el ataque de %s" % (Enemigo.nombre, self.nombre)
    else: 
  print "%s acierta un golpe %s!" % (self.nombre, Enemigo.nombre)
    return Enemigo.salud <= 0
 
class Enemigo(Personaje):
  def __init__(self, Jugador):
    Personaje.__init__(self)
    self.nombre = 'un Orco'
    self.salud = randint(1, Jugador.salud)
 
class Jugador(Personaje):
  def __init__(self):
    Personaje.__init__(self)
    self.estado = 'normal'
    self.salud = 10
    self.salud_max = 10
    
  def salir(self):
    print "%s no puede encontrar el camino de vuelta a casa y muere de inanicion.nR.I.P." % self.nombre
    self.salud = 0
    
  def ayuda(self): 
   print Commands.keys()
  
  def estado(self): 
   print "%s - salud: %d/%d" % (self.nombre, self.salud, self.salud_max)
  
  def cansancio(self):
    print "%s siente cansancio." % self.nombre
    self.salud = max(1, self.salud - 1)
    
  def descanso(self):
    if self.estado != 'normal': 
  print "%s no puede descansar ahora!" % self.nombre; self.Enemigo_ataques()
    else:
      print "%s descansa." % self.nombre
      if randint(0, 1):
        self.Enemigo = Enemigo(self)
        print "%s se desperto de golpe por %s!" % (self.nombre, self.Enemigo.nombre)
        self.estado = 'lucha'
        self.Enemigo_ataques()
      else:
        if self.salud < self.salud_max:
          self.salud = self.salud + 1
        else: 
   print "%s a dormido demasiado." % self.nombre; self.salud = self.salud - 1
        
  def explorar(self):
    if self.estado != 'normal':
      print "%s esta demasiado ocupado en este momento!" % self.nombre
      self.Enemigo_ataques()
    else:
      print "%s explora un pasaje sinuoso." % self.nombre
      if randint(0, 1):
        self.Enemigo = Enemigo(self)
        print "%s encuentra %s!" % (self.nombre, self.Enemigo.nombre)
        self.estado = 'lucha'
      else:
        if randint(0, 1): self.cansancio()
        
  def huir(self):
    if self.estado != 'lucha': 
  print "%s corre en circulos durante un tiempo." % self.nombre 
  self.cansancio()
    else:
      if randint(1, self.salud + 5) > randint(1, self.Enemigo.salud):
        print "%s huye de %s." % (self.nombre, self.Enemigo.nombre)
        self.Enemigo = None
        self.estado = 'normal'
      else: 
    print "%s no puede escapar de %s!" % (self.nombre, self.Enemigo.nombre) 
    self.Enemigo_ataques()
      
  def atacar(self):
    if self.estado != 'lucha': 
  print "%s golpea con fuerza pero sin resultados." % self.nombre 
  self.cansancio()
    else:
      if self.hacer_danio(self.Enemigo):
        print "%s aniquila %s!" % (self.nombre, self.Enemigo.nombre)
        self.Enemigo = None
        self.estado = 'normal'
        if randint(0, self.salud) < 10:
          self.salud = self.salud + 1
          self.salud_max = self.salud_max + 1
          print "%s se siente mas fuerte!" % self.nombre
      else: 
    self.enemigo_ataques()
      
  def enemigo_ataques(self):
    if self.Enemigo.hacer_danio(self): 
  print "%s fue sacrificado por %s!!!nR.I.P." %(self.nombre, self.Enemigo.nombre)
 
Commands = {
  'salir': Jugador.salir,
  'ayuda': Jugador.ayuda,
  'estado': Jugador.estado,
  'descanso': Jugador.descanso,
  'explorar': Jugador.explorar,
  'huir': Jugador.huir,
  'atacar': Jugador.atacar,
  }
 
p = Jugador()
p.nombre = raw_input("Cual es el nombre del personaje? ")
print "(Escribe ayuda para obtener una lista de acciones)n"
print "%s entra en una cueva oscura en busca de aventura." % p.nombre
 
 
while(p.salud > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands(p)
        commandFound = True
        break
    if not commandFound:
      print "%s no se entiende la accion." % p.nombre
 