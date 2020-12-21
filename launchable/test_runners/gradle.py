import click, os
from . import launchable

@click.argument('source_roots', required=True, nargs=-1)
@launchable.optimize.tests
def optimize_tests(client, source_roots):
    def file2test(f:str):
        if f.endswith('.java') or f.endswith('.scala') or f.endswith('.kt'):
            f = f[:f.rindex('.')]   # remove extension
            f = f.replace(os.path.sep,'.')  # directory -> package name conversion
            return f
        else:
            return None

    for root in source_roots:
        client.scan(root, '**/*', file2test)

    client.run()



@click.argument('source_roots', required=True, nargs=-1)
@launchable.record.tests
def record_tests(client, source_roots):
    for root in source_roots:
        client.scan(root, "*.xml")
    client.run()