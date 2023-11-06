"""
MADE IT WITH LOVE FOR 
🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼
🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼
🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼
""" 
from ways import camino_1,camino_2
"""
GAME MAP 
"""
file_map=open("input.txt","r") 
s_map=file_map.readlines()
game_map=[]
for m in s_map:
    aux=m.strip()
    game_map.append(aux.split(r" "))
game_map=[[int(num) for num in sublist] for sublist in game_map]
    
print("==============================")
for m in game_map:
    print(m," \n")
print("==============================")

"""
======================
IA
======================
""" 

"""
Solo vamos a tener en cuenta dos posibles caminos:

          inicio    
            / \
           /   \
          /     \
         /       \
        /         \
       /           \
      /             \
     /               \
  cubeta 1        cubeta 2
    |                 |
  hidrante        hidrante 
    |                 |
  fuego cercano   fuego cecano 
    |                 |
  hidrante        fuego restante 
    |
  fuego restante  

vamos a calcular el costo de los dos caminos y vamos a tomar el de menos costo.
para decidir cual es el fuego mas cercano vamos a usar la distancia euclidiana
"""  

"""
camino 1
"""
w1,c_w1=camino_1(game_map=game_map,algorithm="amplitud")
 
"""
camino 2G
"""
w2,c_w2=camino_2(game_map=game_map,algorithm="amplitud")

if c_w2<c_w1:
    print(w2)
else:
    print(w1)



