# Generated by Django 4.0.2 on 2022-04-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cocinero',
            fields=[
                ('idcocinero', models.AutoField(primary_key=True, serialize=False)),
                ('puesto_assig', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cocinero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('no_curso', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Desperdicios',
            fields=[
                ('iddesperdicios', models.AutoField(db_column='idDesperdicios', primary_key=True, serialize=False)),
                ('peso_solidos', models.FloatField(blank=True,  null=True)),
                ('peso_liquidos', models.FloatField(blank=True,  null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'desperdicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadistics',
            fields=[
                ('idestadistics', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'estadistics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('idestudiante', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(blank=True, max_length=45, null=True)),
                ('asistencia', models.IntegerField()),
                ('estado_est', models.IntegerField()),
            ],
            options={
                'db_table': 'estudiante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListaUsc',
            fields=[
                ('idlista_usc', models.AutoField(db_column='idLista_USC', primary_key=True, serialize=False)),
                ('cantidad_est', models.IntegerField(db_column='Cantidad_est')),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
            ],
            options={
                'db_table': 'lista_usc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('idmenu', models.AutoField(primary_key=True, serialize=False)),
                ('item1', models.CharField(blank=True, max_length=45, null=True)),
                ('item2', models.CharField(blank=True, max_length=45, null=True)),
                ('item3', models.CharField(blank=True, max_length=45, null=True)),
                ('item4', models.CharField(blank=True, max_length=45, null=True)),
                ('item5', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PesoProd',
            fields=[
                ('id_pesoprod', models.AutoField(db_column='id_pesoProd', primary_key=True, serialize=False)),
                ('item1', models.FloatField(blank=True,  null=True)),
                ('item2', models.FloatField(blank=True,  null=True)),
                ('item3', models.FloatField(blank=True,  null=True)),
                ('item4', models.FloatField(blank=True,  null=True)),
                ('item5', models.FloatField(blank=True,  null=True)),
            ],
            options={
                'db_table': 'peso_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('idproduccion', models.AutoField(db_column='idProduccion', primary_key=True, serialize=False)),
                ('cant_est', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
            ],
            options={
                'db_table': 'produccion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('idprofesor', models.AutoField(primary_key=True, serialize=False)),
                ('asignatura', models.CharField(blank=True, db_column='Asignatura', max_length=45, null=True)),
            ],
            options={
                'db_table': 'profesor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rector',
            fields=[
                ('idadmin', models.AutoField(db_column='idAdmin', primary_key=True, serialize=False)),
                ('sede', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'rector',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.IntegerField(db_column='idRol', primary_key=True, serialize=False)),
                ('rol_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('imagen', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_user_user_permissions',
                'managed': False,
            },
        ),
    ]