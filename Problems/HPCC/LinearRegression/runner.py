from os import system

for count in xrange(1, 10):
    command = "ecl run regression.ecl -I\"C:\ecl-ml-master\" --input=\"<request><NOP>" + str(
        count) + "</LName></request>\" --target=thor --server=192.168.56.101:8010"
    import subprocess

    output = subprocess.check_output(command, shell=True)
    raw_input()
