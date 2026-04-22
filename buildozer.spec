[app]
# (str) Title of your application
title = Mortgage Calculator

# (str) Package name
package.name = mortgagecalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let buildozer detect recursively)
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd

# (str) Supported orientation (one of landscape, portrait, portrait-reverse,
# landscape-reverse, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Android architecture for APK build
# 32-bit variant by default
android.arch = arm64-v8a
android.accept_sdk_license = True

# Use newer python-for-android recipes for SDL2_ttf compatibility.
p4a.branch = develop

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Warn on root usage
warn_on_root = 1
