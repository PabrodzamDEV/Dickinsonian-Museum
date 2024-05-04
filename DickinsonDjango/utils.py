def get_user_avatar(user):
    if hasattr(user, 'profile') and user.profile.avatar:
        return user.profile.avatar.url
    return None
