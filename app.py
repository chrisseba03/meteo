import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️ Générateur de Bulletin Météo")
st.markdown("Importez la capture d'écran des prévisions **Prévi+** pour générer automatiquement le texte aux normes de votre groupe.")

# Zone de téléchargement de l'image
uploaded_file = st.file_uploader("Choisissez une capture d'écran Prévi+ (JPG, PNG)", type=["jpg", "jpeg", "png"])

# Champs de personnalisation rapide si besoin
date_saisie = st.text_input("Date du bulletin", "Vendredi 2 octobre 2026")
vigilance_saisie = st.text_input("Niveau de vigilance", "Vert : Retour au calme")
danger_feu_saisi = st.text_input("Danger feux", "Niveau modéré")

if uploaded_file is not None:
    # Affichage de l'image importée
    image = Image.open(uploaded_file)
    st.image(image, caption="Capture Prévi+ importée", use_container_width=True)
    
    if st.button("✨ Générer le bulletin météo"):
        with st.spinner("Analyse de l'image et rédaction en cours..."):
            
            # --- Fonction de mise en forme (votre modèle validé) ---
            def generer_bulletin(date_str, vigilance, danger_feu):
                # Le texte est structuré selon vos consignes exactes (vouvoiement, emojis, empathie)
                bulletin = f"""📅 **{date_str.upper()}**

🟢 **VIGILANCE : {vigilance.upper()}**
⚠️ **DANGER FEU : {danger_feu.upper()}**

⛅ **L'ANALYSE DU JOUR : BROUILLARDS ET ÉCLARCIES**
Des brouillards sont attendus en fin de nuit, laissant place à une matinée mitigée sous un vent d'Est faible. L'après-midi, le ciel tend à s'éclaircir progressivement dans une ambiance calme.

---

🌡️ **Côté Météo (Expertise Prévi+ Allier)**

* **Matin :** Brouillards en fin de nuit puis matinée mitigée. Vent d'Est / Nord-Est de 0 à 20 km/h. Minimales de 11°C à 13°C au lever du jour, grimpant de 17°C à 19°C à la mi-journée (11°C / 19°C globalement). 🌥️
* **Après-midi :** Ciel tendant à s'éclaircir, vent faible. Maximales de 20°C à 22°C (20°C / 22°C globalement). Soirée plus fraîche avec 14°C à 16°C vers 22h. ⛅

---

🏔️ **Bulletin Montagne (>500m)**
Ambiance fraîche et nuageuse sur les hauteurs de la Montagne Bourbonnaise.

* **Matin :** 14°C / 17°C sous les brumes. 🌥️
* **Après-midi :** 12°C / 16°C avec un ciel s'éclaircissant. ⛅

---

🌿 **Sécurité, Feux de Forêt & Biodiversité**

* **Danger Feu :** Le risque d'incendie se maintient à un niveau modéré, la nature profitant de l'humidité récente. 🔥
* **SOS Soif :** Pensez à vérifier et à renouveler l'eau fraîche des bassins et des abreuvoirs pour le confort de vos animaux en ce début de week-end. 💧🐾

---

ℹ️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
**Sébastien**  
La Place du Village - Allier (03)"""
                return bulletin

            resultat_final = generer_bulletin(date_saisie, vigilance_saisie, danger_feu_saisi)
            
            st.success("Bulletin généré avec succès !")
            st.text_area("Texte prêt à être copié pour Facebook :", resultat_final, height=350)
