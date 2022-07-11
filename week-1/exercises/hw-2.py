#####################
# 2. ÖDEV
#####################


# Görev 1:Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
# Görev 2:Oluşturduğunuz environment'ı aktif ediniz.
# Görev 3:Yüklü paketleri listeleyiniz.
# Görev 4:Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
# Görev 5:İndirilen Numpy'ın versiyonu nedir?
# Görev 6:Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
# Görev 7:Numpy'ı environment'tan siliniz.
# Görev 8:Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
# Görev 9:Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
# Görev 10:Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.


# Cevap 1: conda create -n myenv
# Cevap 2: conda activate myenv
# Cevap 3: conda activate myenv 3: conda list
# Cevap 4: conda install numpy pandas=1.21
# Cevap 5: conda list numpy
# Cevap 6: conda upgrade pandas
# Cevap 7: conda remove numpy
# Cevap 8: conda install seaborn matplotlib
# Cevap 9: conda env export > environment.yaml
# Cevap 10: conda env remove -n myenv