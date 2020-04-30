from random import choice, shuffle

"""


Clasificacion de los elementos quimicos

En no metales y metales

Los no metales se clasifican en

                +   pre,sufijos -
halogenos:
    Flur        1   Hipo-oso    -1
    Cloro       3   -oso
    Bromo       5   -ico
    Yodo        7   Per-ico
anfigenos:
    Oxigeno     2   Hipo-oso    -2
    Azufre      4   -oso
    Selenio     6   -ico
    Teluro
nitrogenoides:
    Nitrogeno   3   -oso        -3
    Fosforo     5   -ico
    Arsenico    
    Antimonio
  Especial
    Boro        3   -ico
carbonoides:
    Carbon      4   -ico        -4
    Silicio
    Germanio

Los metales se clasifican en
Metales de valencia fija y valencia variable
los de valencia fija son 
monovalentes:
divalentes:
trivalentes:
tetravalentes:
hexavalentes:

los de valencia variable son
monovalentes y divalentes:
monovalentes y trivalentes:
divalentes y trivalentes:
divalentes y tetravalentes:
trivalentes y tetravalentes:
trivalentes y pentavalentes:
"""


tabla_de_valencias_metales=[
    ['Aluminio','Al','3','Trivalentes'],
    ['Francio','Fr','1','Monovalentes'],
    ['Radio','Ra','2','Divalentes'],
    ['Disprosio','Dy','3','Trivalentes'],
    ['Europio','Eu','3','Trivalentes'],
    ['Escandio','Sc','3','Trivalentes'],
    ['Radical Amonio','NH4','1','Monovalentes'],
    ['Berilio','Be','2','Divalentes'],
    ['Cadmio','Cd','2','Divalentes'],
    ['Zinc','Zn','2','Divalentes'],
    ['Cobre','Cu','1 y 2','Mono y Divalentes'],
    ['Escandio','Sc','3','Trivalentes'],
    ['Estroncio','Sr','2','Divalentes'],
    ['Erbio','Er','3','Trivalentes'],
    ['Iridio','Ir','4','Tetravalentes'],
    ['Lantano','La','3','Trivalentes'],
    ['Magnesio','Mg','2','Divalentes'],
    ['Mercurio','Hg','1 y 2','Mono y Divalentes'],
    ['Niobio','Nb','3 y 5','Tri y Pentavalentes'],
    ['Osmio','Os','4','Tetravalentes'],
    ['Plata','Ag','1','Monovalentes'],
    ['Plomo','Pb','2 y 4','Di y Tetravalentes'],
    ['Praseodimio','Pr','3 y 4','Tri y Tetravalentes'],
    ['Renio','Re','4','Tetravalentes'],
    ['Sodio','Na','1','Monovalentes'],
    ['Rubidio','Rb','1','Monovalentes'],
    ['Tantalio','Ta','3 y 5','Tri y Pentavalentes'],
    ['Vanadio','V','3 y 5','Tri y Pentavalentes'],
    ['Bario','Ba','2','Divalentes'],
    ['Bismuto','Bi','3','Trivalentes'],
    ['Calcio','Ca','2','Divalentes'],
    ['Cesio','Cs','1','Monovalentes'],
    ['Cobalto','Co','2 y 3','Di y Trivalentes'],
    ['Estaño','Sn','2 y 4','Di y Tetravalentes'],
    ['Galio','Ga','3','Trivalentes'],
    ['Hafnio','Hf','4','Tetravalentes'],
    ['Hierro','Fe','2 y 3','Di y Trivalentes'],
    ['Cromo','Cr','2 y 3','Di y Trivalentes'],
    ['Cerio','Ce','3 y 4','Tri y Tetravalentes'],
    ['Holmio','Ho','3','Trivalentes'],
    ['Ytrio','Y','3','Trivalentes'],
    ['Indio','In','3','Trivalentes'],
    ['Litio','Li','1','Monovalentes'],
    ['Manganeso','Mn','2 y 3','Di y Trivalentes'],
    ['Molibdeno','Mo','6','Hexavalentes'],
    ['Magnesio','Mg','2','Divalentes'],
    ['Neodimio','Nd','3','Trivalentes'],
    ['Níquel','Ni','2 y 3','Di y Trivalentes'],
    ['Oro','Au','1 y 3','Mono y Trivalentes'],
    ['Paladio','Pd','4','Tetravalentes'],
    ['Prometeo','Pm','3','Trivalentes'],
    ['Platino','Pt','2 y 4','Di y Tetravalentes'],
    ['Potasio','K','1','Monovalentes'],
    ['Rodio','Rh','4','Tetravalentes'],
    ['Lutecio','Lu','3','Trivalentes'],
    ['Rutenio','Ru','4','Tetravalentes'],
    ['Talio','Tl','1 y 3','Mono y Trivalentes'],
    ['Tecnecio','Tc','7','Heptavalentes'],
    ['Torio','Th','4','Tetravalentes'],
    ['Tulio','Tm','3','Trivalentes'],
    ['Gadolinio','Gd','3','Trivalentes'],
    ['Samario','Sm','3','Trivalentes'],
    ['Uranio','U','6','Hexavalentes'],
    ['Yterbio','Yb','3','Trivalentes'],
    ['Terbio','Tb','3','Trivalentes'],
    ['Ýtrio','Y','3','Trivalentes'],
    ['Wolframio','W','6','Hexavalentes'],
    ['Zirconio','Zr','4','Tetravalentes']]





maxz=len(tabla_de_valencias_metales)

def juego_quimica():
 shuffle(tabla_de_valencias_metales)
 z=1
 print("""
Nombres
Valencias
Grupos
Todos
""")

 op=input('N, V, G, T: ')

 if op=='N' or op=='n':
  for elemento in tabla_de_valencias_metales:
    print ('Cual es el nombre de ',elemento[1],' ?')
    nombre=input()
    if nombre.capitalize()==elemento[0]:
        print('Correcto')
    else:
        print('Incorrecto, la respuesta es ',elemento[0])

 if op=='V' or op=='v':
          
  for elemento in tabla_de_valencias_metales:
    print ('Cual es o son las valencias de '+str(elemento[0])+'('+str(elemento[1])+') ?')
    valencias=input()
    if valencias==elemento[2]:
        print('Correcto')
        z+=1
    else:
        print('Incorrecto, la respuesta es ',elemento[2])

 if op=='G' or op=='g':
  grupo=input('Nombre del grupo: ')
  for elemento in tabla_de_valencias_metales:
      if elemento[3].find(grupo)!=-1:
          print (elemento[0],elemento[1],elemento[2])
      else:
          pass

 if op=='T' or op=='t':
     print('Enter para continuar')
     for p in tabla_de_valencias_metales:
         print (p[0],'('+str(p[1])+')','Oxidación +',p[2],p[3],end="\r")
         xds=input()


while True:
    try:
        juego_quimica()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)
        juego_quimica()

  















