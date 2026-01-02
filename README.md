# Tendências emocionais na música ao longo dos anos
Análise temporal da valência emocional de músicas no catálogo do Spotify até 2023

## Descrição
A música popular reflete tendências culturais e emocionais de diferentes períodos. Com a popularização das plataformas de streaming, tornou-se possível analisar características musicais em larga escala.

Este projeto tem como objetivo avaliar, por meio da métrica de valência (valence) do Spotify, quão positivas ou negativas são as emoções transmitidas pelas músicas ao longo do tempo.

### Escopo
Embora o dataset contenha outras características musicais, como energia e dançabilidade, este projeto se concentrou exclusivamente na valência por ser a métrica mais diretamente associada à pergunta de estudo.

## Dados
### Fonte de Dados
Foram utilizados como referência os dados do [Spotify Dataset 2023](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023), disponível no Kaggle.

## Conteúdo da análise
A análise dos dados foi realizada em um Jupyter Notebook, `analise.ipynb`, para permitir o seguimento de um pipeline de análise:
* **Etapa 1**: Importação dos dados para um dataframe
* **Etapa 2**: Limpeza e tratamento de dados
* **Etapa 3**: Cálculo das métricas
* **Etapa 4**: Apresentação dos resultados obtidos

## Arquivos Disponibilizados
```
analise.ipynb       # Análise dos dados
create_view.sql     # Script em SQL para criação da view `visao_geral`
upload.py           # Script em Python para importação de dados para o banco
README.md           # Documentação
```

## Requerimentos
* SQLite
* Python 3.11+
  * Bibliotecas padrão:
    * sqlite3
  * Bibliotecas adicionais:
    * matplotlib
    * pandas

## Limitações
* Esta análise utiliza apenas os dados do Spotify, não considerando a popularidade em outras plataformas de streaming e meios analógicos.
* A métrica de valência é uma abstração computacional e não representa, de forma absoluta, a interpretação emocional subjetiva de uma música.

## Conclusões obtidas
Os resultados indicam que a distribuição da valência ao longo do catálogo analisado é relativamente equilibrada, porém com uma leve concentração de músicas abaixo do ponto médio (0,5), sugerindo predominância de emoções mais neutras ou negativas.

A análise temporal da valência média mostrou que não há uma tendência clara de aumento do “humor positivo” das músicas ao longo dos anos. Pelo contrário, observa-se uma estabilização — e, em alguns períodos, um leve declínio — da valência média, o que reforça a percepção de que músicas altamente positivas deixaram de ser dominantes ao longo do tempo. A proximidade entre média e mediana ao longo das análises indica que esse comportamento não é causado por poucos outliers extremos, mas sim por uma mudança mais ampla na distribuição das faixas.

Além disso, a análise da relação entre popularidade e valência revelou uma correlação praticamente nula, sugerindo que o sucesso de uma música não está diretamente associado ao seu conteúdo emocional positivo ou negativo. Isso indica que outros fatores, como contexto cultural, identidade artística, estratégias de divulgação e dinâmicas das plataformas de streaming, exercem um papel mais relevante na popularidade das faixas.

Em conjunto, os resultados sugerem que a música popular contemporânea não necessariamente se tornou mais “triste”, mas sim menos centrada em emoções explicitamente positivas. Essa mudança pode refletir transformações culturais mais amplas na forma como emoções são expressas e consumidas na música ao longo do tempo.

Ver também: [Dashboard](https://lookerstudio.google.com/reporting/f2d49bb0-be1e-484a-b0f5-e4fab514ee95)

## Créditos
Este projeto foi realizado como parte do curso de Análise de Dados da [EBAC - Escola Britânica de Artes Criativas e Tecnologia](https://ebaconline.com.br/analista-de-dados).

## Contato
* **Email:** giulianamendonca@outlook.com
* **GitHub:** [giulianamendonca](https://github.com/giulianamendonca)
