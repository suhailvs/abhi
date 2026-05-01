from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import InsuranceBrokingEntry
from .forms import InsuranceBrokingEntryForm

@login_required
def home(request):
    if request.user.is_staff:
        return redirect('admin:index')
    return render(request, 'home.html')
@login_required
def entry_create(request):
    """Create a new insurance broking entry."""
    if request.method == 'POST':
        form = InsuranceBrokingEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            messages.success(request, f"Entry saved successfully! Policy No: {entry.policy_no}")
            return redirect('insurance:entry_detail', pk=entry.pk)
    else:
        form = InsuranceBrokingEntryForm()

    return render(request, 'insurance/entry_form.html', {
        'form': form,
        'title': 'New Insurance Broking Entry',
        'action': 'Create',
    })

@login_required
def entry_detail(request, pk):
    """Display full details of a single entry (mirrors the screen layout)."""
    entry = get_object_or_404(InsuranceBrokingEntry, pk=pk)
    return render(request, 'insurance/entry_detail.html', {
        'entry': entry,
        'title': f'Policy: {entry.policy_no}',
    })

@login_required
def entry_list(request):
    """List all entries with search/filter."""
    qs = InsuranceBrokingEntry.objects.all()

    # Simple search
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(
            policy_no__icontains=q
        ) | qs.filter(
            life_assured__icontains=q
        ) | qs.filter(
            ack_no__icontains=q
        ) | qs.filter(
            dep_name__icontains=q
        )

    paginator = Paginator(qs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'insurance/entry_list.html', {
        'page_obj': page_obj,
        'q': q,
        'title': 'Insurance Broking — Entry Search',
    })

@login_required
def entry_edit(request, pk):
    """Edit an existing entry."""
    entry = get_object_or_404(InsuranceBrokingEntry, pk=pk)
    if request.method == 'POST':
        form = InsuranceBrokingEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Entry updated successfully.")
            return redirect('insurance:entry_detail', pk=entry.pk)
    else:
        form = InsuranceBrokingEntryForm(instance=entry)

    return render(request, 'insurance/entry_form.html', {
        'form': form,
        'entry': entry,
        'title': f'Edit Entry — {entry.policy_no}',
        'action': 'Update',
    })

@login_required
def entry_delete(request, pk):
    """Delete an entry (POST only)."""
    entry = get_object_or_404(InsuranceBrokingEntry, pk=pk)
    if request.method == 'POST':
        policy_no = entry.policy_no
        entry.delete()
        messages.success(request, f"Entry {policy_no} deleted.")
        return redirect('insurance:entry_list')
    return render(request, 'insurance/entry_confirm_delete.html', {'entry': entry})