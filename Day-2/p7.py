import pprint

d = {}
d ['K1'] = [{'url':'cisco.com', 'port':80, 'IP':'1.2.3.4'},{'url':'xyz.com','port':90,'IP':'1.4.7.9'}]
#d['K2'] = [{'K1':[1,2,3,{'K1':[12,25]}]

pprint.pprint(d)
print(d['K1'][1]['port'])
            
