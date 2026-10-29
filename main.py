"""
LAPTOP TROUBLESHOOTING EXPERT SYSTEM
Subject: Foundation of Artificial Intelligence (Course Code: 2ADPC204)
Author: Sushant Harish Mali (Roll No. 2049)
"""

def forward_chaining(facts):
    rules = {
        "Battery problem": ["not_starting", "charger_working"],
        "Charger problem": ["not_charging", "charger_not_working"],
        "Charging port problem": ["not_charging", "charger_working", "port_damaged"],
        "Battery or hardware problem": ["not_starting", "charger_working", "light_on"],
        "Charging indicator problem": ["laptop_charging", "light_off"],
        "Overheating due to blocked vents": ["hot_laptop", "vents_blocked"],
        "Cooling fan problem": ["hot_laptop", "fan_not_working"],
        "High CPU usage": ["slow_laptop", "many_apps"],
        "Low storage problem": ["slow_laptop", "storage_full"],
        "WiFi adapter problem": ["wifi_failed", "other_devices_work"],
        "Router or Internet problem": ["wifi_failed", "other_devices_fail"]
    }
 
    results = []
 
    for problem, conditions in rules.items():
        if all(fact in facts for fact in conditions):
            results.append(problem)
 
    return results
 
 
def backward_chaining(goal, facts):
    rules = {
        "Battery problem": ["not_starting", "charger_working"],
        "Charger problem": ["not_charging", "charger_not_working"],
        "Charging port problem": ["not_charging", "charger_working", "port_damaged"],
        "Battery or hardware problem": ["not_starting", "charger_working", "light_on"],
        "Charging indicator problem": ["laptop_charging", "light_off"],
        "Overheating due to blocked vents": ["hot_laptop", "vents_blocked"],
        "Cooling fan problem": ["hot_laptop", "fan_not_working"],
        "High CPU usage": ["slow_laptop", "many_apps"],
        "Low storage problem": ["slow_laptop", "storage_full"],
        "WiFi adapter problem": ["wifi_failed", "other_devices_work"],
        "Router or Internet problem": ["wifi_failed", "other_devices_fail"]
    }
 
    return goal in rules and all(
        condition in facts for condition in rules[goal]
    )
 
solutions = {
    "Battery problem": "Check the battery and power connection. Have the battery tested if necessary.",
    "Charger problem": "Check the power socket, adapter and cable. Try a compatible working charger.",
    "Charging port problem": "Have the charging port inspected by a technician.",
    "Battery or hardware problem": "Check the battery and power system. Further hardware testing is needed.",
    "Charging indicator problem": "If charging works normally, have the indicator light checked.",
    "Overheating due to blocked vents": "Place the laptop on a hard surface and keep its air vents clear.",
    "Cooling fan problem": "Check whether the fan is obstructed or faulty. Seek repair if necessary.",
    "High CPU usage": "Close unnecessary applications and check Task Manager for high CPU usage.",
    "Low storage problem": "Remove unnecessary files and free up storage space.",
    "WiFi adapter problem": "Check airplane mode, reconnect to WiFi and inspect the network adapter.",
    "Router or Internet problem": "Restart the router and check the Internet connection."
}
 
 
def ask(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please enter yes or no.")
 
 
def run_system():
    print("\n============================================")
    print("      LAPTOP TROUBLESHOOTING EXPERT SYSTEM")
    print("============================================")
    print("1. Laptop not starting")
    print("2. Laptop not charging")
    print("3. Laptop overheating")
    print("4. Laptop running slowly")
    print("5. WiFi not working")
 
    try:
        choice = int(input("\nSelect problem (1-5): "))
    except ValueError:
        print("Invalid input. Enter a number.")
        return
 
    if choice not in range(1, 6):
        print("Invalid choice.")
        return
 
    facts = set()
 
    if choice == 1:
        facts.add("not_starting")
 
        if ask("Is the charger working with a compatible device?"):
            facts.add("charger_working")
        else:
            facts.add("charger_not_working")
 
        if ask("Is the charging light on?"):
            facts.add("light_on")
        else:
            facts.add("light_off")
 
    elif choice == 2:
        facts.add("not_charging")
 
        if ask("Is the charger and power socket working?"):
            facts.add("charger_working")
        else:
            facts.add("charger_not_working")
 
        if "charger_working" in facts:
            if ask("Does the charging port look damaged or loose?"):
                facts.add("port_damaged")
 
        if ask("Does the laptop actually charge even though the light is off?"):
            facts.add("laptop_charging")
            facts.add("light_off")
 
    elif choice == 3:
        facts.add("hot_laptop")
 
        if ask("Are the air vents blocked by dust or objects?"):
            facts.add("vents_blocked")
 
        if ask("Is the cooling fan not spinning or not working properly?"):
            facts.add("fan_not_working")
 
    elif choice == 4:
        facts.add("slow_laptop")
 
        if ask("Are many applications using system resources?"):
            facts.add("many_apps")
 
        if ask("Is the storage almost full?"):
            facts.add("storage_full")
 
    elif choice == 5:
        facts.add("wifi_failed")
 
        if ask("Can other devices connect to the same WiFi?"):
            facts.add("other_devices_work")
        else:
            facts.add("other_devices_fail")
 
    results = forward_chaining(facts)
 
    print("\n============================================")
    print("             DIAGNOSTIC REPORT")
    print("============================================")
 
    if results:
        for problem in results:
            verified = backward_chaining(problem, facts)
 
            if verified:
                print(f"\nPossible problem: {problem}")
                print("Backward chaining verification: Confirmed by rules")
                print(f"Suggested solution: {solutions[problem]}")
    else:
        print("No cause could be identified from the current rules.")
        print("Try basic checks or consult a qualified technician.")
 
    print("\nNote: These are possible causes, not guaranteed diagnoses.")

if __name__ == "__main__":
    run_system()
