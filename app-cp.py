import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta 

# Charger les données
df = pd.read_excel('telecom -orange.xlsx', engine='openpyxl')

# Fonction pour convertir le DataFrame en CSV
def convert_df_to_csv(df):
    csv = df.to_csv(index=False)
    return csv

# Afficher la date actuelle avec formatage HTML pour ajuster la taille de la police
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.markdown(f"<p style='font-size: 16px; color: black;'>Date actuelle : {current_date}</p>", unsafe_allow_html=True)
st.sidebar.title("Analyse des Projets Fibre et Télécom")
st.sidebar.image('data:image/png;base64,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')

# Menu utilisateur
user_menu = st.sidebar.radio(
    'Choisissez une option',
    ('Aperçu général', 'Analyse par Ville et Année', 'Analyse par Date Fin', 'Analyse spécifique aux Projets')
)

# Convertir les colonnes en types numériques
df['Distance Autorisation / ml'] = pd.to_numeric(df['Distance Autorisation / ml'], errors='coerce')
df['Redevance / ml'] = pd.to_numeric(df['Redevance / ml'], errors='coerce')
df['Nombre de chambres'] = pd.to_numeric(df['Nombre de chambres'], errors='coerce')
df['Redevance / Chambre'] = pd.to_numeric(df['Redevance / Chambre'], errors='coerce')
df['Total Redevance'] = pd.to_numeric(df['Total Redevance'], errors='coerce')
df['Date Fin'] = pd.to_datetime(df['Date Fin'], errors='coerce', format='%d/%m/%Y')
df['Date début'] = pd.to_datetime(df['Date début'], errors='coerce', format='%d/%m/%Y')
df = df.drop(columns=['Année', 'Durée en jours'])
# Nettoyer les noms de colonnes
df.columns = df.columns.str.strip()

