# Aplicativo de Streaming de Música

Este é um aplicativo de streaming de música que permite adicionar músicas e criar playlists. O aplicativo tem duas opções para o usuário: administrador e usuário.

O *administrador* tem acesso a todas as funcionalidades do aplicativo e pode adicionar, editar ou excluir músicas, artistas, álbuns e playlists. O administrador também pode visualizar todas as informações armazenadas no banco de dados.

O *usuário* pode adicionar músicas para criar playlists pessoais. Os usuários podem visualizar as informações das músicas, artistas e álbuns existentes no banco de dados.

Como Usar o Aplicativo
O aplicativo tem um menu com três opções: administrador, usuário e sair. O usuário deve escolher uma opção para continuar.

1. Administrador
O administrador tem acesso a todas as funcionalidades do aplicativo. Ao escolher a opção "administrador", o usuário deve inserir as credenciais de login e senha para acessar as funcionalidades do administrador.

Após fazer login, o administrador pode adicionar, editar ou excluir músicas, artistas, álbuns e playlists. O administrador também pode visualizar todas as informações armazenadas no banco de dados.

2. Usuário
Ao escolher a opção "usuário", o usuário pode adicionar músicas e criar playlists pessoais. Os usuários podem visualizar as informações das músicas, artistas e álbuns existentes no banco de dados.

O usuário deve seguir as instruções na tela para adicionar músicas ou criar playlists. Após adicionar uma música ou criar uma playlist, ela será salva no banco de dados.

3. Sair
Ao escolher a opção "sair", o usuário encerra a sessão no aplicativo.

Banco de Dados
O banco de dados do aplicativo é armazenado em um arquivo de texto chamado "db.txt". O arquivo é carregado automaticamente quando o aplicativo é iniciado. Se o arquivo não existir, um novo banco de dados é criado com quatro tabelas: músicas, artistas, álbuns e playlists.

Cada tabela tem campos específicos para armazenar informações relevantes. Quando um usuário adiciona uma nova música ou cria uma playlist, as informações são armazenadas na tabela correspondente no banco de dados.

## Para rodar o aplicativo

No terminal do diretório em que os arquivos estão localizados rode 'py app.py'.