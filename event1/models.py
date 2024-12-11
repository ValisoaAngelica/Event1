# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
