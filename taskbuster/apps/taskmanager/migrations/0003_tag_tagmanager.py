# Generated by Django 3.0.5 on 2020-04-14 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
                'unique_together': {('user', 'name')},
            },
        ),
    ]