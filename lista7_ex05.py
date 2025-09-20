# Crie uma função que abra um arquivo de texto, leia a primeira linha e exiba o
# conteúdo. Garanta que o arquivo será sempre fechado, mesmo se ocorrer
# erro de abertura ou leitura (use finally). Trate arquivo inexistente e falha
# de leitura

def getFile(file):
    try:    
        with open (file, 'r') as text:
            line1 = text.readline()

        if line1:
            print(line1.strip())
        else:
            print('Não há nada na primeira linha')


    except FileNotFoundError:
        print('Arquivo não encontrado')
    
    except Exception as e:
        print(f'Falha ao ler o arquivo: {e}')

    finally:
        print(f'Fechando arquivo...')


with open("arquivo1.txt", "w") as f:
    f.write("Esta é a primeira linha do arquivo 1\nSegunda linha")

with open("arquivo2.txt", "w") as f:
    f.write("") 

getFile("arquivo1.txt")
getFile("arquivo2.txt")
getFile("arquivo3.txt") 
