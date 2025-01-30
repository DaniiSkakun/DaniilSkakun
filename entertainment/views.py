
from django.shortcuts import render, get_object_or_404, redirect
from .models import EntertainmentCenter, Event
from .forms import EntertainmentCenterForm, CenterTypeForm, EventForm
from django.contrib import messages




def center_add(request):
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  
    else:
        form = EntertainmentCenterForm() 
    return render(request, 'entertainment/center_form.html', {'form': form})



def center_edit(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk) 
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST, instance=center)  
        if form.is_valid():
            form.save()  # Збереження змін
            return redirect('center_detail', pk=center.pk)  
    else:
        form = EntertainmentCenterForm(instance=center)  
    return render(request, 'entertainment/center_form.html', {'form': form})



def center_delete(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  
    if request.method == "POST": 
        center.delete()
        return redirect('center_list')  
    return render(request, 'entertainment/center_confirm_delete.html', {'center': center})



def center_list(request):
    centers = EntertainmentCenter.objects.all()  
    return render(request, 'entertainment/center_list.html', {'centers': centers})


def center_detail(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  
    return render(request, 'entertainment/center_detail.html', {'center': center})



def center_type_add(request):
    if request.method == "POST":
        form = CenterTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  
    else:
        form = CenterTypeForm()
    return render(request, 'entertainment/center_type_form.html', {'form': form})




# Список подій
def event_list(request):
    events = Event.objects.all()  # Отримання всіх подій
    return render(request, 'entertainment/event_list.html', {'events': events})


# Створення нової події
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Перенаправлення на сторінку зі списком подій
    else:
        form = EventForm()
    return render(request, 'entertainment/add_event.html', {'form': form})


# Перегляд деталей події
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Отримання події за первинним ключем
    return render(request, 'entertainment/event_detail.html', {'event': event})


# Видалення події
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Отримання події за первинним ключем
    if request.method == 'POST':  # Обробка підтвердження видалення
        event.delete()
        messages.success(request, 'Подію успішно видалено.')
        return redirect('event_list')  # Перенаправлення на список подій
    return render(request, 'entertainment/event_confirm_delete.html', {'event': event})
