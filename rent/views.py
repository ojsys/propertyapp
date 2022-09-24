from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rent.models import Rent, PropertyInfo, Income, Expenses, Owner
from .forms import RentForm, PropertyInfoForm, IncomeForm, ExpenseForm
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage


# View for displaying backent
@login_required(login_url='login')
def backend(request):
    owners = Owner.objects.all()
    for owner in owners:
        get_owner = owner.id
    rents_filter = Rent.objects.all().filter(owner=get_owner)
    current_user = request.user
    name = current_user.first_name
    user_email = current_user.email
    rents = Rent.objects.all().order_by('-id')[:10]
    data = Income.objects.all().order_by('-id')[:10]
    data2 = Expenses.objects.all().order_by('-id')[:10]
    revenue = Income.objects.all().aggregate(totalrev=Sum('payment_amount'))
    
    context = {
        'name': name, 
        'rents': rents, 
        'data': data, 'data2': data2, 
        'revenue': revenue,
        'user_email': user_email,
        'owners': owners,
        'rents_filter': rents_filter,
        }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def rent_roll(request):
    owners = Owner.objects.all()
    for owner in owners:
        get_owner = owner.id
    rents_filter = Rent.objects.all().filter(owner=get_owner)
    return render(request, 'rent_roll.html', {
        'form': RentForm,
        'rents': Rent.objects.all(),
        'owners': owners,
        'rents_filter': rents_filter,
        })


# Function to render the add_rent page
@login_required(login_url="login")
def add_rent(request):
    if request.method == "POST":

        form = RentForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
                # Check if form is valid
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            property_type = form.cleaned_data["property_type"]
            location = form.cleaned_data["location"]
            rent_rate = form.cleaned_data["rent_rate"]
            due_date = form.cleaned_data["due_date"]
            gender = form.cleaned_data["gender"]
            owner = form.cleaned_data["owner"]
            files = form.cleaned_data["files"]

            # New Rent Record
            new_rent = Rent(
                name=name,
                phone=phone,
                email=email,
                property_type=property_type,
                location=location,
                rent_rate=rent_rate,
                due_date=due_date,
                gender=gender,
                owner=owner,
                files=files,
            )
            new_rent.save()
            return render(request, 'add_rent.html', {
                'form':RentForm(),
                 'success':True,
                 
                 })

    else:
        form = RentForm()
    return render(request, 'add_rent.html', {'form': form})


@login_required(login_url='login')
def detail_rent(request, rent_id):
    rent_data = Rent.objects.all()
    rent_detail = get_object_or_404(Rent, pk=rent_id)
    return render(request, 'detail_rent.html', {'rent_detail':rent_detail, 'rent_data':rent_data})

# Function to Edit Rent form
@login_required(login_url='login')
def update_rent(request, rent_id):
    rent_unit = get_object_or_404(Rent, pk=rent_id)
    rent_form = RentForm(request.POST or None, instance=rent_unit)
    if rent_form.is_valid():
        rent_form.save()
        return redirect('backend')
    return render(request, 'update_detail.html', {'form': rent_form}) 

# Function to Delete rent
@login_required(login_url='login')
def delete_rent(request, rent_id):
    rent_id = int(rent_id)
    try:
        rent_unit = Rent.objects.get(id=rent_id)
    except Rent.DoesNotExist:
        return redirect('backend')
    rent_unit.delete()
    return redirect('backend')



@login_required(login_url='login')
def property_info_roll(request):
    owners = Owner.objects.all()
    for owner in owners:
        get_owner = owner.id
    rents_filter = Rent.objects.all().filter(owner=get_owner)
    return render(request, 'property_info_roll.html', {
        'form': PropertyInfoForm,
        'property_info': PropertyInfo.objects.all(),
        'owners': owners,
        'rents_filter': rents_filter,
        })


