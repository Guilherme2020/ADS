from .myapp.models import *

def teste():
    print("####")

    blog_name = Blog()

    blog_name.name = 'MyBlog1'
    blog_name.save()


    entry1 = Entry()
    '''
    entry1.headline = 'perfilLinha'
    entry1.body_text = 'lorem lorem'
    entry1.pub_date = '2018-01-12'
    entry1.blog(blog_name)
    entry1.save()
    '''
    Blog.objects.create(name="my person blog")
    Entry.objects.create(headline='perfilinha',body_text = ' loren loren ',pub_date='2018-01-12'
                         ,blog =blog_name)

    print("Blog criado ")


def script():

    Blog.objects.create(name="Teste")
    Blog.objects.all()
    Blog.objects.all[0]
    Blog.objects.add()
    Blog.objects.set_all()
    Blog.objects.remove()
    Blog.objects.clear()

    Entry.objects.create(headline="perfilLinha", body_text="lorem lorem", pub_date='2018-01-12', blog=Blog)
    Entry.objects.add()
    Entry.objects.remove()
    Entry.objects.clear()
    #erro

if __name__ == '__main__':

    script()

''' 
python manage.py shell
Python 3.5.3 (default, Nov 23 2017, 11:34:05) 
[GCC 6.3.0 20170406] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from myapp.models import *
>>> Blog.objects.create(name="Teste")
<Blog: Blog object (1)>
>>> blog.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'blog' is not defined
>>> Blog.objects.all()
<QuerySet [<Blog: Blog object (1)>]>
>>> Blog.objects.all()[0]
<Blog: Blog object (1)>
>>> Blog.objects.all()[0].name
'Teste'
>>> blog
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'blog' is not defined
>>> blog = Blog.objects.all()[0]
>>> blog
<Blog: Blog object (1)>
>>> Entry.objects.create(headline="perfilLinha", body_text="lorem lorem", pub_date='2018-01-12', blog=blog)
<Entry: Entry object (1)>
>>> 
>>> Entry.objects.add
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'add'
>>> blog
<Blog: Blog object (1)>
>>> blog.objects.add
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/guilherme/Documentos/ADS/Programacao-Internet/slides/exercicios-django/venv/lib/python3.5/site-packages/django/db/models/manager.py", line 178, in __get__
    raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
AttributeError: Manager isn't accessible via Blog instances
>>> b = Blog()
>>> b
<Blog: Blog object (None)>
>>> b.clear
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Blog' object has no attribute 'clear'
>>> b.clear()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Blog' object has no attribute 'clear'
>>> b.objects.clea
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/guilherme/Documentos/ADS/Programacao-Internet/slides/exercicios-django/venv/lib/python3.5/site-packages/django/db/models/manager.py", line 178, in __get__
    raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
AttributeError: Manager isn't accessible via Blog instances
>>> b.objects.clear
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/guilherme/Documentos/ADS/Programacao-Internet/slides/exercicios-django/venv/lib/python3.5/site-packages/django/db/models/manager.py", line 178, in __get__
    raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
AttributeError: Manager isn't accessible via Blog instances
>>> b.objects.clear()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/guilherme/Documentos/ADS/Programacao-Internet/slides/exercicios-django/venv/lib/python3.5/site-packages/django/db/models/manager.py", line 178, in __get__
    raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
AttributeError: Manager isn't accessible via Blog instances
>>> blog.remove
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Blog' object has no attribute 'remove'
>>> blog.objects.remove
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/guilherme/Documentos/ADS/Programacao-Internet/slides/exercicios-django/venv/lib/python3.5/site-packages/django/db/models/manager.py", line 178, in __get__
    raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
AttributeError: Manager isn't accessible via Blog instances
>>> Blog.objects.remove
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'remove'
>>> blog.delete
<bound method Model.delete of <Blog: Blog object (1)>>
>>> blog.delete()
(2, {'myapp.Blog': 1, 'myapp.Entry': 1})
>>> ls
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'ls' is not defined
>>> 

'''