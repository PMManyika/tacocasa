from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import UserForm
from .models import User

from datetime import datetime
import random
from twilio.rest import Client
from .utils import get_random_gift


def find_star(request):
    context = {"form": UserForm(), "sign": "", "gift": ""}

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            birth_date = form.cleaned_data.get("birth_date")
            mobile_number = form.cleaned_data.get("mobile_number")

            # AJAX request for birth date submission
            if (
                request.headers.get("X-Requested-With") == "XMLHttpRequest"
                and birth_date
                and not mobile_number
            ):
                user = User(birth_date=birth_date)
                star_sign = user.get_zodiac_sign()
                return JsonResponse({"success": True, "star_sign": star_sign})

            # Normal POST request handling for mobile number submission
            if mobile_number:
                sign = request.session.get("sign", "")
                gift = request.session.get("gift", "")
                if sign and gift:
                    birth_date_str = request.session.get("birth_date")
                    if birth_date_str:
                        birth_date = datetime.strptime(
                            birth_date_str, "%Y-%m-%d"
                        ).date()
                        User.objects.create(
                            birth_date=birth_date, mobile_number=mobile_number
                        )
                        # Clear the session data
                        del request.session["birth_date"]
                        del request.session["sign"]
                        del request.session["gift"]
                        # Redirect to a success page
                        return redirect("find_starsign_success", sign=sign, gift=gift)
                    else:
                        context["error"] = "Birth date missing. Please start again."
                        return render(request, "starsign/starsign.html", context)
                else:
                    context["error"] = "Sign or gift missing. Please start again."
                    return render(request, "starsign/starsign.html", context)

            # If only birth date is submitted, save the data and update the context
            elif birth_date and not mobile_number:
                user = User(birth_date=birth_date)
                context["sign"] = user.get_zodiac_sign()
                context["gift"] = get_random_gift()
                request.session["sign"] = context["sign"]
                request.session["gift"] = context["gift"]
                request.session["birth_date"] = birth_date.strftime("%Y-%m-%d")

        # If the form is not valid or it's a GET request
        return render(request, "starsign/starsign.html", context)


def find_starsign_success(request, sign, gift):
    return render(request, "starsign/success.html", {"sign": sign, "gift": gift})


def clear_session_and_redirect(request):
    # Clear the relevant session data
    request.session.pop("sign", None)
    request.session.pop("gift", None)
    request.session.pop("birth_date", None)

    # Redirect to the find_starsign view
    return redirect("find_star")
