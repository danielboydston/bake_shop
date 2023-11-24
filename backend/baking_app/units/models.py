from django.db import models

class UnitCategory(models.Model):
    name = models.CharField(max_length=30) 
    
    class Meta:  
        verbose_name_plural = 'Unit categories'

    def __str__(self):
        return self.name

class Unit(models.Model):
    
    class UnitSystem(models.TextChoices):
        IMPERIAL = 'Imperial'
        METRIC = 'Metric'
        UNIVERSAL = 'Universal'
        
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=5) 
    category = models.ForeignKey(UnitCategory, on_delete=models.CASCADE)
    conversion_to_base = models.CharField(max_length=255)
    conversion_from_base = models.CharField(max_length=255)
    unit_system = models.CharField(max_length=9, choices=UnitSystem.choices, default=UnitSystem.METRIC)

    def __str__(self):
        return self.abbr

class BaseUnit(models.Model):
    category = models.OneToOneField(UnitCategory, on_delete=models.CASCADE, primary_key=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.unit}"

