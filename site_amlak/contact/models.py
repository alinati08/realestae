from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Contact(models.Model):
    name=models.CharField(_("نام کاربر"),max_length=50)
    email=models.EmailField(_("آدرس ایمیل "),max_length=254)
    subject=models.CharField(_(" موضوع"), max_length=50)
    content=models.TextField(_("متن "))
    date=models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True ,null=True)
    
    
    class  Meta:
        
        managed = True
        verbose_name = ' ارتباط   '
        verbose_name_plural = '  ارتباط ها   '
        
    def __str__(self) :
        return self.email
    

