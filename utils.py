from  typing  import List,Tuple
from dfs import * 
from math import dist

def way(game_map,start,end,restrictions,algorithm): 
    adj=Adjacents.build_adj(game_map,restrictions)
    graph=Graph(adj)
    if algorithm=="amplitud":
        graph.amplitud(parser_pos(game_map,start[1],start[0]))
    elif algorithm=="profundidad":
        graph.profundidad(parser_pos(game_map,start[1],start[0]))
    return graph.construir_camino(parser_pos(game_map,end[1],end[0]))    

def most_closest_fire(fires:List[Tuple[int,int]],x:int,y:int):
    d1=abs(euclidian_d(y,fires[0][0],x,fires[0][1]))
    d2=abs(euclidian_d(y,fires[1][0],x,fires[1][1]))
    return fires[0] if d1<d2 else fires[1]
     
def less_closest_fire(fires:List[Tuple[int,int]],x:int,y:int):
    d1=abs(euclidian_d(y,fires[0][0],x,fires[0][1]))
    d2=abs(euclidian_d(y,fires[1][0],x,fires[1][1]))
    return fires[1] if d1<d2 else fires[0]

def euclidian_d(y1,y2,x2,x1): 
    return dist((x1,y1),(x2,y2))

def parser_pos(map:List[List[int]], x:int ,y:int )->int:
    """
    from (0,0) (0,1) (0,2)  to 0 1 2 
         (1,0) (1,1) (1,2)     3 4 5     
         (2,0) (2,1) (2,2)     6 7 8
    """
    size_x=len(map[0])
    return (y*size_x) +x


def info(map: List[List[int]]) -> Tuple[List[Tuple[int, int]], Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    """
    Extract info from the map like fires, bucket1, bucket2, hidrant, start.
    """
    fires = []
    bucket1 = ()
    bucket2 = ()
    hidrant = ()
    start = ()
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 2:
                fires.append((y, x))
            elif map[y][x] == 3:
                bucket1 = (y, x)
            elif map[y][x] == 4:
                bucket2 = (y, x)
            elif map[y][x] == 5:
                start = (y, x)
            elif map[y][x] == 6:
                hidrant = (y, x)
    return (fires, bucket1, bucket2, hidrant, start)

