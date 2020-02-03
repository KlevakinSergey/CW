
with open('air.txt', 'r') as f:
    text = f.read()
    text = ''.join(text)
    text = text.replace(',', '').replace('.', '').replace('?', '').replace('!', '').replace(' ','').replace('\n','')
    letters = list(text)
   
    
def get_letters_dict(letters):
    letters_dict = {}
 
    for letter in letters:
        if letter in letters_dict:
            letters_dict[letter] = letters_dict[letter] + 1
        else:
            letters_dict[letter] = 1
    return letters_dict


letters_dict = get_letters_dict(letters)
max_value = max(letters_dict.values())
final_dict = {k:v for k, v in letters_dict.items() if v == max_value}
print(letters_dict)    
print(f'Самый повторяющийся символ: {final_dict}')







    







