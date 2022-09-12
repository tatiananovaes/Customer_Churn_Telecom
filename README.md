Data: setembro de 2022

---
# Previsão de Customer Churn em Operadoras de Telecom
##  Customer_Churn_Telecom
---

O objetivo deste projeto é prever o Customer Churn em uma Operadora de Telecom.

Customer Churn (ou Rotatividade de Clientes, em uma tradução livre) refere-se a uma decisão tomada pelo cliente sobre o término do relacionamento comercial; refere-se também à perda de clientes. A fidelidade do cliente e a rotatividade de clientes sempre somam 100%. Portanto, é muito importante para uma empresa prever os usuários que provavelmente abandonarão o relacionamento comercial e os fatores que afetam essas decisões.

A proposta, então, é criar um modelo de aprendizagem de máquina que possa prever se um cliente irá ou não cancelar seu plano e qual a probabilidade de isso ocorrer. Tanto a análise exploratória quanto o treinamento do modelo foram feitos com Jupyter Notebook; na sequência, com o modelo treinado, foi construída uma interface com o Streamlit (Web App) para a previsão do churn customer a partir de dados informados pelo usuário de forma interativa.

O projeto faz parte da Formação Cientista de Dados, oferecida pela Data Science Academy.


## Dados
Os datasets de treino e de teste foram fornecidos pela Data Science Academy, em arquivos separados (csv). 


## Dependências
O projeto foi executado por meio da linguagem Python no Jupyter Notebook. As bibliotecas utilizadas foram Numpy, Pandas, Seaborn, Matplotlib, Scipy, Scikit-learn, Pyarrow, Joblib, Pickle, Imblearn e XGBoost, além do Streamlit. As versöes utilizadas constam do arquivo requirements.txt.


## Para executar a app no Streamlit:
1- Ter o Anaconda Python instalado

2- Executar: pip install -r requirements.txt

3- Executar: streamlit run app.py

4- Acessar a app no navegador


---

# _Customer Churn Forecast in Telecom Operators_
_The objective of this project is to predict Customer Churn in a Telecom Operator._

_Customer Churn refers to a decision made by the customer about ending the business relationship; it also refers to the loss of customers. Customer loyalty and customer churn always add up to 100%. Therefore, it is very important for a company to predict the users who are likely to leave the business relationship and the factors that affect those decisions._

_The proposal then, is to create a machine learning model that can predict whether or not a customer will cancel their plan and how likely it is to do so. Both exploratory analysis and model training were done with Jupyter Notebook; then, with the trained model, an interface was created with Streamlit (Web App) for the prediction of customer churn from data informed by the user in an interactive way._ 
 
_The project is part of the Data Scientist Training, offered by Data Science Academy._


## _Data_
_Training and test datasets were provided by Data Science Academy, in separate files (csv)._


## _Dependencies_
_The project was run using the Python language in Jupyter Notebook. The libraries used were Numpy, Pandas, Seaborn, Matplotlib, Scipy, Scikit-learn, Pyarrow, Joblib, Pickle, Imblearn, and XGBoost, plus Streamlit. The versions used are in the requirements.txt file._


## _To run the app in Streamlit_:
_1- Have Anaconda Python installed_

_2- Run: pip install -r requirements.txt_

_3- Run: streamlit run app.py_

_4- Access the app in the browser_



---


## Dicionário de Dados // _Data Dictionary_

**Coluna/_Column_**|**Tipo de dado/_Dtype_**      |**Descrição/_Description_**
:-------------|:------------------------:|:-------------------------
state (categorical)|String|Estado nos Estados Unidos
account_length (numeric)|Int|Quantidade de dias de conta ativa
area_code (categorical)|Int|Código de área nos Estados Unidos
international_plan (categorical)|String|Plano de ligações internacionais
voice_mail_plan (categorical)|String|Plano de caixa postal
number_vmail_messages (numeric)|Int|Número de mensagens de voz
total_day_minutes (numeric)|Int|Total de minutos de chamadas efetuadas durante o dia
total_day_calls (numeric)|Int|Total de chamadas efetuadas durante o dia
total_day_charge (numeric)|Float|Valor total devido pelas chamadas durante o dia
total_eve_minutes (numeric)|Float|Total de minutos de chamadas efetuadas durante a noite
total_eve_calls (numeric)|Int|Total de chamadas efetuadas durante a noite
total_eve_charge (numeric)|Float|Valor total devido pelas chamadas durante a noite
total_night_minutes (numeric)|Int|Total de minutos de chamadas efetuadas durante a madrugada
total_night_calls (numeric)|Int|Total de chamadas efetuadas durante a madrugada
total_night_charge (numeric)|Float|Valor total devido pelas chamadas durante a madrugada
total_intl_minutes (numeric)| Int|Total de minutos de chamadas internacionais
total_intl_calls (numeric)|Int|Total de chamadas internacionais
total_intl_charge (numeric)|Float|Valor total devido pelas chamadas internacionais
number_customer_service_calls (numeric)|Int|Número de chamadas de atendimento ao cliente
churn (categorical)|Int|Rotatividade do cliente (yes - distrato, no - permanência)


