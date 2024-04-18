import csv
import json

def load_data(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers,delimiter=',')
        next(numbers_data)
        for row in numbers_data:
            mylist.append(row)
            return mylist
new_list = load_data('enelsp.csv')    
for row in new_list:
    print(row)   

def csv_para_json(nome_arquivo_csv, nome_arquivo_json):
   
    dados_json = []
    with open(nome_arquivo_csv, 'r', newline='', encoding='latin-1') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            dados_json.append(linha)

    with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)


nome_arquivo_csv = r'enelsp.csv'


nome_arquivo_json = 'enelsp.json'


csv_para_json(nome_arquivo_csv, nome_arquivo_json)

print("Conversão concluída!")






def extrair_e_exibir_dados(nome_arquivo_json):
    
    with open(nome_arquivo_json, 'r', encoding='latin-1') as arquivo_json:
        dados = json.load(arquivo_json)
    
    for registro in dados:
        print("Arquivo:", registro["Arquivo"])
        print("Tipo de Ligação:", registro["Tipo_ligacao"])
        print("UC:", registro["UC"])
        print("Data de Vencimento:", registro["Data_vencimento"])
        print("Total da Fatura:", registro["Total_fatura"])
        print("Medidor:", registro["Medidor"])
        print("código de barras:", registro["Boleto"])
        print("icms", (registro ['Aliquota_ICMS'].replace(',','')))
        print("conta contrato", registro ['Conta_contrato'])
        print("unidade", registro ['UC'])
        print("nota fiscal", registro ['Nota_fiscal'])
        print("fisco", registro ['Fisco_2'])
        print("Chave de acesso", registro ['Fisco_2'])
        print("Constante", registro ['Constante'])
        print("Leitura_atual", registro ['Leitura_atual'])
        print("Leitura_anterior", registro ['Leitura_anterior'])
        print("Consumo", registro ['Consumo'])
        print("total fatura", registro ['Total_fatura'])
        print("Consumo", registro ['Consumo'])
        print("CIP", registro ['CIP'])
        print("Aliquota_Pis", registro ['Aliquota_Pis'])
        print("Aliquota_cofins", registro ['Aliquota_Cofins'])
        

nome_arquivo_json = 'enelsp.json'


extrair_e_exibir_dados(nome_arquivo_json)
     