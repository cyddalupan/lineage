from django.db import models

class WikiContent(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class WikiFolder(models.Model):
    name = models.CharField(unique=True, max_length=255)
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class WikiContentArchive(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
