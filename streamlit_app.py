$pip install openai
import openai
import streamlit as st

openai.api_key = "sk-V4tlyCU2xeFpN78rf0vZIaNlkhTqXrCokg9B1YrpAlT3BlbkFJShYe8Hvt0RroLngfwZ2JT4_h47n0diF6MUsCIQg6kA"

def main():
    #st.sidebar.header("PREGO GPT")
    st.markdown("<h1 style='text-align: center; color: green ;'>PREGO GPT</h1>", unsafe_allow_html=True)
    st.sidebar.info("AI Tool for PREGO use")
    st.sidebar.info("Start with the first option before moving to the next")
    op = st.sidebar.selectbox("steps",["Cotizacion","Ruta","Mantenimientos"])
    if op == "Cotizacion":
        cotizacion()

    elif op == "Ruta":
        ruta()
    
    elif op == "Mantenimientos":
        mantenimientos()
    
def OptionSelections(prompt):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-V3",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        pressence_penalty=0
    )
    return response.choices[0].text

def cotizacion():
    #st.header("Generador de Cotizaciones")
    st.info("Para generar una cotizacion por favor sigue el patron mostrado")
    prompt = st.text_area("Escribe la descripcion de la cotizacion")
    if st.button("Enviar"):
        st.text(OptionSelections(prompt))
