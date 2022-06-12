from __future__ import print_function
import click

from csv import DictReader
from google_sheets import process_mentee_csv, process_mentor_csv

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def read_eventbrite_csv(filename):
    registrants = set()
    with open(filename) as eventbrite_csv:
        csv_dict = DictReader(eventbrite_csv)
        for parsed_object in csv_dict:
            registrants.add(parsed_object['Email'])
        

        
        registered_mentees = process_mentee_csv()
        registered_mentors = process_mentor_csv()
        confirmed_mentees = registered_mentees.intersection(registrants)
        confirmed_mentors = registered_mentors.intersection(registrants)

        missing_registrants = registrants.difference(registered_mentees, registered_mentors)
        
        click.clear()

        mentee_index = 1
        click.echo(click.style(f'{len(confirmed_mentees)} registered mentees:\n', bold=True, fg='blue'))
        for mentee in confirmed_mentees:
            click.echo(click.style(f'🏁 {mentee_index}: {mentee} has registered', fg='green'))
            mentee_index +=1 

        mentor_index = 1
        click.echo(click.style(f'\n{len(confirmed_mentors)} registered mentors: \n',fg='blue', bold=True))
        for mentor in confirmed_mentors:
            click.echo(click.style(f'🏁 {mentor_index}: {mentor} has registered', fg='green'))

        click.echo(click.style('\nNames not in mentee or mentor forms: ', fg='blue', bold=True, blink=True))
        for missing_registrant in missing_registrants:
            click.echo(click.style(f'🏁 {missing_registrant}', fg='red'))
        
        click.echo(click.style('\nMaybe their names are in the old forms?'))


        if len(confirmed_mentees) + len(confirmed_mentors) == 10:
            click.echo(click.style('All 10 registrants are confirmed', fg='green'))

        
if __name__ == '__main__':
    read_eventbrite_csv()