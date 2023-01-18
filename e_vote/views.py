from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib import messages

from e_vote.forms import PositionForm, CandidateForm, VoterForm, VoteForm
from e_vote.models import Position, Candidate, Voter, Vote

from e_vote.utils import render_to_pdf


@login_required
def index_view(request):
    return render(request, 'index.html')


@login_required
def home_view(request):
    return render(request, 'home.html')


@login_required
def position_view(request):
    message = ''

    if request.method == "POST":
        position_form = PositionForm(request.POST)

        if position_form.is_valid():
            position_form.save()

            message = "postion added successfully"

            messages.success(request, message)
    else:
        position_form = PositionForm()

    positions = Position.objects.all()

    context = {
        'form': position_form,
        'message': message,
        'positions': positions
    }
    return render(request, "add_position.html", context)


@login_required
def edit_position_view(request, position_id):

    position = Position.objects.get(id=position_id)
    message = ''

    if request.method == "POST":

        position_form = PositionForm(request.POST, instance=position)

        if position_form.is_valid():
            position_form.save()
            message = "Changes made successfully"

        else:
            message = "Form is invalid"

        messages.success(request, message)
    else:
        position_form = PositionForm(instance=position)

    context = {
        'form': position_form,
        'position': position,
        'message': message
    }
    return render(request, 'edit_position.html', context)


@login_required
def delete_position_view(request, position_id):
    position = Position.objects.get(id=position_id)

    position.delete()

    messages.success(request, "Position deleted")

    return redirect(position_view)


@login_required
def candidate_view(request):
    message = ''

    if request.method == "POST":
        candidate_form = CandidateForm(request.POST)

        if candidate_form.is_valid():
            candidate_form.save()

            message = "candidate added successfully"
    else:
        candidate_form = CandidateForm()

    candidate = Candidate.objects.all()

    context = {
        'form': candidate_form,
        'message': message,
        'candidate': candidate
    }
    return render(request, "add_candidate.html", context)


def candidate_pdf_view(request):
    candidates = Candidate.objects.all()

    context = {
        "candidates": candidates,
    }

    pdf = render_to_pdf("candidate_pdf.html", context)

    return HttpResponse(pdf, content_type="application/pdf")


@login_required
def add_candidate_view(request):
    message = ''
    if request.method == "POST":
        candidate_form = CandidateForm(request.POST)

        if candidate_form.is_valid():
            candidate_form.save()

            message = 'Candidate added successfully'

    candidate_form = CandidateForm()

    candidates = Candidate.objects.all

    context = {
        'form': candidate_form,
        'message': message,
        'candidates': candidates

    }

    return render(request, "add_candidate.html", context)


@login_required
def edit_candidate_view(request, candidate_id):

    candidate = Candidate.objects.get(id=candidate_id)
    message = ''

    if request.method == "POST":

        candidate_form = CandidateForm(request.POST, instance=candidate)

        if candidate_form.is_valid():
            candidate_form.save()
            message = "Changes made successfully"

        else:
            message = "Form is invalid"

    else:
        candidate_form = CandidateForm(instance=candidate)

    context = {
        'form': candidate_form,
        'candidate': candidate,
        'message': message
    }
    return render(request, 'edit_candidate.html', context)


@login_required
def delete_candidate_view(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)

    candidate.delete()

    return redirect(candidate_view)


@login_required
def voter_view(request):
    message = ''

    if request.method == "POST":
        voter_form = VoterForm(request.POST)

        if voter_form.is_valid():
            voter_form.save()

            message = "voter added successfully"
    else:
        voter_form = VoterForm()

    voter = Voter.objects.all()

    context = {
        'form': voter_form,
        'message': message,
        'voter': voter
    }
    return render(request, "add_voter.html", context)


@login_required
def add_voter_view(request):
    message = ''
    if request.method == "POST":
        voter_form = VoterForm(request.POST)

        if voter_form.is_valid():
            voter_form.save()

            message = 'voter added successfully'

    else:
        voter_form = VoterForm()

    votes = Voter.objects.all

    context = {
        'form': voter_form,
        'message': message,
        'votes': votes

    }

    return render(request, "add_voter.html", context)


@login_required
def edit_voter_view(request, voter_id):

    voter = Voter.objects.get(id=voter_id)
    message = ''

    if request.method == "POST":

        voter_form = VoterForm(request.POST, instance=voter)

        if voter_form.is_valid():
            voter_form.save()
            message = "Changes made successfully"

        else:
            message = "Form is invalid"

    else:
        voter_form = VoterForm(instance=voter)

    context = {
        'form': voter_form,
        'voter': voter,
        'message': message
    }
    return render(request, 'edit_voter.html', context)


@login_required
def delete_voter_view(request, voter_id):
    voter = Voter.objects.get(id=voter_id)

    voter.delete()

    return redirect(voter_view)


@login_required
def vote_view(request):
    message = ''

    if request.method == "POST":
        vote_form = VoteForm(request.POST)

        if vote_form.is_valid():
            vote_form.save()

            message = "voter added successfully"
    else:
        vote_form = VoteForm()

    vote = Vote.objects.all()

    context = {
        'form': vote_form,
        'message': message,
        'vote': vote
    }
    return render(request, "add_vote.html", context)


@login_required
def add_vote_view(request):
    message = ''
    if request.method == "POST":
        vote_form = VoteForm(request.POST)

        if vote_form.is_valid():
            vote_form.save()

            message = 'vote added successfully'

    else:
        vote_form = VoteForm()

    votes = Vote.objects.all

    context = {
        'form': vote_form,
        'message': message,
        'votes': votes

    }

    return render(request, "add_vote.html", context)


@login_required
def edit_vote_view(request, vote_id):

    vote = Vote.objects.get(id=vote_id)
    message = ''

    if request.method == "POST":

        vote_form = VoteForm(request.POST, instance=vote)

        if vote_form.is_valid():
            vote_form.save()
            message = "Changes made successfully"

        else:
            message = "Form is invalid"

    else:
        vote_form = VoteForm(instance=vote)

    context = {
        'form': vote_form,
        'voter': vote,
        'message': message
    }
    return render(request, 'edit_vote.html', context)


@login_required
def delete_vote_view(request, vote_id):
    vote = Vote.objects.get(id=vote_id)

    vote.delete()

    return redirect(vote_view)


def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()

            message = 'user created successfully'
        else:
            message = 'something went wrong'

    else:
        sign_up_form = UserCreationForm()

    context = {
        'form': sign_up_form
    }

    return render(request, 'registration/sign_up.html', context)
