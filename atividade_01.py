def calcular_salario_final(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    """
    Calcula o salário final de um vendedor, considerando salário fixo, comissão por carro,
    total de vendas e quantidade de carros vendidos.

    Args:
        salario_fixo (float): Valor fixo do salário do vendedor.
        comissao_por_carro (float): Valor da comissão por cada carro vendido.
        total_vendas (float): Valor total das vendas realizadas.
        carros_vendidos (int): Quantidade de carros vendidos.

    Returns:
        float: Salário final do vendedor, incluindo comissões e bônus.
    """

    # Inicializa o salário final com o valor fixo
    salario_final = salario_fixo

    # Calcula a comissão total por carros vendidos e adiciona ao salário
    comissao_carros = comissao_por_carro * carros_vendidos
    salario_final += comissao_carros

    # Adiciona bônus de 5% sobre o total de vendas, se houver vendas
    if total_vendas > 0:
        bonus_vendas = 0.05 * total_vendas
        salario_final += bonus_vendas

    # Adiciona bônus adicional de 10% sobre o total de vendas, se mais de 10 carros forem vendidos
    if carros_vendidos > 10:
        bonus_adicional = 0.10 * total_vendas
        salario_final += bonus_adicional

    return salario_final

# Exemplo de uso da função
salario_fixo = 2000
comissao_por_carro = 150
total_vendas = 50000
carros_vendidos = 12

salario_final = calcular_salario_final(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
print(f"Salário final: R${salario_final:.2f}")
