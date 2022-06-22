from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class Filiere(models.Model):
     nom= models.CharField(max_length=200)
     
     def __str__ (self):
         return self.nom

class Filiere_Licence(Filiere):
     def __str__ (self):
         return self.nom

class Filiere_Master(Filiere):
     def __str__ (self):
         return self.nom

class Departement(models.Model):
     nom= models.CharField(max_length=200)
     filiere= models.ManyToManyField(Filiere, related_name='filiere', blank=True)
     
     def __str__ (self):
         return self.nom


class Etudiant_Licence_Public_L1(models.Model):
     numeroInscription= models.CharField(max_length=6)
     nom= models.CharField(max_length=200)
     photoEtudiant=models.ImageField(null=True)
     nni=models.IntegerField()
     sexe=models.CharField(max_length=200)
     # nationalite= models.CharField(max_length=200)
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     # telephone = PhoneNumberField(unique = True, null = False, blank = False)
     telephoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
     telephone = models.CharField(validators = [telephoneRegex], max_length = 8, unique = True)
     email = models.CharField(max_length=200)
     carteIdentite=models.ImageField(null=True)
     numBac=models.IntegerField()
     serie= models.CharField(max_length=200)
     releveNote=models.ImageField(null=True)
     session= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     pays= models.CharField(max_length=200)
     AnObtantionBac=models.DateField()
     filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)
     
     

     def __str__(self):  
        return self.nom


class Orientation(models.Model):
     nom= models.CharField(max_length=200)
     nni=models.IntegerField()
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     serie= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     filiere=models.CharField(max_length=200)

     def __str__(self):  
        return self.nom 

class Etudiant(models.Model):
     nom= models.CharField(max_length=200)
     photoEtudiant=models.ImageField(null=True)
     nni=models.IntegerField()
     sexe=models.CharField(max_length=200)
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     telephone = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     carteIdentite=models.ImageField(null=True)
     numBac=models.IntegerField()
     serie= models.CharField(max_length=200)
     releveNote=models.ImageField(null=True)
     session= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     pays= models.CharField(max_length=200)
     AnObtantionBac=models.DateField()
     niveau=models.CharField(max_length=200, null=True)

     class Meta:
          abstract=True

class Etudiant_Licence(Etudiant):
     filiere=models.ForeignKey(Filiere_Licence, on_delete=models.CASCADE)     

class Etudiant_Master(Etudiant):
     licence= models.CharField(max_length=200)
     filiere=models.ForeignKey(Filiere_Master, on_delete=models.CASCADE)
     

class Etudiant_Public_Licence(Etudiant_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence(Etudiant_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Public_Licence_Niveau1(Etudiant_Public_Licence):
     def __str__(self):  
        return self.nom 

class Etudiant_Public_Licence_Niveau2(Etudiant_Public_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Public_Licence_Niveau3(Etudiant_Public_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau1(Etudiant_Prive_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau2(Etudiant_Prive_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau3(Etudiant_Prive_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Public_Master(Etudiant_Master):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Master(Etudiant_Master):
     def __str__(self):  
        return self.nom

class Etudiant_Public_Master_Niveau1(Etudiant_Public_Master):
     def __str__(self):  
        return self.nom
class Etudiant_Public_Master_Niveau2(Etudiant_Public_Master):
     def __str__(self):  
        return self.nom
class Etudiant_Prive_Master_Niveau1(Etudiant_Prive_Master):
     def __str__(self):  
        return self.nom
class Etudiant_Prive_Master_Niveau2(Etudiant_Prive_Master):
     def __str__(self):  
        return self.nom