import os
from os.path import dirname, abspath
import shutil
import subprocess
import datetime
from azureml.core import Run
from argparse import ArgumentParser

rosetta_path = None
wd_path = None
output_root = None

def run_command(command, shell=False):
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=shell)
    for line in iter(proc.stdout.readline, b''):
        if (line):
            print (f"{line.decode().rstrip()} [{datetime.datetime.now()}]", flush=True)

    proc.stdout.close()
    proc.wait()

    return proc.returncode


def init():
    global rosetta_path
    global wd_path
    global output_root

    print("Beginning init()", flush=True)
    
    run = Run.get_context()
    ws = run.experiment.workspace

    rosetta_path = abspath("/RoseTTAFold")
    print(f"showing the contents of the RoseTTAFold folder :{rosetta_path}")
    print(os.listdir(rosetta_path))

    wd_path = abspath(dirname(__file__))
    print(f"showing the contents of the working folder :{wd_path}")
    print(os.listdir(wd_path))

    if (output_root is None):
        if (os.getenv('AZUREML_BI_OUTPUT_PATH') is not None):
            # Load output path from environment variable
            output_root = os.environ["AZUREML_BI_OUTPUT_PATH"]
        else:
            # Use a default output path: './outputs'
            output_root = os.path.join(wd_path, "outputs")

    os.makedirs(output_root, exist_ok=True)
    print(f"Output path: {output_root}", flush=True)

    datasets_list = {
        "rosettafold_weights":"/RoseTTAFold/weights/",
        "rosettafold_bfd":"/RoseTTAFold/bfd/",
        "rosettafold_UniRef":"/RoseTTAFold/UniRef30_2020_06/",
        "rosettafold_pdb":"/RoseTTAFold/pdb100_2021Mar03/"
    }

    print("Starting to mount datasets")
    mount_contexts = {}
    for name, mount_path in datasets_list.items():
        mount_contexts[name] = ws.datasets[name].mount(mount_path)
        mount_contexts[name].start()
        print("Mounted dataset ", name)
    print("Mount complete")

    print("Batch init complete!", flush=True)


def run(mini_batch):
    print(f"run method start: {__file__}, run({mini_batch})")

    script_path = os.path.join(rosetta_path, "run_e2e_ver.sh")

    result_list = []

    for input_file in mini_batch:
        input_dir = os.path.dirname(input_file)
        input_filename = os.path.basename(input_file).split(".")[0]
        print(f"Processing input {input_filename} in directory {input_dir}")

        # creating a temp dir for this input
        temp_wd = os.path.join(wd_path, f"temp_wd/{input_filename}")
        os.makedirs(temp_wd, exist_ok=True)
        print(f"Temp wd {temp_wd}", flush=True)

        # run the RoseTTAFold script, run_e2e_ver.sh
        cmd = [ '/bin/sh', script_path, input_file, temp_wd ]
        run_command(cmd)

        result_list.append(f"{os.path.basename(input_file)}: {input_file}")

        # copy outputs to destination
        output_dir = os.path.join(output_root, input_filename)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Moving outputs to {output_dir}")
        OUTPUT_FILENAME = "t000_.e2e.pdb"  # filename is hard-coded in Rosetta Fold code
        if OUTPUT_FILENAME in os.listdir(temp_wd):
            shutil.copy(
                os.path.join(temp_wd, OUTPUT_FILENAME),
                output_dir)
            print(f"Output written for input file {input_filename}")

        # cleanup the temp folder
        try:
            shutil.rmtree(temp_wd)
        except:
            print('Error while deleting temp directory')

    return result_list

def main():
    global output_root

    print("Starting score.py")

    parser = ArgumentParser(description="RoseTTAFold Scoring")
    parser.add_argument("--inputs", help="Path to folder containing input files for scoring")
    parser.add_argument("--outputs", help="Path to output folder for results", required=False)
    args = parser.parse_args()

    if (args.outputs is not None):
        output_root = os.path.abspath(args.outputs)

    inputs = []
    for file in os.listdir(args.inputs):
        inputs.append(os.path.join(args.inputs, file))
        print("Found input file: ", file)

    init()
    run(inputs)

if __name__ == "__main__":
    main()