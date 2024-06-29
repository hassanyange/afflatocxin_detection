from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Crop, CustomUser, Test
from django.views.decorators.csrf import csrf_exempt
from .forms import CropForm, TestForm

# Home view
def admin_home(request):
    all_crop_count = Crop.objects.all().count()
    all_test_count = Test.objects.all().count()

    context = {
        "all_crop_count": all_crop_count,
        "all_test_count": all_test_count,
    }
    return render(request, "hod_template/home_content.html", context)

# Manage crops view
def manage_crops(request):
    crops = Crop.objects.all()
    context = {
        "crops": crops
    }
    return render(request, 'hod_template/manage_crops_template.html', context)

# Add crop view
def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Crop Added Successfully!")
            return redirect('manage_crops')
        else:
            messages.error(request, "Failed to Add Crop. Please ensure the form is valid.")
    else:
        form = CropForm()
    context = {
        'form': form
    }
    return render(request, 'hod_template/add_crop_template.html', context)

# Edit crop view
def edit_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            messages.success(request, "Crop Updated Successfully!")
            return redirect('manage_crops')
        else:
            messages.error(request, "Failed to Update Crop. Please ensure the form is valid.")
    else:
        form = CropForm(instance=crop)
    context = {
        'form': form,
        'id': crop_id
    }
    return render(request, 'hod_template/edit_crop_template.html', context)

# Delete crop view
def delete_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    try:
        crop.delete()
        messages.success(request, "Crop Deleted Successfully!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Crop: {e}")
    return redirect('manage_crops')


# Manage tests view
def manage_tests(request):
    tests = Test.objects.all()
    context = {
        "tests": tests
    }
    return render(request, 'hod_template/manage_tests_template.html', context)

# Add test view
def add_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Test Added Successfully!")
            return redirect('manage_tests')
        else:
            messages.error(request, "Failed to Add Test. Please ensure the form is valid.")
    else:
        form = TestForm()
    context = {
        'form': form
    }
    return render(request, 'hod_template/add_test_template.html', context)

# Edit test view
def edit_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES, instance=test)
        if form.is_valid():
            form.save()
            messages.success(request, "Test Updated Successfully!")
            return redirect('manage_tests')
        else:
            messages.error(request, "Failed to Update Test. Please ensure the form is valid.")
    else:
        form = TestForm(instance=test)
    context = {
        'form': form,
        'id': test_id
    }
    return render(request, 'hod_template/edit_test_template.html', context)

# Delete test view
def delete_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    try:
        test.delete()
        messages.success(request, "Test Deleted Successfully!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Test: {e}")
    return redirect('manage_tests')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
