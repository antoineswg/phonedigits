# T9Tweeting

Script python simple qui chiffre et déchiffre du texte en saisie T9 (comme sur les vieux téléphones à clavier numérique). Fonctionne avec les caractères spéciaux français.

## Fonctionnalités

- **Chiffrement**
- **Déchiffrement**
- **Copie** : Peut copier le résultat dans le presse-papiers si vous installez `pyperclip`.

## Utilisation

1. Assurez-vous d’avoir Python installé.
2. Installez pyperclip :
   ```sh
   pip install pyperclip
   ```
3. Lancez le script :
   ```sh
   python script.py
   ```
4. Choisissez de chiffrer (C) ou déchiffrer (D).
5. Entrez votre texte ou code T9.
6. Copiez ou non le résultat dans votre presse-papiers.

## Caractères pris en charge

- **Nombres :** `0 1 2 3 4 5 6 7 8 9`
- **Alphabet français :** `a b c d e f g h i j k l m n o p q r s t u v w x y z`
- **Caractères spéciaux français** : `œ à â ä ç é è ê ë î ï ô ö ù û ü`

### Pertes
Au déchiffrement, les `majuscules`, les `accents` ainsi que le `œ` seront perdus

## Exemples

```
Texte à chiffrer :
T9Tweeting

Résultat :
8 09 8 9 33 33 8 444 66 4
```
```
Texte à déchiffrer :
8 09 8 9 33 33 8 444 66 4

Résultat :
t9tweeting
```

```
Texte à chiffrer :
Grigny-la-Grande-Borne, une bite sur l'épaule
3 cadavres, sol, quartier mahbol
Face à l'horreur, nous sommes
Nous sommes, des tueurs
Général de guerre et casquette à l'envers
Les pecs en l'air, le bras à Schwarzennegger
Tu gazes on t'monte en l'air pour des billets, (ttt)-verts
Je suis un braqueur, fuck le procureur !
Fuck le procureur ! Fuck ? Le procureur

Résultat :
4 777 444 4 66 999 - 555 2 - 4 777 2 66 3 33 - 22 666 777 66 33 , 0 88 66 33 0 22 444 8 33 0 7777 88 777 0 555 ' 33 7 2 88 555 33
03 0 222 2 3 2 888 777 33 7777 , 0 7777 666 555 , 0 77 88 2 777 8 444 33 777 0 6 2 44 22 666 555
333 2 222 33 0 2 0 555 ' 44 666 777 777 33 88 777 , 0 66 666 88 7777 0 7777 666 6 6 33 7777
66 666 88 7777 0 7777 666 6 6 33 7777 , 0 3 33 7777 0 8 88 33 88 777 7777
4 33 66 33 777 2 555 0 3 33 0 4 88 33 777 777 33 0 33 8 0 222 2 7777 77 88 33 8 8 33 0 2 0 555 ' 33 66 888 33 777 7777
555 33 7777 0 7 33 222 7777 0 33 66 0 555 ' 2 444 777 , 0 555 33 0 22 777 2 7777 0 2 0 7777 222 44 9 2 777 9999 33 66 66 33 4 4 33 777
8 88 0 4 2 9999 33 7777 0 666 66 0 8 ' 6 666 66 8 33 0 33 66 0 555 ' 2 444 777 0 7 666 88 777 0 3 33 7777 0 22 444 555 555 33 8 7777 , 0 ( 8 8 8 )- 888 33 777 8 7777
5 33 0 7777 88 444 7777 0 88 66 0 22 777 2 77 88 33 88 777 , 0 333 88 222 55 0 555 33 0 7 777 666 222 88 777 33 88 777 0 !
333 88 222 55 0 555 33 0 7 777 666 222 88 777 33 88 777 0 ! 0 333 88 222 55 0 ? 0 555 33 0 7 777 666 222 88 777 33 88 777
```
```
Texte à déchiffrer :
4 777 444 4 66 999 - 555 2 - 4 777 2 66 3 33 - 22 666 777 66 33 , 0 88 66 33 0 22 444 8 33 0 7777 88 777 0 555 ' 33 7 2 88 555 33
03 0 222 2 3 2 888 777 33 7777 , 0 7777 666 555 , 0 77 88 2 777 8 444 33 777 0 6 2 44 22 666 555
333 2 222 33 0 2 0 555 ' 44 666 777 777 33 88 777 , 0 66 666 88 7777 0 7777 666 6 6 33 7777
66 666 88 7777 0 7777 666 6 6 33 7777 , 0 3 33 7777 0 8 88 33 88 777 7777
4 33 66 33 777 2 555 0 3 33 0 4 88 33 777 777 33 0 33 8 0 222 2 7777 77 88 33 8 8 33 0 2 0 555 ' 33 66 888 33 777 7777
555 33 7777 0 7 33 222 7777 0 33 66 0 555 ' 2 444 777 , 0 555 33 0 22 777 2 7777 0 2 0 7777 222 44 9 2 777 9999 33 66 66 33 4 4 33 777
8 88 0 4 2 9999 33 7777 0 666 66 0 8 ' 6 666 66 8 33 0 33 66 0 555 ' 2 444 777 0 7 666 88 777 0 3 33 7777 0 22 444 555 555 33 8 7777 , 0 ( 8 8 8 )- 888 33 777 8 7777
5 33 0 7777 88 444 7777 0 88 66 0 22 777 2 77 88 33 88 777 , 0 333 88 222 55 0 555 33 0 7 777 666 222 88 777 33 88 777 0 !
333 88 222 55 0 555 33 0 7 777 666 222 88 777 33 88 777 0 ! 0 333 88 222 55 0 ? 0 555 33 0 7 777 666 222 88 777 33 88 777

Résultat :
grigny-la-grande-borne, une bite sur l'epaule
3 cadavres, sol, quartier mahbol
face a l'horreur, nous sommes
nous sommes, des tueurs
general de guerre et casquette a l'envers
les pecs en l'air, le bras a schwarzennegger
tu gazes on t'monte en l'air pour des billets, (ttt)-verts
je suis un braqueur, fuck le procureur !
fuck le procureur ! fuck ? le procureur
```

## Inspiration
Souvent sur twitter on voit revenir ce genre de tweet alors je me suis que c'était une bonne occasion de faire un outil pour me refaire faire un peu de python et éviter de trop rouiller.

<img src="https://imgur.com/51iang7.png" alt="Exemple de tweet en T9" width="300px"/>

Je doute que quelqu'un voit ce README un jour mais si c'est le cas hésite pas à Star le repo <img src="https://i.imgur.com/bvcIn2O.png" alt="emote 'aga' de 7tv" width="16px"/> stp
