# Cyberchase - Exercice SQL en Shell

![cyb_img](https://cs50.harvard.edu/sql/2024/psets/0/cyberchase/cyberchase.jpg)

## 🎯 Objectif
Cette fois-ci, vous devrez réaliser **TOUT l'exercice uniquement depuis le terminal** (shell). Pas d'interface graphique, pas de GUI SQLite - uniquement la ligne de commande !

## 📋 Prérequis - Installation de SQLite3

### Sur Ubuntu/Debian :
```bash
sudo apt update
sudo apt install sqlite3
```

### Sur macOS :
SQLite3 est normalement préinstallé. Si ce n'est pas le cas :
```bash
brew install sqlite3
```
*Note : Si vous n'avez pas Homebrew, installez-le depuis [brew.sh](https://brew.sh)*

### Vérifier l'installation :
```bash
sqlite3 --version
```

## 🛠️ Installation de l'éditeur de texte Micro (Recommandé)

Micro offre une coloration syntaxique agréable pour éditer vos fichiers SQL.

### Sur Ubuntu/Debian :
```bash
sudo apt install micro
```

### Sur macOS :
```bash
brew install micro
```

### Alternative : Nano
Si vous préférez, vous pouvez utiliser `nano` (préinstallé sur la plupart des systèmes) :
```bash
nano fichier.sql
```

## Travailler avec deux terminaux

**Ouvrez deux fenêtres de terminal côte à côte :**

1. **Terminal 1** : Pour explorer la base de données
   ```bash
   sqlite3 cyberchase.db
   ```
   
2. **Terminal 2** : Pour éditer vos fichiers SQL
   ```bash
   micro 1.sql
   ```


## 📚 Commandes essentielles SQLite3 en shell

Une fois dans SQLite3 (`sqlite3 cyberchase.db`) :

```sql
-- Afficher les tables
.tables

-- Voir le schéma d'une table
.schema episodes

-- Activer l'affichage en colonnes (plus lisible)
.mode column
.headers on

-- Exécuter un fichier SQL
.read 1.sql

-- Quitter SQLite3
.quit
```

## 🔧 Workflow recommandé

1. **Étape 1** : Explorez d'abord la base de données
   ```bash
   sqlite3 cyberchase.db
   sqlite> .tables
   sqlite> .schema episodes
   sqlite> SELECT * FROM episodes LIMIT 5;
   ```

2. **Étape 2** : Éditez votre fichier SQL dans un autre terminal
   ```bash
   micro 1.sql
   ```
   Tapez votre requête, puis sauvegardez :
   - Dans Micro : `Ctrl+S` pour sauvegarder, `Ctrl+Q` pour quitter
   - Dans Nano : `Ctrl+O` pour sauvegarder, `Ctrl+X` pour quitter

3. **Étape 3** : Testez votre requête
   ```bash
   # Méthode 1 : Depuis SQLite3
   sqlite> .read 1.sql
   
   # Méthode 2 : Directement depuis le shell
   sqlite3 cyberchase.db < 1.sql
   ```

## 📊 Redirection de sortie (utile pour vérifier le nombre de lignes)

```bash
# Exécuter et sauvegarder le résultat dans un fichier
sqlite3 cyberchase.db < 1.sql > resultat_1.txt


# Voir le résultat avec pagination
sqlite3 cyberchase.db < 1.sql | less
```

## 🎨 Personnalisation de SQLite3 (Optionnel)

Créez un fichier `.sqliterc` dans votre home pour des paramètres par défaut :

```bash
echo ".mode column
.headers on
.timer on" > ~/.sqliterc
```

Maintenant, SQLite3 utilisera toujours ces paramètres !

---

## Problème à Résoudre

Bienvenue dans le Cyberespace ! Cyberchase est une série télévisée animée et éducative pour enfants, diffusée par le Public Broadcasting Service (PBS) des États-Unis depuis 2002. Conçue à l'origine pour « montrer aux enfants que les mathématiques sont partout et que tout le monde peut être bon en maths », le monde de Cyberchase tourne autour de Jackie, Matt et Inez qui s'associent à Digit, un « cybird », pour empêcher Hacker de prendre le contrôle du Cyberespace et d'infecter la Carte Mère. En chemin, le quatuor apprend des compétences en mathématiques, en sciences et en résolution de problèmes pour contrecarrer les tentatives de Hacker.

Dans une base de données appelée `cyberchase.db`, en utilisant une table appelée `episodes`, trouvez des réponses aux questions de PBS sur les épisodes de Cyberchase jusqu'à présent.

## Schéma

Chaque base de données a un certain « schéma » — les tables et colonnes dans lesquelles les données sont organisées. Dans `cyberchase.db`, vous trouverez une seule table, `episodes`. Dans la table `episodes`, vous trouverez les colonnes suivantes :

- `id`, qui identifie de manière unique chaque ligne (épisode) de la table
- `season`, qui est le numéro de la saison dans laquelle l'épisode a été diffusé
- `episode_in_season`, qui est le numéro de l'épisode dans sa saison donnée
- `title`, qui est le titre de l'épisode
- `topic`, qui identifie les idées que l'épisode visait à enseigner
- `air_date`, qui est la date (exprimée au format `AAAA-MM-JJ`) à laquelle l'épisode a été « diffusé » (c'est-à-dire publié)
- `production_code`, qui est l'ID unique utilisé par PBS pour faire référence à chaque épisode en interne

