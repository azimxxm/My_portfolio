# Generated by Django 3.2.6 on 2021-08-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About/')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('work_type', models.CharField(choices=[('IT specialist', 'IT specialist'), ('Web Developer', 'Web Developer'), ('Android Developer', 'Android Developer'), ('Mobile Developer', 'Mobile Developer'), ('UX / UI Designer', 'UX / UI Designer'), ('IOS Developer', 'IOS Developer')], max_length=50)),
                ('info_work', models.TextField(max_length=255)),
                ('birthday', models.DateField()),
                ('website', models.URLField()),
                ('phone', models.BigIntegerField()),
                ('city', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('degree', models.CharField(choices=[('Junior', 'Junior'), ('Senior', 'Senior'), ('Middle', 'Middle'), ('Team lead', 'Team lead')], max_length=20)),
                ('emil', models.EmailField(max_length=254)),
                ('freelance', models.BooleanField(default=False)),
            ],
        ),
    ]
