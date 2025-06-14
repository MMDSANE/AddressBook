# Generated by Django 5.1.3 on 2025-04-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_contact_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="pic",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="pics/pictures",
                verbose_name="عکس مخاطب",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("published", "Published")],
                default="draft",
                max_length=10,
                verbose_name="وضعیت",
            ),
        ),
    ]
