# Generated by Django 3.0.5 on 2020-05-16 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('film_type', models.PositiveSmallIntegerField(choices=[(4, 'Dramat'), (3, 'Sci-fi'), (0, 'Inny'), (1, 'Horror'), (2, 'Komedia')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('year', models.PositiveSmallIntegerField(default=2000)),
                ('description', models.TextField(default='')),
                ('premiere', models.DateField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters')),
                ('additional', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmsweb.AdditionalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, 'mega słabo'), (0, 'brak'), (5, 'bardzo dobry'), (4, 'dobry'), (2, 'słabo'), (3, 'ujdzie')], default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmsweb.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('films', models.ManyToManyField(related_name='actors', to='filmsweb.Film')),
            ],
        ),
    ]
