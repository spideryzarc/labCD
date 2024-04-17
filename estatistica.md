---
marp: true
theme: default
header: "Revisão de Python - Albert E. F. Muritiba"
# footer: "Laboratório de Ciência de Dados - Albert E. F. Muritiba"
title: "Estatística para Ciência de Dados"
paginate: true
---

# Estatística para Ciência de Dados

---

> **Estatística** é a ciência que se dedica à coleta, análise e interpretação de dados. Ela é uma ferramenta essencial para a tomada de decisões em diversas áreas do conhecimento.

---

- **Estatística Descritiva**
  - Descrever e resumir os dados
  - Tabelas, gráficos e medidas resumo
  - **Exemplo**: média, mediana, moda, variância, desvio padrão, etc.
- **Estatística Inferencial**
  - Inferir conclusões sobre uma população a partir de uma amostra
  - Testes de hipóteses, intervalos de confiança, regressão, etc.
  - **Exemplo**: teste t de Student, ANOVA, regressão linear, etc.
  
---

## Estatística Descritiva

### Medidas de Posição

- **Média**: Balanço entre todos os valores. Busca o valor central.
  - Aritmética: $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$
  - Geométrica: $\bar{g} = \sqrt[n]{\prod_{i=1}^{n} x_i}$
  - Harmônica: $\bar{h} = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}}$

---
```python
import numpy as np
x = np.random.randint(1, 100, 50)
```

```python
# Média Aritmética passo a passo
soma = 0
for i in x:
    soma += i
media = soma / len(x)
print(media)
```

```python
# Média Aritmética com numpy
media = np.mean(x)
```

---
  
```python
# Média Geométrica passo a passo
produto = 1
for i in x:
    produto *= i
media = produto ** (1/len(x))
print(media)
```

```python
# Média Geométrica com numpy
media = np.prod(x) ** (1/len(x))
```

---

```python
# Média Harmônica passo a passo
soma = 0
for i in x:
    soma += 1/i
media = len(x) / soma
print(media)
```

```python
# Média Harmônica com numpy
media = len(x) / np.sum(1/x)
```

---


Suponha que você tem mil reais investidos e a tabela abaixo mostra o retorno mês a mês. Qual é o retorno médio mensal?
-
---

|Mês|Ret. Absoluto|Ret. Relativo|
|---|--:|--:|
|**C.I.**|1000,00|1,0000|
|Janeiro|100,00|1,1000|
|Fevereiro|200,00|1,1818|
|Março|50,00|1,0385|
|Abril|-200,00|0,8519|
|Maio|-30,00|0,9739|
|Junho|100,00|1,0893|
|**Total**|**1220,00**|7,2353*|
|**Média**|**36,67**|1,0392*|

---

- Podemos afirmar que o retorno total foi de R$ 220,00 em 6 meses. O retorno médio foi de R$ 36,67 por mês.

- Mas quando olhamos para o retorno relativo, o total indicado é de 7,2353 , o que é absurdo, pois o valor não ficou 7 vezes maior.
  
- Enquanto a média relativa foi de 1,0392, o que indicaria que o valor ficou 3,92% maior a cada mês. Se isso fosse verdade, o valor final seria de R$ 1259,49.
  
- O que aconteceu? 
  - O total do rendimento relativo é a **multiplicação** dos rendimentos relativos de cada mês.
  - A média relativa é a média **geométrica** dos rendimentos relativos de cada mês.

---
|Mês|Ret. Absoluto|Ret. Relativo|
|---|--:|--:|
|**C.I.**|1000,00|1,0000|
|Janeiro|100,00|1,1000|
|fevereiro|200,00|1,1818|
|março|50,00|1,0385|
|abril|-200,00|0,8519|
|maio|-30,00|0,9739|
|junho|100,00|1,0893|
|**Total**|**1220,00**|1,220|
|**Média**|**36,67**|1,0337|
---

- Quando o total de uma variável é melhor representado pela **soma** dos valores, a média **aritmética** é a melhor escolha. 
- Quando o total é melhor representado pelo **produto** dos valores, a média **geométrica** é a melhor escolha.

E a **média harmônica?** 

