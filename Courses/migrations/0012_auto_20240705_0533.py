
from django.db import migrations

def add_predefined_categories(apps, schema_editor):
    Category = apps.get_model('Courses', 'Category')
    predefined_categories = [
        'Algebra', 'Number theory', 'Geometry', 'Arithmetic', 'Topology', 'Analysis', 'Combinatorics',
        'Trigonometry', 'Applied mathematics', 'Calculus', 'Discrete mathematics', 'Linear algebra',
        'Probability', 'Mathematics', 'Order theory', 'Set theory', 'Abstract algebra', 'Commutative algebra',
        'Foundations', 'Game theory', 'Integral', 'Measure theory', 'Elementary mathematics',
        'Lie algebra and lie group theory'
    ]
    for category in predefined_categories:
        Category.objects.create(name=category)

class Migration(migrations.Migration):

    
    dependencies = [
        ('Courses', '0011_alter_course_category'),
    ]

    operations = [
        migrations.RunPython(add_predefined_categories),
    ]
