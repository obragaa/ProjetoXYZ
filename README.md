# Projeto XYZ
```markdown
# Automatização de Cálculos - Projeto XYZ

Este projeto automatiza o processo de filtragem, multiplicação e armazenamento de valores a partir de um arquivo Excel, utilizando a calculadora do Windows.
```
```markdown
## Estrutura do Projeto

├── files
│ ├── resultados_calc.txt
│ └── value.xlsx
├── src
│ └── cord.py
├── main.py
├── README.md
└── requirements.txt
```
```

## Descrição dos Diretórios e Arquivos

- `files/`: Pasta que contém arquivos de saída.
  - `resultados_calc.txt`: Arquivo que armazena os resultados calculados.
  - `value.xlsx`: Arquivo Excel que contém a base de valores para a automação.
- `src/`: Pasta que contém os arquivos de auxílio do projeto.
  - `cord.py`: Arquivo que contém o código auxiliar para obter coordenadas de cliques na calculadora do Windows.
- `main.py`: Arquivo principal do projeto que inicia a automação.
- `README.md`: Este arquivo, fornecendo informações detalhadas sobre o projeto.
- `requirements.txt`: Arquivo que lista as dependências do projeto.

## Uso do cord.py

O arquivo `cord.py` é uma ferramenta auxiliar que exibe as coordenadas X e Y do ponteiro do mouse na sua tela. Isso pode ser útil para ajustar as coordenadas de cliques na calculadora do Windows, de acordo com a sua tela.

Execute o arquivo `cord.py` para ver as coordenadas do ponteiro do mouse:

```bash
python src/cord.py
```

## Funcionamento

1. Certifique-se de ter o arquivo `value.xlsx` na pasta `files/`.

2. Execute o arquivo `main.py` para iniciar a automação:

   ```bash
   python main.py
   ```

3. O programa irá usar a biblioteca Pandas para filtrar os valores do arquivo `value.xlsx`, tratando todos os valores como inteiros. Caso necessário, o código pode ser adaptado para necessidades específicas.

## Instalação e Uso

1. Clone o repositório:

   ```bash
   git clone https://github.com/obragaa/ProjetoXYZ
   cd ProjetoXYZ
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o arquivo `cord.py` para verificar as coordenadas de cliques (opcional).

4. Execute o arquivo `main.py` para iniciar a automação.

5. Após a execução, os resultados serão armazenados em `files/resultados_calc.txt`.

## Personalização

- **Cálculos Personalizados**: Modifique o código em `main.py` para executar cálculos específicos de acordo com suas necessidades.

## Biblioteca Pandas

Este projeto utiliza a biblioteca Pandas para a manipulação e análise dos dados do arquivo Excel. O Pandas é uma biblioteca poderosa em Python que oferece estruturas de dados flexíveis e eficientes para trabalhar com dados tabulares.

## Dúvidas e Suporte

Para qualquer dúvida ou suporte, sinta-se à vontade para entrar em contato comigo [contato.felipebragaduarte@gmail.com].

```
