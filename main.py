import streamlit as st

# Fonction pour recommander une proposition avec pondération et argumentaire détaillé
def recommander_proposition(fiabilite, cout_initial, productivite, impact_environnemental, offshore, phase_pilote):
    # Pondérations des critères
    pond_fiabilite = 10
    pond_cout_initial = 6
    pond_productivite = 8
    pond_impact = 7
    pond_offshore = 9
    pond_phase_pilote = 5
    
    # Calcul des scores basés sur les réponses
    score_gs10_xi = 0
    score_gs6_ap = 0
    score_gs10_ap = 0
    
    # Fiabilité et disponibilité (plus important si "Oui")
    if fiabilite == "Oui":
        score_gs10_xi += pond_fiabilite
    else:
        score_gs6_ap += pond_fiabilite
    
    # Coût initial (plus important si "Oui")
    if cout_initial == "Oui":
        score_gs6_ap += pond_cout_initial
    else:
        score_gs10_xi += pond_cout_initial
    
    # Productivité énergétique (plus important si "Production maximale recherchée")
    if productivite == "Production maximale recherchée":
        score_gs10_ap += pond_productivite
    else:
        score_gs10_xi += pond_productivite
    
    # Impact environnemental (plus important si "Oui")
    if impact_environnemental == "Oui":
        score_gs10_xi += pond_impact
    else:
        score_gs6_ap += pond_impact
    
    # Adaptation aux contraintes offshore (plus important si "Oui")
    if offshore == "Oui":
        score_gs10_xi += pond_offshore
    else:
        score_gs6_ap += pond_offshore
        score_gs10_ap += pond_offshore
    
    # Phase pilote (plus important si "Oui")
    if phase_pilote == "Oui":
        score_gs10_xi += pond_phase_pilote
    else:
        score_gs6_ap += pond_phase_pilote
        score_gs10_ap += pond_phase_pilote
    
    # Décision finale : la solution avec le score le plus élevé est recommandée
    if max(score_gs10_xi, score_gs6_ap, score_gs10_ap) == score_gs10_xi:
        return "GS10 Xi (synchrone à excitation séparée)", "La GS10 Xi est idéale en raison de sa fiabilité, son adaptation aux contraintes offshore et son impact environnemental limité. Elle est particulièrement recommandée si la fiabilité est essentielle et si vous souhaitez minimiser les risques à long terme. Sa phase pilote permettra de tester la solution avant sa mise en œuvre finale."
    
    elif max(score_gs10_xi, score_gs6_ap, score_gs10_ap) == score_gs6_ap:
        return "GS6 AP (synchrone aimants permanents)", "La GS6 AP est la solution la plus économique avec un bon compromis entre fiabilité et coût. Elle est recommandée si le coût initial est une contrainte majeure tout en garantissant un rendement acceptable. Bien que légèrement moins performant que la GS10, elle offre une bonne solution pour des projets terrestres ou des projets offshore limités."
    
    else:
        return "GS10 AP (synchrone aimants permanents)", "La GS10 AP est idéale pour maximiser la productivité énergétique, avec un rendement exceptionnel. Elle est la solution la plus adaptée si la priorité est de maximiser l'efficacité énergétique tout en restant dans un compromis coût/efficacité acceptable. Elle est aussi un bon choix pour des projets où les contraintes environnementales sont modérées."

# Titre et introduction
st.title("Sélection de la Meilleure Proposition")
st.write("Répondez aux questions suivantes pour obtenir la meilleure offre en fonction de vos priorités.")

# Formulaire pour les critères
fiabilite = st.radio("1. La fiabilité et la disponibilité sont-elles des critères essentiels pour vous ?", ["Oui", "Non"])
cout_initial = st.radio("2. Le coût initial est-il un facteur limitant pour vous ?", ["Oui", "Non"])
productivite = st.radio("3. Quelle priorité accordez-vous à la maximisation de la productivité énergétique ?", ["Production maximale recherchée", "Priorité secondaire"])
impact_environnemental = st.radio("4. L'impact environnemental, notamment l'utilisation de terres rares, est-il un critère décisif dans votre choix ?", ["Oui", "Non"])
offshore = st.radio("5. Votre projet est-il principalement destiné à des conditions offshore nécessitant une solution spécifique ?", ["Oui", "Non"])
phase_pilote = st.radio("6. Êtes-vous prêt à accepter une phase pilote pour tester la solution avant sa mise en production définitive ?", ["Oui", "Non"])

# Calcul de la meilleure proposition
if st.button("Trouver la meilleure offre"):
    proposition, raison = recommander_proposition(fiabilite, cout_initial, productivite, impact_environnemental, offshore, phase_pilote)
    st.subheader(f"Proposition recommandée : {proposition}")
    st.write(raison)
