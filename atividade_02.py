def calcular_idades(h1, h2, m1, m2):
    """
    Calcula a soma e o produto das idades de um grupo de pessoas.

    Args:
        h1 (int): Idade do primeiro homem.
        h2 (int): Idade do segundo homem.
        m1 (int): Idade da primeira mulher.
        m2 (int): Idade da segunda mulher.

    Returns:
        tuple: Uma tupla contendo a soma das idades do homem mais velho com a mulher mais nova
               e o produto das idades do homem mais novo com a mulher mais velha.
               Caso haja algum erro na entrada, retorna uma string com a mensagem de erro.

    Raises:
        ValueError: Se alguma das idades fornecidas não for um número inteiro positivo.

    Exemplo:
        >>> calcular_idades(30, 25, 22, 35)
        (52, 825)

        >>> calcular_idades(30, -2, 22, 35)
        'Erro: Todas as idades devem ser números inteiros positivos.'
    """

    # Validação das idades
    if any(not isinstance(idade, int) or idade <= 0 for idade in (h1, h2, m1, m2)):
        return "Erro: Todas as idades devem ser números inteiros positivos."

    # Determina as idades extremas
    homem_mais_velho = max(h1, h2)
    homem_mais_novo = min(h1, h2)
    mulher_mais_velha = max(m1, m2)
    mulher_mais_nova = min(m1, m2)

    # Cálculos
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return soma, produto
