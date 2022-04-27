# Crystals vs Trucks
[![Tests sur release-main](https://github.com/MoiseMoussetafa/crystals_trucks_project/actions/workflows/python.yml/badge.svg?branch=release-main)](https://github.com/MoiseMoussetafa/crystals_trucks_project/actions/workflows/python.yml)
[![codecov](https://codecov.io/gh/MoiseMoussetafa/crystals_trucks_project/branch/release-main/graph/badge.svg?token=L7JRXT7ZCX)](https://codecov.io/gh/MoiseMoussetafa/crystals_trucks_project)

<p align="center">  
 <img src=https://user-images.githubusercontent.com/72506988/164490624-32c954f8-637e-418a-afa3-6645e6296fa3.png width="500" height="500">
</p>

### Groupe : 
- Léo CHAMONT-HARO
- Moïse MOUSSETAFA
- Mattéo PENAUD

---

### Projet

Réalisation d'un code permettant de résoudre le jeu suivant : https://github.com/vpoulailleau/crystal_trucks.  
Le fichier `game.py` doit être récupéré du jeu original et ne doit pas être modifié.  
Le code réalisé doit générer un fichier `.txt` qui peut être injecté dans le `viewer.py` du jeu original afin de le résoudre.  


### Obligations 

- Python 3.10 sur PC
- Coopération sur GitHub 
  - Utilisation de plusieurs branches
  - Utilisation de pull requests
- Fichier `game.py` non modifiable
- Tests
  - Qualimétrie
  - Automatisation (intégration continue)

---

## Utilisation 

*⚠️ Si les commandes à executer dans un terminal ne fonctionnent pas avec `python3` et `pip3`, réessayer sans le chiffre 3.*

Cloner les répertoires nécessaires :
```
git clone https://github.com/vpoulailleau/crystal_trucks.git

git clone https://github.com/MoiseMoussetafa/crystals_trucks_project.git
```

Depuis le dossier `crystals_trucks_project` :
```
python3 crystals_trucks_project/main.py [seed] [nom_fichier.txt]
```
📓*seed* : nombre correspondant à la graine de randomisation afin d'obtenir une carte de jeu semi-aléatoire  
📓*nom_fichier.txt* : nom du fichier à choisir pour le document texte généré par le `main.py`  

Copier le fichier généré nommé `[nom_fichier.txt]` dans le dossier `crystal_trucks` précédemment cloné. Puis dans ce dernier :
```
pip3 install arcade serial
python3 crystal_trucks/viewer.py -i [nom_fichier.txt]
```

Une interface graphique apparait alors et présente le jeu.  
Les fonctionnalités du `viewer.py` sont disponibles sur le git correspondant.

---

### Sources
- https://github.com/jorisoffouga/methode_dev_collaboratif  
- https://github.com/vpoulailleau/crystal_trucks  
- https://docs.pytest.org/en/7.1.x/  

