import streamlit as st

def recommander_offre():
    st.title("Sélection de la Meilleure Offre")

    # Collecte des réponses utilisateur
    fiabilite_prioritaire = st.selectbox(
        "La fiabilité et la disponibilité sont-elles prioritaires ?",
        ("Oui", "Non")
    )

    cout_initial_contrainte = st.selectbox(
        "Le coût initial est-il une contrainte forte ?",
        ("Oui", "Non")
    )

    productivite_energetique = st.selectbox(
        "Quelle priorité pour la productivité énergétique ?",
        ("Production maximale recherchée", "Priorité secondaire")
    )

    reduction_impacts_environnementaux = st.selectbox(
        "La réduction des impacts environnementaux est-elle clé ?",
        ("Oui", "Non")
    )

    solution_offshore = st.selectbox(
        "Préférez-vous une solution adaptée aux contraintes offshore ?",
        ("Oui", "Non")
    )

    phase_pilote = st.selectbox(
        "Phase pilote acceptée pour tester la solution ?",
        ("Oui", "Non")
    )

    # Données supplémentaires : Disponibilité, Rendement, Coût
    disponibilites = {
        "GS10 Xi": 96.6,
        "GENIALEC": 96.5,
        "SEMERON": 96.7
    }

    rendements = {
        "GS10 Xi": 96.5,
        "GENIALEC": 96.8,
        "SEMERON": 96.7
    }

    couts = {
        "GS10 Xi": 3.0,
        "GENIALEC": 3.2,
        "SEMERON": 3.3
    }

    # Pondération des critères
    poids_fiabilite = 0.3 if fiabilite_prioritaire == "Oui" else 0.1
    poids_cout = 0.4 if cout_initial_contrainte == "Oui" else 0.2
    poids_rendement = 0.2 if productivite_energetique == "Production maximale recherchée" else 0.1
    poids_impact = 0.1 if reduction_impacts_environnementaux == "Oui" else 0.05
    poids_offshore = 0.1 if solution_offshore == "Oui" else 0.05
    poids_pilote = 0.1 if phase_pilote == "Oui" else 0.05

    # Calcul du score pour chaque machine
    scores = {}

    for modele in ["GS10 Xi", "GENIALEC", "SEMERON"]:
        score = 0
        
        # Fiabilité et disponibilité
        score += poids_fiabilite * (disponibilites[modele] / 100)
        
        # Rendement
        score += poids_rendement * (rendements[modele] / 100)
        
        # Coût
        score -= poids_cout * (couts[modele] / 3.5)  # Normalisation du coût (le plus bas est préférable)
        
        # Impact environnemental
        if modele == "GS10 Xi" and reduction_impacts_environnementaux == "Oui":
            score += poids_impact  # GS10 Xi est plus adapté aux critères environnementaux
        
        # Adaptation offshore
        if modele == "GS10 Xi" and solution_offshore == "Oui":
            score += poids_offshore
        
        # Phase pilote
        if modele == "GS10 Xi" and phase_pilote == "Oui":
            score += poids_pilote
        
        scores[modele] = score

    # Trouver le modèle avec le score maximal
    meilleure_offre = max(scores, key=scores.get)

    # Affichage de la proposition
    st.write(f"Proposition recommandée : {meilleure_offre}")

    # Raison de la recommandation
    if meilleure_offre == "GS10 Xi":
        st.write("Raison : Solution fiable, rendement élevé et coût compétitif avec une excellente disponibilité. Adaptée aux préoccupations environnementales et offshore.")
    elif meilleure_offre == "GENIALEC":
        st.write("Raison : Rendement supérieur et bonne disponibilité, mais légèrement plus coûteuse.")
    else:
        st.write("Raison : Solution avec une très bonne disponibilité et rendement élevé, mais coût légèrement plus élevé sur 20 ans.")

# Appel de la fonction
if __name__ == "__main__":
    recommander_offre()
