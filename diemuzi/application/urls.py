from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from django.urls import include
from django.urls import path
from django.views import generic

from about import sitemaps as about_sitemaps
from blog import sitemaps as blog_sitemaps
from contact import sitemaps as contact_sitemaps
from cook import sitemaps as cook_sitemaps
from home import sitemaps as home_sitemaps
from photo import sitemaps as photo_sitemaps

# Sitemaps
sitemaps = {
    'about-static': about_sitemaps.StaticSitemap,
    'blog-static': blog_sitemaps.StaticSitemap,
    'blog-dynamic': blog_sitemaps.DynamicSitemap,
    'blog-dynamic-category': blog_sitemaps.DynamicSitemapCategory,
    'contact-static': contact_sitemaps.StaticSitemap,
    'cook-static': cook_sitemaps.StaticSitemap,
    'cook-dynamic': cook_sitemaps.DynamicSitemap,
    'cook-dynamic-category': cook_sitemaps.DynamicSitemapCategory,
    'home-static': home_sitemaps.StaticSitemap,
    'photo-static': photo_sitemaps.StaticSitemap,
    'photo-dynamic': photo_sitemaps.DynamicSitemap,
    'photo-dynamic-album': photo_sitemaps.DynamicSitemapAlbum
}

# URL Patterns
urlpatterns = [
    # ads.txt
    path('ads.txt', generic.TemplateView.as_view(template_name='asset/random/ads.txt')),

    # robots.txt
    path('robots.txt', generic.TemplateView.as_view(template_name='asset/random/robots.txt')),

    # sitemap.xml
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}, name='sitemap'),

    # sitemap-<section>-static.xml (for example - sitemap-login-static.xml)
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

# Static Content
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# i18n URL Patterns
urlpatterns += i18n_patterns(
    # Diemuzi URLs
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('cook/', include('cook.urls')),
    path('login/', include('login.urls')),
    path('member/', include('member.urls')),
    path('photo/', include('photo.urls')),

    # Contrib URLs
    path('comment/', include('comment.urls')),

    # Django Registration / Password URLs
    path('', include('django.contrib.auth.urls'))
)

# Error Pages
handler400 = 'asset.views.handle_400'
handler403 = 'asset.views.handle_403'
handler404 = 'asset.views.handle_404'
handler500 = 'asset.views.handle_500'

# Debug Settings
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
