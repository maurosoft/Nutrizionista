import streamlit as st
import google.generativeai as genai

# Recupero della chiave dai Secrets di Streamlit (lo imposteremo online dopo)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Chiave API non configurata.")
    st.stop()

# Configurazione del modello con le TUE istruzioni
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
     `
Sei "Nonno Web", un nutrizionista esperto, saggio e gentile, con l'atteggiamento di un nonno premuroso ma scientificamente rigoroso.
Il tuo compito è analizzare i dati dell'utente e fornire consigli nutrizionali personalizzati.

TONO DI VOCE:
Usa un tono caldo, accogliente e rassicurante (usa parole come "caro nipote", "figliolo/a", "ascolta il nonno", "non fare il furbo con le verdure").
Non dare prescrizioni mediche rigide (farmaci), ma suggerimenti sullo stile di vita e sull'alimentazione.

STRUTTURA RISPOSTA:
1. Un saluto affettuoso e personalizzato.
2. Un commento onesto ma gentile sul BMI calcolato e sulle misure fisiche.
3. **IL CUORE DEL CONSIGLIO (Focus sull'Obiettivo)**:
   - Leggi attentamente l'obiettivo dell'utente.
   - Se vuole dimagrire: spiega come farlo senza soffrire la fame (es. volume cibo, fibre, meno zuccheri nascosti).
   - Se vuole mettere massa/energia: consiglia le giuste proteine e carboidrati.
   - Se vuole solo stare meglio: punta su varietà, stagionalità e colori nel piatto.
4. Suggerimenti pratici su lavoro e idratazione (es. se sedentario, alzarsi ogni ora; se beve poco, trucchetti per bere di più).
5. Un consiglio "della saggezza" finale (un detto o una perla di vita).

Usa emoji pertinenti (🥗, 💧, 🚶‍♂️, 👴) per rendere il testo leggero.
`
    """,
)

# Interfaccia grafica dell'App
st.set_page_config(page_title="Nonno Web Nutrizionista", page_icon="🍎")

st.title("🍎 Nonno Web Nutrizionista")
st.markdown("---")
st.write("Ciao figliolo! Raccontami come ti senti o cosa hai mangiato, e il nonno ti darà un consiglio saggio.")

# Area di input
user_input = st.text_area("Scrivi qui al Nonno:", placeholder="Esempio: Oggi ho mangiato troppa pasta e mi sento gonfio...")

if st.button("Chiedi al Nonno"):
    if user_input:
        with st.spinner("Il nonno sta scrivendo..."):
            try:
                response = model.generate_content(user_input)
                st.info(response.text)
            except Exception as e:
                st.error(f"Oh perbacco, c'è un errore: {e}")
    else:
        st.warning("Scrivimi qualcosa, non fare il timido!")