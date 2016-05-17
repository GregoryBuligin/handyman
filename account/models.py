# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class AccountManager(BaseUserManager):
    """
    Overriding methods for Account
    """
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')
        if not kwargs.get('username'):
            raise ValueError('User must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        # account.is_active = True
        account.set_password(password)
        account.is_superuser = False
        account.is_admin = False
        account.is_active = True
        # group = Group.objects.get(name='user_account')
        # account.groups.add(group)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_active = True
        account.is_superuser = True
        account.save()

        return account


class Account(AbstractBaseUser):
    """
    Using for AUTH_USER_MODEL
    """
    email = models.EmailField(
        verbose_name='Эл. Почта',
        unique=True,
        db_index=True)
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=40,
        unique=True,
        db_index=True)

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=40,
        blank=True,
        db_index=True)
    last_name = models.CharField(
        verbose_name='Фимилия',
        max_length=40,
        blank=True,
        db_index=True)

    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='api/avatars/%Y/%m/%d',
        blank=True,
        null=True)
    tagline = models.CharField(
        verbose_name='Статус',
        max_length=140,
        blank=True)

    is_admin = models.BooleanField(default = False) #False
    is_active = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        try:
            this_record = Account.objects.get(id=self.id)
            if this_record.avatar != self.avatar:
                this_record.avatar.delete(save=False)
        except:
            pass
        super(Account, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.avatar.delete(save=False)
        super(Account, self).delete(*args, **kwargs)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def has_perm(self, permissions, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        permissions = (
            ('user_account', 'can GET, POST, PUT, PATCH, DELETE'),
        )
        db_table = "Account"
        verbose_name = "Учетная запись"
        verbose_name_plural = "Учетные записи"
        ordering = ['username', 'email']
        unique_together = ('username', 'email', 'created_at')
