# Generated by Django 3.1.6 on 2022-05-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('OA', models.CharField(choices=[('Access', 'Access'), ('Evasion', 'Evasion'), ('Essentiel+', 'Essentiel+'), ('Access+', 'Access+'), ('Evasion+', 'Evasion+'), ('Tout Canal', 'Tout canal')], default='Access', max_length=50)),
                ('DA', models.DateField(default='2022-01-01')),
                ('NA', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
