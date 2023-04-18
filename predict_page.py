import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

lasso_loaded = data['model']
columns = ['PRICE', 'CONSTRUCTEDAREA', 'ROOMNUMBER', 'BATHNUMBER', 'HASTERRACE',
       'HASLIFT', 'HASAIRCONDITIONING', 'HASPARKINGSPACE',
       'HASNORTHORIENTATION', 'HASSOUTHORIENTATION', 'HASEASTORIENTATION',
       'HASWESTORIENTATION', 'HASBOXROOM', 'HASWARDROBE', 'HASSWIMMINGPOOL',
       'HASDOORMAN', 'HASGARDEN', 'CADCONSTRUCTIONYEAR',
       'DISTANCE_TO_CITY_CENTER', 'DISTANCE_TO_METRO', 'DISTANCE_TO_DIAGONAL',
       'baro_de_viver', 'can_baro', 'can_peguera___el_turo_de_la_peira',
       'canyelles', 'ciutat_meridiana___torre_baro___vallbona',
       'diagonal_mar_i_el_front_maritim_del_poblenou', 'el_baix_guinardo',
       'el_besos', 'el_bon_pastor', 'el_camp_de_larpa_del_clot',
       'el_camp_den_grassot_i_gracia_nova', 'el_carmel', 'el_clot', 'el_coll',
       'el_congres_i_els_indians', 'el_fort_pienc', 'el_gotic', 'el_guinardo',
       'el_parc_i_la_llacuna_del_poblenou', 'el_poble_sec___parc_de_montjuic',
       'el_poblenou', 'el_putxet_i_el_farro', 'el_raval', 'horta',
       'hostafrancs', 'la_barceloneta', 'la_bordeta', 'la_dreta_de_leixample',
       'la_font_de_la_guatlla', 'la_font_den_fargues', 'la_guineueta',
       'la_marina_del_port', 'la_marina_del_prat_vermell',
       'la_maternitat_i_sant_ramon', 'la_nova_esquerra_de_leixample',
       'la_prosperitat', 'la_sagrada_familia', 'la_sagrera', 'la_salut',
       'la_teixonera', 'la_trinitat_nova', 'la_trinitat_vella',
       'la_vall_dhebron___la_clota', 'la_verneda_i_la_pau',
       'la_vila_olimpica_del_poblenou', 'lantiga_esquerra_de_leixample',
       'les_corts', 'les_roquetes', 'les_tres_torres', 'navas', 'pedralbes',
       'porta', 'provencals_del_poblenou', 'sant_andreu', 'sant_antoni',
       'sant_genis_dels_agudells___montbau', 'sant_gervasi___galvany',
       'sant_gervasi___la_bonanova', 'sant_marti_de_provencals',
       'sant_pere___santa_caterina_i_la_ribera', 'sants', 'sants___badal',
       'sarria', 'vallcarca_i_els_penitents',
       'vallvidrera___el_tibidabo_i_les_planes', 'verdun', 'vila_de_gracia',
       'vilapicina_i_la_torre_llobeta', 'zona_franca___port']

for column in columns:
    exec(f"{column} = data['{column}']")

