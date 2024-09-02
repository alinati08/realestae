from django.db import models
from django.utils.translation import gettext as _
from agent.models import Agent
# Create your models here.
class House(models.Model):
    House_statue=[
        ("برای فروش","برای فروش"),
        ("برای اجاره","برای اجاره"),
    ]
    House_park=[
        ("دارد"," دارد "),
        ("ندارد"," ندارد  "),  
    ]
    name = models.CharField(max_length=100)
    desciption= models.CharField(_("توضیحات"),max_length=50)
    address= models.CharField(_("آدرس"),max_length=100)
    price= models.IntegerField(_("  قیمت  فروش"))
    mortgage= models.IntegerField(_("رهن") , null=True)
    rent_price= models.IntegerField(_("اجاره "), null=True)
    aria= models.IntegerField(_("مساحت به متر مربع"), default=0)
    room= models.IntegerField(_("تعداد خواب"),default=0)
    bathroom= models.IntegerField(_("تعداد حمام و دسشویی"),default=0)
    pub_date=models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    first_photo=models.ImageField(_("تصویر شاخص"),upload_to="house/",)
    second_photo=models.ImageField(_("تصویر دوم"),upload_to="house/" ,null=True,blank=True)
    third_photo=models.ImageField(_("تصویر سوم"),upload_to="house/",null=True,blank=True)
    Property_Type=models.ForeignKey("Property_Type",related_name="House", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, null=True)
    house_park=models.CharField(_(" : وضعیت پارکینگ "),max_length=10,choices=House_park,default="ندارد")
    house_statue= models.CharField(_(" : وضعیت فروش "),max_length=10,choices=House_statue,default="برای فروش ")
    agent=models.ForeignKey(Agent,related_name="Agent", verbose_name=_(" مشاوره املاک"), on_delete=models.CASCADE, )
    
    class  Meta:
        
        managed = True
        verbose_name = ' خانه '
        verbose_name_plural = '  خانه ها   '
   
   
    def _value(self):
        if self.mortgage == '0':
            return u'%s' % (self.price)
        elif self.mortgage == '1':
            return u'%s' % (self.rent_price)
       
        
        
    def __str__(self) :
        return self.name
    
    
class Property_Type(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    sluf=models.SlugField(_("عنوان لاتین"))
    published_at=models.DateField(_("تاریخ انتشار "),auto_now=False, auto_now_add=True)
    
    class  Meta:
        
        managed = True
        verbose_name = ' نوع خانه '
        verbose_name_plural = '  نوع خانه  ها   '
    
    def __str__(self) :
        return self.title
    

    
    

class ContactAgent(models.Model):
    house=models.ForeignKey(("House"),verbose_name=_("خانه"),related_name="houses", on_delete=models.CASCADE  )
    name=models.CharField(_("نام کاربر"),max_length=50)
    email=models.EmailField(_("آدرس ایمیل "),max_length=254)
    message=models.TextField(_("متن "))
    date=models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True ,null=True)
    agent=models.ForeignKey(("agent.Agent"),verbose_name=_("مشاور ملک"),related_name="agents", on_delete=models.CASCADE ,null=True )
    
    class  Meta:
        
        managed = True
        verbose_name = ' تماس با مشاور ملک '
        verbose_name_plural = '  تماس ها با مشاورین ملک ها   '
    def __str__(self) :
        return self.email
        
    
