
__author__ = 'wuxian'


class Redprint:
    def __init__(self, name):
        self.name = name
        self.mount = []

    def route(self, rule, **options):
        def decorator(f):
            self.mount.append((f, rule, options))
            return f
        return decorator

    def register(self, blue_print, url_prefix=None):
        for (f, rule, options) in self.mount:
            if url_prefix is None:
                url_prefix = self.name
            endpoint = options.pop("endpoint", f.__name__)
            blue_print.add_url_rule('/' + url_prefix + rule, endpoint, f, **options)
