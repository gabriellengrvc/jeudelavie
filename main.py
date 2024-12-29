import turtle 

#fonction afficher la grille
def afficher_grille(liste_coord):
  for x, y in liste_coord:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for _ in range(4):
      turtle.forward(20)
      turtle.left(90)
      turtle.update()
    turtle.penup()

#fonction qui arrondi les coordonnées pour le bon affichage
def coord_precise(x,y)
  x_precis = x - (x % 20)
  y_precis = y - (y % 20)
  return x_precis, y_precis 

#fonction qui rempli un carré après clic
def remplir(couleur): 
  turtle.pendown()
  turtle.fillcolor(couleur)
  turtle.begin_fill()
  for _ in range(4):
    turtle.forward(20)
    turtle.left(90)
    turtle.update()
  turtle.end_fill()
  turtle.penup()

#fonction qui vérifie si le clic est dans la grille
def clic_valide(x,y):
  return -300 <= x <= 300 and -300 <= y <= 300

#fonction qui compte les voisins d'un carrö
def compter_voisins(x,y):
  voisins = 0 
  positions = [(x+20,y), (x-20,y), (x, y+20), (x, y-20), (x+20, y+20), (x+20, y-20), (x-20, y+20), (x-20, y-20)]
  for x_voisin, y_voisin in positions:
    if (x_voisin, y_voisin) in liste_coord:
      index_voisin = liste_coord.index((x_voisin, y_voisin))
      if (x_voisin, y_voisin) in liste_coord and liste_carre[index_voisin] == 1:
        voisins += 1
  return voisins

#fonction qui dötermine l'ötat de la cellule en fonction des voisins
def voisins(index):
  x,y = liste_coord[index]
  nombre_de_voisins = compter_voisins(x,y)
  if liste_carre[index] == 1:
    if nombre_de_voisins not in [2,3]:
      liste_carre[index] = 0
      turtle.goto(x,y)
      remplir("white") 
      turtle.update()
  else:
    if nombre_de_voisins == 3:
      liste_carre[index] = 1
      turtle.goto(x,y)
      remplir("black")
      turtle.update()

#fonction qui remplit un carré au bonnes coordonnées avec la bonne couleur
def remplir_carre(x,y):
  if not clic_valide(x,y):
    return
  x,y = coord_precise(x,y)
  index = liste_coord.index((x,y))
  if liste_carre[index] == 0:
    liste_carre[index] = 1
    turtle.goto(x,y)
    remplir("black")
    turtle.update()
  else:
    liste_carre[index] = 0 
    turtle.goto(x,y)
    remplir("white")
    turtle.update()

#grandeurs diverses 
taille_carre = 20
max_x = 300
max_y = 300

#variables
index=0

#afficher la fenetre turtle
screen = turtle.Screen()
screen.title("Jeu de la vie")
screen.bgcolor("white")
screen.setup(width=1200, height=675)

#définir les détails turtle
turtle.sped(0)
turtle.pensize(1)
turtle.pencolor("black")
turtle.tracer(0)
turtle.hideturtle()

#créer la liste de colonnes et lignes et intialiser toutes les cellules comme mortes
liste_carre=[]
for _ in range(30*30):
  liste_carre.append(0)

#créer la liste de coordonnées de carrés
liste_coord=[]
for x in range(-max_x, max_x, taille_carré):
  for y in range(-max_y, max_y, taille_carré):
    liste_coord.append((x,y))

#afficher la grille
afficher_grille(liste_coord)

#action lors d'un clic
screen.onclick(remplir_carre)

#fonction de mise à jour qui affiche l'évolution des cellules 
def evolution():
  for index in range(len(liste_carre)):
    voisins(index)
  turtle.update()
  screen.ontimer(evolution, 100) 

#fonction pour lancer le jeu 
def start_game():
  screen.ontimer(evolution, 100) 

screen.onkey(start_game, "Return")
screen.listen()
turtle.done()
