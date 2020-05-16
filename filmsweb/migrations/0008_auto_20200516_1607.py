# Generated by Django 3.0.5 on 2020-05-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmsweb', '0007_auto_20200516_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='film_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (4, 'Dramat'), (1, 'Horror'), (0, 'Inny'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(1, 'mega słabo'), (3, 'ujdzie'), (4, 'dobry'), (5, 'bardzo dobry'), (2, 'słabo'), (0, 'brak')], default=5),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('films', models.ManyToManyField(to='filmsweb.Film')),
            ],
        ),
    ]