---
Suponha que o piloto de corrida fez cinco voltas em um circuito de 10km. A tabela abaixo mostra o tempo e a velocidade média de cada volta. Qual é a velocidade média final do piloto?
-   
---

|Volta|Tempo (h)| Velocidade (km/h)|
|---|--:|--:|
|1	    |0,0455	|220    |
|2	    |0,0450	|222    |
|3	    |0,0500	|200    |
|4	    |0,0435	|230    |
|5	    |0,0495	|202    |
|**Total**	|0,2335	|1074*  |
|**Média**	|0,0467	|214,8* |

---

- Podemos afirmar que o piloto completou o circuito em 0,2335 horas. Cada volta foi feita em média em 0,0467 horas.
- Quando olhamos para a velocidade:
  - O total não faz sentido.
  - A média não corresponde à velocidade média do piloto. Pois, quando dividimos a distância total pela soma dos tempos, obtemos 214,1 km/h.
- Este é um caso em que a média harmônica é mais adequada.

---
$$
v = \frac{\Delta t}{\Delta v}
$$

$$
v = \frac{5 \times 10}{\frac{10}{220} + \frac{10}{222} + \frac{10}{200} + \frac{10}{230} + \frac{10}{202}} 
$$
-
$$
= \frac{5}{\frac{1}{220} + \frac{1}{222} + \frac{1}{200} + \frac{1}{230} + \frac{1}{202}} 
$$
-
$$
= 214,1 \text{ km/h}
$$


---

|Volta|Tempo (h)| Velocidade (km/h)|
|---|--:|--:|
|1	    |0,0455	|220    |
|2	    |0,0450	|222    |
|3	    |0,0500	|200    |
|4	    |0,0435	|230    |
|5	    |0,0495	|202    |
|**Total**	|0,2335	|--  |
|**Média**	|0,0467	|214,1 |

---

- **Mediana**: Valor central de um conjunto de dados ordenados.
  - Se $n$ é ímpar, a mediana é o valor central.
  - Se $n$ é par, a mediana é a média dos dois valores centrais.
```python
# Mediana com numpy
mediana = np.median(x)
```

- Em comparação com a média, a mediana é menos sensível a valores extremos.
- Mediana é mais representativa em distribuições assimétricas.
- Mediana é demanda mais tempo computacional para calcular.


---

- **Moda**: Valor mais frequente em um conjunto de dados.
```python
# Moda com numpy
values, freq = np.unique(x, return_counts=True)
moda = values[np.argmax(freq)]
``` 
  
```python
from scipy import stats
# Moda com scipy
moda = stats.mode(x)
```

> `scipy` é uma biblioteca de código aberto que fornece muitas ferramentas estatísticas e matemáticas.
---

Aplicações:
 - Conjuntos de dados com valores discretos
 - Conjuntos de dados categóricos
  
---

### Medidas de Dispersão

A média, mediana e moda são medidas de posição que descrevem o centro de um conjunto de dados. As medidas de dispersão descrevem a variabilidade dos dados.

Os gráficos abaixo mostram dois conjuntos de dados com a mesma média, mas com diferentes dispersões.

<!-- TODO: Adicionar gráficos -->

---

- **Amplitude**: Diferença entre o maior e o menor valor.
```python
# Amplitude com numpy
amplitude = np.ptp(x)
```
---


- **Variância**: Média dos quadrados das diferenças entre os valores e a média.
  - População: $\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$
  - Amostra: $s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$
```python
# Variância populacional com numpy
variancia = np.var(x, ddof=0)
# Amostra 10 valores de x sem reposição
sample = np.random.choice(x, 10,replace=False) 
# Variância amostral com numpy
variancia = np.var(sample, ddof=1)
```
> `ddof` é o grau de liberdade. Se `ddof=0`, a variância é calculada para a população. Se `ddof=1`, a variância é calculada para a amostra.
> 

---

A razão para usar $n-1$ em vez de $n$ é que a variância amostral é uma estimativa da variância populacional. A simulação abaixo investiga qual fórmula é mais precisa.

