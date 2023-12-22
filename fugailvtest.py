# 实例化对象
import os
import unittest

import coverage

cov = coverage.coverage()
# 开始分析
cov.start()
suite = unittest.defaultTestLoader.discover(os.getcwd(), "testtoo.py")
unittest.TextTestRunner().run(suite)
# 结束分析
cov.stop()
# 结果保存
cov.save()
# 命令行模式展示结果
cov.report()
# 生成HTML覆盖率报告
cov.html_report(directory='covhtml')
