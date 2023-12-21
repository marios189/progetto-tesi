import webbrowser

output_file = 'results.txt'
checkpoint_file = 'checkpoint.txt'

def show_options():
    print("How would you define the site?")
    print("Unknown: 0")
    print("NotTypo: 1")
    print("ProbablyNotTypo: 2")
    print("ProbablyTypo: 3")
    print("Typo: 4")
    print("TypoPhishing: 5")
    print("Malware: 6")
    print("\nPress 'Enter' to continue")

def open_browser(actual_domain, generated_domain):
    webbrowser.open_new_tab(f'http://{actual_domain}')
    webbrowser.open_new_tab(f'http://{generated_domain}')

    show_options()
    value = input()

    with open(output_file, 'a') as output:
        output.write(f"{actual_domain} - {generated_domain} - {value}\n")

def open_file(file_input, start_index=0):
    with open(file_input, 'r') as file:
        for i, line in enumerate(file):
            if i < start_index:
                continue 

            actual_domain, generated_domain = line.strip().split(' - ')
            open_browser(actual_domain, generated_domain)

            checkpoint(i + 1)

def checkpoint(current_index):
    with open(checkpoint_file, 'w') as checkpoint:
        checkpoint.write(str(current_index))

def get_checkpoint():
    try:
        with open(checkpoint_file, 'r') as checkpoint:
            return int(checkpoint.read().strip())
    except FileNotFoundError:
        return 0 

start_index = get_checkpoint()

open_file('test_domains.txt', start_index)