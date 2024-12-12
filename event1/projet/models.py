from django.db import models
class Evenement(models.Model):
    id_evenement = models.AutoField(db_column='ID_EVENEMENT', primary_key=True)  # Field name made lowercase.
    id_organisateur = models.IntegerField(db_column='ID_ORGANISATEUR')  # Field name made lowercase.
    titre = models.CharField(db_column='TITRE', max_length=200)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    lieu = models.CharField(db_column='LIEU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date_evenement = models.DateTimeField(db_column='DATE_EVENEMENT')  # Field name made lowercase.
    capacite = models.IntegerField(db_column='CAPACITE')  # Field name made lowercase.
    programme = models.TextField(db_column='PROGRAMME', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_creation = models.DateTimeField(db_column='DATE_CREATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evenement'


class SInscrireEvent(models.Model):
    id_inscrire = models.AutoField(db_column='ID_INSCRIRE', primary_key=True)  # Field name made lowercase.
    id_evenement = models.IntegerField(db_column='ID_EVENEMENT')  # Field name made lowercase.
    id_utilisateur = models.IntegerField(db_column='ID_UTILISATEUR')  # Field name made lowercase.
    date_inscription = models.DateTimeField(db_column='DATE_INSCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_inscrire_event'


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(db_column='ID_UTILISATEUR', primary_key=True)  # Field name made lowercase.
    nom_utilisateur = models.CharField(db_column='NOM_UTILISATEUR', max_length=100)  # Field name made lowercase.
    email_utilisateur = models.CharField(db_column='EMAIL_UTILISATEUR', unique=True, max_length=150)  # Field name made lowercase.
    mdp_utilisateur = models.CharField(db_column='MDP_UTILISATEUR', max_length=255)  # Field name made lowercase.
    role = models.CharField(db_column='ROLE', max_length=12)  # Field name made lowercase.
    date_creation = models.DateTimeField(db_column='DATE_CREATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilisateur'