import click

@click.command()
@click.option('--username', prompt='Login', help='Your username.')
@click.option('--password', prompt='Password', 
   hide_input=True, help='Your password.')

def getUserPass(username, password):
    """Simple program to get Username and Password."""
    click.echo('Username => %s' % username)
    click.echo('Password => %s' % password)

if __name__ == '__main__':
    getUserPass()
