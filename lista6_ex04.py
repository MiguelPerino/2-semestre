def registrations():

    while True:
        try:
            qnt = int(input('Quantos livros deseja registrar: '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')

    books = []
    for i in range(qnt):
        book_name = input(f'\nLivro {i + 1} - Título: ').strip()
        writer_name = input(f'Livro {i + 1} - Autor: ').strip().title()

        dic = {
            'book': book_name,
            'writer': writer_name
        }

        books.append(dic)

    return books

def organized_print(books):
    #writers without repetition
    writers_set = set()
    for writer in books:
        writers_set.add(writer['writer'])
    
    #dicionary with author: book
    book_by_writer = {}
    for book in books:
        writer = book['writer']
        title = book['book']

        if writer not in book_by_writer:
            book_by_writer[writer] = []
        
        book_by_writer[writer].append(title)

    #quantity of book per author
    qnt_books = []
    for writer in book_by_writer:
        total_book = len(book_by_writer[writer])
        qnt_books.append((writer, total_book))

    #author with more books
    biggest = qnt_books[0]
    for qnt in qnt_books:
        if qnt[1] > biggest[1]:
            biggest = qnt
    
    print('\nAutores: ')
    for writer in writers_set:
        print('-', writer)

    print('\nLivros por autor: ')
    for writer, tittles in book_by_writer.items():
        print(f'- {writer}: {', '.join(tittles)}')

    while True:
        option_writer = input('\nDigite um autor para listar títulos: ').title().strip()
        if option_writer in writers_set:
            print(f'Livros de {option_writer}:')
            for book in book_by_writer[option_writer]:
                print('-', book)
            break
        else:
            print('\nNenhum autor encontrado, tente novamente...')

    print(f'\nAutor com mais livros cadastrados: {biggest[0]} ({biggest[1]})')

organized_print(registrations())
