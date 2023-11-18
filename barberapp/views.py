from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from barberapp.models import Article, Service, Category, Master, Appointment
from datetime import datetime, time, timedelta

# Create your views here.


class BarberappView(View):

    def get(self, request):
        articles = Article.objects.all().only('title', 'content', 'images')
        content = {
            'title': 'BarberShop',
            'articles': articles,
        }
        return render(request, 'barberapp/index.html', context=content)


class ArticleDetailedView(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        content = {
            'title': 'post detailed',
            'article': article,
        }
        return render(request, 'barberapp/article_detailed.html', context=content)


class ServicesView(View):

    def get(self, request):
        category = Category.objects.all()
        masters = Master.objects.all()
        content = {
            'title': 'Services',
            'categorys': category,
            'masters': masters,
        }
        return render(request, 'barberapp/categories.html', context=content)


class CategoryID(View):

    def get(self, request, category_id=None):
        if category_id is not None:
            category = Category.objects.get(id=category_id)
            masters = Master.objects.filter(category=category)
        else:
            masters = Master.objects.all()
        content = {
            'title': 'Category',
            'masters': masters,
            'categorys': Category.objects.all(),
        }
        return render(request, 'barberapp/categories.html', context=content)


class LikeAddView(View):
    def get(self, request, master_id):
        master = Master.objects.get(id=master_id)
        master.rating += 1
        master.save()
        return JsonResponse({'like': master.rating})


class Services(View):

    def get(self, request, master_id):
        master = Master.objects.get(id=master_id)
        category = Category.objects.get(master=master)
        services = Service.objects.filter(category=category)
        today = datetime.now().date()

        start_time = time(10, 0)  # 10:00 AM
        end_time = time(20, 0)  # 8:00 PM

        busy_appointments = Appointment.objects.filter(
            master=master,
            date__range=(today, today + timedelta(days=6)),
            time__range=(start_time, end_time)
        )

        # Создаем словарь, где ключ - это день недели, значение - список свободных дат и времени
        available_appointments = {str(today + timedelta(days=day_offset)): [] for day_offset in range(7)}

        for day_offset in range(7):
            current_date = today + timedelta(days=day_offset)
            current_time = datetime.combine(current_date, start_time)

            while current_time.time() <= end_time:
                if not busy_appointments.filter(date=current_date, time=current_time.time()).exists():
                    available_appointments[str(current_date)].append(current_time)
                current_time += timedelta(minutes=30)
        content = {
            'title': 'Services',
            'services': services,
            'master': master,
            'available_appointments': available_appointments
        }
        return render(request, 'barberapp/services.html', context=content)


class AppointmentView(View):

    def get(self, request, master_id):
        master = Master.objects.get(id=master_id)
        services = request.GET.getlist('selected_service')
        client_name = request.GET.get('name')
        phone_number = request.GET.get('phone_number')
        comments = request.GET.get('comments')
        service = Service.objects.get(id=services[0])
        selected_datetime = request.GET.get('selected_datetime')

        if not selected_datetime:
            return HttpResponseBadRequest("Selected datetime is required.")

        date, time = selected_datetime.split(' ')

        # Проверяем, есть ли уже запись на это время
        existing_appointment = Appointment.objects.filter(master=master, date=date, time=time).first()

        if not existing_appointment:
            # Если записи на это время нет, создаем новую
            new_appointment = Appointment.objects.create(master=master, name=client_name, comments=comments,\
                                                         phone_number=phone_number, service=service, date=date, time=time)
            new_appointment.save()
            html_content = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Резервирование времени</title>
                        <style>
                            body {{
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                height: 100vh;
                                margin: 0;
                            }}

                            .reservation-info {{
                                text-align: center;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="reservation-info">
                            <h1>Время зарезервировано</h1>
                            <p>Стрижка: {new_appointment.service.service_name}</p>
                            <p>Время: { new_appointment.date } { new_appointment.time }</p>
                            <p>Мастер: { new_appointment.master.master_name }</p>
                        </div>
                    </body>
                    </html>
                """
            return HttpResponse(html_content)
        else:
            return HttpResponseBadRequest("Appointment already exists for the selected datetime.")