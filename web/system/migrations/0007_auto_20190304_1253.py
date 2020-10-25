# Generated by Django 2.1.2 on 2019-03-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0006_auto_20190221_1426"),
    ]

    operations = [
        migrations.CreateModel(
            name="Load",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(default="undefined", max_length=255),
                ),
                ("occupancy", models.PositiveSmallIntegerField(default=4)),
                ("data", models.TextField(default="undefined")),
            ],
        ),
        migrations.AlterField(
            model_name="component",
            name="type",
            field=models.CharField(
                choices=[
                    [
                        "converter",
                        [
                            ["hp", "heat pump"],
                            ["pv", "photovoltaic"],
                            ["sol_col", "solar collector"],
                            ["el_res", "electric resistance"],
                            ["gas_burn", "gas burner"],
                        ],
                    ],
                    [
                        "storage",
                        [
                            ["hp_tank", "heat pump tank"],
                            ["sol_tank", "solar storage tank"],
                        ],
                    ],
                    [
                        "distribution",
                        [
                            ["inv", "inverter"],
                            ["dist_pump", "distribution pump"],
                            ["sol_pump", "solar pump"],
                            ["piping", "piping"],
                        ],
                    ],
                ],
                default="undefined",
                max_length=255,
            ),
        ),
    ]
