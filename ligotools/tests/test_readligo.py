from ligotools import readligo as rl
# import numpy as np

def test_searchdir_from_FileList1():
	# hdf_list should be a list instead of SegmentList
	f = rl.FileList()
	hdf_list = f.searchdir()
	assert isinstance(hdf_list, list) == True

def test_searchdir_from_FileList2():
	# there are 3 hdf5 files in directory
	f = rl.FileList()
	temp_list = f.searchdir()
	hdf_list = [x for x in temp_list if "hdf5" in x]
	expected_hdf_num = 3
	actual_hdf_num = len(hdf_list)
	assert actual_hdf_num == expected_hdf_num

def test_searchdir_from_FileList3():
	# there is no gwf file in directory
	f = rl.FileList()
	temp_list = f.searchdir()
	gwf_list = [x for x in temp_list if "gwf" in x]
	expected_gwf_num = 0
	actual_gwf_num = len(gwf_list)
	assert actual_gwf_num == expected_gwf_num

def test_getsegs():
	# seglist should be SegmentList instead of list
	seglist = rl.getsegs(842657792, 842658792, 'H1', flag='DATA', filelist=None)
	assert isinstance(seglist, list) == False


