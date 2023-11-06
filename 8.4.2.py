# linear_list: list=list()

# def linear(nested_lists:list)-> list:
# 	global linear_list
    
# 	for row in nested_lists:

# 		if row==None:
# 			return linear_list

# 		elif type(row)!= list:
# 			linear_list.append((row))

# 		if type(row)==list:
# 			linear(row)
# 	return linear_list

def linear(nested_lists:list)-> list:
		
	linear_list: list=list()
	def linear_add(nes:list)-> list:
		for row in nes:
			if row==None:
				return linear_list
			elif type(row)!= list:
				linear_list.append((row))
			if type(row)==list:
				linear_add(row)
	return linear_list 