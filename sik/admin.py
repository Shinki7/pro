from django.contrib import admin
from .models import *
# Register your models here.

class KlinikAdmin(admin.ModelAdmin):
    list_display = ("nama_klinik", "alamat", "no_kontak",)

class DokterAdmin(admin.ModelAdmin):
    list_display = ("nama_dokter", "spesialis", "tgl_pekerjaan",)

class PemilikAdmin(admin.ModelAdmin):
    list_display = ("nama_pemilik", "no_kontak",)

class HewanAdmin(admin.ModelAdmin):
    list_display = ("nama_hewan", "tgl_lahir","tipe_hewan", "pemilik",)

class PemeriksaanAdmin(admin.ModelAdmin):
    list_display = ("title", "tgl_pemeriksaan", "hewan", "dokter", "klinik",)

class ObatAdmin(admin.ModelAdmin):
    list_display = ("nama_obat", "instruksi",)

class Pem_obatAdmin(admin.ModelAdmin):
    list_display = ("dosis", "frekuensi", "obat", "get_Pemeriksaan", "hewan",)
    def get_Pemeriksaan(self, obj):
        return obj.pemeriksaan
    get_Pemeriksaan.admin_order_field = 'Pemeriksaan'
    get_Pemeriksaan.short_description = 'Pemeriksaan'

admin.site.register(Pem_obat, Pem_obatAdmin)
admin.site.register(Obat, ObatAdmin)
admin.site.register(Pemeriksaan, PemeriksaanAdmin)
admin.site.register(Klinik, KlinikAdmin)
admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pemilik, PemilikAdmin)
admin.site.register(Hewan, HewanAdmin)