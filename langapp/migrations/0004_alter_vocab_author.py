# Generated by Django 4.2.5 on 2023-10-05 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("langapp", "0003_alter_vocab_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vocab",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
