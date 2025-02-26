def verifica_ajustaj(d_alezaj, d_arbore, abatere_alezaj_max, abatere_alezaj_min, abatere_arbore_max, abatere_arbore_min): 
    # Definirea intervalului permis pentru dimensiuni nominale (în mm)
    DIM_MIN = 20
    DIM_MAX = 50

    # Listele de ajustaje preferențiale (recomandate)
    ajustaje_preferentiale = [
        ("H7", "h6"),  # Ajustaj cu joc mic
        ("H7", "p6")   # Ajustaj cu interferență
    ]

    # Declararea vectorilor pentru toleranțe pe trepte IT6 și IT7
    # Se utilizează valori standardizate pentru aceste trepte de toleranță
    tolerante_IT6 = [0.13 if 18 < d <= 30 else 0.16 for d in range(DIM_MIN, DIM_MAX + 1)]
    tolerante_IT7 = [0.21 if 18 < d <= 30 else 0.25 for d in range(DIM_MIN, DIM_MAX + 1)]

    # Verificarea dacă dimensiunile nominale sunt în intervalul permis
    if not (DIM_MIN <= d_alezaj <= DIM_MAX and DIM_MIN <= d_arbore <= DIM_MAX):
        return "Dimensiunile nu se află în intervalul permis (20 mm - 50 mm)."

    # Calcularea dimensiunilor maxime și minime ale alezajului și arborelui
    dim_alezaj_max = round(d_alezaj + abatere_alezaj_max, 4)
    dim_alezaj_min = round(d_alezaj + abatere_alezaj_min, 4)
    dim_arbore_max = round(d_arbore + abatere_arbore_max, 4)
    dim_arbore_min = round(d_arbore + abatere_arbore_min, 4)

    # Calcularea interferenței maxime și minime
    interferenta_max = round(dim_arbore_max - dim_alezaj_min, 4)
    interferenta_min = round(dim_arbore_min - dim_alezaj_max, 4)

    # Determinarea tipului de ajustaj pe baza diferenței între dimensiunile nominale
    diferenta = d_alezaj - d_arbore
    if diferenta > 0:
        tip_ajustaj = "joc"  # Există joc între alezaj și arbore
    elif diferenta < 0:
        tip_ajustaj = "presat"  # Există interferență între alezaj și arbore
    else:
        tip_ajustaj = "interferență zero"  # Dimensiunile nominale sunt egale

    # Determinarea sistemului de ajustaj (alezaj unitar sau arbore unitar)
    if d_alezaj == round(d_alezaj):
        sistem = "alezaj unitar"  # Alezajul este considerat bază unitară
    elif d_arbore == round(d_arbore):
        sistem = "arbore unitar"  # Arborele este considerat bază unitară
    else:
        sistem = "neidentificat"  # Sistemul nu poate fi determinat

    # Calcularea toleranțelor pentru alezaj și arbore
    toleranta_alezaj = round(dim_alezaj_max - dim_alezaj_min, 4)
    toleranta_arbore = round(dim_arbore_max - dim_arbore_min, 4)

    # Determinarea dacă ajustajul este preferențial pe baza toleranțelor standard IT7 și IT6
    index = int(d_alezaj - DIM_MIN)  # Indexul pentru accesarea valorilor de toleranță
    toleranta_it7 = round(tolerante_IT7[index], 4)
    toleranta_it6 = round(tolerante_IT6[index], 4)

    # Verificarea conformității cu ajustajele preferențiale
    este_preferential = (
        toleranta_alezaj == toleranta_it7 and toleranta_arbore == toleranta_it6
    )

    # Construirea raportului detaliat
    rezultat = f"Tip ajustaj: {tip_ajustaj}\n"
    rezultat += f"Sistem: {sistem}\n"
    rezultat += f"Dimensiuni alezaj: max = {dim_alezaj_max} mm, min = {dim_alezaj_min} mm\n"
    rezultat += f"Dimensiuni arbore: max = {dim_arbore_max} mm, min = {dim_arbore_min} mm\n"
    rezultat += f"Interferență: max = {interferenta_max} mm, min = {interferenta_min} mm\n"
    rezultat += f"Toleranță alezaj: {toleranta_alezaj} mm (IT7: {toleranta_it7} mm)\n"
    rezultat += f"Toleranță arbore: {toleranta_arbore} mm (IT6: {toleranta_it6} mm)\n"

    # Adăugarea informațiilor despre ajustaje preferențiale
    if este_preferential:
        rezultat += "Ajustajul este preferențial."
    else:
        rezultat += "Ajustajul NU este preferențial.\n"
        rezultat += "Sugestii pentru ajustaje preferențiale:\n"
        for ajustaj in ajustaje_preferentiale:
            rezultat += f"  - {ajustaj[0]} / {ajustaj[1]}\n"

    # Adăugarea detaliilor suplimentare despre toleranțe
    rezultat += f"\nToleranțele pentru ajustajele preferentiale la dimensiunile nominale date:\n alezaj: {d_alezaj} mm si arbore: {d_arbore} mm:\n"
    rezultat += f"  - IT6: {toleranta_it6} mm\n"
    rezultat += f"  - IT7: {toleranta_it7} mm\n"

    return rezultat