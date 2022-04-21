# Crystals vs Trucks
![Tests sur release](https://github.com/MoiseMoussetafa/crystals_trucks_project/actions/workflows/python.yml/badge.svg)

![image](https://user-images.githubusercontent.com/72506988/164490624-32c954f8-637e-418a-afa3-6645e6296fa3.png)

### Groupe : 
- Léo CHAMONT-HARO
- Moïse MOUSSETAFA
- Mattéo PENAUD

---

### Projet

Réalisation d'un code permettant de résoudre le jeu suivant : https://github.com/vpoulailleau/crystal_trucks.  
Le fichier `game.py` doit être récupéré du jeu original et ne doit pas être modifié.  
Le code réalisé doit générer un fichier `.txt` qui peut être injecté dans le `viewer.py` du jeu original afin de le résoudre.  

Source : https://github.com/jorisoffouga/methode_dev_collaboratif


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

Dans un terminal :
```
git clone https://github.com/vpoulailleau/crystal_trucks.git

git clone https://github.com/MoiseMoussetafa/crystals_trucks_project.git

python3 crystals_trucks_project/main.py [seed] [nom_fichier.txt]

python3 crystal_trucks/viewer.py [nom_fichier.txt]
```

*seed* : nombre correspondant à la graine de randomisation afin d'obtenir une carte de jeu semi-aléatoire  
*nom_fichier.txt* : nom du fichier à choisir pour le document texte généré par le `main.py`  


