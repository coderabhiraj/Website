from django.utils.translation import ugettext_lazy as _
from django.db import models

from account.models import Account

CATEGORY_CHOICES = (
    ('Unisex', 'Unisex'),
    ('Women', 'Women'),
    ('Men', 'Men')
)
SUBCATEGORY_CHOICES = (
    ('T-Shirt', 'T-Shirt'),
    ('Hoodie', 'Hoodie'),
    ('Polo', 'Polo'),
    ('Jeans', 'Jeans'),
    ('Shorts', 'Shorts'),
    ('Sneaker', 'Sneaker'),
    ('Longsleeve', 'Longsleeve'),
    ('Sweatpants', 'Sweatpants'),
    ('Accesoires', 'Accesoires'),
    ('Hats', 'Hats'),
    ('Jacket', 'Jacket'),
)

SIZE_CHOICES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
)


class InserationManager(models.Manager):

    def create_inseration(self, title, description, images, category, subcategory, size):
        if not title:
            raise ValueError("Users must have an email address")
        if not images:
            raise ValueError("Users must have a password")
        if not category:
            raise ValueError("Users must have an title")
        if not size:
            raise ValueError("Users must have an first name")

        inseration = self.model(
            title=title,
            description=description,
            images=images,
            category=category,
            subcategory=subcategory,
            size=size,
        )
        inseration.save(using=self._db)
        return inseration


class Inseration(models.Model):
    inserter = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    images = models.ImageField(upload_to='images/', max_length=50, null=False, blank=False)
    subcategory = models.CharField(max_length=50, null=False, blank=False, choices=SUBCATEGORY_CHOICES)
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50, null=False, blank=False, choices=SIZE_CHOICES)

    inserted_at = models.DateTimeField(_("inserted_at"), auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = InserationManager()

    def inseration_count_for(user):
        """
        returns the number of unread messages for the given user but does not
        mark them seen
        """
        return Inseration.objects.filter(inserter=user).count()

    class Meta:
        ordering = ['-inserted_at']
        verbose_name = _("Insertion")
        verbose_name_plural = _("Insertions")
