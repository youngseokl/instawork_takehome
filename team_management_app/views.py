from django.shortcuts import render
from .models import Member
from .forms import MemberForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def index(request):
    """This page lists all members who have been added (not including the deleted ones)."""
    members = Member.objects.all()

    context = {
        'num_members': members.count(),
        'members': members
    }

    return render(request, 'index.html', context=context)

def AddMember(request):
    """This page displays a form to add a member."""

    # Process form data
    if request.method == 'POST':
        form = MemberForm(request.POST)

        # Populating form data
        member = Member(
            first_name=form.data['first_name'], 
            last_name=form.data['last_name'], 
            phone_number=form.data['phone_number'], 
            email=form.data['email'], 
            status=form.data['status']
        )
        
        member.save()

        # Redirect to home page
        return HttpResponseRedirect('/')

    # Loads empty form
    else:
        form = MemberForm()

    context = {
        'form': form
    }

    return render(request, 'add_member_form.html', context)

def EditMember(request, pk):
    """This page displays a form to edit an existing member."""
    member = get_object_or_404(Member, pk=pk)

    # Process form data
    if request.method == 'POST':
        form = MemberForm(request.POST)

        # Update fields of existing resource
        member.first_name = form.data['first_name']
        member.last_name = form.data['last_name']
        member.phone_number = form.data['phone_number']
        member.email = form.data['email']
        member.status = form.data['status']

        member.save()

        # Redirect to home page
        return HttpResponseRedirect('/')

    # Loads a form with prefilled data
    else:
        form = MemberForm(initial={
            'first_name': member.first_name,
            'last_name': member.last_name,
            'phone_number': member.phone_number,
            'email': member.email,
            'status': member.status
            }
        )

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'edit_member_form.html', context)

def DeleteMember(request, pk):
    """Method to delete an existing resource"""

    member = get_object_or_404(Member, pk=pk)

    member.delete()

    return HttpResponseRedirect('/')