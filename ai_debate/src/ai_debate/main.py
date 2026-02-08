#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_debate.crew import AiDebate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Debate crew with the given inputs. You can modify the inputs as needed to test different propositions.
    """
    inputs = {
        'proposition': 'What was before the Big Bang'
    }

    try:
        AiDebate().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