## 📝 Exercices

Pour chacune des questions suivantes, vous devez écrire une seule requête SQL qui produit les résultats spécifiés par chaque problème. Votre réponse doit prendre la forme d'une seule requête SQL. Vous ne devez faire aucune supposition sur les `id` de certains épisodes : vos requêtes doivent être exactes même si l'`id` d'un épisode particulier était différent. Enfin, chaque requête doit renvoyer uniquement les données nécessaires pour répondre à la question.

1. Dans `1.sql`, écrivez une requête SQL pour lister les titres de tous les épisodes de la saison originale de Cyberchase, la Saison 1.

2. Dans `2.sql`, listez le numéro de saison et le titre du premier épisode de chaque saison.

3. Dans `3.sql`, trouvez le code de production de l'épisode « Hackerized! ».

4. Dans `4.sql`, écrivez une requête pour trouver les titres des épisodes qui n'ont pas encore de sujet répertorié.

5. Dans `5.sql`, trouvez le titre de l'épisode des fêtes diffusé le 31 décembre 2004.

6. Dans `6.sql`, listez les titres des épisodes de la saison 6 (2008) qui ont été publiés en avance, en 2007.

7. Dans `7.sql`, écrivez une requête SQL pour lister les titres et sujets de tous les épisodes enseignant les fractions.

8. Dans `8.sql`, écrivez une requête qui compte le nombre d'épisodes publiés au cours des 6 dernières années, de 2018 à 2023 inclus.
   - 💡 Astuce : Vous pouvez utiliser `BETWEEN` avec des dates, comme `BETWEEN '2000-01-01' AND '2000-12-31'`.

9. Dans `9.sql`, écrivez une requête qui compte le nombre d'épisodes publiés au cours des 6 premières années de Cyberchase, de 2002 à 2007 inclus.

10. Dans `10.sql`, écrivez une requête SQL pour lister les id, titres et codes de production de tous les épisodes. Triez les résultats par code de production, du plus ancien au plus récent.

11. Dans `11.sql`, listez les titres des épisodes de la saison 5, en ordre alphabétique inverse.

12. Dans `12.sql`, comptez le nombre de titres d'épisodes uniques.

13. Dans `13.sql`, écrivez une requête SQL pour explorer une question de votre choix. Cette requête doit :
    - Impliquer au moins une condition, en utilisant `WHERE` avec `AND` ou `OR`

## 🚀 Exercices Bonus (Optionnel)

Vous sentez-vous plus à l'aise ? Essayez ces requêtes avancées !

1. Écrivez une requête SQL pour trouver les titres des épisodes diffusés pendant la période des fêtes, généralement en décembre aux États-Unis.
   - Votre requête doit produire une table avec une seule colonne pour le titre de chaque épisode.
   - Essayez de trouver une meilleure solution que `LIKE` si vous le pouvez !

2. Écrivez une requête SQL pour trouver, pour chaque année, le premier jour de l'année où PBS a publié un épisode de Cyberchase.
   - Votre requête doit produire une table avec deux colonnes, une pour l'année et une pour le mois et le jour les plus précoces où un épisode a été publié cette année-là.

## ✅ Validation des résultats

Voici le nombre de lignes attendu pour chaque requête :

- `1.sql` : 1 colonne, 26 lignes
- `2.sql` : 2 colonnes, 14 lignes
- `3.sql` : 1 colonne, 1 ligne
- `4.sql` : 1 colonne, 26 lignes
- `5.sql` : 1 colonne, 1 ligne
- `6.sql` : 1 colonne, 2 lignes
- `7.sql` : 2 colonnes, 6 lignes
- `8.sql` : 1 colonne, 1 ligne
- `9.sql` : 1 colonne, 1 ligne
- `10.sql` : 3 colonnes, 140 lignes
- `11.sql` : 1 colonne, 10 lignes
- `12.sql` : 1 colonne, 1 ligne

## 🎓 Conseils finaux

1. **Utilisez l'historique** : Dans SQLite3, utilisez les flèches ↑↓ pour naviguer dans l'historique des commandes
2. **Auto-complétion** : Appuyez sur Tab pour l'auto-complétion des noms de tables/colonnes
