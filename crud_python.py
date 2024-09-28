import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criando a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')
conn.commit()

# Função para criar um usuário
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Usuário criado com sucesso!")

# Função para listar os usuários
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Função para atualizar um usuário
def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    print(f"Usuário {user_id} atualizado com sucesso!")

# Função para deletar um usuário
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"Usuário {user_id} deletado com sucesso!")

# Menu de interação
def menu():
    while True:
        print("\nCRUD - Escolha uma opção:")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Sair")
        choice = input("Digite a opção: ")

        if choice == '1':
            name = input("Digite o nome do usuário: ")
            age = int(input("Digite a idade do usuário: "))
            create_user(name, age)
        elif choice == '2':
            read_users()
        elif choice == '3':
            user_id = int(input("Digite o ID do usuário que deseja atualizar: "))
            name = input("Digite o novo nome do usuário: ")
            age = int(input("Digite a nova idade do usuário: "))
            update_user(user_id, name, age)
        elif choice == '4':
            user_id = int(input("Digite o ID do usuário que deseja deletar: "))
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()

# Fechando a conexão ao banco de dados quando o programa termina
conn.close()

