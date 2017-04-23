
1. 如何获得django application的coverage数据

a. install coverage package

b. coverage run --branch hello.py runserver  --noreload 

c. coverage html


2. 如何对django application进行profiling

a. install django-extensions
b. configure the INSTALLED_APPS 
c. python hello.py runprofile
