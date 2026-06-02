from datetime import datetime
import re

linhas_processadas = "linha_processada"
nulos_corrigidos = "nulos_corrigidos"
pedidos_cancelados = "pedidos_cancelados"

sumario = {linhas_processadas: 0, nulos_corrigidos: 0, pedidos_cancelados: 0}

def validar_dado(row):
     global nulos_corrigidos
     # Verificamos se o campo está vazio e preenchemos com um valor padrão
     if row["product_category_name"] == "":
        row["product_category_name"] = "Sem categoria"  
        sumario[nulos_corrigidos] += 1     

     if row["product_height_cm"] == "" or row["product_width_cm"] == "" or row["product_weight_g"] == "" or row["product_length_cm"] == "":
        row = row | {"product_height_cm": "0", "product_width_cm": "0", "product_weight_g": "0", "product_length_cm": "0"}  # Preenche os campos vazios com "0"
        sumario[nulos_corrigidos] += 1    


def padronizar_dado(row):
    # Padronizamos os dados, convertendo para minúsculas e removendo espaços extras
    row["product_category_name"] = row["product_category_name"].strip().lower()
    row["product_height_cm"] = row["product_height_cm"].strip()
    row["product_width_cm"] = row["product_width_cm"].strip()
    row["product_weight_g"] = row["product_weight_g"].strip()
    row["product_length_cm"] = row["product_length_cm"].strip()
    row["product_category_name"] = re.sub(r'[^\w\s]', '', row["product_category_name"]) # Remove caracteres especiais


pedidos_incorretos = []
correta = "correta"
incorreta = "incorreta"
hipoteses = {correta: 0, incorreta: 0}

def validar_order(row):
    # Verificamos se a data está vazia
    if row["order_delivered_customer_date"] == "":
      pedidos_incorretos.append(row)

      if row["order_status"] == "canceled":
        hipoteses[correta] += 1
      else:
        hipoteses[incorreta] += 1

    if row["order_status"] == "canceled":
        sumario[pedidos_cancelados] += 1


def formatar_date(row):
    if row["order_approved_at"] != "":
      data = datetime.strptime(row["order_approved_at"], "%Y-%m-%d %H:%M:%S") # Converte a string para um objeto datetime
      row["order_approved_at"] = data.strftime("%d/%m/%Y") # Formata a data para o formato desejado
   

