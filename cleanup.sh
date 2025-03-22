#!/bin/bash

echo "Starting cleanup process..."

# 1. Create the correct directory structure if it doesn't exist
mkdir -p apps/core/templates/core
mkdir -p apps/core/static/core/css
mkdir -p apps/core/static/core/js
mkdir -p apps/core/static/core/images
mkdir -p templates/components

# 2. Move core files from blog to core (if they don't already exist in core)
if [ -d "apps/core/blog" ]; then
  [ -f "apps/core/__init__.py" ] || mv apps/core/blog/__init__.py apps/core/ 2>/dev/null
  [ -f "apps/core/admin.py" ] || mv apps/core/blog/admin.py apps/core/ 2>/dev/null
  [ -f "apps/core/apps.py" ] || mv apps/core/blog/apps.py apps/core/ 2>/dev/null
  [ -f "apps/core/models.py" ] || mv apps/core/blog/models.py apps/core/ 2>/dev/null
  [ -f "apps/core/tests.py" ] || mv apps/core/blog/tests.py apps/core/ 2>/dev/null
  [ -f "apps/core/urls.py" ] || mv apps/core/blog/urls.py apps/core/ 2>/dev/null
  [ -f "apps/core/views.py" ] || mv apps/core/blog/views.py apps/core/ 2>/dev/null
fi

# 3. Move template files to the correct location
if [ -d "apps/core/hello_world/templates" ]; then
  # Move component templates to templates/components
  [ -f "templates/components/footer.html" ] || mv apps/core/hello_world/templates/components/footer.html templates/components/ 2>/dev/null
  [ -f "templates/components/navbar.html" ] || mv apps/core/hello_world/templates/components/navbar.html templates/components/ 2>/dev/null
  
  # Move core templates to apps/core/templates/core
  [ -f "apps/core/templates/core/404.html" ] || mv apps/core/hello_world/templates/404.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/500.html" ] || mv apps/core/hello_world/templates/500.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/about_us.html" ] || mv apps/core/hello_world/templates/about_us.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/contact.html" ] || mv apps/core/hello_world/templates/contact.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/faq.html" ] || mv apps/core/hello_world/templates/faq.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/index.html" ] || mv apps/core/hello_world/templates/index.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/our_mission.html" ] || mv apps/core/hello_world/templates/our_mission.html apps/core/templates/core/ 2>/dev/null
  [ -f "apps/core/templates/core/partners.html" ] || mv apps/core/hello_world/templates/partners.html apps/core/templates/core/ 2>/dev/null
  
  # Move base.html to templates
  [ -f "templates/base.html" ] || mv apps/core/hello_world/templates/base.html templates/ 2>/dev/null
fi

# 4. Move static files to the correct location
if [ -d "apps/core/hello_world/static" ]; then
  # Move CSS files
  [ -f "apps/core/static/core/css/styles.css" ] || mv apps/core/hello_world/static/css/styles.css apps/core/static/core/css/ 2>/dev/null
  
  # Move image files
  [ -f "apps/core/static/core/images/background-img.jpg" ] || mv apps/core/hello_world/static/images/background-img.jpg apps/core/static/core/images/ 2>/dev/null
  [ -f "apps/core/static/core/images/logo.png" ] || mv apps/core/hello_world/static/images/logo.png apps/core/static/core/images/ 2>/dev/null
  
  # Move JS files
  [ -f "apps/core/static/core/js/navbar.js" ] || mv apps/core/hello_world/static/js/navbar.js apps/core/static/core/js/ 2>/dev/null
  [ -f "apps/core/static/core/js/search.js" ] || mv apps/core/hello_world/static/js/search.js apps/core/static/core/js/ 2>/dev/null
fi

# 5. Move RescueMe settings files
if [ -d "RescueMe/my_project" ]; then
  mkdir -p RescueMe/settings
  [ -f "RescueMe/__init__.py" ] || mv RescueMe/my_project/__init__.py RescueMe/ 2>/dev/null
  [ -f "RescueMe/asgi.py" ] || mv RescueMe/my_project/asgi.py RescueMe/ 2>/dev/null
  [ -f "RescueMe/urls.py" ] || mv RescueMe/my_project/urls.py RescueMe/ 2>/dev/null
  [ -f "RescueMe/wsgi.py" ] || mv RescueMe/my_project/wsgi.py RescueMe/ 2>/dev/null
  
  # Move settings.py to settings/base.py
  [ -f "RescueMe/settings/base.py" ] || mv RescueMe/my_project/settings.py RescueMe/settings/base.py 2>/dev/null
  [ -f "RescueMe/settings/__init__.py" ] || touch RescueMe/settings/__init__.py
  
  # Move development.py and production.py to settings/
  if [ -d "settings" ]; then
    [ -f "RescueMe/settings/development.py" ] || mv settings/development.py RescueMe/settings/ 2>/dev/null
    [ -f "RescueMe/settings/production.py" ] || mv settings/production.py RescueMe/settings/ 2>/dev/null
  fi
fi

# 6. Remove empty directories
find . -type d -empty -delete 2>/dev/null

echo "Cleanup completed. Check for any remaining issues manually."
