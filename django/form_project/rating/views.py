from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Rating, Review

# Create your views here.


@login_required
def review(request):
    if request.method == 'POST':
        # Handle rating submission
        rating_value = request.POST.get('rating')
        item_name = request.POST.get('item', 'General')
        review_text = request.POST.get('review', '')
        review_title = request.POST.get('title', 'Review')
        
        if rating_value:
            # Save rating using the logged-in user
            rating = Rating.objects.create(
                user=request.user,
                item=item_name,
                rating=int(rating_value),
                created_at=timezone.now()
            )
            
            # Save review if provided
            if review_text:
                Review.objects.create(
                    user=request.user,
                    skill=item_name,
                    title=review_title,
                    body=review_text,
                    created_at=timezone.now()
                )
            
            messages.success(request, 'Thank you for your rating and review!')
            return redirect('review')
    
    # Get recent ratings to display
    recent_ratings = Rating.objects.all().order_by('-created_at')[:5]
    
    return render(request, 'rating/review.html', {
        'recent_ratings': recent_ratings
    })
