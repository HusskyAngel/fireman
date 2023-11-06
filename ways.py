from utils import  less_closest_fire, way,info,most_closest_fire

def camino_1(game_map,algorithm):
    fires,bucket1,bucket2,hidrant,start=info(game_map)
    start_to_bucket1=way(game_map,start,bucket1,set([1,2]),algorithm)
    bucket1_to_hidrant=way(game_map,bucket1,hidrant,set([1,2]),algorithm)
    closest_fire=most_closest_fire(fires,hidrant[1],hidrant[0])
    hidrant_to_closestfire=way(game_map,hidrant,closest_fire,set([1]),algorithm)
    closestfire_to_hidrant=way(game_map,closest_fire,hidrant,set([1,2]),algorithm)
    lessclosestfire=less_closest_fire(fires,hidrant[1],hidrant[0])
    hidrant_to_lessclosestfire=way(game_map,hidrant,lessclosestfire,set([1]),algorithm)
    final_way=hidrant_to_lessclosestfire+closestfire_to_hidrant+hidrant_to_closestfire+bucket1_to_hidrant+start_to_bucket1
    cost_1=len(start_to_bucket1)+len(bucket1_to_hidrant)+len(closestfire_to_hidrant)
    cost_2=(len(hidrant_to_closestfire)+len(hidrant_to_lessclosestfire))*2
    cost=cost_1+cost_2
    return final_way,cost 

def camino_2(game_map,algorithm):
    fires,bucket1,bucket2,hidrant,start=info(game_map)
    start_to_bucket2=way(game_map,start,bucket2,set([1,2]),algorithm)
    bucket2_to_hidrant=way(game_map,bucket2,hidrant,set([1,2]),algorithm)
    closest_fire=most_closest_fire(fires,hidrant[1],hidrant[0])
    hidrant_to_closestfire=way(game_map,hidrant,closest_fire,set([1]),algorithm)
    lessclosestfire=less_closest_fire(fires,hidrant[1],hidrant[0])
    hidrant_to_lessclosestfire=way(game_map,closest_fire,lessclosestfire,set([1]),algorithm)
    final_way=hidrant_to_lessclosestfire+hidrant_to_closestfire+bucket2_to_hidrant+start_to_bucket2
    cost_1=len(start_to_bucket2)+len(bucket2_to_hidrant)
    cost_3=(len(hidrant_to_closestfire))*3
    cost_2=len(hidrant_to_lessclosestfire)*2
    cost =cost_1+cost_2+cost_3
    return final_way,cost
     