# Generated by Django 3.0.6 on 2020-09-13 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200910_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_on', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ItemModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]