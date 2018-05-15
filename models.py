# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Genes(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Genes'

    def get_absolute_url(self):
        return "/gene/%s/" % self.id


class Metabolites(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    compartment = models.CharField(max_length=255, blank=True, null=True)
    charge = models.CharField(max_length=255, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Metabolites'

    def get_absolute_url(self):
        return "/metabolite/%s/" % self.id


class Reactions(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolites = models.TextField(blank=True, null=True)
    lower_bound = models.CharField(max_length=255, blank=True, null=True)
    upper_bound = models.CharField(max_length=255, blank=True, null=True)
    gene_reaction_rule = models.TextField(blank=True, null=True)
    subsystem = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reactions'

    def get_absolute_url(self):
        return "/reaction/%s/" % self.id


class Reactionsmeta(models.Model):
    id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey('Metabolites',  db_column='id', blank=True, null=True, on_delete=models.CASCADE)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey('Metabolites', db_column='name',max_length=255, blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.CharField(max_length=255, blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.CharField(max_length=255, blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.CharField(max_length=255, blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.CharField(max_length=255, blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.CharField(max_length=255, blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.CharField(max_length=255, blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.CharField(max_length=255, blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.CharField(max_length=255, blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.CharField(max_length=255, blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.CharField(max_length=255, blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry13 = models.CharField(max_length=255, blank=True, null=True)
    metabolite14 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry14 = models.CharField(max_length=255, blank=True, null=True)
    metabolite15 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry15 = models.CharField(max_length=255, blank=True, null=True)
    metabolite16 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry16 = models.CharField(max_length=255, blank=True, null=True)
    metabolite17 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry17 = models.CharField(max_length=255, blank=True, null=True)
    metabolite18 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry18 = models.CharField(max_length=255, blank=True, null=True)
    metabolite19 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry19 = models.CharField(max_length=255, blank=True, null=True)
    metabolite20 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry20 = models.CharField(max_length=255, blank=True, null=True)
    metabolite21 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry21 = models.CharField(max_length=255, blank=True, null=True)
    metabolite22 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry22 = models.CharField(max_length=255, blank=True, null=True)
    metabolite23 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry23 = models.CharField(max_length=255, blank=True, null=True)
    metabolite24 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry24 = models.CharField(max_length=255, blank=True, null=True)
    metabolite25 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry25 = models.CharField(max_length=255, blank=True, null=True)
    metabolite26 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry26 = models.CharField(max_length=255, blank=True, null=True)
    metabolite27 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry27 = models.CharField(max_length=255, blank=True, null=True)
    metabolite28 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry28 = models.CharField(max_length=255, blank=True, null=True)
    metabolite29 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry29 = models.CharField(max_length=255, blank=True, null=True)
    metabolite30 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry30 = models.CharField(max_length=255, blank=True, null=True)
    metabolite31 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry31 = models.CharField(max_length=255, blank=True, null=True)
    metabolite32 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry32 = models.CharField(max_length=255, blank=True, null=True)
    metabolite33 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry33 = models.CharField(max_length=255, blank=True, null=True)
    metabolite34 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry34 = models.CharField(max_length=255, blank=True, null=True)
    metabolite35 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry35 = models.CharField(max_length=255, blank=True, null=True)
    metabolite36 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry36 = models.CharField(max_length=255, blank=True, null=True)
    metabolite37 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry37 = models.CharField(max_length=255, blank=True, null=True)
    metabolite38 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry38 = models.CharField(max_length=255, blank=True, null=True)
    metabolite39 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry39 = models.CharField(max_length=255, blank=True, null=True)
    metabolite40 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry40 = models.CharField(max_length=255, blank=True, null=True)
    metabolite41 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry41 = models.CharField(max_length=255, blank=True, null=True)
    metabolite42 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry42 = models.CharField(max_length=255, blank=True, null=True)
    metabolite43 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry43 = models.CharField(max_length=255, blank=True, null=True)
    metabolite44 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry44 = models.CharField(max_length=255, blank=True, null=True)
    metabolite45 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry45 = models.CharField(max_length=255, blank=True, null=True)
    metabolite46 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry46 = models.CharField(max_length=255, blank=True, null=True)
    metabolite47 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry47 = models.CharField(max_length=255, blank=True, null=True)
    metabolite48 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry48 = models.CharField(max_length=255, blank=True, null=True)
    metabolite49 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry49 = models.CharField(max_length=255, blank=True, null=True)
    metabolite50 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry50 = models.CharField(max_length=255, blank=True, null=True)
    metabolite51 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry51 = models.CharField(max_length=255, blank=True, null=True)
    metabolite52 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry52 = models.CharField(max_length=255, blank=True, null=True)
    metabolite53 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry53 = models.CharField(max_length=255, blank=True, null=True)
    metabolite54 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry54 = models.CharField(max_length=255, blank=True, null=True)
    metabolite55 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry55 = models.CharField(max_length=255, blank=True, null=True)
    metabolite56 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry56 = models.CharField(max_length=255, blank=True, null=True)
    metabolite57 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry57 = models.CharField(max_length=255, blank=True, null=True)
    metabolite58 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry58 = models.CharField(max_length=255, blank=True, null=True)
    metabolite59 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry59 = models.CharField(max_length=255, blank=True, null=True)
    metabolite60 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry60 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReactionsMeta'

    def get_absolute_url(self):
        return "/reaction/%s/" % self.id


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Meta1(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite', blank=True, null=True)
    stoichiometry = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_1'


class Meta10(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.IntegerField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_10'


class Meta11(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.IntegerField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.IntegerField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_11'


class Meta12(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    field2 = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.IntegerField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.IntegerField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.IntegerField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_12'


class Meta13(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.IntegerField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.IntegerField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.IntegerField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.IntegerField(blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry13 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_13'


class Meta14(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.FloatField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.FloatField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.FloatField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.FloatField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.FloatField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.FloatField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.FloatField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.FloatField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.FloatField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.FloatField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.FloatField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.FloatField(blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry13 = models.FloatField(blank=True, null=True)
    metabolite14 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry14 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_14'


class Meta2(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_2'


class Meta3(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stochiometry3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_3'


class Meta37(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.FloatField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.FloatField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.FloatField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.FloatField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.FloatField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.FloatField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.FloatField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.FloatField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.FloatField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.FloatField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.FloatField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.FloatField(blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry13 = models.FloatField(blank=True, null=True)
    metabolite14 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry14 = models.FloatField(blank=True, null=True)
    metabolite15 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry15 = models.FloatField(blank=True, null=True)
    metabolite16 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry16 = models.FloatField(blank=True, null=True)
    metabolite17 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry17 = models.FloatField(blank=True, null=True)
    metabolite18 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry18 = models.FloatField(blank=True, null=True)
    metabolite19 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry19 = models.FloatField(blank=True, null=True)
    metabolite20 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry20 = models.FloatField(blank=True, null=True)
    metabolite21 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry21 = models.FloatField(blank=True, null=True)
    metabolite22 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry22 = models.FloatField(blank=True, null=True)
    metabolite23 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry23 = models.FloatField(blank=True, null=True)
    metabolite24 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry24 = models.FloatField(blank=True, null=True)
    metabolite25 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry25 = models.FloatField(blank=True, null=True)
    metabolite26 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry26 = models.FloatField(blank=True, null=True)
    metabolite27 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry27 = models.FloatField(blank=True, null=True)
    metabolite28 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry28 = models.FloatField(blank=True, null=True)
    metabolite29 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry29 = models.FloatField(blank=True, null=True)
    metabolite30 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry30 = models.FloatField(blank=True, null=True)
    metabolite31 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry31 = models.FloatField(blank=True, null=True)
    metabolite32 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry32 = models.FloatField(blank=True, null=True)
    metabolite33 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry33 = models.FloatField(blank=True, null=True)
    metabolite34 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry34 = models.FloatField(blank=True, null=True)
    metabolite35 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry35 = models.FloatField(blank=True, null=True)
    metabolite36 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry36 = models.FloatField(blank=True, null=True)
    metabolite37 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry37 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_37'


class Meta4(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_4'


class Meta41(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry1 = models.FloatField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry2 = models.FloatField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry3 = models.FloatField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry4 = models.FloatField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry5 = models.FloatField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry6 = models.FloatField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry7 = models.FloatField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry8 = models.FloatField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry9 = models.FloatField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry10 = models.FloatField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry11 = models.FloatField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry12 = models.FloatField(blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry13 = models.FloatField(blank=True, null=True)
    metabolite14 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry14 = models.FloatField(blank=True, null=True)
    metabolite15 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry15 = models.FloatField(blank=True, null=True)
    metabolite16 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry16 = models.FloatField(blank=True, null=True)
    metabolite17 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry17 = models.FloatField(blank=True, null=True)
    metabolite18 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry18 = models.FloatField(blank=True, null=True)
    metabolite19 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry19 = models.FloatField(blank=True, null=True)
    metabolite20 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry20 = models.FloatField(blank=True, null=True)
    metabolite21 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry21 = models.FloatField(blank=True, null=True)
    metabolite22 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry22 = models.FloatField(blank=True, null=True)
    metabolite23 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry23 = models.FloatField(blank=True, null=True)
    metabolite24 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry24 = models.FloatField(blank=True, null=True)
    metabolite25 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry25 = models.FloatField(blank=True, null=True)
    metabolite26 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry26 = models.FloatField(blank=True, null=True)
    metabolite27 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry27 = models.FloatField(blank=True, null=True)
    metabolite28 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry28 = models.FloatField(blank=True, null=True)
    metabolite29 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry29 = models.FloatField(blank=True, null=True)
    metabolite30 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry30 = models.FloatField(blank=True, null=True)
    metabolite31 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry31 = models.FloatField(blank=True, null=True)
    metabolite32 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry32 = models.FloatField(blank=True, null=True)
    metabolite33 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry33 = models.FloatField(blank=True, null=True)
    metabolite34 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry34 = models.FloatField(blank=True, null=True)
    metabolite35 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry35 = models.FloatField(blank=True, null=True)
    metabolite36 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry36 = models.FloatField(blank=True, null=True)
    metabolite37 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry37 = models.FloatField(blank=True, null=True)
    metabolite38 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry38 = models.FloatField(blank=True, null=True)
    metabolite39 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry39 = models.FloatField(blank=True, null=True)
    metabolite40 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry40 = models.FloatField(blank=True, null=True)
    metabolite41 = models.CharField(max_length=255, blank=True, null=True)
    stoichimetry41 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_41'


class Meta5(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_5'


class Meta6(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite4', blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite5', blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite6', blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_6'


class Meta60(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry1 = models.FloatField(blank=True, null=True)
    metabolite2 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry2 = models.FloatField(blank=True, null=True)
    metabolite3 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry3 = models.FloatField(blank=True, null=True)
    metabolite4 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry4 = models.FloatField(blank=True, null=True)
    metabolite5 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry5 = models.FloatField(blank=True, null=True)
    metabolite6 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry6 = models.FloatField(blank=True, null=True)
    metabolite7 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry7 = models.FloatField(blank=True, null=True)
    metabolite8 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry8 = models.FloatField(blank=True, null=True)
    metabolite9 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry9 = models.FloatField(blank=True, null=True)
    metabolite10 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry10 = models.FloatField(blank=True, null=True)
    metabolite11 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry11 = models.FloatField(blank=True, null=True)
    metabolite12 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry12 = models.FloatField(blank=True, null=True)
    metabolite13 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry13 = models.FloatField(blank=True, null=True)
    metabolite14 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry14 = models.FloatField(blank=True, null=True)
    metabolite15 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry15 = models.FloatField(blank=True, null=True)
    metabolite16 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry16 = models.FloatField(blank=True, null=True)
    metabolite17 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry17 = models.FloatField(blank=True, null=True)
    metabolite18 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry18 = models.FloatField(blank=True, null=True)
    metabolite19 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry19 = models.FloatField(blank=True, null=True)
    metabolite20 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry20 = models.FloatField(blank=True, null=True)
    metabolite21 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry21 = models.FloatField(blank=True, null=True)
    metabolite22 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry22 = models.FloatField(blank=True, null=True)
    metabolite23 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry23 = models.FloatField(blank=True, null=True)
    metabolite24 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry24 = models.FloatField(blank=True, null=True)
    metabolite25 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry25 = models.IntegerField(blank=True, null=True)
    metabolite26 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry26 = models.FloatField(blank=True, null=True)
    metabolite27 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry27 = models.FloatField(blank=True, null=True)
    metabolite28 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry28 = models.FloatField(blank=True, null=True)
    metabolite29 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry29 = models.FloatField(blank=True, null=True)
    metabolite30 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry30 = models.FloatField(blank=True, null=True)
    metabolite31 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry31 = models.FloatField(blank=True, null=True)
    metabolite32 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry32 = models.FloatField(blank=True, null=True)
    metabolite33 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry33 = models.FloatField(blank=True, null=True)
    metabolite34 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry34 = models.FloatField(blank=True, null=True)
    metabolite35 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry35 = models.FloatField(blank=True, null=True)
    metabolite36 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry36 = models.FloatField(blank=True, null=True)
    metabolite37 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry37 = models.FloatField(blank=True, null=True)
    metabolite38 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry38 = models.FloatField(blank=True, null=True)
    metabolite39 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry39 = models.FloatField(blank=True, null=True)
    metabolite40 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry40 = models.FloatField(blank=True, null=True)
    metabolite41 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry41 = models.FloatField(blank=True, null=True)
    metabolite42 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry42 = models.FloatField(blank=True, null=True)
    metabolite43 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry43 = models.FloatField(blank=True, null=True)
    metabolite44 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry44 = models.FloatField(blank=True, null=True)
    metabolite45 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry45 = models.FloatField(blank=True, null=True)
    metabolite46 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry46 = models.FloatField(blank=True, null=True)
    metabolite47 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry47 = models.FloatField(blank=True, null=True)
    metabolite48 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry48 = models.FloatField(blank=True, null=True)
    metabolite49 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry49 = models.FloatField(blank=True, null=True)
    metabolite50 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry50 = models.FloatField(blank=True, null=True)
    metabolite51 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry51 = models.FloatField(blank=True, null=True)
    metabolite52 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry52 = models.FloatField(blank=True, null=True)
    metabolite53 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry53 = models.FloatField(blank=True, null=True)
    metabolite54 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry54 = models.FloatField(blank=True, null=True)
    metabolite55 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry55 = models.FloatField(blank=True, null=True)
    metabolite56 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry56 = models.FloatField(blank=True, null=True)
    metabolite57 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry57 = models.FloatField(blank=True, null=True)
    metabolite58 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry58 = models.FloatField(blank=True, null=True)
    metabolite59 = models.CharField(max_length=255, blank=True, null=True)
    field_stoichiometry59 = models.FloatField(db_column=' stoichiometry59', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    metabolite60 = models.CharField(max_length=255, blank=True, null=True)
    stoichiometry60 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_60'


class Meta7(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite4', blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite5', blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite6', blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite7', blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_7'


class Meta8(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite4', blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite5', blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite6', blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite7', blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite8', blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_8'


class Meta9(models.Model):
    id = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metabolite1 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite1', blank=True, null=True)
    stoichiometry1 = models.IntegerField(blank=True, null=True)
    metabolite2 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite2', blank=True, null=True)
    stoichiometry2 = models.IntegerField(blank=True, null=True)
    metabolite3 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite3', blank=True, null=True)
    stoichiometry3 = models.IntegerField(blank=True, null=True)
    metabolite4 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite4', blank=True, null=True)
    stoichiometry4 = models.IntegerField(blank=True, null=True)
    metabolite5 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite5', blank=True, null=True)
    stoichiometry5 = models.IntegerField(blank=True, null=True)
    metabolite6 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite6', blank=True, null=True)
    stoichiometry6 = models.IntegerField(blank=True, null=True)
    metabolite7 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite7', blank=True, null=True)
    stoichiometry7 = models.IntegerField(blank=True, null=True)
    metabolite8 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite8', blank=True, null=True)
    stoichiometry8 = models.IntegerField(blank=True, null=True)
    metabolite9 = models.ForeignKey(Metabolites, models.DO_NOTHING, db_column='metabolite9', blank=True, null=True)
    stoichiometry9 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_9'
