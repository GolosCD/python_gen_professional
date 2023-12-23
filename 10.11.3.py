'''
Группы слов
Напишите программу, которая группирует слова по их длине.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом. Каждое слово записано строчными латинскими буквами.

Формат выходных данных
Программа должна сгруппировать введенные слова по их длине и вывести полученные группы. 
Для каждой группы должна быть указана длина, а затем через запятую перечислены слова, имеющие соответствующую длину. 
Группы должны быть расположены в порядке увеличения длины, каждая на отдельной строке, слова в группах — в алфавитном порядке, в следующем формате:

<длина> -> <слово>, <слово>, ...
Примечание. Тестовые данные доступны по ссылкам:
'''
import itertools as it

input_list :list = sorted([i for i in input().split()], key = len,reverse = False)
group = it.groupby(input_list,key = len)
for i,gen in group:
    print(f'{i} -> {", ".join(sorted(list(gen)))}')


# INPUT DATA:

# TEST_1:

'''
# TEST_2:
hello beegeek stepik python

# TEST_3:
went outside to the well it looked rather tatty but tried to comince myself it could be magical

# TEST_4:
a a a a a a a a a a a a a

# TEST_5:
a aa aaa aaaa aaaaa aaaaaa aaaaaaa

# TEST_6:
pw kowyegmsihl lnqw tkzladgrfvhpsw bsxnqd oydntwae zygcpxh z pqycrviultoek yfn vxnjwmpoahzludq spuzkvdah seztmhqnpkgfur bxros uczkfqdve hl rdfaypquviwgtsc vchmyuqbp wnxdsuepbvia bhol ihlsnoxfzywvarg gjeabyqkocsixv dqjsriht tgcwe feralzuowhpcxq ztw mlsuy aqgmsuziyxpdtj dcos ypdoejks uynti ebkxaqm xvmft dzqlxmhfkpbvgua erkjdctoqglpb ubdofz hgrfewbctmnv anz wkhbqlatdex x pucrf oxpgsivqrlmj lab gvri dmwpohciqlatf hmyciukvb f furgibvs xcr xvijrlcgdmopf

# TEST_7:
qizutanpgf embokhvsxpjd ynwqkfgtj gltmwavcksqhpzfejnoribyd maoprjbivlgz yuzbqwvxckjernpisoaftlhgm psuxavl feryju qgtkipfdh arsmkzydnhflqijgt lwzprie strhfulywjegn zxtkhrmpgiu nwdmrapihkoytuqxbczev uhcvzmtwiprxbgeqjofnl jibdxnolfpygtch dhskgbrwfpc lrfisqgyu fuhmneizj gzawytcijpem yjfelwdspmc mguztlp enwxhblfcrkduzmsjpto lsgterh uyxfrzohkai uwqsdnhvk lpyr wyikvqtrhzlcpnujagdombf jhnfstmvgxiy ghuspnjvfcqldiotwmkzayxber qdoznhyul lnzjvo vaqmohyerxtlibjfwzdpk pco yuvfgwpxoraetl coepsl pgbxrwun lmsvucjqthgzfdneix yg gbqij azjvrtnqsdmfluy uiea gmfbakdhrxv kzowibjmtrvndcqfyhu fbtmivc dj ztwahcijuvnqyoplgr bdgtvrw wv rnogcb hcnpywxvtzqldkioab zukayjlnspqbdvgfx golyibvnjexqthcukrpafmzwd ul rfuavdoqxgjsbpmzhenitl arvfpgjncolyzbxhiqdku oipmeqdcgsbxfn kbjlhqaxrswpenfvyimz owialx lhpcy rsvlaxkfen v tuirfkoplbn vtyick uqbmlpizorfkdhyntajgx lfhgodvwq iqoezkfucwvgxpbsylahjrmntd bvitgrejnklxopa pmwzits ipbxoretdsvcy wjtpgaexufkvihyqmrobzdsnlc haitsrdqfzukopcwjx hixg kmvdjwzuygr qs aoglcdnuqvswbxm yfgrdaozp vmjfrlagyetcd mbrpxuochlvwqjakydszfg idwayrplkuen ovzlkfxqagmewn lpeyntxmagdqucfbh goful xozjihwmgqyctulsnvpkfreb fhpu a nqjhrtlyaxoukgvescmpibwfd ugjhxnzfq kiptxcorheasjfwbnzg nzckjdimsbptyq fhqutmbcogy jpsrtlbimxgevz dtnbjaemzxk kzowrmexusdvynfiahgbcpl fbvpohzurasqcdwl ziclgeywfmqhsxvpborunjtda hytpigj kznhdjymwgvxtqfolbrp yjlc mtdvejxbrluagzcsnoh
'''