import click

@click.command()
@click.option('--password', prompt='Password', confirmation_prompt=True,
   hide_input=True, help='New Password.')

def getUserPass(password):
    """Simple program to get the new password."""
    click.echo('Password => %s' % password)

if __name__ == '__main__':
    getUserPass()
