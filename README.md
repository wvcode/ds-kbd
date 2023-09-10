# Gerador de Questões para Hackathon

Este código é um script Python que cria uma interface gráfica do usuário (GUI) para gerar questões para um hackathon.

## Propósito

O propósito deste código é fornecer uma maneira fácil e intuitiva para os usuários gerarem questões para um hackathon. A GUI permite que o usuário insira o tipo de questão, o prompt da questão e o conteúdo que a questão deve abordar. Ao clicar no botão "Enviar Solicitação", a função send_hi é chamada, que por sua vez chama a função generate_text, passando o estado atual da GUI.

## Bibliotecas Utilizadas

O código utiliza as seguintes bibliotecas:

- taipy.gui: Esta biblioteca é utilizada para criar a GUI do aplicativo. Ela fornece a classe Gui que facilita a criação de elementos gráficos como botões e campos de texto.

- openai: Esta biblioteca é utilizada para realizar verificações de problemas no texto gerado pelo usuário. Ela oferece recursos de IA para identificar possíveis problemas como viés, linguagem ofensiva, entre outros.

## Como Instalar as Bibliotecas

Para instalar as bibliotecas utilizadas, siga os passos abaixo:

- Certifique-se de ter o Python instalado em sua máquina. Caso ainda não o tenha, faça o download e instale a versão mais recente do Python em https://www.python.org/downloads/

- Abra o terminal ou prompt de comando.

- Instale a biblioteca taipy utilizando o comando:
```
pip install taipy
```

- Em seguida, instale a biblioteca openai utilizando o comando:
```
pip install openai
```
## Outros Recursos Necessários

Além das bibliotecas mencionadas acima, não há outros recursos necessários para executar este código.

Para executar o código, basta abrir o arquivo Python em um editor de texto ou ambiente de desenvolvimento Python, e executar o script.

```python
python main.py
```

Isso iniciará a aplicação GUI e a executará na porta 8080.

# Considerações Finais

Este código oferece uma solução prática e eficiente para a geração de questões para um hackathon. A interface gráfica simplifica o processo de criação das questões, enquanto a verificação do texto garante que as questões geradas estejam de acordo com as diretrizes e normas relevantes.
