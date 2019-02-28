import os, sys, subprocess, threading, time
from collections import OrderedDict
from commands import commands

storm_executable_default = "~/storm/build/bin/storm"
timelimit_default = 7200 # seconds
logdir_default = "log/"

class CommandExecution(object):
    """ Represents the execution of a single command line argument. """
    def __init__(self):
        self.timelimit = None
        self.return_code = None
        self.output = None
        self.wall_time = None
        self.proc = None

    def stop(self):
        self.timelimit = True
        self.proc.kill()

    def run(self, command_line_str, time_limit):
        command_line_list = command_line_str.split()
        command_line_list[0] = os.path.expanduser(command_line_list[0])
        self.proc = subprocess.Popen(command_line_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        start_time = time.time()
        timer = threading.Timer(time_limit, self.stop)
        self.timelimit = False
        self.output = ""
        timer.start()
        try:
            stdout, stderr = self.proc.communicate()
        except Exception as e:
            self.output = self.output + "Error when executing the command:\n{}\n".format(e)
        finally:
            timer.cancel()
            self.wall_time = time.time() - start_time
            self.return_code = self.proc.returncode
        self.output = self.output + stdout.decode('utf8')
        if len(stderr) > 0:
            self.output = self.output + "\n" + "#"*30 + "Output to stderr" + "#"*30 + "\n" + stderr.decode('utf8')
        if self.timelimit and self.wall_time <= time_limit:
            print("WARN: A timelimit was triggered although the measured time is {} seconds which is still below the time limit of {} seconds".format(self.wall_time, time_limit))


def execute_command_line(command_line_str, time_limit):
    """
    Executes the given command line with the given time limit (in seconds).
    :returns the output of the command (including the output to stderr, if present), the runtime of the command and either the return code or None (in case of a timelimit)
    """
    execution = CommandExecution()
    execution.run(command_line_str, time_limit)
    if execution.timelimit:
        return execution.output, execution.wall_time, None
    else:
        return execution.output, execution.wall_time, execution.return_code

if __name__ == "__main__":
    # Make input(..) work in python2...
    try:
        input = raw_input
    except NameError:
        pass
        
    storm_executable = input("Enter path to storm binary [{}]: ".format(storm_executable_default))
    if storm_executable == "":
        storm_executable = storm_executable_default

    storm_executable = os.path.expanduser(storm_executable)
    print("Checking binary.")
    if not os.path.exists(storm_executable):
        raise AssertionError("File '{}' does not exist.".format(storm_executable))

    test_out, test_time, test_code = execute_command_line(storm_executable, 10)
    if test_code != 0:
        raise AssertionError("Could not execute binary {}".format(storm_executable))
    print("\tDone.")
    
    
    selected_benchmarks = OrderedDict()
    done = False
    num_selected = 0
    while not done:
        print("\nPlease select the benchmarks to execute ({} selected): ".format(num_selected))
        available_options = dict()
        sum_b = 0
        i = 1
        for commandset in commands:
            if not commandset in selected_benchmarks:
                print("\t[{}]\t{} ({} commands)".format(i, commandset + " "*(30-len(commandset)), len(commands[commandset])))
                available_options[str(i)] = commandset
                i += 1
                sum_b += len(commands[commandset])
        print("\t[{}]\t{} ({} commands)".format(i, "all" + " "*27, sum_b))
        available_options[str(i)] = "all"
        available_options["d"] = "done"
        option = ""
        while option not in available_options:
            option = input("Enter number (1 to {}) or 'd' if you are done: ".format(i))
        if available_options[option] == "all":
            selected_benchmarks = commands
            num_selected += sum_b
            done = True
        elif available_options[option] == "done":
            done = True
        else:
            selected_benchmarks[available_options[option]] = commands[available_options[option]]
            num_selected += len(commands[available_options[option]])
    
    timelimit_str = input("Enter a time limit in seconds [{}]: ".format(timelimit_default))
    if timelimit_str == "":
        timelimit = timelimit_default
    else:
        timelimit = int(timelimit_str)
    
    logdir = input("Enter path for logfiles [{}]: ".format(logdir_default))
    if logdir == "":
        logdir = logdir_default
    if not os.path.exists(logdir):
        os.makedirs(logdir)
        
    print ("Execution of {} benchmarks with {} seconds time limit starts in 5 seconds. Press Ctrl+C to cancel.".format(num_selected, timelimit))
    time.sleep(5)
    
    i = 1
    start_time_benchmarking = time.time()
    for benchmarkset in selected_benchmarks:
        print("Executing {} benchmarks from '{}'".format(len(selected_benchmarks[benchmarkset]), benchmarkset))
        
        for command in selected_benchmarks[benchmarkset]:
            logfile_pos = command.find("--logfile")
            command_line = storm_executable + " " + command[:logfile_pos]
            output, runtime, returncode = execute_command_line(command_line, timelimit)
            logfile = os.path.join(logdir, "{}-{}".format(benchmarkset, command[logfile_pos + len("--logfile "):].strip()))
            with open(logfile, 'w') as file:
                file.write(output)            
            if returncode == 0:
                print("Command {}/{} finished after {} seconds. Output saved to {}".format(i,num_selected, runtime, logfile))
            elif returncode is None and runtime >= timelimit:
                print("Command {}/{} timed out after {} seconds. Output saved to {}".format(i,num_selected, runtime, logfile))
            else:
                print("ERROR: Command {}/{} finished after {} seconds with non-zero exit code {}. Output saved to {}".format(i,num_selected,runtime,returncode,logfile))
            i += 1
    print("All benchmarks have been executed after {} seconds.".format(time.time() - start_time_benchmarking))
    

    


