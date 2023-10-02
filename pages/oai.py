"""OpenAI API connector."""

# Import from standard library
import os
import logging

# Import from 3rd party libraries
import openai

import os

# Suppress openai request/response logging
# Handle by manually changing the respective APIRequestor methods in the openai package
# Does not work hosted on Streamlit since all packages are re-installed by Poetry
# Alternatively (affects all messages from this logger):
logging.getLogger("openai").setLevel(logging.WARNING)

prompts = {
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
        - Apresenta-se o enunciado da questão
        - Apresenta-se uma frase que deve conter no mínimo 1 e no máximo até 3 lacunas representadas por ___
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


class Openai:
    """OpenAI Connector."""

    @staticmethod
    def build_prompt(
        nivel: str,
        objetivo: str,
        tipo: str,
        area: str,
        tem_introducao: str,
        tem_resposta: str,
    ):
        if tipo in [
            "Escolha Simples",
            "Escolha Múltipla",
            "Dissertativa",
            "Completar as Lacunas",
            "Lógica - O que Faz",
            "Lógica - Qual o Resultado",
            "Lógica - Qual o Erro",
        ]:
            base_prompt = prompts[tipo].format(
                nivel, objetivo, tipo, area, tem_introducao, tem_resposta
            )
        else:
            base_prompt = f"""Você é um especialista em Ciência de Dados.
        Elabore uma questão de nível {nivel} sobre a ementa descrita abaixo:
        Ementa: {objetivo}
        A questão deve ser do tipo: {tipo}
        A questão aborda a área: {area}
        A questão deve ser estruturada da seguinte forma:"""

            if tem_introducao == "Sim":
                base_prompt = (
                    base_prompt + """\n- Apresenta-se uma introdução ao conteúdo"""
                )

            if tipo == "Código SQL":
                base_prompt = (
                    base_prompt
                    + """\n- Apresenta-se o enunciado da questão seguindo o formato:
            - Gera-se uma tabela de dados ficticios
            - Imprime-se a tabela de dados
            - Faz-se uma pergunta que o aluno deve responder com uma instrução SQL"""
                )
            elif tipo == "Código Python":
                base_prompt = (
                    base_prompt
                    + """\n- Apresenta-se o enunciado da questão seguindo o formato:
            - Gera-se uma tabela de dados ficticios
            - Mostra-se a tabela de dados
            - Faz-se uma pergunta que o aluno deve responder com um script Python que pode utilizar as bibliotecas pandas, matplotlib, requests e todas as biliotecas nativas do python"""
                )
            else:
                base_prompt = (
                    base_prompt + """\n- Apresenta-se o enunciado da questão"""
                )

            if tem_resposta == "Sim":
                base_prompt = (
                    base_prompt
                    + """\n- Apresenta-se a resposta correta, e explique a resposta."""
                )

        return base_prompt

    @staticmethod
    def set_key(key: str):
        openai.api_key = key

    @staticmethod
    def moderate(prompt: str) -> bool:
        """Call OpenAI GPT Moderation with text prompt.
        Args:
            prompt: text prompt
        Return: boolean if flagged
        """
        try:
            response = openai.Moderation.create(prompt)
            return response["results"][0]["flagged"]
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")

    @staticmethod
    def complete(prompt: str, temperature: float = 0.9, max_tokens: int = 2048) -> str:
        """Call OpenAI GPT Completion with text prompt.
        Args:
            prompt: text prompt
        Return: predicted response text
        """
        kwargs = {
            "model": "gpt-3.5-turbo-16k",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": 1,  # default
            "frequency_penalty": 0,  # default,
            "presence_penalty": 0,  # default
        }
        try:
            response = openai.ChatCompletion.create(**kwargs)

            lst_resp = [x["message"]["content"] for x in response["choices"]]
            return "\n".join(lst_resp)

        except Exception as e:
            logging.error(f"OpenAI API error: {e}")

    @staticmethod
    def image(prompt: str) -> str:
        """Call OpenAI Image Create with text prompt.
        Args:
            prompt: text prompt
        Return: image url
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512",
                response_format="url",
            )
            return response["data"][0]["url"]

        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
