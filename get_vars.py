"""
runs the bash file get_bandwidth.sh and takes the output file created 
as input and reads the values to create class objects 
"""

import subprocess
import csv
import runpy
import time
# from owlready2 import *

bash_file = "./get_bandwidth.sh"
io_file = "./output.csv"

# process = subprocess.Popen(bash_file)
# process.wait()
# process.kill()

with open(io_file, newline='\n') as f:
    reader = csv.reader(f)
    col_headings = next(reader)
    first_row = next(reader)
        
m_time = first_row[0]
m_stage = first_row[1]
m_bandwidth = first_row[2]
       
onto = get_ontology("./IoBT_v2.owl").load()
with onto:
    class TemporalEntity(Thing):
        pass
    class BandwidthAttack(Thing):
        pass
    class Result(Thing):
        pass
        
timestamp = TemporalEntity(m_time)
stage = BandwidthAttack(m_stage)
bandwidth = Result(m_bandwidth)

"""
for i in TemporalEntity.instances():
    print(i)
for j in BandwidthAttack.instances():
    print(j)
for k in Result.instances():
    print(k)
"""

time.sleep(1)

if m_stage =='Stage1BA':
	runpy.run_path(path_name='color.py')
elif m_stage == 'Stage2BA':
	runpy.run_path(path_name='color2.py')
elif m_stage =='Stage3BA':
	runpy.run_path(path_name='color.py')

        

