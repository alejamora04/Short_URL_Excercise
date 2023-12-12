from django.shortcuts import render
from .forms import OriginalURLForm, ShortURLForm
from .models import UrlHandler
from django.http import HttpResponseRedirect


# Try to set up a Single Page App styling with logic to shorten a URL.
def index(request):    

    # Accept original URL user submitted via HTTP post
    if request.method == 'POST':
        URL_Form = OriginalURLForm(request.POST)

        # Instatiate new model object if form is valid. Store original link to query new model object.
        if URL_Form.is_valid():
            # Store Original URL to Query the model and to provide it to the user.
            full_url = URL_Form.cleaned_data['original_url']
            URL_Form.save()
            # Filter stored model objects by the original full length url.
            url_object = UrlHandler.objects.filter(original_url = full_url)
            single_object = url_object[0]
            # Parse queried objects to store Short_URL and Full URL
            long_link = 'original_url'
            short_link = 'url_suffix'
            url_long_link = getattr(single_object, long_link)
            url_short_link = getattr(single_object, short_link)

            # Store links within context to pass to the templates.
            context = {
                "url_long_link": url_long_link,
                "url_short_link": url_short_link,
            }

        return render(request, 'short_url_app/index.html', context)
    # If form is invalid render empty form & refresh app.
    else:
        URL_Form = OriginalURLForm()
    
    context = {
        'URL_Form': URL_Form,
    }

    return render(request, 'short_url_app/index.html', context)


# Query full link for redirects to original URL given new url pattern.
def url_redirect(request, url_suffix):

    # Queries destination URL via the lookup of the generated shortcut.
    original_url_object = UrlHandler.objects.get(url_suffix = url_suffix)
    # Store value of http address to establish proper redirect
    full_url = original_url_object.original_url

    # Establish a redirect to desired full URL.
    return HttpResponseRedirect(full_url)


# Establish function to expand shortened URL.
def url_expand(request):
    URL_Form = ShortURLForm(request.POST)
    context = {
    'URL_Form': URL_Form,
    }

    # Accept URL Suffix as an input to retrieve the original URL object.
    if request.method == 'POST':
        URL_Form = ShortURLForm(request.POST)

        # If form is valid attempt to query URL if it exist in DB return error message if it doesn't exist or is invalid.
        if URL_Form.is_valid():
            short_url = URL_Form.cleaned_data['url_suffix']
            if UrlHandler.objects.filter(url_suffix = short_url).exists():
                url_object = UrlHandler.objects.filter(url_suffix = short_url)
                single_object = url_object[0]
                url_long_link = single_object.original_url

                # Store links within context to pass to the templates.
                context = {
                    "url_long_link": url_long_link,
                }

                return render(request, 'short_url_app/expand.html', context)
            else:
                url_long_link = "The submitted link is either invalid or does not exist!"
                URL_Form = ShortURLForm(request.POST)

                # Store links within context to pass to the templates.
                context = {
                    "url_long_link": url_long_link,
                    "URL_Form": URL_Form,
                }

                return render(request, 'short_url_app/expand.html', context)
            
        #return render(request, 'short_url_app/expand.html', context)
        return render(request, 'short_url_app/expand.html', context)
    # If form is invalid render empty form & refresh app.
    else:
        URL_Form = ShortURLForm(request.POST)
    


    return render(request, 'short_url_app/expand.html', context)