```python
import numpy as np
pop = np.random.randint(1, 10000, 1000)
v_pop = np.var(pop, ddof=0)
# Variâncias de 1000 amostras de 100 valores de pop
v_A = np.array([np.var(np.random.choice(pop, 100, replace=False), ddof=0) for _ in range(1000)])
v_B = np.array([np.var(np.random.choice(pop, 100, replace=False), ddof=1) for _ in range(1000)])
print('População:', v_pop)
print('Amostra (ddof=0):', np.mean(v_A))
print('Amostra (ddof=1):', np.mean(v_B))
# erro quadrático médio
print('EQM (ddof=0):', np.mean((v_A - v_pop)**2))
print('EQM (ddof=1):', np.mean((v_B - v_pop)**2))
```


---

- **Desvio Padrão**: Raiz quadrada da variância.
  - População: $\sigma = \sqrt{\sigma^2}$
  - Amostra: $s = \sqrt{s^2}$
```python
# Desvio padrão populacional com numpy
desvio_padrao = np.std(x, ddof=0)   
# Desvio padrão amostral com numpy
desvio_padrao = np.std(sample, ddof=1)
```

> Em média, quanto os valores se desviam da média. Os valores de desvio padrão são mais fáceis de interpretar do que os valores de variância, pois estão na mesma unidade dos dados.

---

- **Coeficiente de Variação**: Medida de dispersão relativa.
  - $CV = \frac{s}{\bar{x}} \times 100\%$
```python
cv = np.std(x, ddof=0) / np.mean(x) * 100
```

> Em média, quanto os valores se desviam **percentualmente** da média.
--- 


### Medidas de Forma

Dados podem ainda ser classificados de acordo com a forma da distribuição. As medidas de forma descrevem a forma da distribuição dos dados.

<!-- TODO: Adicionar gráficos -->

---

- **Assimetria**: Medida de desvio da simetria em relação à média.
```python
# Assimetria com scipy.stats
assimetria = stats.skew(x)  
```
> skew > 0: assimetria positiva; 
> skew < 0: assimetria negativa
> skew = 0: simetria

https://blog.proffernandamaciel.com.br/assimetria-e-curtose-dos-dados/

---

- **Curtose**: Medida de achatamento da distribuição.
  - Leptocúrtica: mais alta e fina
  - Mesocúrtica: normal
  - Platicúrtica: mais baixa e larga
```python
# Curtose com scipy.stats
curtose = stats.kurtosis(x)
```
>Curtose > 0: mais picos
>Curtose < 0: menos picos
>Curtose = 0: normal

<!-- TODO: Adicionar gráficos -->

---

### Medidas de Associação

Dados podem ser associados de várias maneiras. As medidas de associação descrevem a relação entre duas variáveis.

Sejam $x$ e $y$ duas variáveis aleatórias...
-

---

- **Covariância**: É a média dos produtos dos desvios de cada valor da média sua respectiva média.
  - População: $\sigma_{xy} = \frac{\sum_{i=1}^{n} (x_i - \mu_x)(y_i - \mu_y)}{n}$
  - Amostra: $s_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{n-1}$
```python
# Covariância com numpy
covariancia = np.cov(x, y, ddof=0)
``` 
> `ddof` é o grau de liberdade. Se `ddof=0`, a covariância é calculada para a população. Se `ddof=1`, a covariância é calculada para a amostra.

---

- **Covariância > 0:** associação positiva, ou seja, quando uma variável aumenta, a outra também aumenta.
- **Covariância < 0:** associação negativa, ou seja, quando uma variável aumenta, a outra diminui.
- **Covariância $\approx$ 0:** pouca ou nenhuma associação.

>Obs.: A covariância é uma medida de associação linear. Ela não é normalizada, o que dificulta a interpretação.

---

- **Correlação**: Medida de associação linear normalizada entre duas variáveis.
  - Coeficiente de correlação de Pearson: $r = \frac{s_{xy}}{s_x \times s_y}$, 
  - onde $s_x$ e $s_y$ são os desvios padrão de $x$ e $y$.
```python
# Correlação com numpy
r = np.corrcoef(x, y)
# Correlação de Pearson com scipy.stats
r, p = stats.pearsonr(x, y)
```

