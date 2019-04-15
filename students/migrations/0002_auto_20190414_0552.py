# Generated by Django 2.1.7 on 2019-04-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('ACTI', 'Activo'), ('IRRE', 'Irregular'), ('BAJ', 'Baja')], default='ACTI', max_length=5),
        ),
    ]