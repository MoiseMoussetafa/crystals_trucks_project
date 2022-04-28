# Utilisation des actions Github

<div align="center">

| <img src="https://cdn.discordapp.com/attachments/827628891266744331/966696776318980106/Copie_de_Design_sans_nom.gif" width="200"/>	| <img src="https://user-images.githubusercontent.com/72506988/164916709-39e3e144-5a36-49fe-a8cb-b25efac263c7.png" width="500"/>  	|
|---	|---	|

</div>
  
### Automatisation des tests

Configuration de workflows grâce aux fichiers `.yml`, stockés dans un dossier spécifique du repo `.github/workflows`.  

Le fichier `python.yml` permet de réaliser tous nos tests dans un workflow :
- lors des push
- lors des pull-request

---

## Qualimétrie avec Flake8
- Respect des conventions de codage (PEP8)   
- Détection d'erreurs d'écriture du code (pyflakes)

## Tests unitaires avec Pytest
Librairie permettant de réaliser des tests unitaires écrits par l’utilisateur pour vérifier le code

---

### Formatage du code avec Black
Dans le fichier `.pre-commit-config.yml`  
Formate le code avant les commits. Vérifié par Flake8.
