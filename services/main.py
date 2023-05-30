from .models import Services
from django.db.models import Q
from account.models import User
from account.models import UserSkills
from services.models import JobSkills

def recommend(request):
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity

    # Retrieve the user's skill set as a list of skill names
    user=request.user
    user_skills = UserSkills.objects.filter(user=user)
    user_skill_names = list(JobSkills.objects.filter(user_skill__in=user_skills).values_list('name', flat=True).distinct())
    # Retrieve all Services that require at least one skill from the user's skill set
    matching_Services = Services.objects.filter(skills__name__in=user_skill_names)

    # Create a matrix where each row represents a Service and each column represents a skill
    Service_skill_matrix = np.zeros((matching_Services.count(), len(user_skill_names)), dtype=np.float32)

    # Fill in the matrix with the Service's proficiency in each skill
    for i, Service in enumerate(matching_Services):
        Service_skill_names = Service.skills.filter(name__in=user_skill_names).values_list('name', flat=True)
        for j, skill_name in enumerate(user_skill_names):
            if skill_name in Service_skill_names:
                Service_skill_matrix[i,j] = 1.0

    # Create a vector representing the user's proficiency in each skill
    user_skill_vector = np.array([1.0 if skill_name in user_skill_names else 0.0 for skill_name in user_skill_names], dtype=np.float32)
    if user_skill_vector.all():
        # Calculate the cosine similarity between the Service skill matrix and the user skill vector
        similarity_scores = cosine_similarity(Service_skill_matrix, user_skill_vector.reshape(1, -1))
        # Sort the Services by similarity score in descending order to obtain a list of recommended Services
        recommended_Services = [matching_Services[i] for i in np.argsort(similarity_scores.ravel()).tolist()[::-1]]
        # return distinct recommended Services

        if recommended_Services:
            return list(set(recommended_Services))
        else:
            return None
    