import sqlite3 #Vai importar o banco de dados

try: #Especifica manipuladores de exceção e/ou código de limpeza para um grupo de instruções
    banco = sqlite3.connect('banco.db') #Cria uma conexão com o banco de dados 

    cursor = banco.cursor() #Executa instruções e buscar resultados de consultas

    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)") #Cria uma tabela no banco de dados

    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ") #Adiciona os dados, na tabela
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ") #Adiciona os dados, na tabela
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ") #Adiciona os dados, na tabela
    banco.commit() #confirmar a ação executada anteriormente
    print("Os dados foram adicionados com sucesso!!") #Mostra o texto, no terminal


    cursor.execute("Select *FROM aluno") #Vai selecionar a coluna alunos na tabela
    print(cursor.fetchall()) #Mostra todos os dados da coluna selecionada


    cursor.execute("DELETE from aluno WHERE idade = 20") #Vai deletar os alunos que tiverem idade igual a 20

    banco.commit() #confirma a ação executada anteriormente
    banco.close() #Não permite alterações posteriores
    print("Os dados foram removidos com sucesso!!") #Mostra o texto, no terminal

except sqlite3.Error as erro: #Quando uma exceção ocorre no bloco try, uma busca por um manipulador de exceção é iniciada.
    print("Erro ao excluir: ", erro) #Mostra o texto, no terminal
