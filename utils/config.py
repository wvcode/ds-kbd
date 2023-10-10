QST_TIPOS = [
    "Escolha Simples",
    "Escolha Múltipla",
    "Dissertativa",
    "Completar as Lacunas",
    "Código SQL",
    "Código Python",
    "Lógica - O que Faz",
    "Lógica - Qual o Resultado",
    "Lógica - Qual o Erro",
]
QST_NIVEIS = ["Fácil", "Médio", "Complexo"]

QST_AREAS = [
    "Gestão de Dados",
    "Transformação Digital",
    "Lógica e Linguagens de Programaçao",
    "Armazenamento, Manipulação e Transformação de Dados",
]

PROMPTS = {
    "Escolha Simples": """Você é um especialista em Ciência de Dados.
        Elabore uma questão de nível {0} sobre a ementa descrita abaixo:
        Ementa: {1}
        A questão deve ser do tipo: {2}
        A questão aborda a área: {3}
        A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - Apresenta-se o enunciado da questão
        - Apresentam-se 5 alternativas de resposta
          - Regras:
            - Apenas uma alternativa pode ser correta.
            - Todas as outras alternativas devem ser incorretas.
        - Apresenta-se qual alternativa é a correta. 
        - Deve-se elaborar uma explicação para o motivo: {5}
        - Deve-se entregar a justificativa de porque as outras alternativas são incorretas: {5}""",
    "Escolha Múltipla": """Você é um especialista em Ciência de Dados.
        Elabore uma questão de nível {0} sobre a ementa descrita abaixo:
        Ementa: {1}
        A questão deve ser do tipo: {2}
        A questão aborda a área: {3}
        A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - Apresenta-se o enunciado da questão
        - Apresentam-se 5 alternativas de resposta
          - Regras:
            - No mínimo 2 alternativas podem ser corretas.
            - No máximo 3 alternativas podem ser corretas.
            - Todas as outras alternativas devem ser incorretas.
        - Apresenta-se qual alternativas são as corretas. 
        - Deve-se elaborar uma explicação para o motivo de cada alternativa ser correta: {5}
        - Deve-se entregar a justificativa de porque as outras alternativas são incorretas: {5}""",
    "Dissertativa": """Você é um especialista em Ciência de Dados.
        Elabore uma questão de nível {0} sobre a ementa descrita abaixo:
        Ementa: {1}
        A questão deve ser do tipo: {2}
        A questão aborda a área: {3}
        A questão deve ser estruturada da seguinte forma:
          - Apresenta-se uma introdução ao conteúdo: {4}
          - Apresenta-se o enunciado da questão
          - Apresenta-se a resposta correta
          - Explique a resposta: {5}""",
    "Completar as Lacunas": """Você é um especialista em Ciência de Dados.
      Elabore uma questão de nível {0} sobre a ementa descrita abaixo:
      Ementa: {1}
      A questão deve ser do tipo: {2}
      A questão aborda a área: {3}
      A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - Apresenta-se o enunciado da questão, que deve conter no mínimo 1 e no máximo até 3 lacunas representadas por ___
        - Apresentam-se 5 alternativas de resposta:
          - Regras:
            - Cada alternativa contem os termos para completar as lacunas
        - Apresenta-se qual alternativa é a correta. Deve-se elaborar uma explicação para o motivo: {5}
        - Também deve ser entregue a justificativa de porque as outras alternativas são incorretas: {5}""",
    "Lógica - O que Faz": """Você é um especialista em Ciência de Dados.
      Elabore uma questão de nível {0} sobre o tema descrito abaixo:
      Tema: {1}
      A questão deve ser do tipo: {2}
      A questão aborda a área: {3}
      A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - A questão é estruturada da seguinte forma:
          - Apresenta-se um código em Python relacionado ao tema. Deve ser um pequeno script de pelo menos 5 linhas  e no máximo 15 linhas.
          - Pergunta-se o que este código faz:
        - Apresenta-se a resposta correta: {5}
        - Explique a resposta: {5}""",
    "Lógica - Qual o Resultado": """Você é um especialista em Ciência de Dados.
      Elabore uma questão de nível {0} sobre o tema descrito abaixo:
      Tema: {1}
      A questão deve ser do tipo: {2}
      A questão aborda a área: {3}
      A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - A questão é estruturada da seguinte forma:
          - Apresenta-se um código em Python relacionado ao tema. Deve ser um pequeno script de pelo menos 5 linhas  e no máximo 15 linhas.
          - Apresenta-se valores que devem ser usados como entrada no código
          - Pergunta-se qual o resultado que o código gerará com os valores fornecidos
        - Apresenta-se a resposta correta: {5}
        - Explique a resposta: {5}""",
    "Lógica - Qual o Erro": """Você é um especialista em Ciência de Dados.
      Elabore uma questão de nível {0} sobre a ementa descrita abaixo:
      Ementa: {1}
      A questão deve ser do tipo: {2}
      A questão aborda a área: {3}
      A questão deve ser estruturada da seguinte forma:
        - Apresenta-se uma introdução ao conteúdo: {4}
        - O enunciado da questão é estruturado da seguinte forma:
          - Apresenta-se um código em Python que executa alguma operação relacionada ao conteudo mencionado na ementa e que contém um erro.
          - Explica-se qual o resultado esperado quando o código é executado
          - Pergunta-se qual o erro que o código possui:
        - Apresenta-se a resposta correta: {5}
        - Explique a resposta: {5}""",
}
