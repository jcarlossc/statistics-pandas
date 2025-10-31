# 📌 Operações Estatísticas

Este projeto demonstra como realizar **operações estatísticas básicas** utilizando a biblioteca **Pandas** em **Python**.

O objetivo é apresentar, de forma simples e didática, como explorar dados por meio de estatísticas descritivas, cálculos de correlação e visualizações que ajudam na análise e interpretação de informações.

---

## 📌 Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas** → Manipulação e análise de dados
* *(Opcional)* Jupyter Notebook → Execução interativa

---

## 📌 Funcionalidades

O projeto inclui exemplos práticos de:

* Cálculo de **média, mediana e moda**
* Cálculo de **desvio padrão e variância**
* **Correlação** entre variáveis
* **Agrupamento** por categorias (`groupby`)
* **Contagem e percentuais** de frequência

---

## 📌 Exemplo de Uso

### 📌 Criação do DataFrame

```python
import pandas as pd

dados = {
    "idade": [23, 25, 31, 35, 40, 29, 23, 37, 41, 30],
    "salario": [2500, 2700, 3200, 4000, 5000, 3100, 2600, 4500, 5200, 3300],
    "departamento": ["RH", "RH", "TI", "TI", "Financeiro", "TI", "RH", "Financeiro", "Financeiro", "TI"]
}

df = pd.DataFrame(dados)
```

### 📌 Cálculo de Média e Desvio Padrão

```python
print("Média salarial:", df["salario"].mean())
print("Desvio padrão:", df["salario"].std())
```

---

### 📌 Clone o repositório:

```bash
git clone https://github.com/jcarlossc/statistics-pandas.git
cd statistics-pandas
```

---

## 📌 Aprendizados

* Como calcular estatísticas descritivas com **Pandas**
* Uso de `groupby()`, `value_counts()` e `corr()` para análise de dados
* Interpretação de **médias, variâncias e correlações**

---

## 📌 Referências

* [Documentação do Pandas](https://pandas.pydata.org/docs/)

---

## 📌 Contribuições

Se quiser contribuir:
1. Faça um fork deste repositório
2. Crie uma branch para sua feature ou correção (git checkout -b minha-feature)
3. Faça commits descritos claramente
4. Submeta um Pull Request

---

## 📌 Licença
Este projeto está licenciado sob a MIT License.

---

## 📌 Autor Carlos da Costa<br>
📌Recife, PE - Brasil<br>
📌Telefone: +55 81 99712 9140<br>
📌Telegram: @jcarlossc<br>
📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>
📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>
📌Email: jcarlossc1977@gmail.com<br>
📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>
📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>
📌GitHub: https://github.com/jcarlossc<br>
📌Kaggle: https://www.kaggle.com/jcarlossc/<br>
📌Twitter/X: https://x.com/jcarlossc1977<br>

---

