
BLessons = [
    dict(Credit=2, Name="AÇIK KAYNAK İŞLETİM SİSTEMLERİ 1"),
    dict(Credit=2, Name="BİLGİSAYARLI TASARIM UYGULAMALARI 1"),
    dict(Credit=2, Name="BİLGİSAYARLI TASARIM UYGULAMALARI 2"),
    dict(Credit=2, Name="BİLİŞİM TEKNİK RESMİ 1"),
    dict(Credit=3, Name="BİLİŞİM TEKNOLOJİLERİNİN TEMELLER 1"),
    dict(Credit=3, Name="BİLİŞİM TEKNOLOJİLERİNİN TEMELLERİ 2"),
    dict(Credit=8, Name="GRAFİK VE ANİMASYON 1"),
    dict(Credit=7, Name="İNTERNET PROGRAMCILIĞI 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM ATÖLYESİ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM ATÖLYESİ 2"),
    dict(Credit=2, Name="OFİS PROGRAMLARI 1"),
    dict(Credit=4, Name="PROGRAMLAMA TEMELLERİ 1"),
    dict(Credit=4, Name="PROGRAMLAMA TEMELLERİ 2"),
    dict(Credit=4, Name="WEB TASARIMI VE PROGRAMLAMA 1 (*)"),
]
ELessons = [
    dict(Credit=2, Name="BİLGİSAYAR DESTEKLİ UYGULAMALAR 1"),
    dict(Credit=3, Name="DİJİTAL ELEKTRONİK 1"),
    dict(Credit=2, Name="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 1"),
    dict(Credit=2, Name="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 2"),
    dict(Credit=9, Name="ELEKTRİK-ELEKTRONİK VE ÖLÇME 1 (*)"),
    dict(Credit=9, Name="ELEKTRİK-ELEKTRONİK VE ÖLÇME 2 (*)"),
    dict(Credit=3, Name="ELEKTRİK ELEKTRONİK ESASLARI 1"),
    dict(Credit=3, Name="ELEKTRİK ELEKTRONİK ESASLARI 2"),
    dict(Credit=6, Name="ELEKTRİK MAKİNELERİ VE KONTROL SİSTEMLERİ 1 (*)"),
    dict(Credit=0, Name="ENDÜSTRİYEL ELEKTRİK SİSTEMLERİ 1"),
    dict(Credit=4, Name="ENDÜSTRİYEL KONTROL SİSTEMLERİ 1"),
    dict(Credit=5, Name="ENDÜSTRİYEL KONTROL VE ARIZA ANALİZ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=2, Name="MİKROKONTROL DEVRELERİ 1"),
    dict(Credit=9, Name="TEMEL ELEKTRİK-ELEKTRONİK ATÖLYESİ 1 (*)")]
MLessons = [
    dict(Credit=4, Name="BİLGİSAYAR DESTEKLİ TASARIM VE ÜRETİM 1 (CAD/CAM)"),
    dict(Credit=4, Name="BİLGİSAYAR DESTEKLİ TASARIM VE ÜRETİM 2 (CAD/CAM)"),
    dict(Credit=8, Name="BİLGİSAYAR KONTROLLÜ TEZGAHLARLA ÜRETİM 1 (CNC) (*)"),
    dict(Credit=2, Name="HİDROLİK PNÖMATİK 1"),
    dict(Credit=8, Name="İMALAT İŞLEMLERİ 1"),
    dict(Credit=24, Name="İŞLETMELERDE MESLEKİ EĞİTİM 1 (*)"),
    dict(Credit=24, Name="İŞLETMELERDE MESLEKİ EĞİTİM 2 (*)"),
    dict(Credit=8, Name="KATI MODELLEME VE ANİMASYON 1"),
    dict(Credit=8, Name="KATI MODELLEME VE ANİMASYON 2"),
    dict(Credit=8, Name="MAKİNE ELEMANLARI VE MEKANİZMALAR 1 (*)"),
    dict(Credit=8, Name="MAKİNE ELEMANLARI VE MEKANİZMALAR 2 (*)"),
    dict(Credit=4, Name="MAKİNE MESLEK RESMİ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=3, Name="TASARI GEOMETRİ 1"),
    dict(Credit=3, Name="TASARI GEOMETRİ 2"),
    dict(Credit=8, Name="TEMEL İMALAT İŞLEMLERİ 1 (*)"),
    dict(Credit=8, Name="TEMEL İMALAT İŞLEMLERİ 2 (*)"),
    dict(Credit=4, Name="TEKNİK RESİM 1"),
    dict(Credit=2, Name="BİLGİSAYAR DESTEKLİ ÇİZİM 1")]

BTotalCredits = 0
for credit in BLessons:
    BTotalCredits += int(credit["Credit"])
print(f'informatic : {BTotalCredits}')

ETotalCredits = 0
for credit in ELessons:
    ETotalCredits += int(credit["Credit"])
print(f'electronic : {ETotalCredits}')

MTotalCredits = 0
for credit in MLessons:
    MTotalCredits += int(credit["Credit"])
print(f'Machine : {MTotalCredits}')




