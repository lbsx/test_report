from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template2.html')

report = [
    {"id": 1, "class": "Test", "method": "test_case1", "description": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "time": "5.1e-05 s", "result": "success", "log": "======== setUp =========\nNone\n======== test 1 =========\n======== tearDown ========="},
    {"id": 2, "class": "Test", "method": "test_case2", "description": "null", "time": "2.0 s", "result": "success", "log": "======== setUp =========\nNone\n======== test 2 =========\n======== tearDown ========="},
    {"id": 3, "class": "Test", "method": "test_case3", "description": "null", "time": "0.00118 s", "result": "fail", "log": "======== setUp =========\nNone\n======== test 3 =========\n======== tearDown ========="},
    {"id": 4, "class": "Test", "method": "test_case4", "description": "null", "time": "1.55e-05 s", "result": "skip", "log": "======== setUp =========\nNone\n======== test 4 =========\n======== tearDown ========="},
    {"id": 5, "class": "ABC", "method": "test_case5", "description": "null", "time": "1.55e-05 s", "result": "skip", "log": "======== setUp =========\nNone\n======== test 4 =========\n======== tearDown ========="},
    {"id": 6, "class": "ABC", "method": "test_case6", "description": "null", "time": "1.55e-05 s", "result": "skip", "log": "======== setUp =========\nNone\n======== test 4 =========\n======== tearDown ========="}
]
result = template.render(testCases=report, start_time='2021-07-06 09:03:01', run_time="4.3h",
                         report_title="template测试报告")

with open('report.html', 'w', encoding='utf-8') as f:
    f.write(result)
