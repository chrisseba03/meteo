import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️ Générateur de Bulletin Météo")
st.markdown("Renseignez les détails pour obtenir votre publication prête à poster sur Facebook.")

# --- 1. Paramètres principaux ---
col_d1, col_d2 = st.columns(2)
with col_d1:
    date_visee = st.date_input("Date du bulletin", datetime.date.today() + datetime.timedelta(days=1))
with col_d2:
    vigilance_saisie = st.text_input("Niveau de vigilance", "Verte : Retour au calme")
    danger_feu_saisi = st.text_input("Danger feux", "Faible à modéré")

# Formattage de la date en français
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois_annee = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

nom_jour = jours_semaine[date_visee.weekday()]
num_jour = "1er" if date_visee.day == 1 else str(date_visee.day)
nom_mois = mois_annee[date_visee.month - 1]
annee = date_visee.year
date_formatee = f"{nom_jour} {num_jour} {nom_mois} {annee}"

# --- 2. Champs de saisie détaillés (pour coller le contenu exact) ---
st.markdown("### 📝 Contenu du bulletin")
titre_analyse = st.text_input("Titre de l'analyse (ex: ÉCLAIRCIES ET PASSAGES NUAGEUX)", "ÉCLAIRCIES ET PASSAGES NUAGEUX")
texte_analyse = st.text_area("Paragraphe de l'analyse du jour", "La journée s'annonce agréable avec une alternance d'éclaircies et de passages nuageux sous un vent nul à très faible. La douceur domine avec des températures proches des moyennes de saison.")

st.markdown("---")
matin_meteo = st.text_area("Côté Météo - Matin", "Éclaircies et passages nuageux. Vent nul. Minimales de 11°C à 13°C au lever du jour, grimpant de 18°C à 20°C à la mi-journée (globalement 11°C / 20°C).")
apres_midi_meteo = st.text_area("Côté Météo - Après-midi", "Éclaircies et passages nuageux persistants. Vent très faible. Maximales de 22°C à 24°C, puis une soirée plus douce affichant 17°C à 19°C vers 22h (globalement 20°C / 24°C).")

st.markdown("---")
montagne_matin = st.text_input("Bulletin Montagne - Matin", "12°C / 21°C sous des nuances de gris et d'éclaircies.")
montagne_apres_midi = st.text_input("Bulletin Montagne - Après-midi", "16°C / 21°C dans une ambiance douce et lumineuse.")

st.markdown("---")
sos_soif_texte = st.text_area("Section SOS Soif / Biodiversité", "Profitez de cette belle journée pour renouveler l'eau fraîche des abreuvoirs et veiller au bien-être de vos animaux de compagnie.")

# --- 3. Génération du bulletin final ---
if st.button("✨ Générer le bulletin météo exact"):
    with st.spinner("Mise en forme rigoureuse en cours..."):
        
        bulletin_genere = f"""📅 **{date_formatee.upper()}**

🟢 **VIGILANCE {vigilance_saisie.upper()}**
⚠️ **DANGER FEU : {danger_feu_saisi.upper()}**

⛅ **L'ANALYSE DU JOUR : {titre_analyse.upper()}**

{texte_analyse}

---

🌡️ **Côté Météo (Expertise Prévi+ Allier)**

* **Matin :** {matin_meteo} 🌤️
* **Après-midi :** {apres_midi_meteo} ⛅

---

🏔️ **Bulletin Montagne (>500m)**
Ambiance sur les hauteurs de la Montagne Bourbonnaise.

* **Matin :** {montagne_matin} 🌤️
* **Après-midi :** {montagne_apres_midi} ⛅

---

🌿 **Sécurité, Feux de Forêt & Biodiversité**

* **Danger Feu :** Le risque d'incendie se maintient à un niveau {danger_feu_saisi.lower()}, la nature profitant de l'accalmie. 🔥
* **SOS Soif :** {sos_soif_texte} 💧🐾

---

ℹ️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
**Sébastien**  
La Place du Village - Allier (03)"""

        st.success("Votre bulletin est parfaitement mis en forme !")
        st.text_area("Copiez le texte ci-dessous :", bulletin_genere, height=450)
