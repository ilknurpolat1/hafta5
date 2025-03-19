def tariholustur(t1, t2):
    tarih1 = t1.split('.')
    tarih2 = t2.split('.')

    yıl1 = int(tarih1[-1])
    yıl2 = int(tarih2[-1])
    ay1 = int(tarih1[-2])
    gün1 = int(tarih1[-3])
    ay2 = int(tarih2[-2])
    gün2 = int(tarih2[-3])

    tarih_listesi = []
    for y in range(yıl1, yıl2 + 1):
        for a in range(1, 13):
            for g in range(1, 32):
                tarih_listesi.append(f"{y}-{a}-{g}")

    return tarih_listesi

def url_olustur():
    gazeteler = ['sabah', 'sözcü', 'cumhuriyet', 'yeni şafak', 'hürriyet']
    kategoriler = ['gündem', 'dunya', 'teknoloji', 'eğitim', 'ekonomi']


    tarihler = tariholustur("01.01.2022", "31.12.2024")

    dosya_yolu =r"C:\Users\lknur\hafta5\h5url.txt"

    try:
        with open(dosya_yolu, 'a', encoding='utf-8') as file:
            for gazete in gazeteler:
                gazete_url = f'www.{gazete}.com.tr'

                for kategori in kategoriler:
                    for tarih in tarihler:
                        tarih_url = f'{gazete_url}/{kategori}/{tarih}'
                        file.write(tarih_url + '\n')
                        print(tarih_url)
    except Exception as e:
        print(f"Dosyaya yazma hatası: {e}")


url_olustur()