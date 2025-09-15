# gerenciando transações
import sqlite3  # Biblioteca para usar banco de dados SQLite
from pathlib import Path  # Para manipular diretórios e caminhos de arquivos

# Pega o diretório onde o arquivo Python está e define como raiz
ROOT_PATH = Path(__file__).parent

# Cria conexão com o banco de dados "meu_banco.db"
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
cursor = conexao.cursor()  # Cria um cursor que executa os comandos SQL
cursor.row factory = sqlite3.Row  # Permite acessar resultados como dicionário (ex: cliente["nome"])

# Tentativa de executar operações no banco de dados
try:
  # Primeira inserção no banco (nome e email de um cliente)
  cursor.execute('INSERT INTO clientes ( nome, email) VALUES (?,?), ('Teste 1', 'teste1@gmail.com'))
  conexao.commit()  # Confirma a operação

  # Segunda inserção, tentando inserir com id definido (id=2)
  cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?), (2, 'Teste 2', 'teste2@gmail.com'))
  conexao.commit()  # Confirma a operação

# Captura qualquer erro que acontecer no bloco try
excepet Exception as exc:
                 print(f"Ops! um erro Ocorreu: {exc}")  # Mostra o erro
                 conexao.rollback()  # Desfaz as operações feitas no banco caso tenha dado erro

# Este bloco roda sempre, independente de dar erro ou não
finally:
  conexao.close()  # Fecha a conexão com o banco de dados