> `p` é o valor-p, que indica a probabilidade de obter uma correlação igual ou mais extrema, assumindo que a hipótese nula é verdadeira.
---

- Os valores da correlação variam de -1 a 1,
- o sinal indica a direção da associação,
- o módulo indica a força da associação.

|Módulo de r|Interpretação|
|---|---|
| $[0,9 - 1]$ |Correlação muito forte|
| $[0,7 - 0,9[$ |Correlação forte|
| $[0,5 - 0,7[$ |Correlação moderada|
| $[0,3 - 0,5[$ |Correlação fraca|
| $[0 - 0,3[$ |Correlação desprezível|
---


## Percentis e Quartis

- **Percentil**: Valor da variável maior que uma certa porcentagem dos dados.
```python
import numpy as np
x = np.array([15, 22, 35, 4, 85])
v = np.percentile(x, 32) 
print(v)
```
> `v` é o valor que é maior que 32% dos dados.

- **Quartil**: Valores de variáveis que dividem os dados em quatro partes iguais.
```python
import numpy as np
x = np.array([15, 22, 35, 4, 85])
q1, q2, q3 = np.percentile(x, [25, 50, 75])
```
> `q1`, `q2` e `q3` são os valores que dividem os dados em quatro partes iguais.

---

## Normalização de Dados

- **Padronização**: Transformação dos dados para ter média zero e desvio padrão um.
  - $z = \frac{x - \bar{x}}{s}$
```python
import numpy as np
x = np.array([15, 22, 35, 4, 85])
z = (x - np.mean(x)) / np.std(x)
```
- Padronização é útil para comparar variáveis com diferentes escalas.
- Padronização é útil para algoritmos de aprendizado de máquina sensíveis à escala.
- Padronização não remove outliers.

---

## Outliers

- **Outliers**: Valores extremos que se desviam significativamente do restante dos dados.
  - Critério de Tukey: $Q_1 - 1.5 \times IQR$ e $Q_3 + 1.5 \times IQR$
```python
import numpy as np
x = np.array([15, 22, 35, 4, 85])
q1, q3 = np.percentile(x, [25, 75])
iqr = q3 - q1
outliers = x[(x < q1 - 1.5*iqr) | (x > q3 + 1.5*iqr)]
```

---

- **Tratamento de Outliers**: 
  - Remoção: remover os outliers do conjunto de dados.
```python
import numpy as np
x = np.array([15, 22, 35, 4, 85])
q1, q3 = np.percentile(x, [25, 75])
iqr = q3 - q1
xa = x[(x >= q1 - 1.5*iqr) & (x <= q3 + 1.5*iqr)]
```
  - Substituição: substituir os outliers por valores mais próximos.
```python
xb = x.copy()
xb[(xb < q1 - 1.5*iqr)] = q1 - 1.5*iqr
xb[(xb > q3 + 1.5*iqr)] = q3 + 1.5*iqr
``` 
  - Ignorar: ignorar os outliers e continuar a análise.
  - Análise separada: analisar os outliers separadamente.

---
## Estatística Inferencial

- **Intervalo de Confiança**: Intervalo que contém o valor real do parâmetro com uma certa probabilidade.
  - Intervalo de confiança para a média: $\bar{x} \pm t_{\alpha/2} \times \frac{s}{\sqrt{n}}$
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
intervalo = stats.t.interval(0.95, len(x)-1, loc=np.mean(x), scale=stats.sem(x))
```

---

- **Teste de Hipóteses**: Teste estatístico para verificar se uma afirmação sobre uma população é verdadeira.
  - Hipótese nula: afirmação a ser testada.
  - Hipótese alternativa: afirmação oposta à hipótese nula.
  - Valor-p: probabilidade de obter um resultado igual ou mais extremo que o observado, assumindo que a hipótese nula é verdadeira.
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
t, p = stats.ttest_1samp(x, 0)
```

---

- **ANOVA**: Análise de variância para comparar médias de três ou mais amostras.
  - Hipótese nula: as médias são iguais.
  - Hipótese alternativa: pelo menos uma média é diferente.
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
z = np.array([5, 10, 15, 20, 25])
f, p = stats.f_oneway(x, y, z)
```

---

- **Regressão Linear**: Modelo estatístico para prever o valor de uma variável a partir de outra.
  - Coeficiente de regressão: $b = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$
  - Intercepto: $a = \bar{y} - b \bar{x}$
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
b, a, r, p, std_err = stats.linregress(x, y)

f = lambda x: a + b*x # Função de regressão
print(f(10)) # Previsão de y para x = 10
```

---

- **Regressão Logística**: Modelo estatístico para prever a probabilidade de um evento binário.
  - Função logística: $p = \frac{1}{1 + e^{-(a + b x)}}$
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
y = np.array([0, 1, 1, 0, 1])
b, a = stats.linregress(x, np.log(y/(1-y)))[:2]
f = lambda x: 1 / (1 + np.exp(-(a + b*x))) # Função de regressão logística
print(f(10)) # Previsão de y para x = 10
```

---

- **Regressão Polinomial**: Modelo estatístico para prever o valor de uma variável a partir de outra.
  - Coeficientes de regressão: $b_0, b_1, b_2, \ldots, b_n$
  - Função de regressão: $f(x) = b_0 + b_1 x + b_2 x^2 + \ldots + b_n x^n$
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
b = np.polyfit(x, y, 2) # Coeficientes de regressão polinomial para grau 2
f = np.poly1d(b) # Função de regressão polinomial
print(f(10)) # Previsão de y para x = 10
```

---

- **Regressão Múltipla**: Modelo estatístico para prever o valor de uma variável a partir de duas ou mais variáveis.
  - Coeficientes de regressão: $b_0, b_1, b_2, \ldots, b_n$
  - Função de regressão: $f(x_1, x_2, \ldots, x_n) = b_0 + b_1 x_1 + b_2 x_2 + \ldots + b_n x_n$
```python
import numpy as np
from scipy import stats
x1 = np.array([15, 22, 35, 4, 85])
x2 = np.array([10, 20, 30, 40, 50])
y = np.array([5, 10, 15, 20, 25])
X = np.column_stack((x1, x2))
b = np.linalg.lstsq(X, y, rcond=None)[0] # Coeficientes de regressão múltipla
f = lambda x1, x2: b[0] + b[1]*x1 + b[2]*x2 # Função de regressão múltipla
print(f(10, 10)) # Previsão de y para x1 = 10 e x2 = 10
```

---

- **Regressão Não Linear**: Modelo estatístico para prever o valor de uma variável a partir de outra.
  - Função de regressão: $f(x) = a e^{b x}$
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
a, b = stats.linregress(x, np.log(y))[:2]
f = lambda x: a * np.exp(b*x) # Função de regressão não linear
print(f(10)) # Previsão de y para x = 10
```

---

- **Bootstrap**: Método de reamostragem para estimar a distribuição de uma estatística.
  - Amostras de bootstrap: amostras de uma população com reposição.
  - Estimativa bootstrap: estatística calculada para cada amostra de bootstrap.
```python
import numpy as np
from scipy import stats
x = np.array([15, 22, 35, 4, 85])
estimativas = [np.mean(np.random.choice(x, len(x))) for _ in range(1000)]
```

---

- **Cross-Validation**: Método de avaliação de modelos de aprendizado de máquina.
  - Conjunto de treinamento: conjunto de dados para treinar o modelo.
  - Conjunto de teste: conjunto de dados para avaliar o modelo.
  - Validação cruzada: técnica para avaliar o desempenho do modelo.
```python
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
model = LinearRegression()  
scores = cross_val_score(model, x.reshape(-1, 1), y, cv=5)
```

---

- **Regularização**: Técnica para evitar overfitting em modelos de aprendizado de máquina.
  - Regressão Ridge: penaliza os coeficientes de regressão.
  - Regressão Lasso: penaliza os coeficientes de regressão e seleciona variáveis.
```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
x = np.array([15, 22, 35, 4, 85])
y = np.array([10, 20, 30, 40, 50])
model = Ridge(alpha=0.1) # Regressão Ridge  
model = Lasso(alpha=0.1) # Regressão Lasso
model.fit(x.reshape(-1, 1), y)
```

---








