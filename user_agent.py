import random

# RANDOM USER AGENT GENERATOR


def RandomAgentChooser():
    with open("user_agents.txt", "r") as rf:
        data = rf.readlines()
        agent = random.choice(data)
        print("user agent now :\n".upper(),
              agent)
    return agent
