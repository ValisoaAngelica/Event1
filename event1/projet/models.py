from django.db import models
from django.utils import timezone

class Organisateur(models.Model):
    id_organisateur = models.AutoField(db_column='ID_ORGANISATEUR', primary_key=True)  # Field name made lowercase.
    nom_organisateur = models.TextField(db_column='NOM_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    email_organisateur = models.TextField(db_column='EMAIL_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    mdp_organisateur = models.TextField(db_column='MDP_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    isorgnisateur = models.IntegerField(db_column='ISORGNISATEUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organisateur'
        
class Evenement(models.Model):
    id_evenement = models.AutoField(db_column='ID_EVENEMENT', primary_key=True)  # Field name made lowercase.
    id_organisateur = models.ForeignKey(Organisateur, db_column="ID_ORGANISATEUR",on_delete=models.CASCADE)  # Field name made lowercase.
    titre = models.TextField(db_column='TITRE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    lieu = models.TextField(db_column='LIEU', blank=True, null=True)  # Field name made lowercase.
    date_evenement = models.DateField(db_column='DATE_EVENEMENT', blank=True, null=True)  # Field name made lowercase.
    date_creation = models.DateField(db_column= "DATE_CREATION",default=timezone.now)
    capacite = models.IntegerField(db_column='CAPACITE', blank=True, null=True)  # Field name made lowercase.
    programme = models.TextField(db_column='PROGRAMME', blank=True, null=True)  # Field name made lowercase.
    # image = models.ImageField(db_column='IMAGE',upload_to='img/', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evenement'

class Participant(models.Model):
    id_participant = models.AutoField(db_column='ID_PARTICIPANT', primary_key=True)  # Field name made lowercase.
    nom_participant = models.TextField(db_column='NOM_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    email_participant = models.TextField(db_column='EMAIL_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    mdp_participant = models.TextField(db_column='MDP_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    isorganisteur = models.IntegerField(db_column='ISORGANISTEUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False

class Inscrire(models.Model):
    id_evenement = models.IntegerField(db_column='ID_EVENEMENT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_EVENEMENT, ID_PARTICIPANT) found, that is not supported. The first column is selected.
    id_participant = models.ForeignKey(Participant, db_column="ID_PARTICIPANT",on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscrire'
        unique_together = (('id_evenement', 'id_participant'),)





