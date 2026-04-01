import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Form, FormField, Submission


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['form_count'] = Form.objects.count()
    ctx['form_draft'] = Form.objects.filter(status='draft').count()
    ctx['form_published'] = Form.objects.filter(status='published').count()
    ctx['form_closed'] = Form.objects.filter(status='closed').count()
    ctx['formfield_count'] = FormField.objects.count()
    ctx['formfield_text'] = FormField.objects.filter(field_type='text').count()
    ctx['formfield_email'] = FormField.objects.filter(field_type='email').count()
    ctx['formfield_number'] = FormField.objects.filter(field_type='number').count()
    ctx['submission_count'] = Submission.objects.count()
    ctx['submission_new'] = Submission.objects.filter(status='new').count()
    ctx['submission_reviewed'] = Submission.objects.filter(status='reviewed').count()
    ctx['submission_archived'] = Submission.objects.filter(status='archived').count()
    ctx['recent'] = Form.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def form_list(request):
    qs = Form.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'form_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def form_create(request):
    if request.method == 'POST':
        obj = Form()
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.status = request.POST.get('status', '')
        obj.submissions = request.POST.get('submissions') or 0
        obj.created_date = request.POST.get('created_date') or None
        obj.share_url = request.POST.get('share_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/forms/')
    return render(request, 'form_form.html', {'editing': False})


@login_required
def form_edit(request, pk):
    obj = get_object_or_404(Form, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.status = request.POST.get('status', '')
        obj.submissions = request.POST.get('submissions') or 0
        obj.created_date = request.POST.get('created_date') or None
        obj.share_url = request.POST.get('share_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/forms/')
    return render(request, 'form_form.html', {'record': obj, 'editing': True})


@login_required
def form_delete(request, pk):
    obj = get_object_or_404(Form, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/forms/')


@login_required
def formfield_list(request):
    qs = FormField.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(form_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(field_type=status_filter)
    return render(request, 'formfield_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def formfield_create(request):
    if request.method == 'POST':
        obj = FormField()
        obj.form_title = request.POST.get('form_title', '')
        obj.label = request.POST.get('label', '')
        obj.field_type = request.POST.get('field_type', '')
        obj.required = request.POST.get('required') == 'on'
        obj.position = request.POST.get('position') or 0
        obj.placeholder = request.POST.get('placeholder', '')
        obj.save()
        return redirect('/formfields/')
    return render(request, 'formfield_form.html', {'editing': False})


@login_required
def formfield_edit(request, pk):
    obj = get_object_or_404(FormField, pk=pk)
    if request.method == 'POST':
        obj.form_title = request.POST.get('form_title', '')
        obj.label = request.POST.get('label', '')
        obj.field_type = request.POST.get('field_type', '')
        obj.required = request.POST.get('required') == 'on'
        obj.position = request.POST.get('position') or 0
        obj.placeholder = request.POST.get('placeholder', '')
        obj.save()
        return redirect('/formfields/')
    return render(request, 'formfield_form.html', {'record': obj, 'editing': True})


@login_required
def formfield_delete(request, pk):
    obj = get_object_or_404(FormField, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/formfields/')


@login_required
def submission_list(request):
    qs = Submission.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(form_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'submission_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def submission_create(request):
    if request.method == 'POST':
        obj = Submission()
        obj.form_title = request.POST.get('form_title', '')
        obj.respondent_email = request.POST.get('respondent_email', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.ip_address = request.POST.get('ip_address', '')
        obj.data_preview = request.POST.get('data_preview', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/submissions/')
    return render(request, 'submission_form.html', {'editing': False})


@login_required
def submission_edit(request, pk):
    obj = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        obj.form_title = request.POST.get('form_title', '')
        obj.respondent_email = request.POST.get('respondent_email', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.ip_address = request.POST.get('ip_address', '')
        obj.data_preview = request.POST.get('data_preview', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/submissions/')
    return render(request, 'submission_form.html', {'record': obj, 'editing': True})


@login_required
def submission_delete(request, pk):
    obj = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/submissions/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['form_count'] = Form.objects.count()
    data['formfield_count'] = FormField.objects.count()
    data['submission_count'] = Submission.objects.count()
    return JsonResponse(data)
