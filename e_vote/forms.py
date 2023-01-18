from django.forms import ModelForm, DateInput

from e_vote.models import Position, Candidate, Voter, Vote


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class CandidateForm(ModelForm):

    class Meta:
        model = Candidate
        fields = '__all__'


class VoterForm(ModelForm):
    class Meta:
        model = Voter
        fields = ("reg_no", "name", "gender", "birth_date")

    widgets = {
        "birth_date": DateInput(attrs={"type": "date"})
    }


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
