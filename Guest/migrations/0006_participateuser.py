# Generated by Django 4.2.2 on 2023-06-15 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0003_initial'),
        ('Guest', '0005_delete_participateuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='participateuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.event')),
                ('rooms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Organizer.room')),
            ],
        ),
    ]