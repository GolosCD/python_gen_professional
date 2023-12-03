suits = ['пик', 'треф', 'бубен', 'червей']

number_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

a =iter([f'{i} {j}' for j in suits for i in number_cards])
b = iter(a)

print(*(a))