# Generated by Django 3.0.5 on 2020-04-16 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_town'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Почты'},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.CreateModel(
            name='zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nick_Recipient', models.CharField(max_length=200)),
                ('You_Nick', models.CharField(max_length=200)),
                ('ArrivalTown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_content_type', to='news.Town')),
                ('YouTown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Town')),
            ],
        ),
    ]