# Aperçu général
if user_menu == 'Aperçu général':
    # Fonction pour formater les grandes valeurs en format abrégé
    def format_abbreviation(value):
        if value >= 1_000_000:
            return f"{value / 1_000_000:.1f}M"  # Millions
        elif value >= 1_000:
            return f"{value / 1_000:.1f}k"  # Milliers
        else:
            return f"{value:.2f}"
    # Calcul des statistiques globales
    annees = df['Année de réalisation'].nunique()  # Nombre d'années distinctes
    villes = df['Ville'].nunique()  # Nombre de villes distinctes
    total_projets = df.shape[0]  # Nombre total de projets

    # Calcul des sommes pour les colonnes numériques
    somme_distance = df['Distance Autorisation / ml'].fillna(0).sum()  # Somme des distances
    somme_redevance = df['Total Redevance'].fillna(0).sum()  # Somme des redevances

    # Nombre de types de programmes distincts
    types_programme = df['Programme'].nunique()

    # Affichage dans Streamlit
    st.markdown("<h1 style='font-size: 32px;'>Top Statistics</h1>", unsafe_allow_html=True)

    # Première ligne de statistiques avec tailles de police ajustées
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<h3 style='font-size: 20px;'>Villes</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #FF6347; font-size: 18px;'>{villes}</h2>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h3 style='font-size: 20px;'>Années</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #4682B4; font-size: 18px;'>{annees}</h2>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<h3 style='font-size: 20px;'>Projets</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #32CD32; font-size: 18px;'>{total_projets}</h2>", unsafe_allow_html=True)

    # Deuxième ligne de statistiques avec tailles de police ajustées
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<h3 style='font-size: 20px;'>Distance Totale (ml)</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #FFD700; font-size: 18px;'>{format_abbreviation(somme_distance)}</h2>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h3 style='font-size: 20px;'>Total Redevance (Dh)</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #8A2BE2; font-size: 18px;'>{format_abbreviation(somme_redevance)}</h2>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<h3 style='font-size: 20px;'>Types de Programmes</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #FF4500; font-size: 18px;'>{types_programme}</h2>", unsafe_allow_html=True)


    st.markdown("<h1 style='font-size:24px;'>Analyse des Projets, Distances et Redevances par Nature Entité</h3>", unsafe_allow_html=True)

    df_projets_nature = df.groupby('Nature Entité').size().reset_index(name='Nombre de Projets')
    fig_projets_nature = px.bar(df_projets_nature, x='Nature Entité', y='Nombre de Projets', 
                                title="Nombre de Projets par Nature Entité", 
                                color='Nature Entité', 
                                barmode='group', 
                                color_discrete_sequence=['#FF4500','#FFA500','#00BFFF','#32CD32','#FFD700', '#FF69B4']  )  
    st.plotly_chart(fig_projets_nature)

    df_distance_nature = df.groupby('Nature Entité')['Distance Autorisation / ml'].sum().reset_index()  
    fig_distance_nature = px.bar(df_distance_nature, x='Nature Entité', y='Distance Autorisation / ml', 
                                title="Distance Autorisation / ml par Nature Entité", 
                                color='Nature Entité', 
                                barmode='group', 
                                color_discrete_sequence=['#00BFFF','#FFD700', '#32CD32', '#FF4500','#FFA500','#FF69B4']  ) 
    st.plotly_chart(fig_distance_nature)

    df_total_redevance_nature = df.groupby('Nature Entité')['Total Redevance'].sum().reset_index() 
    fig_total_redevance_nature = px.bar(df_total_redevance_nature, x='Nature Entité', y='Total Redevance', 
                                        title="Total Redevance par Nature Entité", 
                                        color='Nature Entité', 
                                        barmode='group', 
                                        color_discrete_sequence=['#FFD700','#FF4500', '#FFA500','#00BFFF','#32CD32', '#FF69B4']  )  
    st.plotly_chart(fig_total_redevance_nature)
    
    st.markdown("<h1 style='font-size:24px;'>Analyse des Projets, Distances et Redevances par Types de Programmes</h3>", unsafe_allow_html=True)

    df_projets_programme = df.groupby('Programme').size().reset_index(name='Nombre de Projets')
    fig_projets_programme = px.bar(df_projets_programme, x='Programme', y='Nombre de Projets', 
                                   title="Nombre de Projets par Programme", 
                                   color='Programme', barmode='group',
                                   color_discrete_sequence=['#00BFFF','#32CD32', '#FF4500','#FFA500','#FFD700', '#FF69B4']  )
    st.plotly_chart(fig_projets_programme)

    df_distance_programme = df.groupby('Programme')['Distance Autorisation / ml'].sum().reset_index()  
    fig_distance_programme = px.bar(df_distance_programme, x='Programme', y='Distance Autorisation / ml', 
                                    title="Distance Autorisation / ml par Programme", 
                                    color='Programme', 
                                    barmode='group', 
                                    color_discrete_sequence=['#00BFFF','#32CD32', '#FF4500','#FFA500','#FFD700', '#FF69B4']  )  
    fig_distance_programme.update_traces(hoverinfo="skip")  
    st.plotly_chart(fig_distance_programme)


    df_redevance_programme = df.groupby('Programme')['Total Redevance'].sum().reset_index()
    fig_redevance_programme = px.bar(df_redevance_programme, x='Programme', y='Total Redevance', 
                                    title="Total Redevance par Programme", 
                                    color='Programme', 
                                    barmode='group', 
                                    color_discrete_sequence=['#00BFFF','#32CD32', '#FF4500','#FFA500','#FFD700', '#FF69B4']  )  
    fig_redevance_programme.update_traces(hoverinfo="skip")  
    st.plotly_chart(fig_redevance_programme)

    df_evolution_programme = df.groupby(['Année de réalisation', 'Programme']).size().reset_index(name='Nombre de Projets')
    fig_evolution_programme = px.line(df_evolution_programme, x='Année de réalisation', y='Nombre de Projets', 
                                      color='Programme', 
                                      title="Évolution des Projets par Programme au Fil des Années")
    st.plotly_chart(fig_evolution_programme)

    st.markdown("<h1 style='font-size:24px;'>Analyse des Projets par des Diagrammes circulaires</h3>", unsafe_allow_html=True)
    # Diagramme circulaire des Autorisations
    fig_pie_autorisation = px.pie(df, names='Autorisation', 
                                title="Répartition des Autorisations",
                                hole=0.3,
                                color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700'])  
    st.plotly_chart(fig_pie_autorisation)

    # Répartition des projets avec et sans nom
    projets_counts = df['Nom de projet'].apply(lambda x: 'Avec Nom' if x != 'A Identifier' else 'A Identifier').value_counts()
    fig_nom_projet = px.pie(
        names=projets_counts.index,
        values=projets_counts.values,
        title='Pourcentage des Projets avec Nom vs Aucun Nom',
        color_discrete_sequence=['#FF4500', '#FF8C00'] 
    )
    st.plotly_chart(fig_nom_projet)

    # Diagramme circulaire des Nature Entité
    fig_pie_nature_entite = px.pie(df, names='Nature Entité', 
                                    title="Répartition des Nature Entité",
                                    hole=0.3,
                                    color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700'])  
    st.plotly_chart(fig_pie_nature_entite)
    # Répartition des Programmes
    programme_counts = df['Programme'].value_counts()
    fig_pie_programme = px.pie(
        names=programme_counts.index,
        values=programme_counts.values,
        title='Répartition des Programmes',
        color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700']  
    )
    st.plotly_chart(fig_pie_programme)

    # Distribution des projets à propos de Année de réalisation
    st.markdown("<h1 style='font-size:24px;'>Distribution des projets à propos de Année de réalisation</h3>", unsafe_allow_html=True)

    # Nombre de Projets par Année de réalisation
    df_projets_annee = df.groupby('Année de réalisation').size().reset_index(name='Nombre de Projets')
    fig_projets_annee = px.bar(
        df_projets_annee,
        x='Année de réalisation',
        y='Nombre de Projets',
        title='Nombre de projets par Année de réalisation',
        labels={'Nombre de Projets': 'Nombre de projets'},
        color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700'] 
    )
    st.plotly_chart(fig_projets_annee)

    # Somme des Distances d'Autorisation par Année de Réalisation
    df_distance_annee = df.groupby('Année de réalisation')[['Distance Autorisation / ml']].sum().reset_index()
    fig_distance_annee = px.bar(
        df_distance_annee,
        x='Année de réalisation',
        y='Distance Autorisation / ml',
        title='Somme des Distances d\'Autorisation par Année de Réalisation',
        labels={'Distance Autorisation / ml': 'Distance Autorisation / ml'},
        color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700']  
    )
    st.plotly_chart(fig_distance_annee)

    # Somme des Redevances Totales par Année de Réalisation
    df_redevance_annee = df.groupby('Année de réalisation')[['Total Redevance']].sum().reset_index()
    fig_redevance_annee = px.bar(
        df_redevance_annee,
        x='Année de réalisation',
        y='Total Redevance',
        title='Somme des Redevances Totales par Année de Réalisation',
        labels={'Total Redevance': 'Total Redevance'},
        color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700']
    )
    st.plotly_chart(fig_redevance_annee)

    # Nature Entité à propos de Année de réalisation
    df_nature_annee = df.groupby(['Année de réalisation', 'Nature Entité']).size().reset_index(name='Nombre de Projets')
    fig_nature_annee = px.bar(
        df_nature_annee,
        x='Année de réalisation',
        y='Nombre de Projets',
        color='Nature Entité',
        title='Distribution de Nature Entité à propos de Année de réalisation',
        labels={'y': 'Nombre de Projets', 'color': 'Nature Entité'},
        text_auto=True,
        color_discrete_sequence=['#FF4500', '#FF8C00', '#FFD700']  
    )
    st.plotly_chart(fig_nature_annee)


# Analyse par Ville
if user_menu == 'Analyse par Ville et Année':
    st.sidebar.header("Filtrer par Ville et Année")
    
    # Sélectionner la ville
    villes = df['Ville'].unique().tolist()
    selected_ville = st.sidebar.selectbox("Sélectionnez la Ville", ["Toutes"] + villes)
    
    # Sélectionner l'année
    annees = df['Année de réalisation'].unique().tolist()
    selected_annee = st.sidebar.selectbox("Sélectionnez l'Année", ["Toutes"] + annees)
    
    # Filtrage des données
    if selected_ville != "Toutes" and selected_annee != "Toutes":
        ville_data = df[(df['Ville'] == selected_ville) & (df['Année de réalisation'] == selected_annee)]
    elif selected_ville != "Toutes":
        ville_data = df[df['Ville'] == selected_ville]
    elif selected_annee != "Toutes":
        ville_data = df[df['Année de réalisation'] == selected_annee]
    else:
        ville_data = df

    # Afficher les données filtrées
    st.subheader(f"Projets dans la ville de {selected_ville}" if selected_ville != "Toutes" else "Projets dans toutes les villes")
    st.dataframe(ville_data)
    
   # Analyse des Projets, Distances et Redevances par Nature Entité
    st.subheader(f"Analyse des Projets, Distances et Redevances pour {selected_ville} en {selected_annee}")
    
    df_projets_nature = ville_data.groupby('Nature Entité').size().reset_index(name='Nombre de Projets')
    fig_projets_nature = px.bar(df_projets_nature, x='Nature Entité', y='Nombre de Projets', 
                                title="Nombre de Projets par Nature Entité", 
                                color='Nature Entité', barmode='group',
                                color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
                                )
    st.plotly_chart(fig_projets_nature)

# Distance Autorisation / ml par Nature Entité au fil des années
    df_distance_nature_annee = ville_data.groupby(['Année de réalisation', 'Nature Entité'])['Distance Autorisation / ml'].sum().reset_index()
    fig_distance_nature_annee = px.line(df_distance_nature_annee, x='Année de réalisation', y='Distance Autorisation / ml', 
                                    color='Nature Entité',
                                    title="Évolution des Distances d'Autorisation par Nature Entité",
                                    labels={'Distance Autorisation / ml': 'Distance (ml)'},
                                    color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_distance_nature_annee)

# Total Redevance par Nature Entité au fil des années
    df_redevance_nature_annee = ville_data.groupby(['Année de réalisation', 'Nature Entité'])['Total Redevance'].sum().reset_index()
    fig_redevance_nature_annee = px.line(df_redevance_nature_annee, x='Année de réalisation', y='Total Redevance', 
                                     color='Nature Entité',
                                     title="Évolution du Total Redevance par Nature Entité",
                                     labels={'Total Redevance': 'Redevance Totale'},
                                     color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_redevance_nature_annee)
    # Analyse des Projets, Distances et Redevances par Types de Programmes
    df_projets_programme = ville_data.groupby('Programme').size().reset_index(name='Nombre de Projets')
    fig_projets_programme = px.bar(df_projets_programme, x='Programme', y='Nombre de Projets', 
                                   title="Nombre de Projets par Programme", 
                                   color='Programme', barmode='group')
    st.plotly_chart(fig_projets_programme)

    df_distance_programme = df.groupby('Programme')['Distance Autorisation / ml'].sum().reset_index()  
    fig_distance_programme = px.bar(
        df_distance_programme,
        x='Programme',
        y='Distance Autorisation / ml',
        title="Distance Autorisation / ml par Programme",
        color='Programme',
        barmode='group',
        color_discrete_sequence=['#00BFFF', '#32CD32', '#FF4500', '#FFA500', '#FFD700', '#FF69B4']  
    )
    fig_distance_programme.update_traces(hoverinfo="skip")  
    st.plotly_chart(fig_distance_programme)

    df_redevance_programme = df.groupby('Programme')['Total Redevance'].sum().reset_index()
    fig_redevance_programme = px.bar(
        df_redevance_programme,
        x='Programme',
        y='Total Redevance',
        title="Total Redevance par Programme",
        color='Programme',
        barmode='group',
        color_discrete_sequence=['#00BFFF', '#32CD32', '#FF4500', '#FFA500', '#FFD700', '#FF69B4']  
    )
    fig_redevance_programme.update_traces(hoverinfo="skip")  
    st.plotly_chart(fig_redevance_programme)


    # Évolution des Projets par Programme au fil des années
    df_evolution_programme = ville_data.groupby(['Année de réalisation', 'Programme']).size().reset_index(name='Nombre de Projets')
    fig_evolution_programme = px.line(df_evolution_programme, x='Année de réalisation', y='Nombre de Projets', 
                                      color='Programme', 
                                      title="Évolution des Projets par Programme au Fil des Années",
                                      color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_evolution_programme)

    # Diagrammes circulaires
    st.markdown("<h1 style='font-size:24px;'>Analyse des Projets par Diagrammes Circulaires</h3>", unsafe_allow_html=True)

    fig_pie_autorisation = px.pie(ville_data, names='Autorisation', 
                                  title="Répartition des Autorisations",
                                  hole=0.3,
                                  color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_pie_autorisation)

    projets_counts = ville_data['Nom de projet'].apply(lambda x: 'Avec Nom' if x != 'A Identifier' else 'A Identifier').value_counts()
    fig_nom_projet = px.pie(
        names=projets_counts.index,
        values=projets_counts.values,
        title='Pourcentage des Projets avec Nom vs Aucun Nom',
        color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
    )
    st.plotly_chart(fig_nom_projet)

    fig_pie_nature_entite = px.pie(ville_data, names='Nature Entité', 
                                title="Répartition des Nature Entité",
                                hole=0.3,
                                color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_pie_nature_entite)

    programme_counts = ville_data['Programme'].value_counts()
    fig_pie_programme = px.pie(
        names=programme_counts.index,
        values=programme_counts.values,
        title='Répartition des Programmes',
        color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
    )
    st.plotly_chart(fig_pie_programme)

    # Distribution des projets par année
    st.markdown("<h1 style='font-size:24px;'>Distribution des Projets par Année de réalisation</h3>", unsafe_allow_html=True)

    df_projets_annee = ville_data.groupby('Année de réalisation').size().reset_index(name='Nombre de Projets')
    fig_projets_annee = px.bar(
        df_projets_annee,
        x='Année de réalisation',
        y='Nombre de Projets',
        title='Nombre de Projets par Année de réalisation',
        labels={'Nombre de Projets': 'Nombre de Projets'},
        color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
    )
    st.plotly_chart(fig_projets_annee)

    df_distance_annee = ville_data.groupby('Année de réalisation')['Distance Autorisation / ml'].sum().reset_index()
    fig_line = px.line(df_distance_annee, x='Année de réalisation', y='Distance Autorisation / ml',
                       title="Évolution des Distances d'Autorisation par Année",
                       labels={'Distance Autorisation / ml': 'Distance (ml)'},
                       color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
    st.plotly_chart(fig_line)


   # Somme des Redevances Totales par Année de Réalisation
    df_redevance_annee = ville_data.groupby('Année de réalisation')[['Total Redevance']].sum().reset_index()
    fig_redevance_annee = px.bar(
        df_redevance_annee,
        x='Année de réalisation',
        y='Total Redevance',
        title='Somme des Redevances Totales par Année de Réalisation',
        labels={'Total Redevance': 'Total Redevance'},
        color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
    )
    st.plotly_chart(fig_redevance_annee)

    # Nature Entité par Année de Réalisation
    
    df_nature_annee = ville_data.groupby(['Année de réalisation', 'Nature Entité']).size().reset_index(name='Nombre de Projets')
    fig_nature_annee = px.bar(
            df_nature_annee,
            x='Année de réalisation',
            y='Nombre de Projets',
            color='Nature Entité',
            title='Distribution de Nature Entité par Année de réalisation',
            labels={'y': 'Nombre de Projets', 'color': 'Nature Entité'},
            text_auto=True,
            color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4']
        )
    st.plotly_chart(fig_nature_annee)

# Ajouter une colonne pour le statut de paiement si elle n'existe pas déjà
if 'Payer' not in df.columns:
    df['Payer'] = False

# Analyse par Date Fin
if user_menu == 'Analyse par Date Fin':
    st.sidebar.header("Filtrer par Date Fin")
    
    # Filtrer les dates uniques et s'assurer qu'il n'y a pas de NaT (Not a Time)
    dates_fin = df['Date Fin'].dropna().dt.strftime('%Y-%m-%d').unique().tolist()
    selected_date_fin = st.sidebar.selectbox("Sélectionnez la Date Fin", dates_fin)
    
    # Filtrer les données par Date Fin
    date_fin_data = df[df['Date Fin'].dt.strftime('%Y-%m-%d') == selected_date_fin]
    
    st.subheader(f"Projets avec Date Fin : {selected_date_fin}")
    st.dataframe(date_fin_data)
    
    
    # Obtenir la date actuelle
    date_actuelle = datetime.now()

    # Calculer la date trois mois après
    date_limite = date_actuelle + timedelta(days=90)

    # Filtrer les projets dont la 'Date Fin' est comprise entre la date actuelle et la date limite
    projets_a_payer = df[(df['Date Fin'] >= date_actuelle) & (df['Date Fin'] <= date_limite)]

    # Afficher les projets à payer avec des cases à cocher
    st.subheader("Projets à Payer dans les 3 Prochains Mois")

    # Liste pour stocker les cases à cocher
    checked_status = {}

    for index, row in projets_a_payer.iterrows():
        checkbox_key = f"{row['Nom de projet']} - {row['Date Fin'].strftime('%d/%m/%Y')}"
        is_checked = st.checkbox(checkbox_key, value=row['Payer'], key=checkbox_key)
        checked_status[index] = is_checked

    # Mettre à jour le DataFrame avec le statut des cases à cocher
    for index, is_checked in checked_status.items():
        df.at[index, 'Payer'] = is_checked

    # Résumé des projets à venir
    st.subheader("Résumé des Projets à Venir")
    total_projets_a_payer = projets_a_payer.shape[0]
    total_distance = projets_a_payer['Distance Autorisation / ml'].sum()
    total_redevance = projets_a_payer['Total Redevance'].sum()
    
    st.write(f"Nombre total de projets à payer : {total_projets_a_payer}")
    st.write(f"Distance totale : {total_distance:.2f} ml")
    st.write(f"Total de la redevance : {total_redevance:.2f} Dh")
    

# Analyse spécifique aux Projets
if user_menu == 'Analyse spécifique aux Projets':
    st.sidebar.header("Filtrer par Ville")
    
    # Sélecteur multi-sélection pour les villes
    villes = df['Ville'].unique().tolist()
    selected_villes = st.sidebar.multiselect("Sélectionnez jusqu'à 8 Villes", villes, default=villes[:8])
    
    # Assurez-vous de ne pas sélectionner plus de 8 villes
    if len(selected_villes) > 8:
        st.sidebar.warning("Vous ne pouvez sélectionner que jusqu'à 8 villes.")
        selected_villes = selected_villes[:8]

    # Filtrer les données pour les villes sélectionnées
    filtered_df = df[df['Ville'].isin(selected_villes)]
    
    st.markdown("<h1 style='font-size:28px;'>Détails pour les Villes Sélectionnées</h3>", unsafe_allow_html=True)
    st.dataframe(filtered_df)

    

    # Analyse des Projets
    if not filtered_df.empty:
        st.markdown("<h1 style='font-size:24px;'>Analyse du Projet par Ville (Top 8)</h3>", unsafe_allow_html=True)

        # Nombre de Projets par Ville (Top 8)
        ville_counts = filtered_df['Ville'].value_counts().reset_index()
        ville_counts.columns = ['Ville', 'Nombre de Projets']
        fig_projets_ville = px.bar(ville_counts,
                                  x='Ville',
                                  y='Nombre de Projets',
                                  title="Nombre de Projets par Ville",
                                  color='Ville',
                                  color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_projets_ville)

        # Distance Totale Autorisée par Ville (Top 8)
        distance_totale = filtered_df.groupby('Ville')['Distance Autorisation / ml'].sum().reset_index()
        distance_totale = distance_totale.sort_values(by='Distance Autorisation / ml', ascending=False).head(8)
        fig_distance_ville = px.bar(distance_totale,
                                    x='Ville',
                                    y='Distance Autorisation / ml',
                                    title="Distance Totale Autorisée par Ville",
                                    color='Ville',
                                    color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_distance_ville)

        # Redevance Totale Autorisée par Ville (Top 8)
        redevance_totale = filtered_df.groupby('Ville')['Total Redevance'].sum().reset_index()
        redevance_totale = redevance_totale.sort_values(by='Total Redevance', ascending=False).head(8)
        fig_redevance_totale = px.bar(redevance_totale,
                                      x='Ville',
                                      y='Total Redevance',
                                      title="Redevance Totale Autorisée par Ville",
                                      color='Ville',
                                      color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_redevance_totale)

        
        # Nombre de Projets par Programme pour chaque Ville (Top 8)
        programme_counts = filtered_df.groupby(['Ville', 'Programme']).size().reset_index(name='Nombre de Projets')

        fig_projets_programme_ville = px.bar(programme_counts,
                                            x='Ville',
                                            y='Nombre de Projets',
                                            color='Programme',
                                            title="Nombre de Projets par Programme pour chaque Ville",
                                            barmode='group',
                                            color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_projets_programme_ville)


        # Évolution des Projets par Ville au fil des Années
        filtered_df['Année'] = pd.to_datetime(filtered_df['Date début']).dt.year
        evolution_projets = filtered_df.groupby(['Ville', 'Année']).size().reset_index(name='Nombre de Projets')
        fig_evolution_ville = px.line(evolution_projets,
                                    x='Année',
                                    y='Nombre de Projets',
                                    color='Ville',
                                    title="Évolution des Projets par Ville au fil des Années",
                                    color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_evolution_ville)
        
        # Comparaison des Redevances Totales par Ville en fonction de l'Année

        # Groupement des données par Ville et Année de réalisation pour la Redevance Totale
        redevance_annee_ville = filtered_df.groupby(['Année de réalisation', 'Ville'])['Total Redevance'].sum().reset_index()

        # Création du diagramme
        fig_redevance_annee_ville = px.line(redevance_annee_ville,
                                            x='Année de réalisation',
                                            y='Total Redevance',
                                            color='Ville',
                                            title="Comparaison des Redevances Totales par Ville en Fonction de l'Année",
                                            markers=True,
                                            color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])

        st.plotly_chart(fig_redevance_annee_ville)

        # Comparaison des Distances Autorisées par Ville en Fonction de l'Année
        distance_annee = filtered_df.groupby(['Ville', 'Année'])['Distance Autorisation / ml'].sum().reset_index()
        fig_distance_annee = px.line(distance_annee,
                                    x='Année',
                                    y='Distance Autorisation / ml',
                                    color='Ville',
                                    title="Comparaison des Distances Autorisées par Ville au fil des Années",
                                    color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_distance_annee)

        # Répartition par Nature Entité par Ville
        nature_ville = filtered_df.groupby(['Ville', 'Nature Entité'])['Nom de projet'].count().reset_index()
        nature_ville.columns = ['Ville', 'Nature Entité', 'Nombre de Projets']
        fig_nature_ville = px.bar(nature_ville,
                                  x='Ville',
                                  y='Nombre de Projets',
                                  color='Nature Entité',
                                  title="Répartition par Nature Entité par Ville",
                                  barmode='stack',
                                  color_discrete_sequence=['#FF4500', '#FFA500','#FFD700','#00BFFF','#32CD32', '#FF69B4'])
        st.plotly_chart(fig_nature_ville)

    else:
        st.write("Aucune donnée disponible pour les villes sélectionnées.")

# Exporter les données filtrées
st.sidebar.subheader("Exporter les Données Filtrées")
if st.sidebar.button('Exporter vers CSV'):
    if user_menu == 'Analyse par Ville et Année':
        df_filtered = ville_data
        file_name = f'projets_{selected_ville}_{selected_annee}.csv'
    elif user_menu == 'Analyse par Date Fin':
        df_filtered = date_fin_data
        file_name = f'projets_date_fin_{selected_date_fin}.csv'
    elif user_menu == 'Analyse spécifique aux Projets':
        df_filtered = filtered_df
        file_name = 'projets_specifiques.csv'
    else:
        df_filtered = df
        file_name = 'projets_all.csv'

    # Save the filtered data to a CSV file
    df_filtered.to_csv(file_name, index=False)
    st.sidebar.success(f"Fichier CSV exporté : {file_name}")
