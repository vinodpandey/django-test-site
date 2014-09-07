from django import template
from ..models import User
from allauth.socialaccount.models import SocialAccount
from django.conf import settings

register = template.Library()

"""
checks the use-case where a user is using alternate method to login.
e.g. he had a local account and now he is trying to login with facebook
that has the same email ID. We are suggesting him the method that he used to
login to the website and also the option that he can connect these profiles
"""
@register.inclusion_tag('user_email_validation.html', takes_context=True)
def user_email_validation(context, user_email):
    local_account = False
    provider_list = []
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExists:
        user = None
    if user is not None:
        if user.has_usable_password():
            local_account = True
        providers = SocialAccount.objects.filter(user=user)
        for provider in providers:
            if provider.provider == 'openid' and "me.yahoo.com" in provider.uid:
                provider_list.append('yahoo')
            else:
                provider_list.append(provider.provider)
    else:
        pass
    STATIC_URL = settings.STATIC_URL
    return {'local_account': local_account, 'provider_list': provider_list, 'user_email': user_email,
            'STATIC_URL': STATIC_URL}
