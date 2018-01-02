import time,unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

test_dir='./Test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
if __name__=="__main__":
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'wb')as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description="test baidu")
        runner.run(discover)
    f.close()