from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin,Permission,Group
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings

class Structure(models.Model):
    nom = models.CharField(_("nom du département"),max_length=150,blank=False,null=False)
    responsable = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,blank=True,null=True)
    def __str__(self):
        return self.nom

class UserManager(BaseUserManager):
    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("veuillez spécifier l'é-mail")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("Nom"), max_length=150, blank=False,null=False)
    last_name = models.CharField(_("Prénom"), max_length=150, blank=False,null=False)
    email = models.EmailField(_("Adresse e-mail"), blank=False,null=False,unique=True)
    matricule = models.CharField(_("Matricule"), max_length=20, blank=False,null=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("compte activé"),
        default=True,)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    departement = models.ForeignKey(Structure,on_delete=models.PROTECT,blank=True,null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='comptes_users',  # Add a related_name to avoid clashes
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='comptes_users_permissions',  # Add a related_name to avoid clashes
        help_text=_('Specific permissions for this user.'),
        error_messages={
            'add': _('The permission was not added.'),
            'remove': _('The permission was not removed.'),
        },
    )
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","matricule"]

    class Meta:
        verbose_name = _("utilisateur")
        verbose_name_plural = _("utilisateurs")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)






