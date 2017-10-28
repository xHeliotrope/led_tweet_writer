from subprocess import Popen

def run_processes():
    proc1 = Popen("%s %s %s %s" % ('sudo', 'PYTHONPATH=".:build/lib.linux-arm7l-2.7"', 'python', 'examples/scroll_text.py'), shell=True)
    proc2 = Popen("%s %s" % ('node', 'tweet_writer.js'), shell=True)
    (out, err) = proc1.communicate()
    (out2, err2) = proc2.communicate()
    
run_processes()
