from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """ Add a review to a product """

    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product        
        review.title = request.POST["title"]
        review.description = request.POST["description"]
        review.rating = request.POST["rating"]

        if 'would_recommend' in request.POST:
            review.would_recommend = True
        else:
            review.would_recommend = False

        review.save()
        messages.success(request, 'Successfully added review!')
        
        return redirect(reverse('product_detail', args=[product.id]))

    else:
        messages.error(
            request,
            'Failed to add review. Please ensure the form is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


@login_required
def edit_review(request, review_id):
    """ Allows users to edit their review """

    review = get_object_or_404(Review, pk=review_id)
    review_form = ReviewForm(request.POST, request.FILES, instance=review)

    if review_form.is_valid():
        review.save()

        messages.success(request, 'Your review has been successfully edited')
    else:
        messages.error(
            request,
            'Failed to edit review. Please ensure the form is valid.')

    return redirect(reverse('product_detail', args=(review.product.id,)))
