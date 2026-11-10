None
meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            'ROFL': 'Odpowiedź na żart', 
            'SHEESH': 'Lekka Dezaprobata', 
            'CREEPY': 'Straszny, złowieszczy', 
            'AGGRO': 'Stać się agresywnym/zły'
            }
while True:
    word = input("Wpisz słowo, którego nie rozumiesz: ").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else :
        print('Nie znam takiego słowa.')
