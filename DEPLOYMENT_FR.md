# Mettre le dossier en ligne

## GitHub

1. Décompresser l'archive complète et ouvrir son dossier `rounding-statistical-simulation`.
2. Copier son contenu à la racine du dépôt `Crypticator/rounding-statistical-simulation`, en remplaçant les fichiers de mêmes noms. Le dossier comprend les cinq PDF, les deux archives de distribution et les répertoires complets ; il ne s'agit pas seulement d'un complément.
3. Inclure `thesis/`, `papers/`, `supplementary_data/`, les licences, le README et `CITATION.cff`.
4. Vérifier le dossier avec `python3 tools/verify_package.py` avant tout changement local, puis créer le commit de publication. Une release peut identifier cette édition du paquet sous `2026.11.18`.

Les anciennes copies ou releases conservent leur propre historique. Ne pas les présenter comme des copies de cette édition : les crédits et les empreintes ont changé. Aucun envoi GitHub n'est effectué par la préparation de cette archive.

## Préparer le dépôt Zenodo

Le fichier [ZENODO_DESCRIPTION.md](ZENODO_DESCRIPTION.md) fournit une description en anglais à reprendre dans la notice. Indiquer **Samir Bouftass** comme auteur ; déclarer l'assistance de ChatGPT dans la description, comme dans les manuscrits. Conserver la distinction entre les résultats mathématiques, les vérifications numériques et les audits par IA.

Pour un dépôt de la thèse et de ses matériaux associés, joindre le PDF `THESIS_Rounding_Statistical_Simulation_v0_6.pdf` et l'archive complète. Les quatre articles peuvent également faire l'objet de notices séparées avec leur supplément correspondant. La répartition des licences est documentée dans `LICENSING.md` : CC BY 4.0 pour les documents et données concernés, MIT pour le code.

Aucun DOI n'est inventé ou réservé dans ce dossier. Après attribution effective d'un DOI, l'ajouter à la notice bibliographique correspondante dans `CITATION.cff`. L'archive préparée ne constitue pas un dépôt accepté ou publié.
