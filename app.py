import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Générateur Météo - La Place du Village", page_icon="🌤️", layout="centered")

st.title("🌤️ Générateur de Bulletin Météo Automatique")
st.markdown("Renseignez ou collez les éléments du jour pour générer votre publication prête pour Facebook.")

# --- Formulaire de saisie ---
col1, col2 = st.columns(2)
with col1:
    date_saisie = st.text_input("Date du bulletin", "Mercredi 30 septembre 2026")
    vigilance_saisie = st.text_input("Niveau de vigilance", "Jaune : Orages et pluies")
with col2:
    danger_feu_saisi = st.text_input("Danger feux", "Niveau modéré")
    
# Zone pour coller les données brutes ou les grandes lignes
donnees_brutes = st.text_area("Texte ou données brutes (matin, après-midi, montagnes...)", 
                              placeholder="Collez ici les éléments du bulletin ou de Prévi+...")

# Zone pour vos notes personnelles / touches humaines
notes_perso = st.text_area("Vos notes personnelles ou remarques du jour (optionnel)", 
                           placeholder="Ex: Petite pensée pour nos jardins qui avaient bien besoin de cette eau...")

if st.button("✨ Générer le bulletin météo"):
    with st.spinner("Mise en forme selon vos critères en cours..."):
        
        # Logique de construction du bulletin avec vos critères stricts
        bulletin_genere = f"""📅 **{date_saisie.upper()}**

🟡 **VIGILANCE : {vigilance_saisie.upper()}**
⚠️ **DANGER FEU : {danger_feu_saisi.upper()}**

⛈️ **L'ANALYSE DU JOUR**
{donnees_brutes if donnees_brutes else "Une perturbation traverse le pays et apporte un changement de temps bienvenu."}

{f"*{notes_perso}*" if notes_perso else ""}

---

🌡️ **Côté Météo (Expertise Prévi+ Allier)**

* **Matin :** Analyse des températures et du vent au lever du jour. 🌥️
* **Après-midi :** Évolution des conditions et des maximales. ⚡🌧️

---

🏔️ **Bulletin Montagne (>500m)**
Ambiance sur les hauteurs de la Montagne Bourbonnaise.

* **Matin :** Conditions fraîches ou nuageuses. 🌥️
* **Après-midi :** Évolution sur les reliefs. ⛈️

---

🌿 **Sécurité, Feux de Forêt & Biodiversité**

* **Danger Feu :** Le risque d'incendie se maintient à un niveau modéré. Restez prudents en milieu naturel. 🔥
* **SOS Soif :** Pensez à vérifier et à renouveler régulièrement l'eau fraîche des bassins et des abreuvoirs pour le confort de vos animaux. 💧🐾

---

ℹ️ Retrouvez toutes les prévisions actualisées sur https://previplus.fr/

Amicalement,  
**Sébastien**  
La Place du Village - Allier (03)"""

        st.success("Votre bulletin est prêt !")
        st.text_area("Copiez le texte ci-dessous pour votre publication Facebook :", bulletin_genere, height=400)
