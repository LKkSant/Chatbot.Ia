import streamlit as st
from transformers import pipeline

# Inicializar pipeline QA com modelo em português
qa_pipeline = pipeline(
    "question-answering",
    model="pierreguillou/bert-base-cased-squad-v1.1-portuguese",
    tokenizer="pierreguillou/bert-base-cased-squad-v1.1-portuguese"
)

# FAQ inicial
faq = {
   "Olá, qual o horário de atendimento de vocês?": "Oi! Atendemos de segunda a sexta-feira, das 9h às 18h.",
    "Como posso falar com o suporte se tiver um problema?": "Você pode mandar um e-mail para suporte@empresa.com ou usar o chat no nosso site, tá bom?",
    "Quais serviços vocês oferecem?": "Oferecemos suporte técnico, consultoria personalizada e treinamentos online para ajudar você.",
    "Vocês atendem nos finais de semana?": "No momento, nosso atendimento é só de segunda a sexta, das 9h às 18h.",
    "Posso cancelar um serviço se eu não gostar?": "Claro, é só falar com a gente que ajudamos você a cancelar, sem complicação.",
    "Como faço para recuperar minha senha?": "É fácil! Na página de login tem a opção 'Esqueci minha senha', é só clicar lá e seguir os passos.",
    "Tem suporte para celular?": "Sim! Nosso sistema funciona direitinho em smartphones e tablets.",
    "Onde fica o escritório de vocês?": "Estamos na Av. Principal, 123, no Centro da Cidade XYZ, passa lá quando quiser!",
    "Quero fazer um orçamento, como faço?": "É só enviar um e-mail para vendas@empresa.com com as informações do que você precisa.",
    "Quais formas de pagamento aceitam?": "Aceitamos cartão de crédito, boleto e transferência bancária, para facilitar para você.",
    "Vocês fazem suporte remoto?": "Sim, usamos ferramentas como TeamViewer e AnyDesk para ajudar você de longe.",
    "Quanto tempo demora para atender uma solicitação?": "Normalmente respondemos em até 48 horas úteis, mas sempre tentamos ser mais rápidos!",
    "Posso acompanhar o status do meu pedido?": "Claro! Você pode ver tudo pelo painel do cliente no nosso site.",
    "Vocês oferecem algum tipo de treinamento?": "Sim, temos treinamentos online e também presenciais, dependendo da sua necessidade.",
    "O atendimento é só em português?": "Sim, nosso atendimento é feito em português para garantir a melhor comunicação.",
    "Posso agendar uma reunião com um consultor?": "Com certeza! É só mandar uma mensagem no nosso site que agendamos para você.",
    "Como atualizo meus dados no sistema?": "Basta acessar seu perfil no painel e editar as informações que quiser.",
    "Tem alguma política de reembolso?": "Sim, a gente analisa caso a caso, conforme nossa política que está disponível no site.",
    "Quais navegadores funcionam melhor com a plataforma?": "Recomendamos usar o Chrome, Firefox ou Edge atualizados para o melhor desempenho.",
    "Como recebo as novidades e atualizações?": "Enviamos e-mails para você sempre que temos algo novo ou importante.",
}


# Função para criar contexto a partir de FAQ + textos externos
def montar_contexto(faq_dict, textos_externos=[]):
    contexto = "\n".join([f"Q: {q}\nA: {a}" for q, a in faq_dict.items()])
    for texto in textos_externos:
        contexto += "\n" + texto
    return contexto

# Funções para balões de chat
def bot_message(msg):
    st.markdown(f"""
        <div style="background-color:#e0f7fa; padding:10px; border-radius:10px; margin:10px 0; max-width:75%; float:left;">
            🤖 {msg}
        </div>
        <div style="clear:both;"></div>
        """, unsafe_allow_html=True)

def user_message(msg):
    st.markdown(f"""
        <div style="background-color:#b2dfdb; padding:10px; border-radius:10px; margin:10px 0; max-width:75%; float:right;">
            🙋 {msg}
        </div>
        <div style="clear:both;"></div>
        """, unsafe_allow_html=True)
        
# Setup da página   
st.set_page_config(page_title="Assistente Virtual Local", layout="wide")
st.title("🤖 Assistente Virtual-Tech")

menu = st.sidebar.selectbox("Menu", ["Chat", "FAQ",])

# Estado para guardar textos externos e histórico
if "textos_externos" not in st.session_state:
    st.session_state.textos_externos = []

if "historico" not in st.session_state:
    st.session_state.historico = []

if menu == "Chat":
    st.header("Chat")
    contexto = montar_contexto(faq, st.session_state.textos_externos)

    pergunta = st.text_input("Faça sua pergunta:")

    if pergunta:
        resultado = qa_pipeline(question=pergunta, context=contexto)
        resposta = resultado["answer"]
        st.session_state.historico.append({"pergunta": pergunta, "resposta": resposta})

    # Mostrar histórico
    for troca in st.session_state.historico:
        st.markdown(f"**Você:** {troca['pergunta']}")
        st.markdown(f"**Assistente:** {troca['resposta']}")

elif menu == "FAQ":
    st.header("Perguntas Frequentes")
    for pergunta, resposta in faq.items():
        st.markdown(f"**Q:** {pergunta}")
        st.markdown(f"**A:** {resposta}")
        st.write("---")

elif menu == "Sobre":
    st.header("Sobre este assistente")
    st.write("""
    Este assistente virtual utiliza um modelo de linguagem pré-treinado em português para responder perguntas frequentes.  
    Ele roda localmente, usa a biblioteca Transformers e Streamlit para a interface.  
    Você pode carregar documentos PDF e TXT para ampliar o conhecimento dele.
    """)
