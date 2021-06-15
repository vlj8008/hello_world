from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.

def admin_console(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    form = UserProfileForm(data=request.POST or None, instance=item)
    # POST is request to the dB that server accepts data in form. This is when user
    # changes the fields in the product.
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            # save new details to dB
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item, }
    return render(request, "profiles/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = UserProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def createRecord(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        # ProductForm() creates empty version of form.
        form = UserProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/createRecord.html', context)
