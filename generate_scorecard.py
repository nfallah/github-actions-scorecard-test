import subprocess
import json

def main():
    i = 0
    with open('config.txt', 'r') as file:
        urls = file.readlines()
    for url in urls:
        args = ['scorecard', '--repo', url, '--format', 'json']
        result = subprocess.run(args, capture_output=True, text=True)
        with open(f'{i}.json', 'w') as file2:
            file2.write(json.loads(result.stdout))
        i += 1

if __name__ == "__main__":
    main()