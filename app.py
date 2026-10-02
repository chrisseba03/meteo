import streamlit as st
import datetime
from PIL import Image
from google import genai

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️️ Assistant Météo Intelligent (IA Gemini)")
st.markdown("Importez une capture d'écran **ou** collez vos informations brutes : l'intelligence artificielle s'occupe du reste !")

# --- 1. Paramètres principaux ---
col_d1, col_d2 = st.columns(2)
with col_d1:
    date_defaut = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
    date_formatee = st.text_input("Date du bulletin (JJ/MM/AAAA)", date_defaut)
with col_d2:
    vigilance_saisie = st.text_input("Niveau de vigilance", "Verte : Retour au calme")
    danger_feu_saisi = st.text_input("Danger feux", "Faible à modéré")

# --- 2. Module d'import (Image OU Texte brut) ---
st.markdown("### 📥 Source des données météo")
type_source = st.radio("Choisissez votre méthode :", ["Importer une capture d'écran", "Coller du texte brut"], horizontal=True)

image_recuperee = None
texte_brut_fourni = ""

if type_source == "Importer une capture d'écran":
    image_file = st.file_uploader("Glissez la capture d'écran des prévisions ici (JPG, PNG)", type=["jpg", "jpeg", "png"])
    if image_file is not None:
        image_recuperee = Image.open(image_file)
        st.image(image_recuperee, caption="Capture prête pour analyse par l'IA", use_container_width=True)
else:
    texte_brut_fourni = st.text_area("Collez vos notes, températures ou prévisions brutes ici :", height=150, placeholder="Ex: Temps couvert ce matin avec 14°C, belles éclaircies cet l'après-midi et 23°C prévus...")

notes_perso = st.text_input("Ajouter une petite note personnelle ou consigne pour l'IA (optionnel)", "")

# --- 3. Bouton d'automatisation par l'IA ---
if st.button("✨ Lancer l'IA pour rédiger le bulletin"):
    if image_recuperee is None and not texte_brut_fourni.strip():
        st.warning("Veuillez d'abord importer une capture d'écran ou coller du texte.")
    else:
        with st.spinner("L'intelligence artificielle rédige le bulletin avec le sourire..."):
            try:
                # Initialisation sécurisée via les secrets configurés sur Streamlit Cloud
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                # Consigne stricte pour l'IA
                prompt_ia = f"""
                Rédige un bulletin météo destiné à un groupe Facebook local pour l'Allier en te basant sur les éléments fournis.
                
                Règles de rédaction strictes :
                1. Rédige avec de l'empathie, de la positivité et de la joie.
                2. Utilise le vouvoiement.
                3. Ne mets AUCUNE étoile (pas de formatage en gras avec des **).
                4. Structure ta réponse en renvoyant clairement :
                   - Le titre de l'analyse
                   - Le paragraphe de l'analyse générale
                   - Le résumé du matin et de l'après-midi
                   - Les informations pour la Montagne Bourbonnaise
                
                Éléments textuels fournis par l'administrateur : {texte_brut_fourni}
                Consigne supplémentaire : {notes_perso}
                """
                
                # Préparation du contenu à envoyer à l'IA (image ou texte)
                contenu_requete = [prompt_ia]
                if image_recuperee is not None:
                    contenu_requete.append(image_recuperee)
                
                # Appel au modèle
                response = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=contenu_requete
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

ℹ️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
Sébastien  
La Place du Village - Allier (03)"""

                st.success("Analyse terminée avec succès par l'IA !")
                st.text_area("Copiez le texte ci-dessous pour Facebook :", bulletin_genere, height=450)

            except Exception as e:
                if "503" in str(e):
                    st.warning("Le serveur de l'IA connaît un petit pic de trafic passager. Patientez quelques secondes et relancez le bouton ! 🌤️")
                else:
                    st.error(f"Erreur lors de la communication avec l'IA : {e}")
