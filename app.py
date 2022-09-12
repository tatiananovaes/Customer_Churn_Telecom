# Web App Customer Churn para empresas de Telecom // Web App Customer Churn for Telecom Companies

# Imports
import joblib
import pickle
import numpy as np
import pandas as pd
import streamlit as st


# Carrega o modelo // Load the model
model = joblib.load(open('./models/best_model.pkl', 'rb'))
dic_cut = joblib.load(open('./datasets/dic_cut.pkl', 'rb'))

# Função para fazer as previsões // Function to make predictions


def predict_churn(state, account_length, area_code, international_plan, voice_mail_plan, number_vmail_messages, total_day_minutes, total_day_calls, total_eve_minutes, total_eve_calls, total_night_minutes, total_night_calls, total_intl_minutes, total_intl_calls):

    # Carrega o array com as variáveis // Load the array with the variables
    cols = ['state', 'account_length', 'area_code', 'international_plan', 'voice_mail_plan', 'number_vmail_messages', 'total_day_minutes',
            'total_day_calls', 'total_eve_minutes', 'total_eve_calls', 'total_night_minutes', 'total_night_calls', 'total_intl_minutes', 'total_intl_calls']

    input = np.array([state, account_length, area_code, international_plan, voice_mail_plan, number_vmail_messages, total_day_minutes, total_day_calls,
                      total_eve_minutes, total_eve_calls, total_night_minutes, total_night_calls, total_intl_minutes, total_intl_calls]).reshape(1, -1)

    df_new = pd.DataFrame(input, columns=cols)

    # Discretização de variáveis numéricas // Discretization of numeric variables
    cols_discret = [col for col in df_new.columns if col.startswith('total')]
    for col in cols_discret:
        df_new[col] = df_new[col].astype(np.int64)
        df_new[col] = pd.cut(df_new[col], bins=dic_cut[col],
                             include_lowest=True, labels=['1', '2', '3', '4', '5'])

    # One Hot Encoding
    onehot_features = ['state', 'area_code', 'total_day_minutes', 'total_day_calls', 'total_eve_minutes',
                       'total_eve_calls', 'total_night_minutes', 'total_night_calls', 'total_intl_minutes', 'total_intl_calls']

    for col in onehot_features:
        onehots = pd.get_dummies(df_new[col], prefix=col)
        df_new = df_new.join(onehots)

    # Remoção das colunas originais // Removing the original columns
    df_new = df_new.drop(columns=onehot_features)

    # Complementação das colunas não informadas com 0 // Complement of columns not informed with 0
    cols_base = ['account_length', 'international_plan', 'voice_mail_plan', 'number_vmail_messages', 'state_AK', 'state_AL', 'state_AR', 'state_AZ', 'state_CA', 'state_CO', 'state_CT', 'state_DC', 'state_DE', 'state_FL', 'state_GA', 'state_HI', 'state_IA', 'state_ID', 'state_IL', 'state_IN', 'state_KS', 'state_KY', 'state_LA', 'state_MA', 'state_MD', 'state_ME', 'state_MI', 'state_MN', 'state_MO', 'state_MS', 'state_MT', 'state_NC', 'state_ND', 'state_NE', 'state_NH', 'state_NJ', 'state_NM', 'state_NV', 'state_NY', 'state_OH', 'state_OK', 'state_OR', 'state_PA', 'state_RI', 'state_SC', 'state_SD', 'state_TN', 'state_TX', 'state_UT', 'state_VA', 'state_VT', 'state_WA', 'state_WI', 'state_WV', 'state_WY', 'area_code_408', 'area_code_415', 'area_code_510', 'total_day_minutes_1', 'total_day_minutes_2',
                 'total_day_minutes_3', 'total_day_minutes_4', 'total_day_minutes_5', 'total_day_calls_1', 'total_day_calls_2', 'total_day_calls_3', 'total_day_calls_4', 'total_day_calls_5', 'total_eve_minutes_1', 'total_eve_minutes_2', 'total_eve_minutes_3', 'total_eve_minutes_4', 'total_eve_minutes_5', 'total_eve_calls_4', 'total_eve_calls_5', 'total_night_minutes_1', 'total_night_minutes_2', 'total_night_minutes_3', 'total_night_minutes_4', 'total_night_minutes_5', 'total_night_calls_1', 'total_night_calls_2', 'total_night_calls_3', 'total_night_calls_4', 'total_night_calls_5', 'total_intl_minutes_1', 'total_intl_minutes_2', 'total_intl_minutes_3', 'total_intl_minutes_4', 'total_intl_minutes_5', 'total_intl_calls_1', 'total_intl_calls_2', 'total_intl_calls_3', 'total_intl_calls_4', 'total_intl_calls_5']

    cols_new = [col for col in cols_base if col not in df_new.columns]

    for col in cols_new:
        df_new[col] = 0

    # Previsão // Prediction
    prediction = model.predict(df_new)

    return prediction


