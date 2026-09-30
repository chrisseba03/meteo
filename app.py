import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️ Générateur de Bulletin Météo")
st.markdown("Préparez votre publication à l'avance pour le lendemain ou les jours suivants.")

# --- Sélection de la date cible ---
col_d1, col_d2 = st.columns(2)
with col_d1:
    # Par défaut, propose la date du lendemain pour vos publications anticipées
    date_visee = st.date_input("Date du bulletin", datetime.date.today() + datetime.timedelta(days=1))
with col_d2:
    vigilance_saisie = st.text_input("Niveau de vigilance", "Vert : Retour au calme")
    danger_feu_saisi = st.text_input("Danger feux", "Niveau modéré")

# Formattage de la date en français (ex: "Jeudi 1er octobre 2026")
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois_annee = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

nom_jour = jours_semaine[date_visee.weekday()]
num_jour = "1er" if date_visee.day == 1 else str(date_visee.day)
nom_mois = mois_annee[date_visee.month - 1]
annee = date_visee.year

date_formatee = f"{nom_jour} {num_jour} {nom_mois} {annee}"

# --- Zones de saisie ---
donnees_brutes = st.text_area("Texte ou données brutes (matin, après-midi, tendances...)", 
                              placeholder="Collez ici les éléments de Prévi+ pour ce jour-là...")

notes_perso = st.text_area("Vos notes personnelles ou remarques du jour (optionnel)", 
                           placeholder="Ex: Une petite pensée pour ceux qui préparent les récoltes...")

if st.button("✨ Générer le bulletin météo"):
    with st.spinner("Mise en forme en cours..."):
        
        bulletin_genere = f"""📅 **{date_formatee.upper()}**

🟢 **VIGILANCE : {vigilance_saisie.upper()}**
⚠️ **DANGER FEU : {danger_feu_saisi.upper()}**

⛅ **L'ANALYSE DU JOUR**
{donnees_brutes if donnees_brutes else "Des conditions à suivre de près pour notre département."}

{f"*{notes_perso}*" if notes_perso else ""}

---

🌡️ **Côté Météo (Expertise Prévi+ Allier)**

* **Matin :** Analyse des températures et du vent au lever du jour. 🌥️
* **Après-midi :** Évolution des conditions et des maximales. ⛅

---

🏔️ **Bulletin Montagne (>500m)**
Ambiance sur les hauteurs de la Montagne Bourbonnaise.

* **Matin :** Conditions fraîches ou nuageuses. 🌥️
* **Après-midi :** Évolution sur les reliefs. ☀️

---

🌿 **Sécurité, Feux de Forêt & Biodiversité**

* **Danger Feu :** Le risque d'incendie se maintient à un niveau modéré. Restez prudents en milieu naturel. 🔥
* **SOS Soif :** Pensez à vérifier et à renouveler régulièrement l'eau fraîche des bassins et des abreuvoirs pour le confort de vos animaux. 💧🐾

---

ℹ️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
**Sébastien**  
La Place du Village - Allier (03)"""

        st.success(f"Votre bulletin pour le **{date_formatee}** est prêt !")
        st.text_area("Copiez le texte ci-dessous pour votre publication Facebook :", bulletin_genere, height=400)
