
from django.db import models

from django.utils.translation import gettext as _



# Create your models here.
class Agent (models.Model):
    name = models.CharField(_("نام") , max_length=100)
    image=models.ImageField(_("تصویر"), upload_to="agent/", null=True)
    description=models.CharField(_("توضیحات "), max_length=50)
  
    phone_number =models.CharField(_("شماره موبایل "),max_length=11, blank=True)
    email=models.EmailField(_("ایمیل"), max_length=254)
    adress=models.CharField(_("آدرس"),max_length=200)
    telegram=models.CharField(_("آیدی تلگرام "), max_length=25 , null=True)
    
    class  Meta:
        
        managed = True
        verbose_name = 'مشاور ملک'
        verbose_name_plural = 'مشاوران ملک'
  
    def __str__(self) :
        return self.name