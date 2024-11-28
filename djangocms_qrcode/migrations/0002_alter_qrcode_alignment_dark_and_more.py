# Generated by Django 4.2.13 on 2024-06-22 16:58

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("djangocms_qrcode", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qrcode",
            name="alignment_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="alignment_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="finder_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="finder_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrcode",
            name="quiet_zone",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="border color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="alignment_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="alignment_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="finder_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="finder_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrfilelink",
            name="quiet_zone",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="border color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="alignment_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="alignment_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="alignment light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="finder_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder dark color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="finder_light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="finder light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="light",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="light color",
            ),
        ),
        migrations.AlterField(
            model_name="qrpagelink",
            name="quiet_zone",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="border color",
            ),
        ),
    ]
