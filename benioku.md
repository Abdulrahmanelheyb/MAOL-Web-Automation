# MAOL Web Otomasyonu
### Bu Proje maol sisteminde öğrenci dereceleri otomasyonu şekilde okumak için oluşturulmuştur.



- ***Algoritmalar***
    - Öğrenci verileri Excel'den okumak
    - okunmuş olan verileri döngü ile dereceleri web'ten okumak 
    - son olarak tüm verileri Excel üzerine yazdırmak.
- ***Gerekenler***
    - Web Sürücü <br>
      Lütfen tarayıcınızı uygun Sürücü Seçiniz.
        - [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
        - [Firefox](https://github.com/mozilla/geckodriver/releases)
        - [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
        - [Opera](https://github.com/operasoftware/operachromiumdriver/releases)

- ***Değişkenler***
    ```python
    # region Globals
    excelFilePath = "C:\\Users\\abdul\\Desktop\\2020-2021-yeni-kayıt-listesi-yeni2.xlsx"
    workBookWritePath = "C:\\Users\\abdul\\Desktop\\Students-Data.xlsx"
    DriverPath = "C:\\WebDrivers\\msedgedriver.exe"
    # endregion
    ```
    - excelFilePath \
    Okunacak Öğrenci Excel Dosyası.
    - workBookWritePath \
    Oluşturulmuş Excel Dosyası Çıkış Yolu ve Adi
    - DriverPath \
    Web sürücü Yolu.