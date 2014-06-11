from requests import request, HTTPError

from django.core.files.base import ContentFile


"""def save_profile_picture(strategy, user, response, details, is_new=False,
                         *args, **kwargs):
    # Save Facebook profile photo into a user profile, assuming a profile model
    # with a profile_photo file-type attribute
    if is_new and strategy.backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            profile = user.get_profile()
            profile.profile_photo.save('{0}_social.jpg'.format(user.username),
                                       ContentFile(response.content))
            profile.save()


def get_user_avatar(strategy, details, response, uid, user, *args, **kwargs):
    social = kwargs.get('social') or strategy.storage.user.get_social_auth(
        strategy.backend.name,
        uid
    )
    url = None
    if strategy.backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    if url:
        social.set_extra_data({'photo': url})

def get_friends(strategy, details, response, uid, user, *args, **kwargs):
    social = kwargs.get('social') or strategy.storage.user.get_social_auth(
        strategy.backend.name,
        uid
    )
    url = None
    if strategy.backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/friends" % response['id']

    if url:
        social.set_extra_data({'friends': url})"""