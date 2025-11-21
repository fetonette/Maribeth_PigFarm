from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Pig, UserProfile, Feedback


class PigSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Pig.objects.filter(is_available=True)

    def lastmod(self, obj):
        return getattr(obj, "updated_at", obj.created_at)


class UserProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return UserProfile.objects.all()

    def lastmod(self, obj):
        return getattr(obj, "updated_at", obj.created_at)


class FeedbackSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Feedback.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'available_pigs', 'description', 'view_cart', 'customer_reservation_list']

    def location(self, item):
        return reverse(item)
