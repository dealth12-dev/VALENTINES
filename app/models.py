from django.db import models

class FirstMeeting(models.Model):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"First Meeting {self.id}"

class MemorableDate(models.Model):

    image = models.ImageField(upload_to='media/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Memorable Date {self.description}"

class MilestoneAchievement(models.Model):
   
    image = models.ImageField(upload_to='media/')
    description = models.TextField()

    def __str__(self):
        return f"Milestone on {self.description}"

class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='media/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Photo {self.id}"

class LoveLetter(models.Model):
    letter_content = models.TextField()

    def __str__(self):
        return f"{self.letter_content}"

class VideoMemory(models.Model):
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Video {self.id}"

class SpecialMessage(models.Model):
    message = models.TextField()

    def __str__(self):
        return f"{self.message }"
