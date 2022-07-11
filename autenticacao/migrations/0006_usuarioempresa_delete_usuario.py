# Generated by Django 4.0.6 on 2022-07-11 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autenticacao', '0005_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_EMPRESA', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.empresa')),
                ('USUARIO', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]