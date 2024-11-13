import subprocess
import json
from scorecard_template import MARKDOWN_TEMPLATE

def main():
    with open('config.txt', 'r') as file:
        urls = file.read().splitlines()
    for url in urls:
        args = ['scorecard', '--repo', url, '--format', 'json']
        result = subprocess.run(args, capture_output=True, text=True)
        create_markdown(json.loads(result.stdout))

def create_markdown(jsonfile):
    checks = []
    for check in jsonfile['checks']:
        score = check['score']
        if score < 0: score = '*N/A*'
        name = f'[{check['name']}]({check['documentation']['url']})'
        assessment = '*N/A*' if score == '*N/A*' else (1 if score <= 3.3 else 2 if score <= 6.6 else 3 if score <= 9.9 else 4)
        notes = check['reason']
        checks.append(f'|{score}|{name}|{assessment}|{notes}|')
    checks_md = '\n'.join(checks)
    markdown_data = MARKDOWN_TEMPLATE.format(
        scorecard_date = jsonfile['date'],
        scorecard_version = jsonfile['scorecard']['version'],
        scorecard_score = jsonfile['score'],
        scorecard_rows = checks_md
    )
    elements = jsonfile['repo']['name'].split('/')
    name = elements[2]
    owner = elements[1]
    with open(f'{owner}_{name}.md', 'w') as file:
        file.write(markdown_data)

if __name__ == "__main__":
    main()