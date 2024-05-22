def prompt_generate_club( date , day):

    return f"""
            you are an information extractor of the events happening on a particular day and date from a corpus of text.
            To determine the main events planned for {date} or weekly or biweekly events held on {day} from the extracted text of a website of a club, we need to analyze the text to identify any specific event . Here is a general approach to extracting this information:

            1. Events:
            - Analyze the text for any mentions of events, activities, or specials scheduled for every {day} or {date}.

            I do not need any information for events which is not on above mentioned date. Answer in as few words as possible
            
            The information can be in German , translate it to english before using and return the result in english"""

def prompt_consolidate_club():
    return "you are an event summrizer of the three days mentioned below. summarise the events of the three days and answer in brief of the events happening on the specific days/dates"
    
