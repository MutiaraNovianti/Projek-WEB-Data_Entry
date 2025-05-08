from django.shortcuts import render, redirect
from .forms import * 
from .models import *
from django.http import JsonResponse


# Create your views here.
def set_data_entry(request):
    form = AddressForm()
    context = {
        'form': form,
    }
    return render(request, 'data_entry/data_entry.html', context)

'''
def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    context = None
    form = PenggunaForm(None)
    email_p = None

    if request.method == "POST":
        form = PenggunaForm(request.POST, request.FILES)
        if form.is_valid():
            # Simpan ID pengguna pada saat user klik menu sign in
            email = form.cleaned_data['email']
            request.session['email'] = email
            request.session.modified = True
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            email_p = request.session['email']
            context = {
                'form': form,
                'list_pengguna': list_pengguna,
                'email_p': email_p,
            }
            return render(request, 'data_entry/data_entry_1.html', context)
    else:
        context = {
            'form': form,
            'list_pengguna': list_pengguna,
        }
        return render(request, 'data_entry/data_entry_1.html', context)

'''

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    email_p = None

    if request.method == "POST":
        form = PenggunaForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['email'] = email
            request.session.modified = True
            form.save()
            email_p = request.session['email']
        # Tidak peduli valid atau tidak, tetap render halaman
        context = {
            'form': form,
            'list_pengguna': Pengguna.objects.all().order_by('-id'),
            'email_p': email_p,
        }
        return render(request, 'data_entry/data_entry_1.html', context)

    else:
        form = PenggunaForm()
        context = {
            'form': form,
            'list_pengguna': list_pengguna,
        }
        return render(request, 'data_entry/data_entry_1.html', context)



def view_pengguna(request):
    pass

def view_pengguna(request, id):
    try:
        pengguna = Pengguna.objects.get(pk=id)
        return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def get_pengguna_detail_api(request, user_id):
    try:
        pengguna = Pengguna.objects.get(pk=user_id)
        data = {
            'email': pengguna.email,
            'address_1': pengguna.address_1,
            'address_2': pengguna.address_2,
            'city': pengguna.city,
            'state': pengguna.state,
            'zip_code': pengguna.zip_code,
            'tanggal_join': pengguna.tanggal_join.strftime('%Y-%m-%d')  # Format date as string
        }
        return JsonResponse(data)
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User not found'},status=404)
    
def set_content(request):
    form = ContentForm()
    context = {}
    email = request.session.get('email')
    pengguna = None
    isi_tabel = None

    if email:
        try:
            pengguna = Pengguna.objects.get(email=email)
            isi_tabel = Content.objects.filter(author=pengguna)
            
            if request.method == 'POST':
                form = ContentForm(request.POST)
                if form.is_valid():
                    content = form.save(commit=False)
                    content.author = pengguna
                    content.save()
                    return redirect('data_entry:set_content')
            else:
                
                form = ContentForm(initial={'author': pengguna})
                
        except Pengguna.DoesNotExist:
            pass  

    context = {
        'form': form,
        'email': email,
        'pengguna': pengguna,
        'isi_tabel': isi_tabel,
    }
    return render(request, 'data_entry/content.html', context)

from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect,reverse
def delete_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    pengguna.delete()
    return redirect('data_entry:set_pengguna')

def update_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    if request.method == 'POST':
        form = PenggunaForm(request.POST,request.FILES, instance=pengguna)
        if form.is_valid():
            form.save()
            return redirect('data_entry:set_pengguna')
    else:
        form = PenggunaForm(instance=pengguna)
    return render(request, 'data_entry/update_pengguna.html', {'form': form, 'pengguna': pengguna})

def view_content(request, id):
    content = get_object_or_404(Content, id=id)
    return render(request, 'data_entry/content_detail.html', {'content': content})

def edit_content(request, id):
    content = get_object_or_404(Content, id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST,request.FILES, instance=content)
        if form.is_valid():
            form.save()
            return redirect('data_entry:set_content')
    else:
        form = ContentForm(instance=content)
    return render(request, 'data_entry/edit_content.html', {'form': form, 'content': content})

def delete_content(request, id):
    content = get_object_or_404(Content, id=id)
    content.delete()
    return redirect('data_entry:set_content')