# Markdown
st.markdown(
    '<style>body{background-color: White;}</style>', unsafe_allow_html=True)

# Título
st.title('Web App Customer Churn para empresas de Telecom')
st.write('''Forneça as informações solicitadas abaixo para prever se o cliente irá rescindir o contrato com a empresa.''')


# Função para encoding de variável binária


def encoding_var_binaria(param):
    return 1 if param == 'Sim' else 0


# Função para encoding de variável binária com base na média


def encoding_var_avg(var, avg):
    return 1 if var >= avg else 0


# Variável state
state = st.selectbox(
    'Estado do cliente (nos Estados Unidos):', ['WV', 'MN', 'NY', 'AL', 'WI', 'OH', 'OR', 'WY', 'VA', 'CT', 'MI', 'ID', 'VT', 'TX', 'UT', 'IN', 'MD', 'KS', 'NC', 'NJ', 'MT', 'CO', 'NV', 'WA', 'RI', 'MA', 'MS', 'AZ', 'FL', 'MO', 'NM', 'ME', 'ND', 'NE', 'OK', 'DE', 'SC', 'SD', 'KY', 'IL', 'NH', 'AR', 'GA', 'DC', 'HI', 'TN', 'AK', 'LA', 'PA', 'IA', 'CA'])

# Variável area_code
area_code = st.selectbox('Código de área do cliente:', ['408', '415', '510'])

# Variável international_plan
international_plan = st.selectbox(
    "O cliente tem plano para ligações internacionais?", ['Sim', 'Não'])
international_plan = encoding_var_binaria(international_plan)

# Variável voice_mail_plan
voice_mail_plan = st.selectbox(
    "O cliente tem plano para caixa postal?", ['Sim', 'Não'])
voice_mail_plan = encoding_var_binaria(voice_mail_plan)

# Variável account_lenght
account_length = st.number_input(
    'Há quantos dias a conta do cliente está ativa?', 0, key=1)
account_length = encoding_var_avg(float(account_length), 100.86)

# Variável number_vmail_messages
number_vmail_messages = int(st.number_input(
    'Número de mensagens de voz do cliente:', 0, key=2))
number_vmail_messages = encoding_var_avg(float(account_length), 7.97)

# Variável total_day_minutes
total_day_minutes = int(st.number_input(
    'Total de minutos de chamadas efetuadas durante o dia:', 0, key=3))

# Variável total_day_calls
total_day_calls = int(st.number_input(
    'Total de chamadas efetuadas durante o dia:', 0, key=4))

# Variável total_eve_minutes
total_eve_minutes = int(st.number_input(
    'Total de minutos de chamadas efetuadas durante a noite:', 0, key=5))

# Variável total_eve_calls
total_eve_calls = st.number_input(
    'Total de chamadas efetuadas durante a noite:', 0, key=6)

# Variável total_night_minutes
total_night_minutes = int(st.number_input(
    'Total de minutos de chamadas efetuadas durante a madrugada:', 0, key=7))

# Variável total_night_calls
total_night_calls = int(st.number_input(
    'Total de chamadas efetuadas durante a madrugada:', 0, key=8))

# Variável total_intl_minutes
total_intl_minutes = int(st.number_input(
    'Total de minutos de chamadas internacionais:', 0, key=9))

# Variável total_intl_calls
total_intl_calls = int(st.number_input(
    'Total de chamadas internacionais:', 0, key=10))


# Resposta do modelo // Model response

# Previsão positiva // Positive prediction
result_html_yes = """
<div style="background-color:#F08080"; padding: 10px>
<h2 style="color:white; text-align:center;">Este cliente provavelmente deixará de utilizar os serviços da empresa.</h2>
</div>
"""

# Previsão negativa // Negative prediction
result_html_no = """
<div style="background-color:#00B63C"; padding: 10px>
<h2 style="color:black; text-align:center;">Este cliente provavelmente continuará utilizando os serviços da empresa.</h2>
</div>
"""

# Botão para previsão // Button for prediction
if st.button("Fazer Previsão"):

    # Gera a previsão // Generate the prediction
    output = predict_churn(state, account_length, area_code,
                           international_plan, voice_mail_plan,
                           number_vmail_messages,
                           total_day_minutes, total_day_calls,
                           total_eve_minutes, total_eve_calls,
                           total_night_minutes, total_night_calls,
                           total_intl_minutes, total_intl_calls)

    # Imprime o resultado // Print the result
    if output == 1:
        st.markdown(result_html_yes, unsafe_allow_html=True)
    else:
        st.markdown(result_html_no, unsafe_allow_html=True)
