import pyautogui
import pyperclip
import time

import pandas as pd

# Abrir o menu Iniciar
pyautogui.press('win')

# Digitar "calculadora" e pressionar Enter para abrir a Calculadora do Windows
pyautogui.write('calculadora')
pyautogui.press('enter')

# Aguardar a Calculadora abrir
time.sleep(5)

# Carregar o arquivo Excel em um DataFrame
excel_file = "files/values.xlsx"  # Substitua pelo caminho do seu arquivo Excel
df = pd.read_excel(excel_file)

# Filtrar valores com base nas colunas A e B
filtro_a_b = df[(df['A'].notnull()) & (df['B'].notnull())]

# Criar uma lista para armazenar os resultados filtrados
resultados_calc = []

# Processar os valores de ambas as colunas A e B
for index, row in filtro_a_b.iterrows():
    valor_a = int(row['A'])
    valor_b = int(row['B'])

    # Fazer alguma operação com valor_a e valor_b
    print("Processando valores de A:", valor_a)
    print("Processando valores de B:", valor_b)

    # Clicar nos botões para a conta
    pyautogui.write(str(valor_a))
    pyautogui.click(x=1249, y=641)  # Clicar no botão "x"
    pyautogui.write(str(valor_b))
    pyautogui.click(x=1246, y=846)  # Clicar no botão "="

    # Aguardar um pouco para a operação ser realizada
    time.sleep(1)

    # Selecionar o resultado e copiar para a área de transferência
    pyautogui.hotkey('ctrl', 'a')  # Selecionar tudo
    pyautogui.hotkey('ctrl', 'c')  # Copiar

    # Obter o resultado da área de transferência usando pyperclip
    result_text = pyperclip.paste()  # Use pyperclip para acessar a área de transferência
    print("Resultado:", result_text)
    print("-----------------------------------")

    # Adicionar o resultado à lista
    resultados_calc.append(str(result_text))


# Escrever os valores filtrados num arquivo de texto
nome_arquivo = "resultados_calc.txt"
with open(f"files/{nome_arquivo}", 'w') as arquivo:
    for valor in resultados_calc:
        arquivo.write(valor + '\n')

# Fechar a Calculadora
pyautogui.hotkey('alt', 'f4')
