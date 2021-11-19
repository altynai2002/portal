from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    CHOICES =(
        ('US', 'United State'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhstan'),
        ('UZ', 'Uzbekistan'),
        ('TJ', 'Tajikistan'),
        ('RU', 'Russia'),
        ('CHN', 'China')
    )
    country = models.CharField(max_length=300, choices=CHOICES)
    birthday = models.DateField()
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # objects = ProfileManager()

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"



# class Post(models.Model):
#     # title = models.CharField(max_length=100, verbose_name="Название")
#     # description = models.TextFIeld(verbose_name="Описание")
#     # img = models.ImageField(verbose_name="Картинка", null=True)
#     # date = models.DateField()
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Публикация"
#         verbose_name_plural = "Публикации"
