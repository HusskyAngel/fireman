from typing import List

def parser_pos(map:List[List[int]], x:int ,y:int )->int:
    """
    from (0,0) (0,1) (0,2)  to 0 1 2 
         (1,0) (1,1) (1,2)     3 4 5     
         (2,0) (2,1) (2,2)     6 7 8
    """
    size_x=len(map[0])
    return (y*size_x) +x

class UtilsAdjacent: 
    @staticmethod 
    def is_validx(x:int ,map:List[List[int]])->bool:
        return False if (x<0 or x>= len(map[0])) else True

    @staticmethod 
    def is_validy(y:int ,map:List[List[int]])->bool:
        return False if (y<0 or y>= len(map)) else True

class Adjacents:
    """
    Constructs the adjacents
    """
    @staticmethod
    def build_adj(map:list,restrictions:set)->List[list[int]]:
        adjs=[]
        for y in range(len(map)):
            for x in range(len(map[y])):
                adjs_aux=[]
                if(UtilsAdjacent.is_validy(y+1,map) and map[y+1][x] not in restrictions):
                    adjs_aux.append( parser_pos(map,x,y+1)) 
                if(UtilsAdjacent.is_validy(y-1,map) and map[y-1][x] not in restrictions):
                    adjs_aux.append( parser_pos(map,x,y-1))
                if(UtilsAdjacent.is_validx(x-1,map) and map[y][x-1] not in restrictions):
                    adjs_aux.append( parser_pos(map,x-1,y))
                if(UtilsAdjacent.is_validx(x+1,map) and map[y][x+1] not in restrictions):
                    adjs_aux.append( parser_pos(map,x+1,y))
                adjs.append(adjs_aux)
        return adjs


class Graph(object):
    def __init__(self, adyacencia):
        self.ady = adyacencia
        self._init_grafo(-1)

    def _init_grafo(self, inicio):
        self.encontrado = [False for n in self.ady]
        self.procesado = [False for n in self.ady]
        self.padre = [-1 for n in self.ady]
        self.inicio = inicio

    def amplitud(self, inicio):
        """Usar busqueda en profundidad desde inicio a todo el grafo"""
        self._init_grafo(inicio)
        q = [inicio]
        self.encontrado[inicio] = True

        while q:
            v = q.pop(0)
            self.procesado[v] = True
            
            for vecino in self.ady[v]:
                if not self.encontrado[vecino]:
                    q.append(vecino)
                    self.encontrado[vecino] = True
                    self.padre[vecino] = v

    def profundidad(self,inicio): 
        """Usar busqueda en profundidad desde inicio a todo el grafo"""
        self._init_grafo(inicio)
        q = [inicio]
        self.encontrado[inicio] = True
        while q:
            v = q.pop()
            self.procesado[v] = True
            
            for vecino in self.ady[v]:
                if not self.encontrado[vecino]:
                    q.append(vecino)
                    self.encontrado[vecino] = True
                    self.padre[vecino] = v


    def construir_camino(self, destino):
        """Devuelve el camino entre los vertices inicio y destino"""
        if self.padre[destino] == -1 or self.inicio == -1:
            return None

        camino = [destino]
        p = destino
        while p != self.inicio:
            camino.append(self.padre[p])
            p = self.padre[p]

        return camino
