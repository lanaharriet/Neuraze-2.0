from .models import LearningInsight


def track_learning(user, feature):
    insight = LearningInsight.objects.get(user=user)

    insight.total_actions += 1

    if feature == "library":
        insight.library_uses += 1
    elif feature == "mindgarden":
        insight.mindgarden_uses += 1
    elif feature == "whisper":
        insight.whisper_uses += 1
    elif feature == "crystal":
        insight.crystal_uses += 1
    elif feature == "community":
        insight.community_uses += 1

    insight.save()
