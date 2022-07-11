# Generated by Django 4.0.6 on 2022-07-11 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autenticacao', '0003_usuario_usuario_alter_empresa_data_cadastro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='DATA_CADASTRO',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='DATA_CADASTRO',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='USUARIO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]