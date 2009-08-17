"""
Convo: IRC Conversation tracking

Enables extraction of conversations in possibly messy IRC environment
Methodology:
1) Direct Addressing: "<username>:" to form an conversation between two
   entitites

2) Implicit Addressing: Correlated topics - use statistical correlation between
   words to extract relations between lines

Assumptions:
1) Each line is +/- semantically isolated
2) Atleast once in the conversation, the participants are directly addressed

Techniques:
1) Find a direct addressal
2) Cache last x conversations from either participant to find a origin
3) Match every line subsequently for y non-matching lines

Future Ideas:
1) Monitor nick changes
2) Keep persistent data about users - (whois)
3) Read across multiple files

"""

from collections import MutableSet

class Conversation:
    def __init__(self, seed, conversation, entities):
        pass


class ConnTracker:
    def __init__(self, log_file, offset):
        """
            Open log_file for reading, and seek to offset
        """
        log = open(log_file, 'r')

        find_speakers(log)

        self.log = parse_0(self, log)
        self.log.seek(offset)

        # TODO: Get from 
        self.speakers = MutableSet()

    def parse(self, log):
        """
            Read through current log file, populate the set of speakers,
            and break each line into (speaker, references, text)
        """
        parsed_log = []

        for line in log:
            


    def track():
        pass



