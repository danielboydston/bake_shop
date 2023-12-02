from django.db import models
import re
from decimal import Decimal
from fractions import Fraction


class Config(models.Model):
    item = models.CharField(max_length=255, primary_key=True)
    value = models.TextField()

    def __str__(self):
        return self.item


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
        
    name = models.CharField(max_length=30, unique=True)
    abbr = models.CharField(max_length=5, unique=True) 
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
    

class PhysicalQty:

    def __init__(self, qty:Decimal, unit:Unit):
        self.qty = qty
        self.unit = unit

    def __str__(self):
        return f"{self.qty} {self.unit.abbr}"
    
    def convert(self, to_unit:Unit):
        """
        Returns a new PhysicalQty equal to this instance but in to_units
        """
        new_pq = False
        
        if self.unit.category == to_unit.category:
            # Convert to base
            equation = re.sub(r'[^ub0-9+\-*/\.]', '', self.unit.conversion_to_base)
            base = BaseUnit.objects.get(pk=self.unit.category.pk)
            u = self.qty
            b = eval(equation)

            # Convert from base
            
            equation = re.sub(r'[^ub0-9+\-*/\.a]', '', to_unit.conversion_from_base)
            new_pq = PhysicalQty(eval(equation), to_unit)
        else:
            raise ValueError(f"Cannot convert between {self.unit.category} and {to_unit.category} unit categories")

        return new_pq
    
    def mutate(self, to_unit: Unit):
        """
        Alters the current instance to be in to_units
        """
        new_pq = self.convert(to_unit)
        self.qty = new_pq.qty
        self.unit = new_pq.unit
        return True

    def as_fraction(self):
        """
        Displays the PhysicalQty as a fraction
        """
        max_denom = Config.objects.get(item="max_fraction_denominator")
        frac = Fraction(self.qty).limit_denominator(max_denom.value)
        whole = 0
        num = frac.numerator
        while num > frac.denominator:
            whole += 1
            num -= frac.denominator
        whole_str = ''
        if whole > 0:
            whole_str = f"{whole}-"
        
        return f"{whole_str}{num}/{frac.denominator} {self.unit.abbr}"
