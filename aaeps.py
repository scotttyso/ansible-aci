#!/usr/bin/env python3
from dotmap import DotMap
import json
import sys
jdata = DotMap(json.load(open(f'{sys.argv[1]}', 'r')))
aaep = DotMap()
aaeps_missing_mappings = []
for e in jdata.imdata:
    match_epgs = False
    for item in e.infraAttEntityP.children:
        if item.get('infraGeneric'):
            aaep[e.infraAttEntityP.attributes.name] = []
            match_epgs = True
            for i in item.infraGeneric.children:
                aaep[e.infraAttEntityP.attributes.name].append(i.infraRsFuncToEpg.attributes.tDn)
    if match_epgs == False: aaeps_missing_mappings.append(e.infraAttEntityP.attributes.name)
print(f'{"=" * 91}\n  AAEP with EPG Mappings\n{"=" * 91}')
print(json.dumps(aaep, indent=4))
print(f'{"=" * 91}\n  AAEP with no EPG Mappings\n{"=" * 91}')
print(aaeps_missing_mappings)
outfile = open(f'./{sys.argv[1]}_with_mappings.json', 'w')
outfile.write(json.dumps(aaep, indent=4))
outfile.close()

outfile = open(f'./{sys.argv[1]}_without_mappings.json', 'w')
outfile.write(json.dumps(aaeps_missing_mappings, indent=4))
outfile.close()

