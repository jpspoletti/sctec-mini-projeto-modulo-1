# -*- coding: utf-8 -*-
import csv
from pathlib import Path
import sys
from funcoes import formatar_date, validar_dado, padronizar_dado, validar_order, hipoteses, correta, incorreta, sumario, pedidos_cancelados, linhas_processadas, nulos_corrigidos

# Configurações para garantir a codificação UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

app_dir = Path(__file__).parent
input_products = app_dir / "olist_products_dataset.csv"
input_orders = app_dir / "olist_orders_dataset.csv"
output_products = app_dir / "products_validated.csv"
output_orders = app_dir / "orders_validated.csv"


with open(input_products, "r", newline="") as csv_file:
    leitor = csv.DictReader(csv_file)
    writer = csv.DictWriter(open(output_products, "w", newline=""), fieldnames=leitor.fieldnames)
    writer.writeheader()

    for row in leitor:
        validar_dado(row)
        padronizar_dado(row)
        sumario[linhas_processadas] += 1
        writer.writerow(row)
        
        
with open(input_orders, "r", newline="") as csv_file:
    leitor = csv.DictReader(csv_file)
    writer = csv.DictWriter(open(output_orders, "w", newline=""), fieldnames=leitor.fieldnames)
    writer.writeheader()


    for row in leitor:
        validar_order(row) 
        formatar_date(row) 
        sumario[linhas_processadas] += 1
        writer.writerow(row)

   
print(f"Hipótese foi correta em: {hipoteses[correta]} e incorreta em: {hipoteses[incorreta]}")
print(f"Portanto a hipótese é {correta if hipoteses[correta] > hipoteses[incorreta] else incorreta}.")

print(f"Total de linhas processadas: {sumario[linhas_processadas]}")
print(f"Total de nulos corrigidos: {sumario[nulos_corrigidos]}")
print(f"Total de pedidos cancelados: {sumario[pedidos_cancelados]}")