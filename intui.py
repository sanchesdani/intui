import streamlit as st
import random

def main():
    st.set_page_config(page_title="Simulador de Vieses de Intuição", layout="wide")
    
    st.title("🧠 Simulador de Vieses de Intuição")
    st.markdown("""
    Este simulador demonstra vários vieses cognitivos que afetam nossa tomada de decisão e julgamento.
    Selecione um viés abaixo para aprender sobre ele e experimentar uma demonstração interativa.
    """)
    
    # Sidebar com seleção de viés
    st.sidebar.header("Menu")
    bias_options = {
        "Viés de Confirmação": confirmation_bias,
        "Efeito Anchoring": anchoring_effect,
        "Viés de Disponibilidade": availability_bias,
        "Viés do Otimismo": optimism_bias,
        "Efeito Enquadramento": framing_effect,
        "Viés do Status Quo": status_quo_bias,
        "Sobre": about_page
    }
    selected_bias = st.sidebar.selectbox("Selecione um viés:", list(bias_options.keys()))
    
    # Mostra a página selecionada
    bias_options[selected_bias]()

def confirmation_bias():
    st.header("Viés de Confirmação")
    st.markdown("""
    **Definição:** Tendência de buscar, interpretar, favorecer e lembrar informações que confirmam 
    as próprias crenças ou hipóteses, dando desproporcionalmente menos consideração a possibilidades alternativas.
    """)
    
    st.subheader("Experimento Interativo")
    st.write("Imagine que você acredita que moedas tendem a cair mais com 'cara' para cima.")
    
    # Simulação de lançamento de moeda
    if st.button("Lançar moeda"):
        result = random.choice(["cara", "coroa"])
        st.write(f"Resultado: {result}")
        
        if result == "cara":
            st.success("Veja! Isso confirma sua hipótese!")
        else:
            st.warning("Hmm, isso não confirma sua hipótese. Você pode estar tentando descartar este resultado?")
    
    st.markdown("""
    **Reflexão:** Quantas vezes você precisaria lançar a moeda para ter certeza? 
    Você daria o mesmo peso para resultados que confirmam e que contradizem sua hipótese?
    """)

def anchoring_effect():
    st.header("Efeito Anchoring (Ancoragem)")
    st.markdown("""
    **Definição:** Tendência de depender muito da primeira informação recebida (a "âncora") 
    ao tomar decisões, mesmo quando essa informação é irrelevante.
    """)
    
    st.subheader("Experimento Interativo")
    st.write("Responda rapidamente (sem calcular):")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("8 × 7 × 6 × 5 × 4 × 3 × 2 × 1")
        guess1 = st.number_input("Sua estimativa:", min_value=0, key="guess1")
    
    with col2:
        st.write("1 × 2 × 3 × 4 × 5 × 6 × 7 × 8")
        guess2 = st.number_input("Sua estimativa:", min_value=0, key="guess2")
    
    if guess1 and guess2:
        real_answer = 40320
        st.write(f"Resposta correta: {real_answer}")
        
        st.write("**Sua primeira estimativa:**", guess1)
        st.write("**Sua segunda estimativa:**", guess2)
        
        if guess1 > guess2:
            st.info("Observe como a sequência decrescente (primeira pergunta) levou a uma estimativa maior que a sequência crescente, mesmo sendo a mesma conta!")
        
    st.markdown("""
    **Explicação:** O primeiro número da sequência serve como âncora, influenciando sua estimativa final.
    """)

def availability_bias():
    st.header("Viés de Disponibilidade")
    st.markdown("""
    **Definição:** Tendência de superestimar a probabilidade de eventos que vêm facilmente à mente, 
    geralmente porque são recentes, emocionantes ou frequentemente cobertos pela mídia.
    """)
    
    st.subheader("Teste Rápido")
    st.write("O que mata mais pessoas por ano?")
    
    option = st.radio("Escolha:", [
        "Ataques de tubarão",
        "Queda de partes de aviões",
        "Acidentes com cocos caindo de árvores"
    ])
    
    if option:
        st.write("**Respostas corretas (mortes anuais estimadas):**")
        st.write("- Ataques de tubarão: ~10")
        st.write("- Queda de partes de aviões: ~50")
        st.write("- Acidentes com cocos: ~150")
        
        st.warning("A maioria superestima os primeiros itens porque são mais divulgados na mídia!")
    
    st.markdown("""
    **Reflexão:** Como a cobertura da mídia pode distorcer nossa percepção de risco?
    """)

