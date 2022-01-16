from typing import Dict, List

replaced_start: Dict[str, str] = {
    'class Solution {': 'class Solution:',
    '->': '.',
    '//': '#',
    '/': '//',
    'false': 'False',
    'true': 'True',
    '||': 'or',
    '"': '\'',
    '.push(': '.append(',
    '.push_back(': '.append(',
    '.emplace(': '.append(',
    '.pop_front(': '.popleft(',
    '.pop_back(': '.pop(',
    '.insert(': '.add(',
    '.erase(': '.remove(',
    '.top()': '[-1]',
    '.front()': '[0]',
    '.back()': '[-1]',
    'INT_MAX': 'inf',
    'INT_MIN': '-inf',
    'nullptr': 'None'
}

replaced_end: Dict[str, str] = {
    '&&': 'and',
}

useless: List[str] = [
    'const ', 'string ', 'string& ', 'long ', 'int ', 'bool ', 'char ', '++', '--', ';',  '}', '{'
]
