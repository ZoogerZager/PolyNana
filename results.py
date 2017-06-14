import os
import polynanna


class Results:
    """This class handles the I/O file operations and offers console output."""

    def __init__(self, polyanna, results_directory=os.getcwd() + '\Results'):
        self.polyanna = polyanna
        self.results_directory = results_directory
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)
        if not os.path.exists(results_directory + '\Individual_Results'):
            os.mkdir(results_directory + '\Individual_Results')

    def print_results(self):
        """Print results to the console."""
        for participant in self.polyanna.participants:
            print('{:<9} -->  {}'.format(participant.name, participant.giving_to))


    def write_full_results(self):
        """Write results to a .txt file."""
        os.chdir(self.results_directory)
        with open('full_results.txt', 'w') as f:
            for participant in self.polyanna.participants:
                f.write('{:<9} -->  {} \n'.format(participant.name, participant.giving_to))


    def write_individual_results(self):
        """Write individual results to separate files.

        Note:
            This is to keep the program's selections confidential from the
            program's operator. Participants can be instructed to open the .txt
            file with their name, it will provide their intended recipient.
        """
        os.chdir(self.results_directory + '\Individual_Results')
        for participant in self.polyanna.participants:
            filename = '{}.txt'.format(participant.name)
            with open(filename, 'w') as file:
                file.write(participant.giving_to)


def main():
    polyanna = polynanna.main()
    results = Results(polyanna)
    results.print_results()
    results.write_full_results()
    results.write_individual_results()


if __name__ == '__main__': main()
