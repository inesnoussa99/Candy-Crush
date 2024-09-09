from  random import randint 
import matplotlib.pyplot as plt



def init_jeu(size):
  """
    Créé une grille de jeu de taille size*size avec un nombre de billes de chaque couleur aléatoire placées
    aléatoirement.
    Paramètres :
        - size (int) : la taille du côté de la grille 
    Retour : 
        - le jeu initial avec des bonbons de couleur et de place aléatoire (grille)
    """
  jeu = []
  for i in range(size):
    ligne = []
    for j in range(size):
      n = randint(1, 4)
      ligne.append(n)
    jeu.append(ligne)
  return jeu

def affichage_grille(grille, nb_type_bonbons):
    """
        Affiche la grille de jeu "grille" contenant au maximum "nb_type_bonbons"
        de couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons-1, cmap ='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
    
def horizontal(grille):
    """
    Prend en paramètre une grille et supprime les combinaisons horizontales, en initialisant un compteur des modifications horizontales
    Renvoie le compteur
    """
    grille_bis = copier_jeu(grille)
    compteur1 = 0
    for i in range(len(grille)):
        for j in range(1, len(grille[i])-1):
                if grille_bis[i][j] == grille_bis[i][j-1] and grille_bis[i][j] == grille_bis[i][j+1]:
                    for k in range(-1,2,1):
                        grille[i][j+k] = 0
                    compteur1 +=1 
    return compteur1

def copier_jeu(grille):
  """
    Copie la grille de taille size*size, chaque case avec la même valeur que dans la grille initiale.
    Paramètres : 
        - grille initale du jeu
    Retour : 
        - copie de la grille initiale
    """
  copie_jeu = []
  for i in range(len(grille)):
    ligne = []
    for j in range(len(grille[i])):
      ligne.append(grille[i][j])
    copie_jeu.append(ligne)
  return copie_jeu

def boucher_trous(grille):
    """
    Prend la grille en paramètres et positionne des valeurs aléatoires entre 1 et 4 dans les cases vides
    Renvoie la nouvelle grille remplie 
    """
    grille_bis = copier_jeu(grille)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille_bis[i][j] == 0:
                grille[i][j] = randint(1,4)
    return grille


def vertical(grille):  
    """
    Prend en paramètre une grille et supprime les combinaisons verticales, en initialisant un compteur des modifications verticales
    Renvoie le compteur
    """   
    grille_bis = copier_jeu(grille)
    compteur2 = 0          
    j = 0
    while j <len(grille):
        for i in range(1, len(grille)-1):
            if grille_bis[i][j] == grille_bis[i-1][j] and  grille_bis[i][j] == grille_bis[i+1][j]:
               for k in range(-1,2,1):
                   grille[i+k][j] = 0
               compteur2 += 1 
        j += 1
    return compteur2

def nettoyer(grille):
    """
    Prend la grille en paramètres et enlève toutes les combinaisons déjà existantes avant que le joueur joue, 
    et les remplace
    Renvoie la grille sans combinaisons déjà existantes
    """
    horizontal(grille)
    vertical(grille)
    boucher_trous(grille)
    return grille

def entrer_coordonnees(jeu):
  """
  Demande les coordonnées des deux bonbons que le joueur veut permuter en vérifiant qu'ils soient dans la     grille et adjacents horizontalement ou verticalement et les renvoie.
  Paramètres : 
      - jeu (grille) : grille avec les coordonnées des différents bonbons
  Retour : 
      - i, j, a, b (int) : les coordonnées des deux bonbons : abscisse1, ordonne1, abscisse2, ordonne2
  """
  print("Bienvenue dans candy crush !")
  i = -1
  j = -1
  while i < 0 or i >= len(jeu) or j < 0 or j >= len(jeu):
    print("Entrez les coordonnées du bonbon : ")
    i = int(input("Ligne : "))
    j = int(input("Colonne : "))
    if i < 0 or i >= len(jeu) or j < 0 or j >= len(jeu):
      print(f"Les coordonnées du bonbon doivent être comprises entre {0} et {len(jeu)-1}.")
  a = -1
  b = -1
  valid = True
  while valid :
    print("Entrez les coordonnées du deuxième bonbon avec lequel vous voulez permuter le premier: ")
    a = int(input("Ligne : "))
    b = int(input("Colonne : "))
    if a < 0 or a >= len(jeu) or b < 0 or b >= len(jeu):
      print(f"Les coordonnées du bonbon doivent être comprises entre {0} et {len(jeu)-1}.")
      valid = True
    elif abs(a-i)+abs(b-j) != 1 :
      print("Le deuxième bonbon doit être adjacent horizontalement ou verticalement au premier.")
      valid = True
    else : 
      print("Vos choix ont été pris en compte.")
      valid = False
  return i,j,a,b


def add_zeros (grille,element_neutre):
    n=len(grille)
    grille2=[]
    for i in range (n+2):
        l=[]
        for j in range (n+2):
            l.append(element_neutre)
        grille2.append(l)
    for i in range (1,n+1) :
        for j in range (1,n+1):
            grille2[i][j]=grille[i-1][j-1]
    return grille2 


def detect_grille (grille,x,y): 
    t=[]
    h=x+1
    k=y+1
    grille_copie=add_zeros(grille,0)
    if grille_copie[h-1][k]==grille_copie[h][k]==grille_copie[h+1][k]:
                    t=[[h-2,k-1],[h-1,k-1],[h,k-1]]
    else :
            if grille_copie[h][k-1]==grille_copie[h][k]==grille_copie[h][k+1]:
                    t=[[h-1,k-2],[h-1,k-1],[h-1,k]]
    return t 

def grille_jouable(grille):
    """
    Prend la grille en paramètres et enlève toutes les combinaisons existantes jusqu'à ce qu'il n'y en ait plus
    Renvoie la grille au joueur sur laquelle il peut jouer
    """
    compteur1, compteur2 = -1, -1
    while compteur1 != 0 or  compteur2 != 0:
        compteur1, compteur2 = horizontal(grille), vertical(grille)  
        nettoyer(grille)
    return grille


def permutation (grille,x,y,a,b):
    """
    Prend la grille ainsi que les coordonnées des deux bonbons choisis par l'utilisateur en paramètres 
    et permutent les deux bonbons choisis
    """
    z= grille[x][y]
    grille[x][y] = grille[a][b]
    grille[a][b] = z
    

def randomly_generated_tab() :
    """
    Génére aléatoirement une valeur entre 1 et 4 et l'assigne à une case
    """
    t=[]
    for i in range (3) :
        t.append(randint(1,4))
    return t


def detecte_coordonnees_combinaisons(L):
    """
    Prend la liste des coordonnées des bonbons de la combinaison
    Renvoie un booléen, True si la combinaison est composée de 3 bonbons, sinon False
    """
    if len(L)==3 :
        return True 
    else :
        return False 
    

    
def gravite (grille,L) :
    """
    Prend la grille en paramètres ainsi que la liste des coordonnées de la combinaison des bonbons
    Applique la gravité sur tous les bonbons qui en ont besoin
    Renvoie la grille une fois la gravité appliquée
    """
    row=L[0][1]
    if L[0][0]==L[1][0]:
        line=L[0][0]
        for i in range (line,0,-1) :
            grille[i][row:row+3]=grille[i-1][row:row+3]
        grille[0][row:row+3]=randomly_generated_tab()
    else :
        i=L[-1][0]
        while i-2>=0:
            grille[i][row]=grille[i-3][row]
            i=i-1
        for i in range (3):
            grille[i][row]=randint(1,4)
    return grille



#Programme principal :
size=6
grille=init_jeu(size)
grille=grille_jouable(grille)
nb_type_bonbons=5
affichage_grille(grille, nb_type_bonbons)
c=0

while True :
    grille=grille_jouable(grille)
    affichage_grille(grille, nb_type_bonbons)
    x,y,a,b=entrer_coordonnees(grille) 
    grille_bis=copier_jeu(grille)  
    permutation (grille_bis,x,y,a,b) 
    L= detect_grille(grille_bis,a,b) 
    if (detecte_coordonnees_combinaisons(L)) :            
        permutation (grille,x,y,a,b) 

        grille = gravite(grille,L) 
        c+=3
affichage_grille(grille, nb_type_bonbons)

def test_detecte_coordonnees_combinaison():
    """
        Test la fonction detecte_coordonnees_combinaison(grille,i,j).
        Pour chaque cas de test, affiche True si le test passe,
        False sinon
    """
    #Test1 : lorsque le bonbon intervertit est entre deux bonbons de la même couleur verticalement
    grille = [[1,2,3,1],[2,3,1,3],[2,3,1,2],[3,2,1,2]]
    i = 2
    j = 2
    print(detecte_coordonnees_combinaisons(detect_grille(grille,i,j))) == True
    
    #Test2 : lorsque le bonbon intervertit est entre deux bonbons de la même couleur horizontalement
    grille = [[1,1,1,2],[2,3,2,3],[2,3,2,3],[3,2,3,2]]
    i = 0
    j = 1
    print(detecte_coordonnees_combinaisons(detect_grille(grille,i,j))) == True
    
    #Test3 : lorsqu'aucune combinaison est disponible 
    grille = [[0,1,0,1],[2,3,2,3],[0,1,0,1],[2,3,2,3]]
    i = 2
    j = 1
    print(detecte_coordonnees_combinaisons(detect_grille(grille,i,j))) == False
    
    #Test4 : lorsque les 3 bonbons sont alignés mais forment un angle
    grille = [[1,1,2,3],[1,0,0,3],[0,1,0,2],[2,2,1,1]]
    i = 0
    j = 0
    print(detecte_coordonnees_combinaisons(detect_grille(grille,i,j))) == False 
    
    #Test5 : lorsque le bonbon n'est pas dans la grille
    grille = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    i = -1
    j = 3
    print(detecte_coordonnees_combinaisons(detect_grille(grille,i,j))) == False




        