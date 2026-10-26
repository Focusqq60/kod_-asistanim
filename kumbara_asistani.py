atilan_tl=float(input("kumbarana kaç tl attın="))
guncel_kur=float(input("dolar kurunu girin="))
dolar=atilan_tl/guncel_kur
print(f"\nKumbaraya eklenen tutar: {atilan_tl:.2f} TL")
print(f"güncel döviz kuru: {guncel_kur:.2f}")
print(f"kumbaradaki artışın güncel karsılıgı: {dolar:.2f} Dolar")