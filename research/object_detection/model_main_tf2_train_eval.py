r"""Script to run train and eval for TF2.

For using the script run:

python object_detection/model_main_tf2_train_eval.py \
            --model_dir PATH/TO/MODEL_DIR \
            --pipeline_config_path PATH/TO/DIR/pipeline.config \
            --num_train_steps <TRAIN_STEPS> \
            --sample_1_of_n_eval_examples 1 \
            --eval_time <EVAL_EVERY_N_SECONDS> \
            --task_name <TRAINS_TASK_NAME>
            
"""

import os
import subprocess
import time
import signal
import argparse

from trains import Task


parser = argparse.ArgumentParser()
parser.add_argument(
    '--model_dir',
    required=True,
    type=str,
    help='Path to output model directory '
                       'where event and checkpoint files will be written.'
)
parser.add_argument(
    '--pipeline_config_path',
    required=True, 
    type=str,
    help='Path to pipeline config.'
)
parser.add_argument(
    '--eval_time',
    type=str,
    default='1800',
    help='How much time needs to pass during training to run eval. Default is 30 min (1800s'
)

parser.add_argument(
    '--num_train_steps',
    type=str,
    default='',
    help='Number of train steps.'
)
parser.add_argument(
    '--checkpoint_every_n',
    default='1000', 
    type=str,
    help='Integer defining how often we checkpoint.'
)
parser.add_argument(
    '--eval_timeout',
    default='1', 
    type=str,
    help='Number of seconds to wait for an'
                     'evaluation checkpoint before exiting. Used in OD_API model_main. DO NOT CONFUSE WITH eval_time!!!!!!!!!!!!'
)
parser.add_argument(
    '--eval_on_train_data',
    default='', 
    type=str,
    help='Enable evaluating on train '
                  'data (only supported in distributed training).'
)
parser.add_argument(
    '--sample_1_of_n_eval_examples',
    default='', 
    type=str,
    help='Will sample one of '
                     'every n eval input examples, where n is provided.'
)
parser.add_argument(
    '--sample_1_of_n_eval_on_train_examples',
    default='', 
    type=str,
    help='Will sample '
                     'one of every n train input examples for evaluation, '
                     'where n is provided. This is only used if '
                     '`eval_training_data` is True.'
)
parser.add_argument(
    '--use_tpu',
    default='', 
    type=str,
    help='Whether the job is executing on a TPU.'
)
parser.add_argument(
    '--tpu_name',
    default='', 
    type=str,
    help='Name of the Cloud TPU for Cluster Resolvers.'
)
parser.add_argument(
    '--num_workers',
    default='', 
    type=str,
    help='When num_workers > 1, training uses '
    'MultiWorkerMirroredStrategy. When num_workers = 1 it uses '
    'MirroredStrategy.'
)
parser.add_argument(
    '--record_summaries',
    default='', 
    type=str,
    help='Whether or not to record summaries during'
                      ' training.'
)
parser.add_argument(
    '--project_name',
    default='forsight-detection', 
    type=str,
    help='Name of the project for Trains logging.'
)
parser.add_argument(
    '--task_name',
    default='', 
    type=str,
    help='Name of the task for Trains logging.'
)

args = parser.parse_args()

#-----------------------------------------------------------------------------TRAIN--------------------------------------------------------------------------------------------------

train_command = []
train_command.append('python3')
train_command.append('object_detection/model_main_tf2.py')


train_command.append('--model_dir')
train_command.append(args.model_dir)

train_command.append('--pipeline_config_path')
train_command.append(args.pipeline_config_path)

if(args.num_train_steps):
    train_command.append('--num_train_steps=' + args.num_train_steps)

if(args.checkpoint_every_n):
    train_command.append('--checkpoint_every_n=' + args.checkpoint_every_n)

if(args.eval_on_train_data):
    train_command.append('--eval_on_train_data=' + args.eval_on_train_data)

if(args.sample_1_of_n_eval_examples):
    train_command.append('--sample_1_of_n_eval_examples=' + args.sample_1_of_n_eval_examples)

if(args.sample_1_of_n_eval_on_train_examples):
    train_command.append('--sample_1_of_n_eval_on_train_examples=' + args.sample_1_of_n_eval_on_train_examples)

if(args.use_tpu):
    train_command.append('--use_tpu=' + args.use_tpu)

if(args.tpu_name):
    train_command.append('--tpu_name=' + args.tpu_name)

if(args.num_workers):
    train_command.append('--num_workers=' + args.num_workers)

if(args.record_summaries):
    train_command.append('--record_summaries=' + args.record_summaries)

if(args.project_name):
    train_command.append('--project_name=' + args.project_name)

if(args.task_name):
    train_command.append('--task_name=' + args.task_name)

train_command.append('--alsologtostderr')


#--------------------------------------------EVAL-----------------------------------------------------------------------------------------------------------------------------------------------

eval_command = []
eval_command.append('python3')
eval_command.append('object_detection/model_main_tf2.py')

eval_command.append('--model_dir')
eval_command.append(args.model_dir)

eval_command.append('--checkpoint_dir')
eval_command.append(args.model_dir) # checkpoint_dir is the same as model_dir so we can use model_dir for this

eval_command.append('--pipeline_config_path')
eval_command.append(args.pipeline_config_path)

if(args.eval_timeout):
    eval_command.append('--eval_timeout='+args.eval_timeout)

if(args.eval_on_train_data):
    eval_command.append('--eval_on_train_data=' + args.eval_on_train_data)

if(args.sample_1_of_n_eval_examples):
    eval_command.append('--sample_1_of_n_eval_examples=' + args.sample_1_of_n_eval_examples)

if(args.sample_1_of_n_eval_on_train_examples):
    eval_command.append('--sample_1_of_n_eval_on_train_examples=' + args.sample_1_of_n_eval_on_train_examples)

if(args.use_tpu):
    eval_command.append('--use_tpu=' + args.use_tpu)

if(args.tpu_name):
    eval_command.append('--tpu_name=' + args.tpu_name)

if(args.num_workers):
    eval_command.append('--num_workers=' + args.num_workers)

if(args.record_summaries):
    eval_command.append('--record_summaries=' + args.record_summaries)

if(args.project_name):
    eval_command.append('--project_name=' + args.project_name)

if(args.task_name):
    eval_command.append('--task_name=' + args.task_name)
    
eval_command.append('--alsologtostderr')


#--------------------------------------------------------------------------------------------------PROGRAM-----------------------------------------------------------------------------------

def train():
    proc = subprocess.Popen(train_command, shell=False)
    return proc
def eval():
    proc2 = subprocess.Popen(eval_command, shell=False)
    return proc2
            
if __name__ == '__main__':    
    is_train = True
    STOP = True
    
    task = Task.init(project_name=args.project_name, task_name=args.task_name)
    task.connect_configuration(args.pipeline_config_path)
    
    while True:
        if is_train == True:
            STOP=True
            p = train()
            try:
                p.wait(timeout=int(args.eval_time))
            except subprocess.TimeoutExpired:
                STOP = False
                os.kill(p.pid, signal.SIGTERM)
            time.sleep(10)
            is_train= False
        if is_train == False:
            q = eval()
            try:
                q.wait()
            except:
                time.sleep(10)
            is_train = True
        if STOP == True:
            break
