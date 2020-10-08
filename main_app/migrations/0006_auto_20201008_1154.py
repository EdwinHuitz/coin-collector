# Generated by Django 3.1.2 on 2020-10-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201007_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default=('P', 'Pending'), max_length=1, verbose_name='CAC Certification')),
            ],
        ),
        migrations.AlterField(
            model_name='grading',
            name='company',
            field=models.CharField(choices=[('N', 'NGC / Numismatic Guaranty Corporation'), ('P', 'PCGS / Professional Coin Grading Service'), ('A', 'ANA / American Numismatic Association Certification Service'), ('O', 'Other')], default='N', max_length=1, verbose_name='Grading Company'),
        ),
    ]