from django.contrib import admin

from Anagrafica.models import *

@admin.register(Amministrazione)
class AmministrazioneAdmin(admin.ModelAdmin):
    list_display = ["ID", "sigla", "nome"]
    fieldsets = [
        (
            "Dati", {
                "fields": [("nome", "sigla")]
            }
        )
    ]

@admin.register(Sezione)
class SezioneAdmin(admin.ModelAdmin):
    list_display = ["ID", "amministrazione_str", "nome"]
    fieldsets = [
        (
            "Dati", {
                "fields": ["amministrazione", ("nome", "sigla")]
            }
        )
    ]
    
    @admin.display(description="Amministrazione")
    def amministrazione_str(self, obj):
        return obj.amministrazione.sigla + " - " + obj.amministrazione.nome

@admin.register(Ufficio)
class UfficioAdmin(admin.ModelAdmin):
    list_display = ["ID", "sezione_str", "nome", "n_ufficio"]
    fieldsets = [
        (
            "Dati", {
                "fields": ["sezione", ("nome", "n_ufficio")]
            }
        )
    ]
    list_filter = ["sezione__amministrazione__sigla"]
    
    @admin.display(description="Sezione")
    def sezione_str(self, obj):
        return obj.sezione.amministrazione.sigla + " - " + obj.sezione.nome