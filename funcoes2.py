def loginUsuario(perfil):
    # Verifica se o valor do parâmetro perfil é igual a 'admin' (considerando letras maiúsculas e minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chama a função loginUsuario com diferentes valores
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMIN')