import click, os, i18n, locale

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')
translations_folder = os.path.join(os.path.dirname(__file__), 'translations')

try:
    twodloc = locale.getlocale()[0].split("_")[0]
except IndexError:
    twodloc = "en"

i18n.set('locale', twodloc)
i18n.set('fallback', 'en')

i18n.load_path.append(translations_folder)


class KoterCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


cli = KoterCLI(help=i18n.t('koter.main.help'))

if __name__ == '__main__':
    cli()
