from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_blogpost_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(blank=True, help_text='Comma-separated tags', max_length=200),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Amit Bhalla', max_length=100),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='read_time',
            field=models.PositiveIntegerField(default=5, help_text='Estimated reading time in minutes'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
    ]
