# Anomaly-detection-in-public-procurements
Detecção de anomalias em licitações públicas utilizando pseudo-label e algoritmos de classificação com aprendizado de máquina.

- pip install openpyxl
- pip install pandas
- pip install seaborn

============================================================

Identificação da licitação

Município — cidade onde a licitação/contratação ocorreu (ex.: Ribeirão Preto, Taubaté, Andradina).
Entidade — órgão/fundação responsável pela contratação (ex.: FAEPA, prefeituras, fundações de apoio a universidades/hospitais).
Código da Licitação — identificador único do processo licitatório no sistema de origem.
Modalidade de licitação — o tipo de procedimento usado para contratar (Pregão Eletrônico, Dispensa, Inexigibilidade, regulamentos internos da FAEPA, etc.). Define as regras jurídicas seguidas.
Número do edital — número oficial do edital publicado.
Data do edital — data de publicação/abertura do processo. É a coluna que usamos para a série temporal.

O que está sendo comprado

Objeto — descrição geral do que a licitação pretende contratar (ex.: "aquisição de materiais de escritório").
Descrição do objeto contratado — detalhamento mais específico do objeto.
Produto (item) — o item individual dentro do objeto (cada linha da planilha normalmente representa um item, não a licitação inteira).
Quantidade do objeto contratado (item) — quantas unidades daquele item foram efetivamente contratadas.
Unidade do objeto contratado — unidade de medida do item contratado (kg, unidade, caixa...). Observação: no seu arquivo, essa coluna veio 100% vazia.

Valores de referência (orçamento estimado pela administração)

Valor unitário orçamento estimativo lote — preço unitário de referência quando os itens são agrupados em lote.
Quantidade orçamento estimativo lote — quantidade estimada para aquele lote.
Unidade de medida orçamento estimativo lote — unidade de medida correspondente ao lote.
Valor unitário orçamento estimativo item — preço unitário de referência por item individual (mais granular que o do lote).
Quantidade orçamento estimativo item — quantidade estimada por item.
Unidade de medida orçamento estimativo item — unidade de medida do item.

(Existem versões "lote" e "item" porque licitações às vezes agrupam vários produtos num lote só, e às vezes detalham item por item — sua base tem os dois níveis.)

O participante e o resultado

CNPJ do participante candidato — CNPJ da empresa que participou/concorreu.
Nome do participante candidato — razão social da empresa.
Resultado da Habilitação — se aquele participante foi Classificado, Desclassificado, Habilitado, Inabilitado, Desistiu, etc. Quase metade das linhas está vazia aqui — provável indício de que essas linhas são só orçamento estimativo, sem uma proposta de fornecedor associada ainda.
Valor da Proposta — valor que o participante efetivamente propôs para aquele item. Essa é a coluna com os outliers extremos que identificamos (valores de bilhões/trilhões que não fazem sentido).
