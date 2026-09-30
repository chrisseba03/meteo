import streamlit as st
import datetime
from PIL import Image
from google import genai

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️ Assistant Météo Intelligent (IA Gemini)")
st.markdown("Importez votre capture Prévi+ : l'intelligence artificielle la lit, extrait les données et rédige votre bulletin toute seule !")

# --- Configuration de la clé API ---
api_key_saisie = st.text_input("Clé API Google Gemini (optionnel si configurée dans Streamlit)", type="password")

# --- 1. Paramètres principaux ---
col_d1, col_d2 = st.columns(2)
with col_d1:
    date_defaut = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
    date_formatee = st.text_input("Date du bulletin (JJ/MM/AAAA)", date_defaut)
with col_d2:
    vigilance_saisie = st.text_input("Niveau de vigilance", "Verte : Retour au calme")
    danger_feu_saisi = st.text_input("Danger feux", "Faible à modéré")

# --- 2. Module d'import de la capture d'écran ---
st.markdown("### 📥 Capture d'écran Prévi+")
image_file = st.file_uploader("Glissez la capture d'écran des prévisions ici (JPG, PNG)", type=["jpg", "jpeg", "png"])

image_recuperee = None
if image_file is not None:
    image_recuperee = Image.open(image_file)
    st.image(image_recuperee, caption="Capture prête pour analyse par l'IA", use_container_width=True)

notes_perso = st.text_input("Ajouter une petite note personnelle ou consigne pour l'IA (optionnel)", "")

# --- 3. Bouton d'automatisation par l'IA ---
if st.button("✨ Lancer l'IA pour rédiger le bulletin"):
    if image_recuperee is None:
        st.warning("Veuillez d'abord importer une capture d'écran.")
    else:
        with st.spinner("L'intelligence artificielle analyse l'image et rédige le bulletin..."):
            try:
                # Initialisation du client GenAI
                client = genai.Client(api_key=api_key_saisie if api_key_saisie else None)
                
                # Consigne stricte pour l'IA
                prompt_ia = f"""
                Analyse cette capture d'écran météorologique de Prévi+ pour l'Allier.
                Extrais les informations clés pour rédiger un bulletin météo destiné à un groupe Facebook local.
                
                Règles de rédaction strictes :
                1. Rédige avec de l'empathie, de la positivité et de la joie.
                2. Utilise le vouvoiement.
                3. Ne mets AUCUNE étoile (pas de formatage en gras avec des **).
                4. Structure ta réponse en renvoyant clairement :
                   - Le titre de l'analyse
                   - Le paragraphe de l'analyse générale
                   - Le résumé du matin et de l'après-midi
                   - Les informations pour la Montagne Bourbonnaise
                
                Consigne supplémentaire de l'administrateur : {notes_perso}
                """
                
                # Appel au modèle Gemini 2.5 Flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_recuperee, prompt_ia]
                )
                
                texte_ia_brut = response.text
                
                # Construction finale rigoureuse aux couleurs de votre groupe (sans étoiles)
                bulletin_genere = f"""📅 {date_formatee}

🟢 VIGILANCE {vigilance_saisie.upper()}
⚠️ DANGER FEU : {danger_feu_saisi.upper()}

⛅ L'ANALYSE DU JOUR

{texte_ia_brut}

---

🌿 Sécurité, Feux de Forêt & Biodiversité

* Danger Feu : Le risque d'incendie se maintient à un niveau {danger_feu_saisi.lower()}, la nature profitant de l'accalmie. 🔥
* SOS Soif : Profitez de cette belle journée pour renouveler l'eau fraîche des abreuvoirs et veiller au bien-être de vos animaux de compagnie. 💧🐾

---

ℹ️️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
Sébastien  
La Place du Village - Allier (03)"""

                st.success("Analyse terminée avec succès par l'IA !")
                st.text_area("Copiez le texte ci-dessous pour Facebook :", bulletin_genere, height=450)

            except Exception as e:
                st.error(f"Erreur lors de la communication avec l'IA : {e}")
