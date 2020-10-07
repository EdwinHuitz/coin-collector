from django.db import models
from django.urls import reverse
# Create your models here.
#name, origin, year, denom, mint
LETTERS=(
   ('PO','Poor'),
   ('FR','Fair'),
   ('AG','Almost Good'),
   ('G','Good'),
   ('VG','Very Good'),
   ('F','Fine'),
   ('VF','Very Fine'),
   ('XF','Extra Fine'),
   ('AU','Almost Good'),
   ('MS','Mint-State'),
   ('PF','Proof'),
   ('SP','Specimen'),
)
NUMBERS=(
   ('1','1'),
   ('2','2'),
   ('3','3'),
   ('4','4-6'),
   ('8','8-10'),
   ('12','12-15'),
   ('20','20-25'),
   ('30','30-35'),
   ('40','40-45'),
   ('50','50-58'),
   ('60','60-70'),
)
COMPANIES=(
   ('N','NGC / Numismatic Guaranty Corporation'),
   ('P','PCGS / Professional Coin Grading Service'),
   ('A','ANA / American Numismatic Association Certification Service'),
   ('O','Other'),
)
class Coin(models.Model):
   name = models.CharField(max_length=100)
   origin = models.CharField(max_length=100)
   year = models.IntegerField()
   denom = models.CharField(max_length=100)
   mint = models.CharField(max_length=100)

   def __str__(self):
      return self.name
   def get_absolute_url(self):
      return reverse('detail',kwargs={'coin_id':self.id})
   
class Grading(models.Model):
   letter = models.CharField('Letter Grade',
      max_length=2,
      choices=LETTERS,
      default=LETTERS[0][0]
      )
   number = models.CharField( 'Numeric Grade',
      max_length=2,
      choices=NUMBERS,
      default=NUMBERS[0][0]
      )
   company = models.CharField('Grading Company',
      max_length=1,
      choices=COMPANIES,
      default=COMPANIES[0][0]
      )
   coin = models.ForeignKey(Coin,on_delete=models.CASCADE)
   def __str__(self):

      return f"Graded {self.get_letter_display()}-{self.get_number_display()} By {self.get_company_display()}"