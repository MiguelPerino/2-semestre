# Faça um programa que leia os dados de n livros (título e autor) e armazene
# em uma lista de dicionários. Mostre os autores cadastrados sem repetição e
# permita que o usuário digite o nome de um autor para listar os títulos dos
# livros desse autor. 

def registrations():
    quantity = int(input('Informe a quantidade de livros: '))

    books = []
    for i in range(quantity):
        book_name = input(f'\nTítulo {i+1} - Título: ').title().strip()
        writer = input(f'Autor {i+1} - Autor: ').title().strip()

        dic = {
            'book_name': book_name,
            'writer':writer,
        }
        books.append(dic)

    return books

def consultation(books):

    set_writer = set()
    for writer in books:
        set_writer.add(writer['writer'])
    
    print('\nAutores cadastrados:')
    for w in set_writer:
        print('-', w)

    option = input('\nInforme o nome de um autor para consulta: ').title().strip()

    print(f'Livros de {option}:')
    for book in books:
        if book['writer'] == option:
            print('-', book['book_name'])
        
library = registrations()

consultation(library)
