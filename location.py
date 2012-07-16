from pymongo import Connection, GEO2D

def loc_query():
    db  = Connection().geo_example
    db.places.create_index([('loc', GEO2D)])      #create a geospatial index

    db.places.insert({'loc': [2, 5]})
    db.places.insert({'loc': [30, 5]})
    db.places.insert({'loc': [1, 2]})
    db.places.insert({'loc': [4, 4]})

    #query by $near
    for loc in db.places.find({'loc': {'$near': [3, 6]}}).limit(3):
        repr(loc)
    
        #query by $within a $box
        for loc in db.places.find({'loc': {'$within': \
                                           {'$box': [[2, 2], [5, 6]]}}}):
            repr(loc)
    
            #query by $within a $center
            for loc in db.places.find({'loc': {'$within': \
                                               {'$center': [[0, 0], 6]}}}):
                repr(loc)
                
if __name__ == '__main__':
    loc_query()
