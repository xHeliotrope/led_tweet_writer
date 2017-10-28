from subprocess import Popen, call, PIPE
import os

def run_processes():
    my_env = os.environ.copy()
    my_env["PYTHONPATH"] = ".:/home/pi/Development/rpi_ws281x/python/build/lib.linux-arm7l-2.7/:/home/pi/Development/rpi_ws281x/pyton/examples/"
    proc1 = Popen("%s %s %s" % ('sudo', '/usr/bin/python', 'examples/scroll_text.py'), env=my_env, stdout=PIPE, shell=True)
    proc2 = Popen("%s %s" % ('/home/pi/.nvm/versions/node/v8.8.1/bin/node', 'tweet_writer.js'), stdout=PIPE, shell=True)
    (out, err) = proc1.communicate()
    (out2, err2) = proc2.communicate()
    proc1.wait()
    proc2.wait()
    #call(['sudo', 'PYTHONPATH=".:build/lib.linux-arm7l-2.7"', 'python', 'examples/scroll_text.py'], shell=True)
    
run_processes()
