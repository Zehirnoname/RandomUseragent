import random

def random_user_agent():
    """Generates a dynamic User-Agent"""
    browsers = ["Chrome", "Firefox", "Safari", "Edge"]
    os_list = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "iPhone; CPU iPhone OS 17_2 like Mac OS X"
    ]
    browser_versions = {
        "Chrome": f"{random.randint(60, 100)}.0.{random.randint(1000, 5000)}.{random.randint(100, 500)}",
        "Firefox": f"{random.randint(60, 100)}.{random.randint(0, 10)}",
        "Safari": f"{random.randint(500, 600)}.{random.randint(0, 20)}.{random.randint(0, 30)}",
        "Edge": f"{random.randint(80, 100)}.0.{random.randint(500, 1500)}.{random.randint(0, 100)}",
    }
    browser = random.choice(browsers)
    os = random.choice(os_list)
    version = browser_versions[browser]
    return f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"

def save_user_agents_to_file(num_agents, filename="random_useragents.txt"):
    """Saves the User-Agents to a file"""
    user_agents = []
    for _ in range(num_agents):
        user_agents.append(random_user_agent())
    
    with open(filename, 'w') as file:
        for user_agent in user_agents:
            file.write(user_agent + "\n")
    
    print(f"{num_agents} random User-Agent(s) have been saved to '{filename}'.")
    print(f"Program developed by Zehir.")
    print(f"For more information, visit GitHub: https://github.com/Zehirnoname/")

def main():
    """Main program function"""
    print("Welcome to the Random User-Agent Generator!")
    print("This program will generate random User-Agent strings and save them to a file.")
    print("You can specify how many User-Agent strings you want to generate.")
    print("Program developed by Zehir.")
    print("GitHub repository: https://github.com/Zehirnoname/")
    
    num_agents = int(input("How many random User-Agents would you like to generate? "))
    save_user_agents_to_file(num_agents)

if __name__ == "__main__":
    main()
