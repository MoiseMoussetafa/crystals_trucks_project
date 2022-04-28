# Fichiers pour tests unitaires

<img src="https://user-images.githubusercontent.com/72506988/164979339-1e2da37a-bdf5-47d4-b9a9-62ab51426af9.png" width="300"/>

`test_trucks.py` est le fichier regroupant nos tests unitaires afin de valider le fonctionnement de nos fichiers .py permettant le fonctionnement du code.  
Ces tests sont lancés grâce à Pytest.

⚠️ A noter : le prefixe "test" devant le nom du fichier ainsi que devant chaque fonction de test n'est pas anodin : il permet à pytest de déterminer où se trouve le fichier et quels sont les fonctions à lancer pour réaliser les tests.

- test_create_game_seed_0() : Création d'une partie avec la map 0  
- test_create_game_seed_5() : Création d'une partie avec la map 5
- test_truck_creation_0_0_0() : Création d'un camion en 0,0
- test_truck_creation_5_20_3() : Création d'un camion en 20,3 
- test_truck_dig_0_0(capsys) : Tentative de dig en 0,0
- test_truck_dig_25_4(capsys) : Tentative de dig en 25,4
- test_truck_progress_dig_2(capsys) : Test de la fonction progress en faisant creuser un camion 0,0
- test_truck_zigzag_carre(capsys) : Test d'une stratégie de couverture de la map
- test_nearest_basic(capsys) : Test de la fonction permettant au camion d'aller au cristal le plus proche 
- test_nearest_angle(capsys) : Test de la fonction permettant au camion d'aller au cristal le plus proche même dans un angle (cf expected)
- test_get_nearest_crystal_easy() : Test de la fonction permettant au camion de détecter le crystal le plus proche
- test_get_nearest_crystal_further() : Test de la fonction permettant au camion de détecter le crystal le plus proche avec une plus grande portée
- test_get_nearest_crystal_backward() : Test de la fonction permettant au camion de détecter s'il a oublié un cristal sur son chemin
- test_count_crystals_wo_bounds() : Test de la fonction de détermination du nombre de cristaux sur la carte
- test_count_crystals_with_bounds() : Test de la fonction de détermination du nombre de cristaux dans une zone verticale donnée 

Les tests sont réalisés avec des maps témoins.
