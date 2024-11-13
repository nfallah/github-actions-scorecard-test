import subprocess
import json

def main():
    i = 0
    with open('config.txt', 'r') as file:
        urls = file.read().splitlines()
        #print(urls)
    for url in urls:
        args = ['scorecard', '--repo', url, '--format', 'json']
        result = subprocess.run(args, capture_output=True, text=True)
        with open(f'report_{i}.json', 'w') as file2:
            str = result.stdout
            jsonfile = json.loads(result.stdout)
            file2.write(str)
            #TODO: work with jsonfile to generate MD table
        i += 1

if __name__ == "__main__":
    main()