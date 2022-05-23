# FILENAME janelaptop_nvidia_specs.py
# SOURCE http://www.macvidcards.com/store/p1/Nvidia_GTX_780_3_GB_and_6_GB.html
# REFERENCE https://www.guru3d.com/articles-pages/geforce-gtx-780-review,2.html
# REFRENCE https://github.com/f0k/cudamat
# LEARNING kernel gpu testing https://blog.esciencecenter.nl/writing-testable-gpu-code-23bbda3a5d62

# TESTING cuda version https://stackoverflow.com/questions/9727688/how-to-get-the-cuda-version

nvidia_card = "GTX 780 6"


def main():
	jane_kepler_nvidia_specs()


def jane_kepler_nvidia_specs():
	"""
	The deep technical specs of janes GPU

	GPU Engine Specs:
	CUDA Cores: 2304
	Base Clock: 863 MHz
	Boost Clock: 902 MHz
	Texture Fill Rate: 160.5 GT/s
	Bus: PCIe 2.0
	Memory Specs:
	Memory Detail: 3072 or 6144 MB GDDR5
	Memory Interface Width: 384-Bit
	Memory Clock: 6.0 Gbps
	Memory Bandwidth: 288.4 GB/s
	"""
	print("jane_kepler_nvidia_specs did not run, its not called yet")






if __name__ == '__main__':
	main()
