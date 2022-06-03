import pygame
import sys
import random

# ech permet de modifier l'echelle de la figure.
ech=int(sys.argv[1])
# color_background permet de récupérer la couleur du fond.
color_background=tuple(sys.argv[2])



def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def start(ech,background_color):
    dico_possibilite = {1:['A','B','C'],2:['A','C','B'],3:['B','A','C'],4:['B','C','A'],5:['C','A','B'],6:['C','B','A']}
    dico_possibilite2 ={7:['A','B','C'],8:['A','C','B'],9:['B','A','C'],10:['B','C','A'],11:['C','A','B'],12:['C','B','A']}
    dico_coord = {1:(0,0),2:(240,0),3:(480,0),4:(0,240),5:(240,240),6:(480,240),7:(0,480),8:(240,480),9:(480,480),10:(0,720),11:(240,720),12:(480,720)}
    global width,height,screen
    width = ech*13
    height = 17*ech
    screen = pygame.surface.Surface((width, height))
    screen.fill(hex_to_rgb(background_color))
    affiche_carre_latin(dico_possibilite, dico_coord, dico_possibilite2)
    
def fig(matrice,ech,x0,y0):
    line_color = (0, 0, 0)
    noir = (0,0,0,255)
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == "A":
                if pygame.Surface.get_at(screen, (x0 + ech*(j+1)+30,y0+ ech*(i+1))) == noir:
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1), y0 + ech * (i + 1)),(x0 + ech * (j + 1) + 60,y0 +  ech * (i + 1)), width=7)
                else:
                    pygame.draw.line(screen, line_color, (x0 + ech*(j+1),y0 +  ech*(i+1)), (x0 + ech*(j+1)+60,y0 +  ech*(i+1)))
            if matrice[i][j] == "B":
                if pygame.Surface.get_at(screen, (x0 + ech * (j + 1)+30, y0 + ech * (i + 1)+60)) == noir:
                    pygame.draw.line(screen, line_color, (x0 + ech* (j + 1), y0 + ech * (i + 1)+60),(x0 + ech * (j + 1)+60, y0 + ech * (i + 1) + 60), width=7)
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1) + 60, y0 + ech * (i + 1)+60),(x0 + ech * (j + 1),y0 + ech * (i + 1) + 60))
                elif pygame.Surface.get_at(screen, (x0 + ech * (j + 1)+60,y0 +  ech * (i + 1) + 30)) == noir:
                    pygame.draw.line(screen, line_color,(x0 + ech * (j + 1) + 60, y0 + ech * (i + 1)), (x0 + ech * (j + 1) + 60, y0 + ech * (i + 1) + 60),width=7)
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1) + 60, y0 + ech * (i + 1)+60),(x0 + ech * (j + 1), y0 + ech * (i + 1) + 60))
                else:
                    pygame.draw.lines(screen, line_color, False, [(x0 + ech * (j + 1)+60,y0 +  ech * (i + 1)), (x0 + ech * (j + 1)+60, y0 + ech * (i + 1)+60), (x0 + ech * (j + 1), y0 + ech * (i+1)+60)])
                    
            if matrice[i][j] == "C":
                if pygame.Surface.get_at(screen, (x0 + ech * (j + 1), y0 + ech * (i + 1)+30)) == noir:
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1), y0 + ech * (i + 1)), (x0 + ech * (j + 1), y0 + ech * (i + 1)+60),width=7)
                    
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1)+60,y0 +  ech * (i + 1)), (x0 + ech * (j + 1)+60, y0 + ech * (i + 1) + 60))
                    
                elif pygame.Surface.get_at(screen, (x0 + ech * (j + 1)+60, y0 + ech * (i + 1)+30)) == noir:
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1)+60,y0 +  ech * (i + 1)), (x0 + ech * (j + 1)+60,y0 +  ech * (i + 1) + 60),width=7)
                    
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1), y0 + ech * (i + 1)), (x0 + ech * (j + 1), y0 + ech * (i + 1)+60))
                    
                else:
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1), y0 + ech * (i + 1)), (x0 + ech * (j + 1), y0 + ech * (i + 1)+60))
                    
                    pygame.draw.line(screen, line_color, (x0 + ech * (j + 1)+60, y0 + ech * (i + 1)), (x0 + ech * (j + 1)+60,y0 +  ech * (i + 1) + 60))
                    


def carre_latin_lettre(x,y,z):
    matrice = [[0] * 3 for _ in range(3)]
    for i in range(3):
        matrice[i][0] = x
        matrice[i][1] = y
        matrice[i][2] = z
        x,y,z = z,x,y

    return(matrice)

def carre_latin_lettre2(x, y, z):
    matrice = [[0] * 3 for _ in range(3)]
    for i in range(3):
        matrice[i][0] = x
        matrice[i][1] = y
        matrice[i][2] = z
        x, y, z = y, z, x

    return(matrice)

def affichage_matrice(matrice):
    for i in range(len(matrice)):
        print(matrice[i])
        
def affiche_carre_latin(dico_possibilite,dico_coord,dico_possibilite2):
    for cle,val in dico_possibilite.items():
        x,y,z = val
        x0,y0 = dico_coord[cle]
        matrice = carre_latin_lettre(x,y,z)
        fig(matrice,60,x0,y0)
    for cle,val in dico_possibilite2.items():
        x,y,z = val
        x0,y0 = dico_coord[cle]
        matrice = carre_latin_lettre2(x,y,z)
        fig(matrice,60,x0,y0)
    # Enregistre la figure
    fichier='oeuvre.png'
    pygame.image.save(screen,fichier)


#permet de démarrer le script.
start(ech,color_background)
#if __name__ == "__main__":
    
    #(204, 221, 255)
    #total_matrice()