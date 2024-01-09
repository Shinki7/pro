from django.db import models

# Create your models here.

class Klinik(models.Model):
    class Meta:
        verbose_name_plural = 'klinik'

    def __str__(self):
        return self.nama_klinik
    
    nama_klinik = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    no_kontak = models.CharField(max_length=100)

class Dokter(models.Model):
    class Meta:
        verbose_name_plural = 'dokter'

    def __str__(self):
        return self.nama_dokter
    
    nama_dokter = models.CharField(max_length=100)
    tgl_pekerjaan = models.DateField()
    spesialis = models.CharField(max_length=100)
    klinik = models.ManyToManyField(Klinik)

class Pemilik(models.Model):
    class Meta:
        verbose_name_plural = 'pemilik'

    def __str__(self):
         return self.nama_pemilik

    nama_pemilik = models.CharField(max_length=100,  blank=False, unique=True) 
    no_kontak = models.CharField(max_length=100)

class Hewan(models.Model):
    class Meta:
        verbose_name_plural = 'hewan'

    def __str__(self):
        return self.nama_hewan

    nama_hewan = models.CharField(max_length=100)
    tgl_lahir = models.DateField()
    tipe_hewan = models.CharField(max_length=100)
    pemilik = models.ForeignKey(Pemilik, on_delete=models.PROTECT, blank=False)

class Pemeriksaan(models.Model):
    class Meta:
        verbose_name_plural = 'pemeriksaan'

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=80)
    tgl_pemeriksaan = models.DateField()
    klinik = models.ForeignKey(Klinik, on_delete=models.PROTECT, blank=False)
    dokter = models.ForeignKey(Dokter, on_delete=models.PROTECT, blank=False)
    hewan = models.ForeignKey(Hewan, on_delete=models.PROTECT, blank=False)

class Obat(models.Model):
    class Meta:
        verbose_name_plural = 'obat'

    def __str__(self):
        return self.nama_obat

    nama_obat = models.CharField(max_length=100)
    instruksi = models.CharField(max_length=100)

class Pem_obat(models.Model):
    class Meta:
        verbose_name_plural = 'pem_obat'

        def __str__(self):
            return self.hewan

    dosis = models.CharField(max_length=100)
    frekuensi = models.CharField(max_length=100)
    obat = models.ForeignKey(Obat, on_delete=models.PROTECT, blank=False)
    pemeriksaan = models.ForeignKey(Pemeriksaan, on_delete=models.PROTECT, blank=False)
    hewan = models.ForeignKey(Hewan, on_delete=models.PROTECT, blank=False)