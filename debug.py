arquivo = open("clientes.txt", "r")
clientes = []
for linha in arquivo:
    clientes.append(linha.strip('\n'))
arquivo.close()
opção = 0
while opção != 5:
  print("Cadastro de Clientes - ADS")
  print("1 - Listar Clientes")
  print("2 - Inserir Cliente")
  print("3 - Remover Cliente")
  print("4 - Alterar Cliente")
  print("5 - Sair")
  opção = int(input("Digite a opção desejada: "))
  if(opção==1):
    print("Clientes: ")
    for cliente in clientes:
      print(cliente)
  elif(opção==2):
    novoCliente = input("Digite o nome do novo cliente: ")
    clientes.append(novoCliente)
  elif(opção==3):
    cliente = input("Digite o nome do cliente a ser removido: ")
    if(cliente in clientes):
      clientes.remove(cliente)
    else:
      print("Cliente não encontrado")
  elif(opção==4):
    cliente = input("Digite o nome do cliente a ser alterado: ")
    if(cliente in clientes):
      novoNome = input("Digite o novo nome: ")
      indice = clientes.index(cliente)
      clientes[indice] = novoNome
    else:
      print("Cliente não encontrado")
  elif(opção==5):
    print("Saindo...")
  else:
    print("Opção Inválida")
arquivo = open("clientes.txt", "w")
for cliente in clientes:
  print(cliente)
  arquivo.write(cliente + "\n")