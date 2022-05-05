import conexao

while(True):
    print('=-=-=-=-=-=-=-ESTOQUE-=-=-=-=-=-=-')
    print('|          1-ADICIONAR           |')
    print('|          2-PESQUISAR           |')
    print('|          3-ALTERAR             |')
    print('|          4-APAGAR              |')
    print('=-'*17)
    escolha = int(input("QUAL OPERAÇÃO DESEJA FAZER?"))
    if escolha==1:#adicionar ou create
        id =      input("| ID DO PRODUTO")
        nome =    input("| NOME DO PRODUTO")
        valor   = input("| VALOR:")
        unidade = input('| UNIDADE:')
        conexao.create(id,nome,valor,unidade)
    elif escolha==2:
        print('para pesquisar o preço você deve passar o nome[1] ou id[2]')
        escolha= int(input('[1]ID\n [2]nome'))
        if escolha == 1:
            escolha= input('DIGITE O ID: ')
        elif escolha == 2:
            escolha= input('DIGITE O NOME: ')
        conexao.read(escolha)
    elif escolha == 3:
        print('oque vc deseja alterar?')
        escolha= int(input('[1]ID\n[2]NOME\n[3]VALOR\n[4]UNIDADE'))
        if escolha == 1:
            escolha= input('DIGITE O ID ATUAL:')
            alterar= input('DIGITE O ID NOVO:')
            conexao.update(escolha,alterar)
        elif escolha == 2:
            escolha= input('DIGITE O ID DO PRODUTO:')
            alterar= input('DIGITE O NOME NOVO: ')
            conexao.update(escolha,alterar)
        if escolha == 3:
            escolha= input('DIGITE O ID DO PRODUTO:')
            alterar= input('DIGITE O VALOR NOVO: ')
            conexao.update(escolha,alterar)
        elif escolha == 4:
            escolha= input('DIGITE O ID DO PRODUTO:')
            alterar= input('DIGITE A NOVA UNIDADE: ')
            conexao.update(escolha,alterar)
    elif escolha == 4:
        escolha = input('DIGITE O ID DO PRODUTO')
        conexao.update()
