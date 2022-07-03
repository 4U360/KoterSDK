import click, yaml, i18n, socket, pathlib, platform, json, logging, uuid, re, psutil, speedtest, git
from installer import KoterCLI
from koter import Koter
from git import RemoteProgress

def getSystemInfo():
    try:
        wifi = speedtest.Speedtest()
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        lat_lon = wifi.lat_lon
        info["network"] = {
            "download": wifi.download(),
            "upload": wifi.upload(),
            "lat": lat_lon[0],
            "lon": lat_lon[1]
        }

        return info
    except Exception as e:
        logging.exception(e)



class ProgressPrinter(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

DEFAULT_SETUP = {
    "can_share": False
}

@click.command()
@click.option('--server', default="koter.4u360.dev.br", help=i18n.t('koter.setup.option.server.help'))
@click.option('--client_certificate', default=None, help=i18n.t('koter.setup.option.client_certificate.help'))
@click.option('--client_secret_key', default=None, help=i18n.t('koter.setup.option.client_secret_key.help'))
@click.version_option(version="1.0.0")
def cli(server, client_certificate: click.Path, client_secret_key: click.Path):
    setup_file = pathlib.Path("koter_setup.yaml")
    setup_file.touch(exist_ok=True)

    with open(setup_file) as handler:
        data = yaml.full_load(handler)
        koter_setup = DEFAULT_SETUP

        if data:
            koter_setup.update(data)

    with open(setup_file, "w+") as handler:
        koter_setup["server"] = server
        koter_setup["integration_id"] = click.prompt(i18n.t('koter.setup.prompt.unique_integration_id'))
        koter_setup["secret_key"] = click.prompt(i18n.t('koter.setup.prompt.secret_key'))
        koter_setup["audience"] = "koter.com.br"
        koter_setup["issuer"] = click.prompt(i18n.t('koter.setup.prompt.issuer'))
        koter_setup["algorithm"] = click.prompt(i18n.t('koter.setup.prompt.algorithm'),
                                                type=click.Choice([str(alg) for alg in Koter.algorithms]),
                                                show_default=True, default=Koter.default_algorithm)

        koter_setup["can_share"] = click.confirm(i18n.t('koter.setup.confirm.share_info'))

        if koter_setup["can_share"]:
            click.echo(click.style(i18n.t('koter.setup.messages.collecting_machine_data'), bold=True, fg="yellow"))
            koter_setup["shared"] = getSystemInfo()
        else:
            koter_setup["shared"] = {}

        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = click.prompt(i18n.t('koter.setup.prompt.server_port'), type=int, default=8000)
        result_of_check = a_socket.connect_ex(("127.0.0.1", port))

        if result_of_check == 0:
            click.echo(click.style(i18n.t('koter.setup.messages.open_port') % port, bold=True, fg="green"))
        else:
            click.echo(click.style(i18n.t('koter.setup.messages.closed_port') % port, bold=True, fg="yellow"))

        koter_setup["port"] = port

        yaml.dump(koter_setup, handler)
        koter = Koter(server=server, setup=koter_setup, client_certificate=client_certificate, client_secret_key=client_secret_key)
        koter.report()
        click.echo(click.style(i18n.t('koter.setup.messages.downloading_sdk'), bold=True, fg="yellow"))
        Koter.download_sdk()