import json

fr: str = 'food_services.json'

district: dict = dict()

oper_company: dict = dict()

with open (fr, 'r',encoding = 'utf8') as fo:
    f=json.load(fo)
    for mini_dict in f:

        #словарь районов и заведений
        d = mini_dict.get('District')
        district[d] = district.get(d,0)+1

        if mini_dict.get('IsNetObject').lower() =='да':
            oc = mini_dict.get('OperatingCompany')
            oper_company[oc] = oper_company.get(oc,0)+1

max_distr = max(district, key = lambda x: district.get(x))
max_oc = max(oper_company, key = lambda x: oper_company.get(x))

print(f'{max_distr}: {district.get(max_distr)}')

print(f'{max_oc}: {oper_company.get(max_oc)}')



