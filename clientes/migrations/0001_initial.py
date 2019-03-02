# Generated by Django 2.1.7 on 2019-02-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
