# estudo banco de dados Python aula 1
import sqlite3  # Biblioteca nativa do Python para trabalhar com SQLite (banco de dados leve, baseado em arquivos locais)

from pathlib import Path  # Usado para manipulação de caminhos de arquivos de forma mais prática e compatível entre sistemas operacionais

# ROOT_PATH guarda o caminho da pasta onde o arquivo atual (este script) está salvo
ROOT_PATH = Path(__file__).parent

# Criando uma conexão com o banco de dados chamado "meu_banco.db"
# Se o arquivo não existir, o SQLite cria automaticamente
conexao = sqlite3.connect(ROOT_PATH /_'meu_banco.db')  
cursor = conexao.cursor()  # Criamos o cursor, que é o objeto que executa os comandos SQL dentro da conexão
cursor.row_facture = sqlite3.Row  # Faz com que os resultados de consultas possam ser acessados como dicionário (ex: cliente["nome"])

# -----------------------------
# Função para criar a tabela
def criar_tabela(conexao, cursor):
    # SQL para criar a tabela "clientes"
    cursor.execute("CRATE TABLE clientes (id ITEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100), email VARCHAR (1150))")
    conexao.commit()  # Salva as alterações no banco
    conexao.close()   # Fecha a conexão

# -----------------------------
# Função para inserir um único registro
def inserir_registro(conexao, cursor,nome, email):
  data = ("Joao", "Joao@gmail.com")  # Dados que serão inseridos
  cursor.execute("INSERT INTO clientes (nome, email) VALUES(?,?);", data)
  conexao.commit()
  conexao.close()

# -----------------------------
# Função para atualizar um registro existente
def atualizar_registro(conexao, cursor, id, nome, email):
  data = (nome, email, id)  # Dados que serão usados na atualização
  cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", data)
  conexao.commit()
  conexao.close()

  # Chamada da função para atualizar o cliente de id=1
  aatualizar_registro(conexao, cursor, 1, "Maria", "Maria@gmail.com")

# -----------------------------
# deletar registros
def excluir_registro(conexao, cursor, id):
    data = (id,)  # O "id" do cliente a ser excluído
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)
    conexao.commit()
    conexao.close()

    # Exemplo de uso: exclui cliente com id=1
    excluir_registro(conexao, cursor, 1)

# -----------------------------
# operação em lote (inserir vários clientes de uma só vez)
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?,?);", dados)
    conexao.commit()
    conexao.close()

 # Exemplo de dados a serem inseridos em lote:
 # dados = [
 #    ("maria", "maria@gmail.com"),
 #    ("pedro", "pedro@gmail.com"),
 #    ("joao", "joao@gmail.com"), ]
 # inserir_muitos(conexao, cursor, dados)

inserir_muitos(conexao, cursor, dados )  # Chamada da função, mas "dados" precisa estar definido antes

# -----------------------------
# for cliente in dados:
#    inserir_registro(conexao, cursor, cliente[0], cliente[1])  
# (esse trecho faria a inserção registro por registro, mas já temos a versão em lote acima)

# -----------------------------
# consulta de um único resultado
def recuperar_cliente(conexao, cursor, id):
    # cursor.row_facture = sqlite3.Row # poderia ativar novamente para acessar como dicionário
    cursor.execute("SELECT * FROM clientes WHERE id = ?;", (id,))
    return cursor.fetchone()  # Retorna apenas UM cliente

# -----------------------------
# consulta de vários resultados
def listar_clientes(cursor):
      return cursor.execute("SELECT * FROM clientes ORDER BY nome;")  # Retorna todos os clientes ordenados pelo nome

# Recupera cliente de id=2
cliente = recuperar_cliente(conexao, cursor, 2)
print(dict(cliente))  # Converte em dicionário para exibir
print(cliente['id'], cliente["nome"], cliente["email"])  # Acessa os campos do cliente por chave

# Lista todos os clientes cadastrados
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))  # Converte cada linha em dicionário e imprime

# Boas-vindas ao sistema com base no nome
print(f'Seja bem vindo ao sistema {cliente["nome"]}')
print(f'Seja bem vindo ao sistema {cliente[1]}')  # Aqui acessa por índice (não é seguro, pode causar erro se mudar a tabela)