def optimism_bias():
    st.header("Viés do Otimismo")
    st.markdown("""
    **Definição:** Tendência de acreditar que temos menos probabilidade de experimentar eventos negativos 
    e mais probabilidade de experimentar eventos positivos do que outras pessoas.
    """)
    
    st.subheader("Questionário")
    st.write("Em comparação com a média das pessoas, qual a probabilidade de:")
    
    q1 = st.slider("Você desenvolver uma doença séria?", 0, 100, 20)
    q2 = st.slider("Você ter um casamento feliz?", 0, 100, 80)
    q3 = st.slider("Você perder o emprego nos próximos 5 anos?", 0, 100, 20)
    
    if st.button("Analisar respostas"):
        st.write("**Resultados típicos:**")
        st.write("- A maioria das pessoas se avalia como abaixo da média para eventos negativos")
        st.write("- E acima da média para eventos positivos")
        st.write("- Estatisticamente, isso é impossível (nem todos podem estar acima da média!)")
        
        st.success("Isso mostra nosso otimismo natural em relação ao nosso próprio futuro.")

def framing_effect():
    st.header("Efeito Enquadramento")
    st.markdown("""
    **Definição:** Tendência de reagir de maneira diferente a uma mesma escolha dependendo de como ela é apresentada (positiva ou negativamente).
    """)
    
    st.subheader("Experimento Clássico (Tversky & Kahneman)")
    st.write("Imagine um surto de doença que espera-se mate 600 pessoas. Dois programas alternativos foram propostos:")
    
    tab1, tab2 = st.tabs(["Enquadramento Positivo", "Enquadramento Negativo"])
    
    with tab1:
        st.write("""
        - Programa A: 200 pessoas serão salvas
        - Programa B: 1/3 de probabilidade de salvar 600 pessoas, 2/3 de probabilidade de salvar ninguém
        """)
        choice1 = st.radio("Qual você escolheria?", ["Programa A", "Programa B"], key="choice1")
    
    with tab2:
        st.write("""
        - Programa C: 400 pessoas morrerão
        - Programa D: 1/3 de probabilidade que ninguém morra, 2/3 de probabilidade que 600 morram
        """)
        choice2 = st.radio("Qual você escolheria?", ["Programa C", "Programa D"], key="choice2")
    
    if choice1 and choice2:
        st.write("**Observação:** Os programas A/C e B/D são estatisticamente equivalentes, apenas enquadrados de forma diferente.")
        st.write("A maioria escolhe A no primeiro cenário e D no segundo, mostrando aversão a risco em ganhos e busca por risco em perdas.")

def status_quo_bias():
    st.header("Viés do Status Quo")
    st.markdown("""
    **Definição:** Preferência pela manutenção do estado atual das coisas, mesmo quando mudanças poderiam ser benéficas.
    """)
    
    st.subheader("Teste de Decisão")
    st.write("Você herdou uma quantia significativa de dinheiro. O que faz?")
    
    option = st.radio("Escolha:", [
        "Deixar na poupança (baixo risco, baixo retorno)",
        "Investir em um fundo moderado (algum risco, retorno médio)",
        "Investir em ações de crescimento (alto risco, alto potencial)"
    ])
    
    if option:
        st.write("**Pesquisas mostram:**")
        st.write("- A maioria das pessoas prefere opções conservadoras com o dinheiro 'herdado'")
        st.write("- Mas tomariam decisões mais arriscadas com dinheiro 'ganho'")
        st.write("- Isso reflete nossa aversão a mudanças quando já estamos em uma posição confortável")

def about_page():
    st.header("Sobre este Simulador")
    st.markdown("""
    Este aplicativo demonstra vários vieses cognitivos que afetam nosso julgamento e tomada de decisão.
    
    **Vieses incluídos:**
    - Viés de Confirmação
    - Efeito Anchoring
    - Viés de Disponibilidade
    - Viés do Otimismo
    - Efeito Enquadramento
    - Viés do Status Quo
    
    **Como usar:**
    Selecione um viés no menu à esquerda para aprender sobre ele e participar de uma demonstração interativa.
    
    **Objetivo:**
    Ajudar a reconhecer esses vieses em situações do dia-a-dia para tomar decisões mais racionais.
    """)
    
    st.markdown("---")
    st.write("Desenvolvido com Python e Streamlit")
    st.write("Baseado em pesquisas de psicologia cognitiva e economia comportamental")

if __name__ == "__main__":
    main()