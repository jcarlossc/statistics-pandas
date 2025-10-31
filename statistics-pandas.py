{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "739ab322",
   "metadata": {
    "papermill": {
     "duration": 0.004129,
     "end_time": "2025-10-31T02:53:05.355312",
     "exception": false,
     "start_time": "2025-10-31T02:53:05.351183",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h1>📌 Operações Estatísticas em Pandas</h1>\n",
    "\n",
    "<p style='font-size:16px;'>O Pandas é uma das bibliotecas mais poderosas do Python para manipulação e análise de dados. Ele oferece diversas funções estatísticas prontas, que permitem entender melhor os seus dados sem precisar de cálculos manuais ou uso de planilhas.</p>\n",
    "<p style='font-size:16px;'>Neste notebook, vamos explorar as principais operações estatísticas que você pode realizar com o Pandas</p>\n",
    "\n",
    "<h4>📌 Autor: Carlos da Costa</h4>\n",
    "📌Recife, PE - Brasil<br>\n",
    "📌Telefone: +55 81 99712 9140<br>\n",
    "📌Telegram: @jcarlossc<br>\n",
    "📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>\n",
    "📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>\n",
    "📌Email: jcarlossc1977@gmail.com<br>\n",
    "📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>\n",
    "📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>\n",
    "📌GitHub: https://github.com/jcarlossc<br>\n",
    "📌Kaggle: https://www.kaggle.com/jcarlossc/<br>\n",
    "📌Twitter/X: https://x.com/jcarlossc1977<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "27ff407e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:05.363390Z",
     "iopub.status.busy": "2025-10-31T02:53:05.363106Z",
     "iopub.status.idle": "2025-10-31T02:53:07.139713Z",
     "shell.execute_reply": "2025-10-31T02:53:07.138839Z"
    },
    "papermill": {
     "duration": 1.782386,
     "end_time": "2025-10-31T02:53:07.141467",
     "exception": false,
     "start_time": "2025-10-31T02:53:05.359081",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Importação da biblioteca Pandas.\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb16c6d2",
   "metadata": {
    "papermill": {
     "duration": 0.00289,
     "end_time": "2025-10-31T02:53:07.148089",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.145199",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Criando um DataFrame</h2>\n",
    "<p style='font-size:16px;'>Antes de começar, precisamos criar um pequeno conjunto de dados (DataFrame):</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "657a046e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.155786Z",
     "iopub.status.busy": "2025-10-31T02:53:07.155063Z",
     "iopub.status.idle": "2025-10-31T02:53:07.162790Z",
     "shell.execute_reply": "2025-10-31T02:53:07.161892Z"
    },
    "papermill": {
     "duration": 0.013144,
     "end_time": "2025-10-31T02:53:07.164218",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.151074",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "dados = pd.DataFrame(\n",
    "    { \"idade\": [23, 25, 31, 35, 40, 29, 23, 37, 41, 30], \n",
    "     \"salario\": [2500, 2700, 3200, 4000, 5000, 3100, 2600, 4500, 5200, 3300], \n",
    "     \"departamento\": [\"RH\", \"RH\", \"TI\", \"TI\", \"Financeiro\", \"TI\", \"RH\", \"Financeiro\", \"Financeiro\", \"TI\"] }\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9bdf50d8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.172001Z",
     "iopub.status.busy": "2025-10-31T02:53:07.171397Z",
     "iopub.status.idle": "2025-10-31T02:53:07.185444Z",
     "shell.execute_reply": "2025-10-31T02:53:07.184502Z"
    },
    "papermill": {
     "duration": 0.01921,
     "end_time": "2025-10-31T02:53:07.186794",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.167584",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   idade  salario departamento\n",
      "0     23     2500           RH\n",
      "1     25     2700           RH\n",
      "2     31     3200           TI\n",
      "3     35     4000           TI\n",
      "4     40     5000   Financeiro\n",
      "5     29     3100           TI\n",
      "6     23     2600           RH\n",
      "7     37     4500   Financeiro\n",
      "8     41     5200   Financeiro\n",
      "9     30     3300           TI\n"
     ]
    }
   ],
   "source": [
    "print(dados)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b863fbd",
   "metadata": {
    "papermill": {
     "duration": 0.003023,
     "end_time": "2025-10-31T02:53:07.193177",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.190154",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Estatísticas Descritivas</h2>\n",
    "\n",
    "<p style='font-size:16px;'>Com o método describe(), é possível visualizar rapidamente algumas medidas de posição e dispersão:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c07570a5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.201014Z",
     "iopub.status.busy": "2025-10-31T02:53:07.200691Z",
     "iopub.status.idle": "2025-10-31T02:53:07.221416Z",
     "shell.execute_reply": "2025-10-31T02:53:07.220329Z"
    },
    "papermill": {
     "duration": 0.0263,
     "end_time": "2025-10-31T02:53:07.222774",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.196474",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           idade      salario\n",
      "count  10.000000    10.000000\n",
      "mean   31.400000  3610.000000\n",
      "std     6.669999  1000.499875\n",
      "min    23.000000  2500.000000\n",
      "25%    26.000000  2800.000000\n",
      "50%    30.500000  3250.000000\n",
      "75%    36.500000  4375.000000\n",
      "max    41.000000  5200.000000\n"
     ]
    }
   ],
   "source": [
    "print(dados.describe())\n",
    "# count: quantidade de observações\n",
    "# mean: média aritmética\n",
    "# std: desvio padrão\n",
    "# min: valor menos\n",
    "# 25%: primeiro quartil\n",
    "# 50%: segundo quartil ou mediana\n",
    "# 75%: terceiro quartil\n",
    "# max: valor máximo"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "974e0c60",
   "metadata": {
    "papermill": {
     "duration": 0.002915,
     "end_time": "2025-10-31T02:53:07.229009",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.226094",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Medidas de Tendência Central</h2>\n",
    "\n",
    "<p style='font-size:16px;'>Essas medidas ajudam a entender o comportamento médio dos dados:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ef6450e2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.237726Z",
     "iopub.status.busy": "2025-10-31T02:53:07.237436Z",
     "iopub.status.idle": "2025-10-31T02:53:07.246877Z",
     "shell.execute_reply": "2025-10-31T02:53:07.245984Z"
    },
    "papermill": {
     "duration": 0.016215,
     "end_time": "2025-10-31T02:53:07.248327",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.232112",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média: 31.4\n",
      "Mediana: 30.5\n",
      "Moda: 23\n"
     ]
    }
   ],
   "source": [
    "# Média → soma de todos os valores dividida pela quantidade:\n",
    "print(\"Média:\", dados[\"idade\"].mean()) \n",
    "\n",
    "# Mediana → valor central da amostra ordenada:\n",
    "print(\"Mediana:\", dados[\"idade\"].median()) \n",
    "\n",
    "# Moda → valor mais frequente:\n",
    "print(\"Moda:\", dados[\"idade\"].mode().values[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d680ee4d",
   "metadata": {
    "papermill": {
     "duration": 0.002959,
     "end_time": "2025-10-31T02:53:07.254621",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.251662",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Medidas de Dispersão</h2>\n",
    "\n",
    "<p style='font-size:16px;'>Essas medidas indicam o quanto os dados estão espalhados:</p>\n",
    "<p style='font-size:16px;'>Quanto maior o desvio padrão, mais os valores se afastam da média.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b04cb57c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.261839Z",
     "iopub.status.busy": "2025-10-31T02:53:07.261546Z",
     "iopub.status.idle": "2025-10-31T02:53:07.267040Z",
     "shell.execute_reply": "2025-10-31T02:53:07.266054Z"
    },
    "papermill": {
     "duration": 0.010711,
     "end_time": "2025-10-31T02:53:07.268421",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.257710",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desvio padrão: 1000.499875062461\n",
      "Variância: 1001000.0\n"
     ]
    }
   ],
   "source": [
    "# Desvio padrão:\n",
    "print(\"Desvio padrão:\", dados[\"salario\"].std()) \n",
    "\n",
    "# Variância:\n",
    "print(\"Variância:\", dados[\"salario\"].var())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eca7eebe",
   "metadata": {
    "papermill": {
     "duration": 0.003241,
     "end_time": "2025-10-31T02:53:07.275394",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.272153",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Estatísticas por Grupo</h2>\n",
    "\n",
    "<p style='font-size:16px;'>O método groupby() é essencial para comparar grupos dentro dos dados:</p>\n",
    "\n",
    "<p style='font-size:16px;'>Esse exemplo mostra a média salarial por departamento, algo muito útil em relatórios corporativos e análises financeiras.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "30dea1dc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.283301Z",
     "iopub.status.busy": "2025-10-31T02:53:07.283009Z",
     "iopub.status.idle": "2025-10-31T02:53:07.294266Z",
     "shell.execute_reply": "2025-10-31T02:53:07.293427Z"
    },
    "papermill": {
     "duration": 0.016689,
     "end_time": "2025-10-31T02:53:07.295466",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.278777",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "departamento\n",
      "Financeiro    4900.0\n",
      "RH            2600.0\n",
      "TI            3400.0\n",
      "Name: salario, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Média de salário por departamento:\n",
    "print(dados.groupby(\"departamento\")[\"salario\"].mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2de92640",
   "metadata": {
    "papermill": {
     "duration": 0.003123,
     "end_time": "2025-10-31T02:53:07.302037",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.298914",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Correlação</h2>\n",
    "\n",
    "<p style='font-size:16px;'>Para verificar se duas variáveis estão relacionadas, usamos:<p>\n",
    "\n",
    "<p style='font-size:16px;'>Uma correlação próxima de 1 indica relação positiva forte, enquanto próxima de -1 indica relação negativa.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9bd7408b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.309903Z",
     "iopub.status.busy": "2025-10-31T02:53:07.309320Z",
     "iopub.status.idle": "2025-10-31T02:53:07.318855Z",
     "shell.execute_reply": "2025-10-31T02:53:07.317971Z"
    },
    "papermill": {
     "duration": 0.015064,
     "end_time": "2025-10-31T02:53:07.320337",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.305273",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           idade  salario\n",
      "idade    1.00000  0.98335\n",
      "salario  0.98335  1.00000\n"
     ]
    }
   ],
   "source": [
    "print(dados[[\"idade\", \"salario\"]].corr())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8502a70",
   "metadata": {
    "papermill": {
     "duration": 0.003172,
     "end_time": "2025-10-31T02:53:07.326989",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.323817",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Frequência e Percentuais</h2>\n",
    "\n",
    "<p style='font-size:16px;'>Para entender a distribuição de categorias, use:</p>\n",
    "\n",
    "<p style='font-size:16px;'>Esses comandos mostram a contagem e o percentual de cada departamento.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cbc1ea0a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-31T02:53:07.335263Z",
     "iopub.status.busy": "2025-10-31T02:53:07.334674Z",
     "iopub.status.idle": "2025-10-31T02:53:07.343551Z",
     "shell.execute_reply": "2025-10-31T02:53:07.342512Z"
    },
    "papermill": {
     "duration": 0.014465,
     "end_time": "2025-10-31T02:53:07.344871",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.330406",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "departamento\n",
      "TI            4\n",
      "RH            3\n",
      "Financeiro    3\n",
      "Name: count, dtype: int64\n",
      "departamento\n",
      "TI            40.0\n",
      "RH            30.0\n",
      "Financeiro    30.0\n",
      "Name: proportion, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Frequência:\n",
    "print(dados[\"departamento\"].value_counts())\n",
    "\n",
    "# Percentual:\n",
    "print(dados[\"departamento\"].value_counts(normalize=True) * 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88d4c7ff",
   "metadata": {
    "papermill": {
     "duration": 0.003352,
     "end_time": "2025-10-31T02:53:07.351831",
     "exception": false,
     "start_time": "2025-10-31T02:53:07.348479",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2>📌 Conclusão</h2>\n",
    "\n",
    "<p style='font-size:16px;'>O Pandas facilita muito o trabalho com estatísticas em Python. Com poucos comandos, você pode obter informações valiosas sobre médias, dispersões, correlações e muito mais — tudo de forma rápida e intuitiva.</p>\n",
    "\n",
    "<p style='font-size:16px;'>Essas ferramentas são a base para análises exploratórias, relatórios de negócios e até para preparar dados antes de aplicar algoritmos de Aprendizado de Máquina.</p>"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 31153,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 6.95975,
   "end_time": "2025-10-31T02:53:07.873726",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-10-31T02:53:00.913976",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
