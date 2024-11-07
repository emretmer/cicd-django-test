#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django

def main():
    """Run administrative tasks."""
    # Django ayarlarını doğru şekilde yüklüyoruz
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    
    # Django'yu başlatıyoruz
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Django'yu başlatmadan önce, testlerde ihtiyaç duyulan ayarları yüklemek için django.setup() ekleyebilirsiniz
    django.setup()

    # Komutları çalıştır
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
