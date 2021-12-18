import runpy

a = 'Stage2BA'
if a =='Stage1BA':
	runpy.run_path(path_name='color.py')
elif a == 'Stage2BA':
	runpy.run_path(path_name='gray.py')
elif a=='Stage3BA':
	runpy.run_path(path_name='picture.py')
