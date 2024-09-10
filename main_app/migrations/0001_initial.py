# Generated by Django 5.1.1 on 2024-09-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('file', models.FileField(upload_to='memoires/')),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('language', models.CharField(choices=[('PT', 'Portugais'), ('FR', 'Français'), ('BI', 'Bilíngue')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('language', models.CharField(choices=[('PT', 'Portugais'), ('FR', 'Français'), ('BI', 'Bilingue')], max_length=2)),
                ('location', models.CharField(choices=[('EX', "À l'extèrieur"), ('IN', "À l'intèrieur")], max_length=2)),
                ('has_music', models.CharField(choices=[('M', 'Avec musique'), ('N', 'Sans musique')], max_length=1)),
            ],
        ),
    ]
