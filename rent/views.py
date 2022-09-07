from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rent.models import Rent, PropertyInfo, Income, Expenses
from .forms import RentForm, PropertyInfoForm, IncomeForm, ExpenseForm
from django.db.models import Sum

# View for displaying backent
@login_required(login_url='login')
def backend(request):
    
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
        }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def rent_roll(request):
    return render(request, 'rent_roll.html', {
        'form': RentForm,
        'rents': Rent.objects.all()
        })


# Function to render the add_rent page
@login_required(login_url="login")
def add_rent(request):
    if request.method == "POST":
        form = RentForm(request.POST)
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
            )
            new_rent.save()
            return render(request, 'add_rent.html', {'form':RentForm(), 'success':True})

    else:
        form = RentForm()
    return render(request, 'add_rent.html', {'form': form})


@login_required(login_url='login')
def property_info_roll(request):
    return render(request, 'property_info_roll.html', {
        'form': PropertyInfoForm,
        'property_info': PropertyInfo.objects.all()
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
    return render(request, 'financials.html', {
        'form': IncomeForm,
        'form2': ExpenseForm,
        'incomes': Income.objects.all(),
        'expenses': Expenses.objects.all(),
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



def builder(request):
    return redirect(request, 'www.clyentel.com')
