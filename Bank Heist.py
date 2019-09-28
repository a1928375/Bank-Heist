available = {
        "statue" : (15, 30000) ,
        "mask" : (9, 16000) ,
        "urn" : (8, 15000) ,
} 

limit = 20

taken = [ "mask", "urn" ] 

def heistvalid(available, limit, taken):
    return sum([available[ele][0] for ele in taken]) < limit

def heisttotal(available, limit, taken): 
    return sum([available[ele][1] for ele in taken])
    
print (heistvalid(available, limit, taken) == True)

print (heisttotal(available, limit, taken) == 31000)

allthree = ["statue", "mask", "urn"]

print (heistvalid(available, limit, allthree) == False)

print (heisttotal(available, limit, allthree) == 61000)
