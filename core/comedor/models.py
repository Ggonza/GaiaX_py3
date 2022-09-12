# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone

from crum import get_current_user
from django.db import models
from core.models import BaseModel, DespBaseModel


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cocinero(models.Model):
    idcocinero = models.AutoField(primary_key=True)
    puesto_assig = models.CharField(max_length=45, blank=True, null=True)
    user_user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cocinero'


class Curso(models.Model):
    idcurso = models.AutoField(primary_key=True)
    no_curso = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Desperdicios(DespBaseModel):
    iddesperdicios = models.AutoField(db_column='idDesperdicios', primary_key=True)  # Field name made lowercase.
    peso_solidos = models.FloatField(  blank=True, null=True)
    peso_liquidos = models.FloatField(  blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usu_creacion_id = user.pk
        super(Desperdicios, self).save()

    class Meta:
        managed = True
        db_table = 'desperdicios'


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


class Estadistics(models.Model):
    idestadistics = models.AutoField(primary_key=True)
    desperdicios_iddesperdicios = models.ForeignKey(Desperdicios, models.DO_NOTHING, db_column='Desperdicios_idDesperdicios')  # Field name made lowercase.
    produccion_idproduccion = models.ForeignKey('Produccion', models.DO_NOTHING, db_column='produccion_idProduccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estadistics'


class Estudiante(models.Model):
    idestudiante = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    asistencia = models.IntegerField()
    estado_est = models.IntegerField()
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_idcurso')

    class Meta:
        managed = False
        db_table = 'estudiante'


class ListaUsc(models.Model):
    idlista_usc = models.AutoField(db_column='idLista_USC', primary_key=True)  # Field name made lowercase.
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_idcurso')
    cantidad_est = models.IntegerField(db_column='Cantidad_est')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    profesor_idprofesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='profesor_idprofesor')

#sobreescritura del metodo SAVE()
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                zend = Profesor.objects.get(user_user_id=user.pk).idprofesor
                curzo = Profesor.objects.get(idprofesor=zend).curso_idcurso_id
                self.profesor_idprofesor_id= zend
                self.curso_idcurso_id = curzo
        super(ListaUsc, self).save()

    class Meta:
        managed = False
        db_table = 'lista_usc'


class Menu(models.Model):
    idmenu = models.AutoField(primary_key=True)
    item1 = models.CharField(max_length=45, blank=True, null=True)
    item2 = models.CharField(max_length=45, blank=True, null=True)
    item3 = models.CharField(max_length=45, blank=True, null=True)
    item4 = models.CharField(max_length=45, blank=True, null=True)
    item5 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class PesoProd(models.Model):
    id_pesoprod = models.AutoField(db_column='id_pesoProd', primary_key=True)  # Field name made lowercase.
    item1 = models.FloatField(  blank=True, null=True)
    item2 = models.FloatField(  blank=True, null=True)
    item3 = models.FloatField(  blank=True, null=True)
    item4 = models.FloatField(  blank=True, null=True)
    item5 = models.FloatField(  blank=True, null=True)
    menu_idmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu_idmenu')

    #sobreescritura del metodo SAVE()
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     user = get_current_user()
    #     asd = PesoProd.objects.last().id_pesoprod
    #     print('peso : ', asd)
    #     if user is not None:
    #         if not self.pk:
    #             id_coci = Cocinero.objects.get(user_user_id= user.pk)
    #             c_est = ListaUsc.objects.filter(fecha__gte=timezone.now() - timedelta(1)).aggregate(Sum('cantidad_est'))
    #             Produccion.objects.create(
    #                                       cant_est= c_est['cantidad_est__sum'],
    #                                       peso_prod_id_pesoprod=self.id_pesoprod,
    #                                       usu_creacion=user
    #                                       )
    #     super(PesoProd, self).save()

    class Meta:
        managed = False
        db_table = 'peso_prod'


class Produccion(BaseModel):
    idproduccion = models.AutoField(db_column='idProduccion', primary_key=True)  # Field name made lowercase.
    cant_est = models.IntegerField(blank=True, null=True)
    peso_prod_id_pesoprod = models.ForeignKey(PesoProd, models.DO_NOTHING, db_column='peso_prod_id_pesoProd', null=True, blank=True)  # Field name made lowercase.
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     user = get_current_user()
    #     if user is not None:
    #         if not self.pk:
    #             self.usu_creacion = user
    #         else:
    #             self.usu_actualiza = user
    #     super(Produccion, self).save()

    class Meta:
        managed = True
        db_table = 'produccion'


class Profesor(models.Model):
    idprofesor = models.AutoField(primary_key=True)
    asignatura = models.CharField(db_column='Asignatura', max_length=45, blank=True, null=True)  # Field name made lowercase.
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_idcurso')
    user_user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profesor'


class Rector(models.Model):
    idadmin = models.AutoField(db_column='idAdmin', primary_key=True)  # Field name made lowercase.
    sede = models.CharField(max_length=45, blank=True, null=True)
    user_user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rector'


class Rol(models.Model):
    idrol = models.IntegerField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    rol_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class UserUser(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    imagen = models.CharField(max_length=100, blank=True, null=True)
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Rol_idRol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group'),)


class UserUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('user', 'permission'),)
