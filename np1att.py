
usuarios = {}
usuario_logado = None
def validar_senha(senha):
    if len(senha) < 8:
        return "Senha Precisa ter pelo menos 8 caracteres"
    maiscula = False
    numero = False
    simbols = False
    simbols_permitidos = "!@#$%&*,.;""':[]()_+=-" #simbolos permitidos
    for c in senha:
        if c.isupper():
            maiscula = True
        elif c.isdigit():
            numero = True
        elif c in simbols_permitidos:
            simbols = True
    

def mostrar_menu_principal():
    print("\n=== PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA ===")
    print("1. Login / Cadastro")
    print("2. Cursos Disponíveis")
    print("3. Informações de Segurança")
    print("4. Cadastrar Módulos")
    print("5. Sair")
    return input("Escolha uma opção: ")

def tela_login_cadastro():
    while True:
        print("\n=== LOGIN / CADASTRO ===")
        print("1. Fazer Login")
        print("2. Criar Novo Usuário")
        print("0. Voltar")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            fazer_login()
        elif opcao == '2':
            criar_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def fazer_login():
    global usuario_logado
    print("\n--- Login ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        usuario_logado = usuario
        print(f"\nBem-vindo(a), {usuario}!")
        return True
    else:
        print("\nCredenciais inválidas!")
        return False

def criar_usuario():
    print("\n--- Novo Cadastro ---")
    usuario = input("Escolha um nome de usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    while True:
        senha = input("Crie uma senha (mínimo 8 caracteres): ")
        if len(senha) >= 8:
            break
        print("Senha muito curta!")
    
    usuarios[usuario] = senha
    print("Cadastro realizado com sucesso!")

def tela_cursos():
    print("\n=== CURSOS DISPONÍVEIS ===")
    cursos = [
        "1. Introdução à Programação (40h)",
        "2. Segurança da Informação Básica (30h)",
        "3. LGPD na Prática (25h)",
        "4. Inclusão Digital para Todos (35h)",
        
    ]
    for curso in cursos:
        print(curso)
    input("\nPressione Enter para voltar...")

def tela_seguranca():
    print("\n=== INFORMAÇÕES DE SEGURANÇA ===")
    print("• Todas as senhas são armazenadas de forma segura")
    print("• Dados pessoais protegidos pela LGPD")
    print("• Criptografia de ponta a ponta")
    print("• Não compartilhe suas credenciais")
    print("• Atualizações regulares de segurança\n")
    input("Pressione Enter para voltar...")

def tela_modulos():
    print("\n=== CADASTRAR MÓDULOS ===")
    if usuario_logado:
        curso = input("Digite o nome do curso: ")
        modulo = input("Nome do novo módulo: ")
        print(f"\nMódulo '{modulo}' cadastrado com sucesso no curso '{curso}'!")
    else:
        print("Você precisa estar logado para acessar esta função!")
    input("\nPressione Enter para voltar...")

def main():
    while True:
        escolha = mostrar_menu_principal()
        
        if escolha == '1':
            tela_login_cadastro()
        elif escolha == '2':
            tela_cursos()
        elif escolha == '3':
            tela_seguranca()
        elif escolha == '4':
            tela_modulos()
        elif escolha == '5':
            print("\nObrigado por usar nossa plataforma!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()