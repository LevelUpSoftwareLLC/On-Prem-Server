from djongo import models

class Metadata(models.Model):
    headers = models.JSONField()
    description = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    robots_txt = models.TextField(blank=True, null=True)
    sitemap_xml = models.TextField(blank=True, null=True)

class Link(models.Model):
    destination = models.URLField()
    anchor_text = models.CharField(max_length=255, blank=True, null=True)
    rel = models.CharField(max_length=50, blank=True, null=True)
    found_on = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    url = models.URLField()
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

class Script(models.Model):
    url = models.URLField()
    type = models.CharField(max_length=50, blank=True, null=True)

class WebPage(models.Model):
    url = models.URLField(unique=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    crawled_at = models.DateTimeField(auto_now=True)
    http_status = models.IntegerField(default=200)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    is_indexed = models.BooleanField(default=False)
    last_modified = models.DateTimeField(blank=True, null=True)
    size = models.IntegerField(default=0)
    
    outgoing_links = models.ArrayField(model_container=Link)
    metadata = models.EmbeddedField(model_container=Metadata)
    images = models.ArrayField(model_container=Image)
    scripts = models.ArrayField(model_container=Script)