@login_required(login_url="login")
def property_info(request):
    if request.method == "POST":
        form = PropertyInfoForm(request.POST, request.FILES)
        
        # Check if form is valid
        if form.is_valid():
            property_name = form.cleaned_data["property_name"]
            property_type = form.cleaned_data["property_type"]
            property_location = form.cleaned_data["property_location"]
            property_description = form.cleaned_data["property_description"]
            property_owner = form.cleaned_data["property_owner"]
            property_images = form.cleaned_data["property_images"]

            # New Rent Record
            new_property = PropertyInfo(
                property_name=property_name,
                property_type=property_type,
                property_location = property_location,
                property_description=property_description,
                property_owner=property_owner,
                property_images=property_images,
            )
            new_property.save()
            return render(request, 'property_info.html', {'form':PropertyInfoForm(), 'success':True})

    else:
        form = PropertyInfoForm()
    return render(request, 'property_info.html', {'form': form})


@login_required(login_url='login')
def financials(request):
    owners = Owner.objects.all()
    for owner in owners:
        get_owner = owner.id
    rents_filter = Rent.objects.all().filter(owner=get_owner)
    return render(request, 'financials.html', {
        'form': IncomeForm,
        'form2': ExpenseForm,
        'incomes': Income.objects.all(),
        'expenses': Expenses.objects.all(),
        'owners': owners,
        'rents_filter': rents_filter,
        })


@login_required(login_url='login')
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            payment_date = form.cleaned_data["payment_date"]
            tenant = form.cleaned_data["tenant"]
            payment_desc = form.cleaned_data["payment_desc"]
            payment_amount = form.cleaned_data["payment_amount"]
            

            new_income = Income(
                payment_date=payment_date,
                tenant=tenant,
                payment_desc=payment_desc,
                payment_amount=payment_amount,

            )
            new_income.save()
            return render(request, 'add_income.html', {'form': IncomeForm(), 'success': True})
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})


@login_required(login_url='login')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            payment_date = form.cleaned_data['payment_date']
            payment_method = form.cleaned_data["payment_method"]
            paid_to = form.cleaned_data["paid_to"]
            payment_desc = form.cleaned_data["payment_desc"]
            payment_amount = form.cleaned_data["payment_amount"]

            new_expense = Expenses(
                payment_date=payment_date,
                payment_method=payment_method,
                paid_to=paid_to,
                payment_desc=payment_desc,
                payment_amount=payment_amount,
                
            )
            new_expense.save()
            return render(request, 'add_expense.html', {'form2': ExpenseForm(), 'success': True})
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'expense': form})

# Function to Update Income Details
@login_required(login_url='login')
def update_income(request, income_id):
    income_unit = get_object_or_404(Income, pk=income_id)
    income_form = IncomeForm(request.POST or None, instance=income_unit)
    if income_form.is_valid():
        income_form.save()
        return redirect('backend')
    return render(request, 'update_income.html', {'form': income_form})

# Function to Delete an income detail
@login_required(login_url='login')
def delete_income(request, income_id):
    income_id = int(income_id)
    try:
        income_unit = Income.objects.get(id=income_id)
    except Income.DoesNotExist:
        return redirect('backend')
    income_unit.delete()
    return redirect('backend')


# Function to Update Expense Details
@login_required(login_url='login')
def update_expense(request, expense_id):
    expense_unit = get_object_or_404(Expenses, pk=expense_id)
    expense_form = ExpenseForm(request.POST or None, instance=expense_unit)
    if expense_form.is_valid():
        expense_form.save()
        return redirect('backend')
    return render(request, 'update_expense.html', {'form': expense_form})

# Function to Delete an Expense detail
@login_required(login_url='login')
def delete_expense(request, expense_id):
    expense_id = int(expense_id)
    try:
        expense_unit = Expenses.objects.get(id=expense_id)
    except Expenses.DoesNotExist:
        return redirect('backend')
    expense_unit.delete()
    return redirect('backend')

# Function for filtering by ownership of property
def owner_view(request, owner_id):
    get_owner = get_object_or_404(Owner, pk=owner_id)
    owners = Owner.objects.all()
    rents = Rent.objects.all().filter(owner=(get_owner.id))
    
    return render(request, 'owner.html', {'owners':owners, 'get_owner':get_owner, 'rents':rents})

