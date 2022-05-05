import conexao

while(True):
    print('=-=-=-=-=-=-=-ESTOQUE-=-=-=-=-=-=-')
    print('|          1-ADICIONAR           |')
    print('|          2-PESQUISAR           |')
    print('|          3-ALTERAR             |')
    print('|          4-APAGAR              |')
    print('=-'*17)
    escolha = int(input("QUAL OPERAÇÃO DESEJA FAZER?"))
    if escolha==1:
        