def show_predict_page():
    st.title("RealEstiMate")

    st.subheader("Smart pricing for smarter sales")
    st.write('We need some information to predict the square meter price')

    PRICE = st.slider('Total Price',37000,4854000,37000)

    CONSTRUCTEDAREA = st.slider('Constructed Area  (m^2)',21,959,21)

    ROOMNUMBER = st.slider('Number of Rooms',0,4,0)

    BATHNUMBER = st.slider('Number of Bathrooms',0,12,0)

    HASTERRACE = st.checkbox("Terrace")
    if HASTERRACE:
        HASTERRACE = 1
    else:
        HASTERRACE = 0

    HASLIFT = st.checkbox("Lift")
    if HASLIFT:
        HASLIFT = 1
    else:
        HASLIFT = 0

    HASAIRCONDITIONING = st.checkbox("Air Conditioning")
    if HASAIRCONDITIONING:
        HASAIRCONDITIONING = 1
    else:
        HASAIRCONDITIONING = 0

    HASPARKINGSPACE = st.checkbox("Parking")
    if HASPARKINGSPACE:
        HASPARKINGSPACEG = 1
    else:
        HASPARKINGSPACE = 0

    orientation_columns = ['HASNORTHORIENTATION','HASSOUTHORIENTATION', 
    'HASEASTORIENTATION','HASWESTORIENTATION']
    orientation_selection = st.multiselect('Select One Orientation:', options=orientation_columns)
    HASBOXROOM = st.checkbox('Box Room')
    if HASBOXROOM:
        HASBOXROOM = 1
    else:
        HASBOXROOM = 0

    HASWARDROBE = st.checkbox('Wardrobe')
    if HASWARDROBE:
        HASWARDROBE = 1
    else:
        HASWARDROBE =0

    HASSWIMMINGPOOL = st.checkbox('Swimming pool')
    if HASSWIMMINGPOOL:
        HASSWIMMINGPOOL = 1
    else:
        HASSWIMMINGPOOL = 0

    HASDOORMAN = st.checkbox('Door Man')
    if HASDOORMAN:
        HASDOORMAN = 1
    else:
        HASDOORMAN = 0

    HASGARDEN = st.checkbox('Garden')
    if HASGARDEN:
        HASGARDEN =1
    else:
        HASGARDEN =0

    CADCONSTRUCTIONYEAR = st.slider('Construction Year',1588,2018,1588)

    DISTANCE_TO_CITY_CENTER = st.slider('Distance to City Center (km)',0.0545,8.8532,0.0545)

    DISTANCE_TO_METRO = st.slider('Distance to Metro (km)',0.0007,4.0996,0.0007)

    DISTANCE_TO_DIAGONAL = st.slider('Distance to Diagonal (km)',0.0022,7.0077,0.0022)

    dummy_columns = ['baro_de_viver', 'can_baro', 'can_peguera___el_turo_de_la_peira',
       'canyelles', 'ciutat_meridiana___torre_baro___vallbona',
       'diagonal_mar_i_el_front_maritim_del_poblenou', 'el_baix_guinardo',
       'el_besos', 'el_bon_pastor', 'el_camp_de_larpa_del_clot',
       'el_camp_den_grassot_i_gracia_nova', 'el_carmel', 'el_clot', 'el_coll',
       'el_congres_i_els_indians', 'el_fort_pienc', 'el_gotic', 'el_guinardo',
       'el_parc_i_la_llacuna_del_poblenou', 'el_poble_sec___parc_de_montjuic',
       'el_poblenou', 'el_putxet_i_el_farro', 'el_raval', 'horta',
       'hostafrancs', 'la_barceloneta', 'la_bordeta', 'la_dreta_de_leixample',
       'la_font_de_la_guatlla', 'la_fontstreamlit run app.py_den_fargues', 'la_guineueta',
       'la_marina_del_port', 'la_marina_del_prat_vermell',
       'la_maternitat_i_sant_ramon', 'la_nova_esquerra_de_leixample',
       'la_prosperitat', 'la_sagrada_familia', 'la_sagrera', 'la_salut',
       'la_teixonera', 'la_trinitat_nova', 'la_trinitat_vella',
       'la_vall_dhebron___la_clota', 'la_verneda_i_la_pau',
       'la_vila_olimpica_del_poblenou', 'lantiga_esquerra_de_leixample',
       'les_corts', 'les_roquetes', 'les_tres_torres', 'navas', 'pedralbes',
       'porta', 'provencals_del_poblenou', 'sant_andreu', 'sant_antoni',
       'sant_genis_dels_agudells___montbau', 'sant_gervasi___galvany',
       'sant_gervasi___la_bonanova', 'sant_marti_de_provencals',
       'sant_pere___santa_caterina_i_la_ribera', 'sants', 'sants___badal',
       'sarria', 'vallcarca_i_els_penitents',
       'vallvidrera___el_tibidabo_i_les_planes', 'verdun', 'vila_de_gracia',
       'vilapicina_i_la_torre_llobeta', 'zona_franca___port']

    selected_columns = st.multiselect('Select One Location:', options=dummy_columns)

    ok = st.button('Calculate price/m^2')
    if ok:
            X = np.array([[PRICE,CONSTRUCTEDAREA,ROOMNUMBER, BATHNUMBER,
            HASTERRACE, HASLIFT, HASAIRCONDITIONING, HASPARKINGSPACE,
            HASNORTHORIENTATION, HASSOUTHORIENTATION, HASEASTORIENTATION,
            HASWESTORIENTATION, HASBOXROOM, HASWARDROBE, HASSWIMMINGPOOL,
            HASDOORMAN, HASGARDEN, CADCONSTRUCTIONYEAR, DISTANCE_TO_CITY_CENTER,
            DISTANCE_TO_METRO, DISTANCE_TO_DIAGONAL, baro_de_viver, can_baro,
            can_peguera___el_turo_de_la_peira, canyelles, ciutat_meridiana___torre_baro___vallbona,
            diagonal_mar_i_el_front_maritim_del_poblenou, el_baix_guinardo,
            el_besos, el_bon_pastor, el_camp_de_larpa_del_clot, el_camp_den_grassot_i_gracia_nova,
            el_carmel, el_clot, el_coll, el_congres_i_els_indians, el_fort_pienc,
            el_gotic, el_guinardo, el_parc_i_la_llacuna_del_poblenou, el_poble_sec___parc_de_montjuic,
            el_poblenou, el_putxet_i_el_farro, el_raval, horta, hostafrancs, la_barceloneta,
            la_bordeta, la_dreta_de_leixample, la_font_de_la_guatlla, la_font_den_fargues,
            la_guineueta, la_marina_del_port, la_marina_del_prat_vermell, la_maternitat_i_sant_ramon,
            la_nova_esquerra_de_leixample, la_prosperitat, la_sagrada_familia, la_sagrera,
            la_salut, la_teixonera, la_trinitat_nova, la_trinitat_vella, la_vall_dhebron___la_clota,
            la_verneda_i_la_pau, la_vila_olimpica_del_poblenou, lantiga_esquerra_de_leixample,
            les_corts, les_roquetes, les_tres_torres, navas, pedralbes,
            porta, provencals_del_poblenou, sant_andreu, sant_antoni,
            sant_genis_dels_agudells___montbau, sant_gervasi___galvany,
            sant_gervasi___la_bonanova, sant_marti_de_provencals,
            sant_pere___santa_caterina_i_la_ribera, sants, sants___badal,
            sarria, vallcarca_i_els_penitents,
            vallvidrera___el_tibidabo_i_les_planes, verdun, vila_de_gracia,
            vilapicina_i_la_torre_llobeta, zona_franca___port]])

    price = lasso_loaded.predict(X)
    st.subheader(f'The estimated price/m2 is ${output[0]:.2f}')
