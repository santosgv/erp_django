# Generated by Django 4.0.3 on 2022-07-11 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_alter_usuario_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='EMPRESA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.empresa'),
        ),
    ]