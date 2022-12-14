from django.db        import models  
from django.utils     import timezone


class Archivo(models.Model):

    EXTENSION_CHOICES = (
    ('pdf', 'PDF'),
    ('xls', 'XLS'),
    ('xlsx', 'XLSX'),
    ('doc', 'DOC'),
    ('docx', 'DOCX'),
    ('png', 'PNG'),
    ('jpg', 'JPG'),
    ('txt', 'TXT'),
    ('ppt', 'PPT'),
    ('pptx', 'PPTX'),
    )

    nombre = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    arch = models.FileField(upload_to='documents')
    extension = models.CharField(max_length=5, choices = EXTENSION_CHOICES, default='pdf')
    fecha = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table="archivos"
        ordering = ["nombre", "fecha"] 

    def __str__(self):
        return f"{self.nombre} - {self.desc} - {self.extension} - {self.fecha}"

