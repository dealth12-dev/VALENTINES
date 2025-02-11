from django.views.generic import TemplateView
from .models import *


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["first_meeting"] = FirstMeeting.objects.first()
        context["memorable_dates"] = MemorableDate.objects.all()
        context["milestones"] = MilestoneAchievement.objects.all()
        context["photos"] = PhotoGallery.objects.all()
        context["love_letters"] = LoveLetter.objects.all()
        context["video_memories"] = VideoMemory.objects.all()
        context["special_messages"] = SpecialMessage.objects.all()
        return context


