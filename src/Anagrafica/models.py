from django.db import models

class Amministrazione(models.Model):

    ID = models.AutoField(primary_key=True)
    sigla = models.CharField("Sigla", blank=True, null=False, max_length=10)
    nome = models.CharField("Nome", blank=False, null=False, max_length=250)

    class Meta:
        verbose_name = "Amministrazione"
        verbose_name_plural = "Amministrazioni"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Amministrazione_detail", kwargs={"pk": self.pk})

class Sezione(models.Model):

    ID = models.AutoField(primary_key=True)
    amministrazione = models.ForeignKey(Amministrazione, verbose_name="Amministrazione", blank=False, null=False, on_delete=models.DO_NOTHING)
    sigla = models.CharField("Sigla", blank=True, null=False, max_length=10)
    nome = models.CharField("Nome", blank=False, null=False, max_length=250)

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

    def __str__(self):
        return self.amministrazione.sigla + " - " + self.nome

    def get_absolute_url(self):
        return reverse("Sezione_detail", kwargs={"pk": self.pk})

class Ufficio(models.Model):

    ID = models.AutoField(primary_key=True)
    sezione = models.ForeignKey(Sezione, verbose_name="Sezione", blank=False, null=False, on_delete=models.DO_NOTHING)
    nome = models.CharField("Nome", blank=False, null=False, max_length=250)
    n_ufficio = models.CharField("N. Ufficio", blank=True, null=False, max_length=5)
    
    class Meta:
        verbose_name = "Ufficio"
        verbose_name_plural = "Uffici"

    def __str__(self):
        return self.sezione.amministrazione.sigla + " - " + self.sezione.nome + self.nome + (" - " + self.n_ufficio) if self.n_ufficio != "" else ""

    def get_absolute_url(self):
        return reverse("Ufficio_detail", kwargs={"pk": self.pk})
