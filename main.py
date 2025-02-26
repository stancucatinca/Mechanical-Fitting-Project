from ajustaj import verifica_ajustaj
# Exemplu de utilizare
alezaj = float(input("Introduceti dimensiunea nominala a alezajului[mm]: "))  # Diametrul alezajului în mm
arbore = float(input("Introduceti dimensiunea nominala a arborelui[mm]: ")) # Diametrul arborelui în mm
abatere_alezaj_max = float(input("Introduceti abaterea maximă a alezajului[mm]: "))
abatere_alezaj_min = float(input("Introduceti abaterea minima a alezajului[mm]: "))
abatere_arbore_max = float(input("Introduceti abaterea maximă a arborelui[mm]: "))
abatere_arbore_min = float(input("Introduceti abaterea minima a arborelui[mm]: "))

#Propunere de dimensiuni pentru afisarea unui ajustaj presat si preferential
#alezaj = 20  # Diametrul alezajului în mm
#arbore = 22  # Diametrul arborelui în mm
#abatere_alezaj_max = 0.19  # Abaterea maximă alezaj
#abatere_alezaj_min = -0.02  # Abaterea minimă alezaj
#abatere_arbore_max = 0.10   # Abaterea maximă arbore
#abatere_arbore_min = -0.03   # Abaterea minimă arbore

rezultat = verifica_ajustaj(alezaj, arbore, abatere_alezaj_max, abatere_alezaj_min, abatere_arbore_max, abatere_arbore_min)
print(rezultat)
