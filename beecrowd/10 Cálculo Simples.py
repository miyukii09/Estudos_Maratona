codigo1, quantidade1, valor_unitario1 = input().split()
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
valor_unitario1 = float(valor_unitario1)

codigo2, quantidade2, valor_unitario2 = input().split()
codigo2 = int(codigo2)
quantidade2 = int(quantidade2)
valor_unitario2 = float(valor_unitario2)

total = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
