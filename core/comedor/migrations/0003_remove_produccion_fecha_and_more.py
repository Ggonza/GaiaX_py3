# Generated by Django 4.0.2 on 2022-04-08 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comedor', '0002_produccion_fecha_actualiza_produccion_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccion',
            name='fecha',
        ),
        migrations.AddField(
            model_name='produccion',
            name='peso_prod_id_pesoprod',
            field=models.ForeignKey(blank=True, db_column='peso_prod_id_pesoProd', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comedor.pesoprod'),
        ),
    ]