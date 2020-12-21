import click, sys, os, glob
from . import launchable
from os.path import join

@launchable.optimize.tests
def optimize_tests(client):
    # Read targets from stdin, which generally looks like //foo/bar:zot
    for pkg in sys.stdin:
        # //foo/bar:zot -> foo/bar/zot
        build = pkg.lstrip('/').replace(':', '/')
        # TODO: This test path naming "build" may need to be revisited.
        client.test_path([{ 'type': 'build', 'name': build }])

    client.run()



@click.argument('workspace', required=True)
@launchable.record.tests
def record_tests(client, workspace):
    """
    Takes Bazel workspace, then report all its test results
    """
    base = join(workspace, 'bazel-testlogs')
    if not os.path.exists(base):
        exit("No such directory: %s" % base)
    for xml in glob.iglob(join(base, '**/test.xml'), recursive=True):
        pkg = xml[len(base)+1:-8]    # extract the part that matches '**' which represents the pacakge
        client.scan(xml, pkg)  # TODO: how we do this depends on how we design this abstraction

    client.run()