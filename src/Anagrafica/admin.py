from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display
from django.utils.safestring import mark_safe

from unfold.contrib.filters.admin import (
    AutocompleteSelectFilter,
    AutocompleteSelectMultipleFilter
)

from Anagrafica.models import *

@admin.register(Amministrazione)
class AmministrazioneAdmin(ModelAdmin):
    list_display = ["edit", "sigla", "nome"]
    list_editable = ["sigla", "nome"]
    search_fields = ["nome", "sigla"]
    fieldsets = [
        (
            "Dati", {
                "fields": [("nome", "sigla")]
            }
        )
    ]

    @display(description="")
    def edit(self, obj):
        return mark_safe(f'<a href="{obj.get_admin_url()}"><span class="material-symbols-outlined">edit_square</span></a>')

@admin.register(Sezione)
class SezioneAdmin(ModelAdmin):
    list_display = ["edit", "amministrazione", "nome"]
    list_editable = ["amministrazione", "nome"]
    search_fields = ["amministrazione__sigla", "amministrazione__nome", "nome", "sigla"]
    fieldsets = [
        (
            "Dati", {
                "fields": ["amministrazione", ("nome", "sigla")]
            }
        )
    ]

    @display(description="")
    def edit(self, obj):
        return mark_safe(f'<a href="{obj.get_admin_url()}"><span class="material-symbols-outlined">edit_square</span></a>')

@admin.register(Ufficio)
class UfficioAdmin(ModelAdmin):
    list_display = ["edit", "sezione", "nome", "n_ufficio"]
    search_fields = ["sezione__amministrazione__sigla", "sezione__amministrazione__nome", "sezione__sigla", "sezione__nome", "nome", "n_ufficio"]
    list_filter = (
        ["sezione", AutocompleteSelectFilter],
    )
    list_filter_submit = True
    list_editable = ["sezione", "nome", "n_ufficio"]

    fieldsets = [
        (
            "Dati", {
                "fields": ["sezione", ("nome", "n_ufficio")]
            }
        )
    ]

    @display(description="")
    def edit(self, obj):
        return mark_safe(f'<a href="{obj.get_admin_url()}"><span class="material-symbols-outlined">edit_square</span></a>')



# UNFOLD USER SETTINGS
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass