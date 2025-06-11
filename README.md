# Chatbot.Ia
Projeto da Faculdade de chat interativo com IA 

Um chat bot simples que responde perguntas pré programadas, utilizando o

Objetivo do Projeto:

O objetivo principal foi criar um chatbot interativo que:

Responda dúvidas frequentes automaticamente

Entenda linguagem natural em português

Atenda em tempo real, de forma acessível

Funcione localmente no computador.



Como funciona a Inteligência Artificial:

A IA usada é baseada em um modelo pré-treinado chamado bert-base-cased-squad-v1.1-portuguese, da Hugging Face.
Esse modelo é capaz de fazer "question answering", ou seja, responder perguntas com base em um contexto de conhecimento previamente definido, como uma base de perguntas frequentes (FAQ).

Tecnologias utilizadas

Python: linguagem principal:

Transformers (Hugging Face): para carregar o modelo de IA local

Streamlit: para criar uma interface web simples e interativa

st.session_state: para manter o histórico das conversas

FAQ customizado: usamos exemplos simulando conversas reais e informais

Como funciona na prática
O usuário digita uma pergunta (ex: "Bom dia, onde é o escritório?")

A IA compara a pergunta com o contexto de perguntas e respostas salvas

O modelo retorna a melhor resposta encontrada no contexto

A interface mostra a conversa com balões de chat coloridos, emojis e histórico salvo

PASSO A PASSO para iniciar a aplicação:

No terminal digite:

streamlit run chatbot_local.py

