from django.db import models

class Evenement(models.Model):
    id_evenement = models.AutoField(db_column='ID_EVENEMENT', primary_key=True)  # Field name made lowercase.
    id_organisateur = models.IntegerField(db_column='ID_ORGANISATEUR')  # Field name made lowercase.
    titre = models.TextField(db_column='TITRE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    lieu = models.TextField(db_column='LIEU', blank=True, null=True)  # Field name made lowercase.
    date_evenement = models.DateField(db_column='DATE_EVENEMENT', blank=True, null=True)  # Field name made lowercase.
    capacite = models.IntegerField(db_column='CAPACITE', blank=True, null=True)  # Field name made lowercase.
    programme = models.TextField(db_column='PROGRAMME', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evenement'


class Inscrire(models.Model):
    id_evenement = models.IntegerField(db_column='ID_EVENEMENT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_EVENEMENT, ID_PARTICIPANT) found, that is not supported. The first column is selected.
    id_participant = models.IntegerField(db_column='ID_PARTICIPANT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscrire'
        unique_together = (('id_evenement', 'id_participant'),)


class Organisateur(models.Model):
    id_organisateur = models.AutoField(db_column='ID_ORGANISATEUR', primary_key=True)  # Field name made lowercase.
    nom_organisateur = models.TextField(db_column='NOM_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    email_organisateur = models.TextField(db_column='EMAIL_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    mdp_organisateur = models.TextField(db_column='MDP_ORGANISATEUR', blank=True, null=True)  # Field name made lowercase.
    isorgnisateur = models.IntegerField(db_column='ISORGNISATEUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organisateur'


class Participant(models.Model):
    id_participant = models.AutoField(db_column='ID_PARTICIPANT', primary_key=True)  # Field name made lowercase.
    nom_participant = models.TextField(db_column='NOM_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    email_participant = models.TextField(db_column='EMAIL_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    mdp_participant = models.TextField(db_column='MDP_PARTICIPANT', blank=True, null=True)  # Field name made lowercase.
    isorganisteur = models.IntegerField(db_column='ISORGANISTEUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participant'