# Conexão de Python com Banco de Dados SQLite
Este projeto demonstra os conceitos fundamentais de como conectar a linguagem de programação Python com um banco de dados relacional leve, o SQLite.

O código foi desenvolvido com base nos aprendizados de cursos sobre Bancos de Dados Relacionais e Não-Relacionais, e integração de Python com APIs de banco de dados.

## 💻 Tecnologias Utilizadas
Python: Linguagem de programação principal.

SQLite: Banco de dados relacional leve, ideal para pequenos projetos e prototipagem.

Biblioteca sqlite3: Biblioteca nativa do Python, usada para interagir com o SQLite sem a necessidade de drivers externos.

Módulo pathlib: Usado para gerenciar e manipular caminhos de arquivos de forma robusta e compatível entre diferentes sistemas operacionais.

## 📁 Estrutura do Projeto
O projeto consiste em um ou mais scripts Python que realizam as seguintes operações:

Conexão com o Banco de Dados: Estabelece a conexão com um arquivo de banco de dados (meu_banco.db).

Criação de Tabelas: Executa comandos SQL para criar uma tabela chamada clientes com colunas para id, nome e email.

Inserção de Dados: Demonstra como inserir registros (linhas) na tabela clientes.

Manipulação de Transações: Usa o cursor para executar comandos SQL e o commit() para salvar as alterações de forma segura.

Tratamento de Erros: Inclui uma estrutura de try-except-finally para garantir que a conexão seja fechada corretamente, mesmo em caso de erros.
