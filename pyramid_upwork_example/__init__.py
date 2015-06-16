from pyramid.config import Configurator


def get_acl_group(user_uid, request):
    """ACL logic goes here.

    This function should return a list even of one memeber
    of the groups that should be assigned to given ``user_uid``.

    Return none if no grups should be assigned to this ``user_uid``.

    """
    return ('view',)


def main(global_config, **settings):
    """Main app configuration binding."""

    config = Configurator(
        settings=settings,
        root_factory="pyramid_upwork_example.models.RootFactory")

    # ACL authorization callback for pyramid-upwork
    config.registry.get_acl_group = get_acl_group

    # External includes
    config.include('pyramid_upwork')

    # Views and routing
    config.add_view('pyramid_upwork_example.views.MainPage',
                    renderer='templates/main.jinja2',
                    permission='view')

    return config.make_wsgi_app()
