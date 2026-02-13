def exercicio_1():
    """Oi, Tudo bem?"""
    print("Oi, Tudo bem?")

def exercicio_2():
    """Estou com fome!"""
    print("Estou com fome!")

def exercicio_3():
    """Uma imagem de Cachorro"""
    print("Uma imagem de Cachorro")
    print("  0_____")
    print("   || ||  ")

def exercicio_4():
    """Meu Animal Favorito e onde moro"""
    print("Meu Animal Favorito é a ovelha")
    print("  o-###-")
    print("    | |   #")
    print("")
    print("Eu moro em São Paulo")
    print(" ")
    print("   _|_")
    print("  |   |")
    print("  |#  |_____")
    print("  |   |     |")
    print("  |  #|   # |")
    print("  |   | #   |")

def exercicio_5():
    """Olá repetido 5 vezes"""
    print("Olá, " * 5)

def exercicio_6():
    """Concatenação de strings"""
    print("Olá, " + "Tudo bem?")

def exercicio_7():
    """Repetições e concatenações"""
    print("ha " * 3)
    print("ba" + "na"*2)
    print("Bra" + "sil" + "!"*10)

def exercicio_8():
    """Jeito fácil e difícil"""
    print("O Jeito facil...")
    print("##############################")
    print("##############################")
    print("##############################")
    print("")
    print("O Jeito difícil...")
    print("#" * 30)
    print("#" * 30)
    print("#" * 30)

def exercicio_9():
    r"""Padrão com /\ e \/"""
    print(r"/\  "*10)
    print(r"  \/"*10)

def exercicio_10():
    """Parabéns com dinossauro e bolo"""
    print("Parabéns!!!!!!!!!!!")
    print("")
    print("Aqui vai um dinossauro!")
    print()
    print("             __")
    print("            / _)")
    print("     .-^^^-/ /")
    print("  __/       /")
    print(" <__.|_|-|_|")
    print("")
    print("E aqui vai um bolo! hummmmmmmm")
    print("")
    print(" i"*10)
    print("#" * 21)
    print("=" * 21)
    print("#" * 21)
    print("=" * 21)
    print("#" * 21)

def exercicio_11():
    """Mistura de poções do mago"""
    print("Dev. Valdeney Sousa Amaral")
    print("Turma 186")
    print()
    print("01. Um mago precisa misturar duas substâncias para criar uma poção.")
    print("Peça ao usuário os dois volumes (em ml) e exiba o total da poção")
    print()
    p1 = float(input('Primeira poção em ml: '))
    p2 = float(input('Segunda poção em ml: '))
    print(f'Soma das misturas em ml das poções: {p1 + p2} ml')

def exibir_menu():
    """Exibe o menu de opções"""
    print("\n" + "="*50)
    print("MENU DE EXERCÍCIOS ASCII - IFPI - Prof. Ritomar")
    print("="*50)
    print("1  - Exercício 1: Saudação")
    print("2  - Exercício 2: Estou com fome")
    print("3  - Exercício 3: Imagem de Cachorro")
    print("4  - Exercício 4: Animal Favorito e Cidade")
    print("5  - Exercício 5: Olá repetido")
    print("6  - Exercício 6: Concatenação de strings")
    print("7  - Exercício 7: Repetições e concatenações")
    print("8  - Exercício 8: Jeito fácil e difícil")
    print(r"9  - Exercício 9: Padrão /\ e \/")
    print("10 - Exercício 10: Parabéns com dinossauro e bolo")
    print("11 - Exercício 11: Mistura de Poções")
    print("0  - Sair")
    print("="*50)

def main():
    """Função principal com o menu"""
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (0-11): ")
        
        print("\n" + "-"*50)
        
        match opcao:
            case "1":
                exercicio_1()
            case "2":
                exercicio_2()
            case "3":
                exercicio_3()
            case "4":
                exercicio_4()
            case "5":
                exercicio_5()
            case "6":
                exercicio_6()
            case "7":
                exercicio_7()
            case "8":
                exercicio_8()
            case "9":
                exercicio_9()
            case "10":
                exercicio_10()
            case "11":
                exercicio_11()
            case "0":
                print("Encerrando o programa. Até logo!")
                break
            case _:
                print("Opção inválida! Por favor, escolha um número de 0 a 11.")
        
        print("-"*50)
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
