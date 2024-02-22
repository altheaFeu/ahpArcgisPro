# Mise à jour de la toolbox "Analyse Hiérarchique des Processus (AHP)" pour ArcGIS PRO

[![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-10.8.2-brightgreen.svg)](https://www.arcgis.com/index.html)
[![ArcPy](https://img.shields.io/badge/ArcPy-3.1-blue.svg)](https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen.svg)](LICENSE.md)

## Présentation

Cette toolbox permet de réaliser une Analyse Hiérarchique des Processus (AHP) en évaluant la qualité des poids attribués à chaque couche raster dans une géodatabase.

Elle a été mise à jour pour être compatible avec la version d'ArcPy 3.1 et d'ArcGIS Pro 10.8.2.

**Mohammed Habboub** en est le créateur, et vous pouvez consulter son travail sur [digital-geography.com](https://digital-geography.com/ahp-arcgis-10-x-using-python/).

## Installation

1. Ouvrez ArcGIS Pro et accédez à l'onglet **Catalog**.
2. Faites un clic droit dans la zone de contenu de Catalog et sélectionnez **Ajouter une boîte à outils**.
3. Choisissez les fichiers python à ajouter à la boîte à outil.

## Utilisation

### AHP1 : Création d'une Matrice AHP

Cet outil vous permet de générer une matrice AHP vide. Il identifie automatiquement toutes les couches raster présentes dans la géodatabase.

*Note : L'outil peut analyser entre 2 et 15 couches maximum*

### AHP2 : Analyse de la Matrice

Cet outil analyse la matrice de comparaison générée par AHP1 et produit un indice de consistance (CI) ainsi qu'un ratio de consistance (CR).

Une fois que vous avez exécuté AHP2, une seconde table appelée **TableCI** est créée pour stocker les résultats.

## Interprétation des Résultats

Si le CR dépasse 1, cela indique que la matrice doit être améliorée. Vous devrez ajuster les poids attribués à chaque couche pour garantir une consistance optimale.

**Remarque :** N'hésitez pas à consulter la documentation complète pour une compréhension approfondie de chaque étape du processus.
